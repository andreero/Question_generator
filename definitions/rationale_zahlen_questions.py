from questions import Question, QuestionSet
from random import randint, choice
from definitions.common import randdecimal, male_names, female_names


koordinaten_zuordnen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Koordinatensystem',
    title='Koordinaten zuordnen',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Bestimme den richtigen Quadranten für den lila Punkt',
            formula='',
            correct='I',
            wrong_1='II',
            wrong_2='III',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'purple'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'gold'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'tab:brown'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'blue'},
                ],
            }),
        Question(
            instruction='Bestimme den richtigen Quadranten für den brauner Punkt',
            formula='',
            correct='III',
            wrong_1='IV',
            wrong_2='II',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'purple'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'gold'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'tab:brown'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'blue'},
                ],
            }),
        Question(
            instruction='Bestimme den richtigen Quadranten für den gelber Punkt',
            formula='',
            correct='II',
            wrong_1='I',
            wrong_2='IV',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'purple'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'gold'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'tab:brown'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'blue'},
                ],
            }),
        Question(
            instruction='Bestimme den richtigen Quadranten für den blauer Punkt',
            formula='',
            correct='IV',
            wrong_1='II',
            wrong_2='I',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'purple'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'gold'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'tab:brown'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'blue'},
                ],
            }),
        Question(
            instruction='Bestimme für lila Punkt seine Koordinaten.',
            formula='',
            correct='({{x4}}|{{y4}})',
            wrong_1='({{x3}}|{{y3}})',
            wrong_2='({{x2}}|{{y2}})',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'gold'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'blue'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Bestimme für brauner Punkt seine Koordinaten.',
            formula='',
            correct='({{x2}}|{{y2}})',
            wrong_1='({{x1}}|{{y1}})',
            wrong_2='({{x3}}|{{y3}})',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'gold'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'blue'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Bestimme für gelber Punkt seine Koordinaten.',
            formula='',
            correct='({{x1}}|{{y1}})',
            wrong_1='({{x4}}|{{y4}})',
            wrong_2='({{x2}}|{{y2}})',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'gold'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'blue'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Bestimme für blauer Punkt seine Koordinaten.',
            formula='',
            correct='({{x3}}|{{y3}})',
            wrong_1='({{x2}}|{{y2}})',
            wrong_2='({{x4}}|{{y4}})',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'gold'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'blue'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
    ]
)

koordinaten_eintragen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Koordinatensystem',
    title='Koordinaten zuordnen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Wie lauten die Koordinaten für den lila eingezeichneten Punkt?',
            formula='Koordinaten: ( ___|___ )',
            correct='{{x4}};{{y4}}',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'blue'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'gold'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Wie lauten die Koordinaten für den brauner eingezeichneten Punkt?',
            formula='Koordinaten: ( ___|___ )',
            correct='{{x2}};{{y2}}',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'blue'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'gold'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Wie lauten die Koordinaten für den gelber eingezeichneten Punkt?',
            formula='Koordinaten: ( ___|___ )',
            correct='{{x3}};{{y3}}',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'blue'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'gold'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
        Question(
            instruction='Wie lauten die Koordinaten für den blauer eingezeichneten Punkt?',
            formula='Koordinaten: ( ___|___ )',
            correct='{{x1}};{{y1}}',
            variables={
                'x1': (randint, 1, 5),
                'y1': (randint, 1, 5),
                'x2': (randint, -5, -1),
                'y2': (randint, 1, 5),
                'x3': (randint, -5, -1),
                'y3': (randint, -5, -1),
                'x4': (randint, 1, 5),
                'y4': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-5',
                                'xmax': '5',
                                'ymin': '-5',
                                'ymax': '5'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{y1}}', 'color': 'blue'},
                    {'x': '{{x2}}', 'y': '{{y2}}', 'color': 'tab:brown'},
                    {'x': '{{x3}}', 'y': '{{y3}}', 'color': 'gold'},
                    {'x': '{{x4}}', 'y': '{{y4}}', 'color': 'purple'},
                ],
            }),
    ]
)

rechenubungen_mit_rationalen_zahlen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit rationalen Zahlen',
    instruction='Addiere die rationalen Zahlen im Kopf',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}+{{v2}}=___',
            correct='{{"%.1f"|format(v1+v2)}}',
            variables={
                'v1': (randdecimal, 2, 9),
                'v2': (randdecimal, 2, 9),
            }),
        Question(
            formula='(-{{v1}})+{{v1}}=___',
            correct='0',
            variables={
                'v1': (randdecimal, 2, 9),
                'v2': (randdecimal, 2, 9),
            }),
        Question(
            formula='{{v1*10}}+{{v2*10}}.{{v3}}=___',
            correct='{{(v1+v2)*10}}.{{v3}}',
            variables={
                'v1': (randint, 11, 29),
                'v2': (randint, 11, 29),
                'v3': (randint, 1, 9),
            }),
        Question(
            formula='{{v1}} + (-{{v2}}) = ___ ',
            correct='{{"%.1f"|format(v1-v2)}}',
            variables={
                'v1': (randdecimal, 50, 90),
                'v2': (randdecimal, 11, 49),
            }),
        ]
)

rechenubungen_mit_bruchen_1_gap = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit Brüchen (1)',
    instruction='Addiere die rationalen Zahlen und wandle Brüche oder Dezimalzahlen um.',
    question_type='gap',
    hint='Um Dezimalzahlen in Brüche umzuwandeln, multipliziere die sie mit dem Nenner des Bruchs, '
         'und nehme das als Zähler. Der Nenner wird vom anderen Bruch einfach übernommen.',
    questions=[
        Question(
            formula='{{v1}}/{{v2}}+{{v3}} <br> = ___+{{v3}}<br> = ___ ',
            correct='{{"%.1f"|format(v1/v2)}};{{"%.1f"|format(v1/v2+v3)}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [5, 10]),
                'v3': (randdecimal, 2, 9),
            }),
        Question(
            formula='-{{v1}}/{{v2}}+{{v3}} <br> = ___+{{v3}}<br> = ___ ',
            correct='{{"%.1f"|format((-v1/v2))}};{{"%.1f"|format((-v1/v2)+v3)}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [5, 10]),
                'v3': (randdecimal, 2, 9),
            }),
        ]
)

rechenubungen_mit_bruchen_1_mc = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit Brüchen (1)',
    instruction='Setze das richtige Vergleichszeichen ein. <br> Berechne zuerst die Terme.',
    question_type='MC',
    questions=[
        Question(
            formula='-{{v1}}+{{v2}}+{{"%.1f"|format(v1-v2)}} ___ 0 ',
            correct='=',
            wrong_1='>',
            wrong_2='<',
            variables={
                'v1': (randdecimal, 3, 7),
                'v2': (randdecimal, 1.1, 2.9),
            }),
        Question(
            formula='1 ___ {{v2}}/{{v1}}+{{v1-v2-1}}/{{v1}} ',
            correct='>',
            wrong_1='=',
            wrong_2='<',
            variables={
                'v1': (randint, 5, 12),
                'v2': (choice, [1, 3]),
            }),
        ]
)

rechenubungen_mit_bruchen_2 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit Brüchen (2)',
    instruction='Addiere die Brüche im Kopf',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}/{{v2}}+{{v2-v1}}/{{v1}} = ___ ',
            correct='1',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 1, 4),
            }),
        Question(
            formula='-{{v1}}/{{v2}} + {{v1+v3}}/{{v2}}',
            correct='{{v3}}/{{v2}}',
            variables={
                'v1': (randint, 11, 29),
                'v2': (randint, 2, 9),
                'v3': (randint, 1, 5),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und löse die Aufgabe.',
            formula='{{v1}}/{{v2*v3}} + {{v4}}/{{v2}}<br> = {{v1}}/{{v2*v3}}+___/{{v2*v3}} <br> = ___',
            correct='{{v4*v3}};{{(v4*v3+v1)}}/{{v2*v3}}',
            variables={
                'v1': (randint, -15, -5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 4),
                'v4': (randint, 2, 5),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und löse die Aufgabe.',
            formula='{{v1}}/{{v2}} + 1/{{v3}}<br> = ___/{{v2*v3}}+___/{{v2*v3}} <br> = ___',
            correct='{{v1*v3}};{{v2}};{{v1*v3+v2}}/{{v2*v3}}',
            variables={
                'v1': (randint, -6, -4),
                'v2': (randint, 2, 3),
                'v3': (choice, [5, 7]),
            }),
        ]
)

rechenubungen_mit_bruchen_3 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit Brüchen (3)',
    instruction='Addiere die rationalen Zahlen und wandle Brüche oder Dezimalzahlen um.',
    question_type='gap',
    questions=[
        Question(
            formula='-{{v1}} +(-{{v2}}/{{v3}})<br> = -{{v1}} +( ___ )<br> = ___',
            correct='-{{"%.1f"|format(v2/v3)}};-{{"%.1f"|format(v1+v2/v3)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (randint, 1, 4),
                'v3': (choice, [5, 10]),
            }),
        Question(
            formula='{{v1}} +(-{{v2}}/{{v3}})<br> = {{v1}} +( ___ )<br> = ___',
            correct='-{{"%.1f"|format(v2/v3)}};{{"%.1f"|format(v1-v2/v3)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (randint, 1, 4),
                'v3': (choice, [5, 10]),
            }),
        Question(
            formula='-{{v1}} +(-{{v2}}/4)<br> = -{{v1}} +( ___ )<br> = ___',
            correct='-{{"%.2f"|format(v2/4)}};-{{"%.2f"|format(v1+v2/4)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (choice, [1, 3]),
            }),
        Question(
            formula='{{v1}} +(-{{v2}}/4)<br> = {{v1}} +( ___ )<br> = ___',
            correct='-{{"%.2f"|format(v2/4)}};{{"%.2f"|format(v1-v2/4)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (choice, [1, 3]),
            }),
        ]
)

rechenubungen_mit_bruchen_4 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Addition rationaler Zahlen',
    title='Rechenübungen mit Brüchen (4)',
    instruction='Addiere die rationalen Zahlen.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}/{{v3}}+(-{{v2}}/{{v3}}) = ___ ',
            correct='{{v1-v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 3, 20),
            }),
        Question(
            formula='{{v1}}/{{v3}}+{{v2}}/{{v3}} = ___ ',
            correct='{{v1+v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 3, 20),
            }),
        ]
)

vorzeichen_bestimmen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Vorzeichen bestimmen',
    instruction='Wie lautet das fehlende Vorzeichen?',
    question_type='MC',
    hint='Sind die Vorzeichen beider Faktoren gleich, ist das Ergebnis positiv. '
         'Sind die Vorzeichen beider Faktoren dagegen unterschiedlich, ist das Ergebnis negativ.',
    questions=[
        Question(
            formula='(-{{v1}}):(-{{v1*2}}) = ___0.5',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{"%.1f"|format(v1*v2)}}:(-{{v1}}) = ___{{v2}}',
            correct='-',
            wrong_1='+',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [0.2, 0.4, 0.6, 0.8]),
            }),
        Question(
            formula='{{"%.1f"|format(v1*v2)}}:{{v2}} = ___{{v1}}',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [0.2, 0.4, 0.5]),
            }),
        ]
)

divisionsaufgaben_dragmatch = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Vorzeichen bestimmen',
    instruction='Ordne den Divisionsaufgaben das richtige Ergebnis zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='1:(-2)|(-0.5);'
                    '1:4|0.25;'
                    '(-1):(-5)|0.2;'
                    '1:10|0.1;'
                    '(-1):3|(-0.\\bar{33})',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{"%.1f"|format(v1*v2)}}:(-{{v1}}) = ___{{v2}}',
            correct='-',
            wrong_1='+',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [0.2, 0.4, 0.6, 0.8]),
            }),
        Question(
            formula='{{"%.1f"|format(v1*v2)}}:{{v2}} = ___{{v1}}',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [0.2, 0.4, 0.5]),
            }),
        ]
)

question_sets = [
    # koordinaten_zuordnen,
    # koordinaten_eintragen,
    rechenubungen_mit_rationalen_zahlen,
    rechenubungen_mit_bruchen_1_gap,
    rechenubungen_mit_bruchen_1_mc,
    rechenubungen_mit_bruchen_2,
    rechenubungen_mit_bruchen_3,
    rechenubungen_mit_bruchen_4,
    vorzeichen_bestimmen,
    ]
