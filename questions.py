import random
import hashlib
import json
from typing import Dict, List

from jinja2 import Template, StrictUndefined
from jinja2.exceptions import UndefinedError

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
        random.seed()
        
        for variable_name, variable_values in self.variables.items():
            if isinstance(variable_values, tuple):
                function, *arguments = variable_values
                generated_variables[variable_name] = function(*arguments)
            else:
                generated_variables[variable_name] = variable_values
        return generated_variables

    @staticmethod
    def render_template(template_string: str, template_variables: Dict[str, str]) -> str:
        """ Render jinja2 template string with provided parameters"""
        if not isinstance(template_string, str):
            return template_string
        try:
            template = Template(template_string, undefined=StrictUndefined)
            return template.render(template_variables)
        except UndefinedError as e:
            raise ValueError(f'Error in template {template_string}: {e}')

    def render_list_or_tuple(self, template_list, template_variables):
        rendered_sequence = list()
        for template in template_list:
            if isinstance(template, (list, tuple)):
                rendered_field = self.render_list_or_tuple(template_list=template, template_variables=template_variables)
            elif isinstance(template, dict):
                rendered_field = self.render_dict(template_dict=template, template_variables=template_variables)
            else:
                rendered_field = self.render_template(template_string=template, template_variables=template_variables)
            rendered_sequence.append(rendered_field)
        if isinstance(template_list, tuple):
            rendered_sequence = tuple(rendered_sequence)
        return rendered_sequence

    def render_dict(self, template_dict, template_variables):
        rendered_dict = dict()
        for key, value in template_dict.items():
            if isinstance(value, (list, tuple)):
                rendered_field = self.render_list_or_tuple(template_list=value, template_variables=template_variables)
            elif isinstance(value, dict):
                rendered_field = self.render_dict(template_dict=value, template_variables=template_variables)
            else:
                rendered_field = self.render_template(template_string=value, template_variables=template_variables)
            rendered_dict[key] = rendered_field
        return rendered_dict

    def render_image_definition(self, template_variables):
        """ Replace {{variables}} in image templates with actual values, so the image can be generated."""
        if not isinstance(self.image, dict):
            return self.image
        return self.render_dict(self.image, template_variables=template_variables)

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
            'image': self.render_image_definition(template_variables=generated_variables),
        }
        return generated_strings


class QuestionSet:
    def __init__(self, grade, capital, subcapital, title, instruction, question_type, questions,
                 function_name=None, hint=None, output_directory=''):
        self.leitidee = ''
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

    @staticmethod
    def _generate_image_description_hash(image_desc) -> str:
        if isinstance(image_desc, dict):
            image_dict_str = json.dumps(image_desc, sort_keys=True).encode('utf-8')
            image_hash = hashlib.md5(image_dict_str).hexdigest()
        else:
            image_hash = image_desc
        return image_hash

    def generate_questions(self, questions_to_generate: int) -> List[Dict[str, str]]:
        """ Try to generate unique questions from the provided question set,
            rerolling when encountering a duplicate question. """
        question_list = []
        seen_questions = set()
        max_retries = questions_to_generate*50
       
        for i in range(max_retries):  # try to generate n questions, but give up after max_retries attempts
            if len(question_list) >= questions_to_generate:
                break
            question = random.choice(self.questions).render()

            if self.question_type in ['MC', 'buttons', 'gap', 'lineCombineRight']:
                if question.get('image'):
                    unique_image_part = self._generate_image_description_hash(question['image'])
                    unique_part = question['correct'] + unique_image_part
                else:
                    unique_part = question['answer'] + question['correct']
                    # unique_part = question['answer']
 
                if unique_part in seen_questions:
                    continue
                seen_questions.add(unique_part)
                question_list.append(question)

            elif self.question_type in ['dragGroup', 'dragMatch', 'dragSort']:  # Those types have multiple parts
                if self.question_type == 'dragGroup':
                    drag_parts = question['correct'].replace('~', ';').split(';')
                elif self.question_type == 'dragSort':
                    drag_parts = [question['correct']]  # some parts can repeat
                else:
                    drag_parts = question['correct'].replace('|', ';').split(';')
                drag_parts = [part for part in drag_parts if part]  # Filter out empty strings
                seen_parts = set()
                for part in drag_parts:
                    if part in seen_questions or part in seen_parts:
                        break
                    else:
                        seen_parts.add(part)
                else:
                    seen_questions.update(drag_parts)
                    question_list.append(question)
        else:
            print(f'Warning: Could not generate enough unique questions '
                  f'for question set {self.title} after {max_retries} retries.')
            print(f'Please define more question templates or increase the range of random variables.')
        return question_list

    def render_question_image(self, image_dict: Dict[str, str]) -> str:
        """ Render a png file from the provided description and return its path. """
        image = Image(axis_limits=image_dict.get('axis_limits'),
                      dots=image_dict.get('dots'),
                      texts=image_dict.get('texts'),
                      charts=image_dict.get('charts'),
                      arrows=image_dict.get('arrows'),
                      polygons=image_dict.get('polygons'),
                      angles=image_dict.get('angles'),
                      wedges=image_dict.get('wedges'),
                      lines=image_dict.get('lines'),
                      ellipses=image_dict.get('ellipses'),
                      arcs=image_dict.get('arcs'),
                      table=image_dict.get('table'),
                      pie_chart=image_dict.get('pie_chart'),
                      draw_grid=image_dict.get('draw_grid', True),
                      draw_axes=image_dict.get('draw_axes', True),
                      y_scale=image_dict.get('y_scale', 1),
                      )
        image.output_directory = self.output_directory
        image_path = image.draw_image()
        return image_path

    def render_questions(self, n) -> List[Dict[str, str]]:
        questions = self.generate_questions(questions_to_generate=n)
        questions_with_extra_data = list()
        seen_images = dict()
        for question in questions:
            question['leitidee'] = ''
            question['grade'] = self.grade
            question['capital'] = self.capital
            question['subcapital'] = self.subcapital
            question['title'] = self.title
            question['instruction'] = question.get('instruction') or self.instruction
            question['type'] = self.question_type
            question['hint'] = question.get('hint') or self.hint
            question['visual'] = 'Nein'
            question['solution'] = ''
            question['niveau_start'] = 'G'
            question['niveau_end'] = 'M'
            if question.get('image') and isinstance(question['image'], dict):
                image_dict = question['image']
                image_desc_hash = self._generate_image_description_hash(image_dict)
                if image_desc_hash not in seen_images:
                    rendered_image_path = self.render_question_image(image_dict=image_dict)
                    seen_images[image_desc_hash] = rendered_image_path
                question['image'] = seen_images[image_desc_hash]
                question['visual'] = 'Ja'
            questions_with_extra_data.append(question)
        return questions_with_extra_data
