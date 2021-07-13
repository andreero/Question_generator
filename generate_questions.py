from question_definitions import question_sets
from config import Config as cfg
import csv


def write_questions_to_csv_file(csv_file_path, headers, questions):
    with open(csv_file_path, 'a+', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        if csv_file.tell() == 0:
            writer.writeheader()
        for question in questions:
            writer.writerow(question)


def main(config):
    for question_set in question_sets:
        generated_questions = question_set.render_questions(n=config.QUESTIONS_PER_QUESTION_SET)
        write_questions_to_csv_file(csv_file_path=config.CSV_FILE_PATH,
                                    headers=config.CSV_HEADERS,
                                    questions=generated_questions)


if __name__ == '__main__':
    main(config=cfg)
