import os
import subprocess
import sys

# Install jinja2 and matplotlib, if it's not already installed
try:
    import jinja2
    import matplotlib
    import numexpr
except ImportError:
    print('Jinja2 or matplotlib are not installed, trying to install...')
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])
    import jinja2


from question_definitions import question_sets
from config import Config as cfg
import csv


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
        question_set.output_directory = os.path.dirname(config.CSV_FILE_PATH)
        generated_questions = question_set.render_questions(n=config.QUESTIONS_PER_QUESTION_SET)
        write_questions_to_csv_file(csv_file_path=config.CSV_FILE_PATH,
                                    headers=config.CSV_HEADERS,
                                    questions=generated_questions)


if __name__ == '__main__':
    main(config=cfg)
