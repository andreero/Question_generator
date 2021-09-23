import os


class Config:
    QUESTIONS_PER_QUESTION_SET = 5
    CSV_FILE_PATH = './sheets/{grade}/{capital}.csv'
    CSV_HEADERS = [
        'grade',
        'leitidee',
        'capital',
        'subcapital',
        'title',
        'type',
        'visual',
        'image',
        'instruction',
        'answer',
        'correct',
        'wrong_1',
        'wrong_2',
        'wrong_3',        
        'hint',        
        'solution',
        'niveau_start',
        'niveau_end',
    ]

# 'Klassenstufe': os.environ['grade'],
# 'Leitidee': data['leitidee'],
# 'Oberthema': data['capital'],
# 'Unterthema': data['subcapital'],
# 'Aufgabentitel': data['title'],
# 'Aufgabentyp'  : data['type'],
# 'Visualisierung'  : 'Ja' if data['image'] != '' else 'Nein',
# 'Icon-Datei-Bezeichnung'  : data['image'],
# 'Anweisung': data['instruction'],
# 'Aufgabenstellung'   : data['question'],
# 'Lösung'  : data['correct'],
# 'Lösungf 1'  : data['wrong_1'],
# 'Lösungf 2'  : data['wrong_2'],
# 'Lösungf 3'  : data['wrong_3'],
# 'Hinweis'  : data['hint'],
# 'Rechenweg'  : data['solution'],
# 'Niveaustufe 1'  : data['niveau_start'],
# 'Niveaustufe 2'  : data['niveau_end'],