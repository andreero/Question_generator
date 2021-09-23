import os
import subprocess
import sys
import csv
import traceback

# Install necessary libraries, if they're not already installed
try:
    import jinja2
    import matplotlib
    import numexpr
    from slugify import slugify
except ImportError:
    print('Necessary libraries are not installed, trying to install...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    import jinja2
    from slugify import slugify


from question_definitions import question_sets
from config import Config as cfg


def write_questions_to_csv_file(csv_file_path, headers, questions):
    os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
    with open(csv_file_path, 'a+', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if csv_file.tell() == 0:
            writer.writeheader()
        for question in questions:
            writer.writerow(question)


def main(config):
    for question_set in question_sets:
        output_path = config.CSV_FILE_PATH.format(grade=question_set.grade, capital=slugify(question_set.capital))
        question_set.output_directory = os.path.dirname(output_path)
        try:
            generated_questions = question_set.render_questions(n=config.QUESTIONS_PER_QUESTION_SET)
            write_questions_to_csv_file(csv_file_path=output_path,
                                        headers=config.CSV_HEADERS,
                                        questions=generated_questions)
        except Exception as e:
            print(f'Uncaught exception while generating questions from '
                  f'set {question_set.title} in {question_set.capital}')
            raise e

if __name__ == '__main__':
    main(config=cfg)
