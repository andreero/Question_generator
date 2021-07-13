from jinja2 import Template, StrictUndefined
from jinja2.exceptions import UndefinedError
import random
from typing import Dict


class Question:
    def __init__(self, formula, correct, wrong_1=None, wrong_2=None, wrong_3=None, variables=None):
        self.formula = formula
        self.correct = correct
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
        self.variables = variables if variables is not None else {}

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

    def render(self):
        """ Return a randomized question string from the provided question definition. """
        generated_variables = self.generate_variables()
        generated_strings = {
            'answer': self.render_template(template_string=self.formula, template_variables=generated_variables),
            'correct': self.render_template(template_string=self.correct, template_variables=generated_variables),
            'wrong_1': self.render_template(template_string=self.wrong_1, template_variables=generated_variables),
            'wrong_2': self.render_template(template_string=self.wrong_2, template_variables=generated_variables),
            'wrong_3': self.render_template(template_string=self.wrong_3, template_variables=generated_variables),
        }
        return generated_strings


class QuestionSet:
    def __init__(self, capital, subcapital, title, instruction, question_type, questions, function_name=None):
        self.function_name = function_name
        self.capital = capital
        self.subcapital = subcapital
        self.title = title
        self.instruction = instruction
        self.question_type = question_type
        self.questions = questions

    def generate_questions(self, n):
        question_list = []
        for i in range(n):
            question = random.choice(self.questions)
            question_list.append(question.render())
        return question_list

    def render_questions(self, n):
        questions = self.generate_questions(n)
        questions_with_extra_data = list()
        for question in questions:
            question['functionname'] = self.function_name
            question['capital'] = self.capital
            question['subcapital'] = self.subcapital
            question['title'] = self.title
            question['instruction'] = self.instruction
            question['type'] = self.question_type
            questions_with_extra_data.append(question)
        return questions_with_extra_data
