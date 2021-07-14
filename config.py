import os


class Config:
    QUESTIONS_PER_QUESTION_SET = 10
    grade = os.environ.get('grade')
    mode = os.environ.get('capital')
    CSV_FILE_PATH = "./sheets/"+grade+"/"+mode+".csv"
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
        'image',
    ]
