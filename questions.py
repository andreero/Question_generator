from jinja2 import Template, StrictUndefined
from jinja2.exceptions import UndefinedError
import random
from typing import Dict, List
from images import Image


class Question:
    def __init__(self, formula, correct, wrong_1=None, wrong_2=None, wrong_3=None,
                 variables=None, instruction=None, hint=None, image=None):
        self.formula = formula
        self.correct = correct
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
        self.variables = variables if variables is not None else {}
        self.instruction = instruction
        self.hint = hint
        self.image = image

    def generate_variables(self):
        """ Generate values from provided variables definition list
            The variables list comes in the following format:
            {'v1': (randint, 2, 10)} and the output is
            {'v1': 4} (where 4 is the actual random int).
        """
        generated_variables = {}
        for variable_name, variable_values in self.variables.items():
            random.seed()
            function, *arguments = variable_values
            generated_variables[variable_name] = function(*arguments)
        return generated_variables

    @staticmethod
    def render_template(template_string: str, template_variables: Dict[str, str]) -> str:
        """ Render jinja2 template string with provided parameters"""
        if template_string is None:
            return ''
        try:
            template = Template(template_string, undefined=StrictUndefined)
            return template.render(template_variables)
        except UndefinedError as e:
            raise ValueError(f'Error in template {template_string}: {e}')

    def render_image_definition(self, vars):
        """ Replace {{variables}} in image templates with actual values, so the image can be generated."""
        if not self.image:
            return
        generated_image_dict = {}
        for field_name, field_templates in self.image.items():
            if isinstance(field_templates, list):
                field_list = list()
                for template in field_templates:
                    if isinstance(template, dict):
                        rendered_entry = dict()
                        for key, value in template.items():
                            rendered_field = self.render_template(template_string=value, template_variables=vars)
                            rendered_entry[key] = rendered_field
                    else:
                        rendered_entry = self.render_template(template_string=template, template_variables=vars)
                    field_list.append(rendered_entry)
                generated_image_dict[field_name] = field_list
            elif isinstance(field_templates, dict):
                field_dict = dict()
                for key, value in field_templates.items():
                    rendered_field = self.render_template(template_string=value, template_variables=vars)
                    field_dict[key] = rendered_field
                generated_image_dict[field_name] = field_dict
            else:
                generated_image_dict[field_name] = self.render_template(template_string=field_templates, template_variables=vars)
        return generated_image_dict

    def render(self) -> Dict[str, str]:
        """ Return a randomized question string from the provided question definition. """
        generated_variables = self.generate_variables()
        generated_strings = {
            'instruction': self.render_template(template_string=self.instruction, template_variables=generated_variables),
            'answer': self.render_template(template_string=self.formula, template_variables=generated_variables),
            'correct': self.render_template(template_string=self.correct, template_variables=generated_variables),
            'wrong_1': self.render_template(template_string=self.wrong_1, template_variables=generated_variables),
            'wrong_2': self.render_template(template_string=self.wrong_2, template_variables=generated_variables),
            'wrong_3': self.render_template(template_string=self.wrong_3, template_variables=generated_variables),
            'hint': self.hint,
            'image': self.render_image_definition(vars=generated_variables),
        }
        return generated_strings


class QuestionSet:
    def __init__(self, grade, capital, subcapital, title, instruction, question_type, questions,
                 function_name=None, hint=None, output_directory=''):
        self.grade = grade
        self.function_name = function_name
        self.capital = capital
        self.subcapital = subcapital
        self.title = title
        self.instruction = instruction
        self.question_type = question_type
        self.questions = questions
        self.hint = hint
        self.output_directory = output_directory

    def generate_questions(self, n) -> List[Dict[str, str]]:
        """ Try to generate unique questions from the provided question set,
            rerolling when encountering a duplicate question. """
        question_list = []
        seen_questions = set()
        max_retries = n*50
        for i in range(max_retries):  # try to generate n questions, but give up after 10*n attempts
            if len(question_list) >= n:
                break
            question = random.choice(self.questions).render()

            if self.question_type in ['MC', 'buttons', 'gap', 'lineCombineRight']:
                if question.get('image'):
                    unique_part = question['correct']
                else:
                    unique_part = question['answer']
                if unique_part in seen_questions:
                    continue
                seen_questions.add(unique_part)
                question_list.append(question)

            elif self.question_type in ['dragGroup', 'dragMatch']:  # Those types have multiple parts
                if self.question_type == 'dragGroup':
                    drag_parts = question['correct'].replace('~', ';').split(';')
                else:
                    drag_parts = question['correct'].replace('|', ';').split(';')
                for part in drag_parts:
                    if part in seen_questions:
                        break
                else:
                    seen_questions.update(drag_parts)
                    question_list.append(question)
        else:
            print(f'Warning: Could not generate enough unique questions '
                  f'for question set {self.title} after {max_retries} retries.')
            print(f'Please define more question templates or increase the range of random variables.')
        return question_list

    def render_questions(self, n) -> List[Dict[str, str]]:
        questions = self.generate_questions(n)
        questions_with_extra_data = list()
        for question in questions:
            question['functionname'] = self.function_name
            question['capital'] = self.capital
            question['subcapital'] = self.subcapital
            question['title'] = self.title
            question['instruction'] = question.get('instruction') or self.instruction
            question['type'] = self.question_type
            question['hint'] = question.get('hint') or self.hint
            if question.get('image') and question['image']:
                image_dict = question['image']
                image = Image(axis_limits=image_dict.get('axis_limits'),
                              dots=image_dict.get('dots'),
                              charts=image_dict.get('charts'),
                              arrows=image_dict.get('arrows'),
                              )
                image.output_directory = self.output_directory
                question['image'] = image.draw_image()
            questions_with_extra_data.append(question)
        return questions_with_extra_data
