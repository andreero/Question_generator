import os


class Config:
    QUESTIONS_PER_QUESTION_SET = 15
    CSV_FILE_PATH = './sheets/{grade}/{capital}.csv'
    CSV_HEADERS = [
        'functionname',
        'capital',
        'subcapital',
        'title',
        'instruction',
        'answer',
        'correct',
        'wrong_1',
        'wrong_2',
        'wrong_3',
        'type',
        'hint',
        'image',
    ]
