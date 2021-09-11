from questions import Question, QuestionSet
from random import randint, choice
from definitions.common import randdecimal


koordinaten_zuordnen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Koordinatensystem',
    title='Koordinaten zuordnen',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Bestimme den richtigen Quadranten für den lila Punkt.',
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
            instruction='Bestimme den richtigen Quadranten für den brauner Punkt.',
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
            instruction='Bestimme den richtigen Quadranten für den gelber Punkt.',
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
            instruction='Bestimme den richtigen Quadranten für den blauer Punkt.',
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
            formula='<mat>{{v1}}/{{v2}}+{{v3}} <br> = ___+{{v3}}<br> = ___ </mat>',
            correct='{{"%.1f"|format(v1/v2)}};{{"%.1f"|format(v1/v2+v3)}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [5, 10]),
                'v3': (randdecimal, 2, 9),
            }),
        Question(
            formula='<mat>-{{v1}}/{{v2}}+{{v3}} <br> = ___+{{v3}}<br> = ___</mat>',
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
            formula='<mat>-{{v1}}+{{v2}}+{{"%.1f"|format(v1-v2)}} ___ 0 </mat>',
            correct='=',
            wrong_1='>',
            wrong_2='<',
            variables={
                'v1': (randdecimal, 3, 7),
                'v2': (randdecimal, 1.1, 2.9),
            }),
        Question(
            formula='<mat>1 ___ {{v2}}/{{v1}}+{{v1-v2-1}}/{{v1}} </mat>',
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
            formula='<mat>{{v1}}/{{v2}}+{{v2-v1}}/{{v1}} = ___ </mat>',
            correct='1',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 1, 4),
            }),
        Question(
            formula='<mat>-{{v1}}/{{v2}} + {{v1+v3}}/{{v2}}</mat>',
            correct='{{v3}}/{{v2}}',
            variables={
                'v1': (randint, 11, 29),
                'v2': (randint, 2, 9),
                'v3': (randint, 1, 5),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und löse die Aufgabe.',
            formula='<mat>{{v1}}/{{v2*v3}} + {{v4}}/{{v2}}<br> = {{v1}}/{{v2*v3}}+___/{{v2*v3}} <br> = ___</mat>',
            correct='{{v4*v3}};{{(v4*v3+v1)}}/{{v2*v3}}',
            variables={
                'v1': (randint, -15, -5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 4),
                'v4': (randint, 2, 5),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und löse die Aufgabe.',
            formula='<mat>{{v1}}/{{v2}} + 1/{{v3}}<br> = ___/{{v2*v3}}+___/{{v2*v3}} <br> = ___</mat>',
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
            formula='<mat>-{{v1}} +(-{{v2}}/{{v3}})<br> = -{{v1}} +( ___ )<br> = ___</mat>',
            correct='-{{"%.1f"|format(v2/v3)}};-{{"%.1f"|format(v1+v2/v3)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (randint, 1, 4),
                'v3': (choice, [5, 10]),
            }),
        Question(
            formula='<mat>{{v1}} +(-{{v2}}/{{v3}})<br> = {{v1}} +( ___ )<br> = ___</mat>',
            correct='-{{"%.1f"|format(v2/v3)}};{{"%.1f"|format(v1-v2/v3)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (randint, 1, 4),
                'v3': (choice, [5, 10]),
            }),
        Question(
            formula='<mat>-{{v1}} +(-{{v2}}/4)<br> = -{{v1}} +( ___ )<br> = ___</mat>',
            correct='-{{"%.2f"|format(v2/4)}};-{{"%.2f"|format(v1+v2/4)}};',
            variables={
                'v1': (randint, 15, 60),
                'v2': (choice, [1, 3]),
            }),
        Question(
            formula='<mat>{{v1}} +(-{{v2}}/4)<br> = {{v1}} +( ___ )<br> = ___</mat>',
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
            formula='<mat>{{v1}}/{{v3}}+(-{{v2}}/{{v3}}) = ___ </mat>',
            correct='{{v1-v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 3, 20),
            }),
        Question(
            formula='<mat>{{v1}}/{{v3}}+{{v2}}/{{v3}} = ___ </mat>',
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
            formula='<mat>(-{{v1}}):(-{{v1*2}}) = ___0.5</mat>',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{"%.1f"|format(v1*v2)}}:(-{{v1}}) = ___{{v2}}</mat>',
            correct='-',
            wrong_1='+',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [0.2, 0.4, 0.6, 0.8]),
            }),
        Question(
            formula='<mat>{{"%.1f"|format(v1*v2)}}:{{v2}} = ___{{v1}}</mat>',
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
    title='Divisionsaufgaben',
    instruction='Ordne den Divisionsaufgaben das richtige Ergebnis zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1}}:(-{{v1*2}})|(-0.5);'
                    '{{v2}}:{{v2*4}}|0.25;'
                    '(-{{v3}}):(-{{v3*5}})|0.2;'
                    '{{v4}}:{{v4*10}}|0.1;'
                    '(-{{v5}}):{{v5*3}}|(-0.\\bar{33})',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
                'v4': (randint, 1, 5),
                'v5': (randint, 1, 5),
            }),
        ]
)

divisionsaufgaben_dragsort = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Divisionsaufgaben',
    instruction='Schiebe die Divisionsaufgaben in das Feld mit dem richtigen Ergebnis.',
    question_type='dragSort',
    questions=[
        Question(
            formula='',
            correct='0.5|(-{{v1}}):(-{{v1*2}})~{{v2}}.5:{{(v2*2+1)|round|int}};'
                    '-0.5|{{v3}}.5:(-{{(v3*2+1)|round|int}});'
                    '2.5|(-{{v4*5}}):(-{{v4*2}})~{{"%.1f"|format(v5*5)}}:{{"%.1f"|format(v5*2)}};'
                    '-2.5|(-{{v4*5}}):{{v4*2}}~{{"%.1f"|format(v5*5)}}:(-{{"%.1f"|format(v5*2)}});',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
                'v4': (randint, 1, 5),
                'v5': (randdecimal, 0.1, 0.7),
                'v6': (randint, 1, 5),
                'v7': (randdecimal, 0.1, 0.7),
            }),
        ]
)

division_mir_bruchen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Division mir Brüchen',
    instruction='Berechne die Aufgabe.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1*v2}}/{{v3}}:{{v2}} = ___<br> = ___</mat>',
            correct='({{v1*v2}}:{{v2}})/{{v3}}~{{v1*v2}}/({{v3}}:{{v2}});{{v1}}/{{v3}}~{{v1*v2*v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 5),
            }),
        Question(
            formula='<mat>{{v1*v2}}/{{v3}}:{{v2}} = ___<br> = ___',
            correct='{{v1*v2}}/({{v3}}*{{v2}})~({{v1*v2}}*{{v2}})/{{v3}};{{v1}}/{{v3}}~{{v1*v2*v2}}/{{v3}}</mat>',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 4),
                'v3': (randint, 2, 5),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}:{{v3}}/{{v4}} = {{v1}}/{{v2}}*___<br> = ___/___<br> = ___',
            correct='{{v4}}/{{v3}}~{{v3}}/{{v4}};'
                    '{{v1}}*{{v4}}~{{(-v1)}}*{{v4}};'
                    '{{v2}}*{{v3}}~{{v2}}*{{v4}};'
                    '{{v1*v4}}/{{v2*v3}}~{{v1*v3}}/{{v2*v4}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 7),
                'v3': (randint, 2, 4),
                'v4': (randint, 5, 7),
            }),
        ]
)

bruche_dividieren = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Brüche dividieren',
    instruction='Löse die Divisionsaufgabe. Gib das Ergebnis als gekürzten Bruch an.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>5/{{v1}} : {{v2}}</mat>',
            correct='5/{{v1*v2}}',
            variables={
                'v1': (randint, 7, 9),
                'v2': (randint, 7, 9),
            }),
        Question(
            formula='<mat>{{v1*v2}}/{{v2*v3}} : (-{{v1}})</mat>',
            correct='-1/{{v3}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
                'v3': (randint, 2, 5),
            }),
        Question(
            formula='<mat>-{{v1*4}}/{{v1*2}} : {{v2*4}}/{{v1*2}}</mat>',
            correct='-{{v1}}/{{v2}}',
            variables={
                'v1': (choice, [3, 5]),
                'v2': (choice, [4, 6, 7, 8]),
            }),
        Question(
            formula='<mat>{{v1*5}}/{{v3}} : {{v2*5}}/{{v2*v2}}</mat>',
            correct='{{v1*v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 4),
                'v3': (choice, [5, 7, 11]),
            }),
        ]
)

umkehraufgaben_bilden_1_mc = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Umkehraufgaben bilden (1)',
    instruction='Wie lautet die Umkehraufgabe?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}} : Divisor = -{{v2}} <br> Umkehraufgabe: ___ : ___ = ___</mat>',
            correct='{{v1}}~{{v2}}~-{{v1}}~Divisor;'
                    '(-{{v2}})~{{v2}}~(-{{v1}})~Divisor;'
                    'Divisor~(-{{v2}})~{{v1}}~-{{v1}}',
            variables={
                'v1': (randdecimal, 2, 5),
                'v2': (randint, 6, 9),
            }),
        ]
)

umkehraufgaben_bilden_1_gap = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Umkehraufgaben bilden (1)',
    instruction='Berechne den Divisor mit Hilfe der Umkehraufgabe.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>-{{v1}} : ? = 1/{{v2}} <br> Umkehraufgabe: ___ : ___ = ?</mat>',
            correct='-{{v1}};1/{{v2}};-{{v2}}/{{(1/v1)|round|int}}',
            variables={
                'v1': (choice, [0.1, 0.2, 0.25, 0.5]),
                'v2': (choice, [3, 7, 9]),
            }),
        ]
)

umkehraufgaben_bilden_2_mc = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Umkehraufgaben bilden (2)',
    instruction='Wie lautet die Umkehraufgabe?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>Dividend : (-{{v1}}) = {{v2}}.5<br> Umkehraufgabe: ___ __ ___= ___</mat>',
            correct='-{{v1}}~{{v1}}~-{{v2}}.5~Dividend;'
                    '*~:~+~-;'
                    '{{v2}}.5~-{{v2}}.5~{{v1}}~-{{v1}};'
                    'Dividend~-{{v2}}.5~{{v1}}~-{{v1}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 5),
            }),
        ]
)

umkehraufgaben_bilden_2_gap = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Dividieren rationaler Zahlen',
    title='Umkehraufgaben bilden (2)',
    instruction='Berechne den Divisor mit Hilfe der Umkehraufgabe.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>? : (-{{v2}}) = {{v1}}<br> Umkehraufgabe: {{v1}} __ (-{{v2}}) = ___</mat>',
            correct='*;-{{v1*v2}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 3, 9),
            }),
        ]
)

rechenubungen_mit_rationalen_zahlen_2 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit rationalen Zahlen',
    instruction='Subtrahiere die rationalen Zahlen im Kopf',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>-{{v1}}-{{v2}} = ___</mat> ',
            correct='-{{"%.1f"|format(v1+v2)}}',
            variables={
                'v1': (randdecimal, 2, 5),
                'v2': (randdecimal, 2, 5),
            }),
        Question(
            formula='<mat>{{v1}}-{{v2}} = ___ </mat>',
            correct='{{"%.1f"|format(v1-v2)}}',
            variables={
                'v1': (randdecimal, 21, 29),
                'v2': (randdecimal, 11, 19),
            }),
        Question(
            instruction='Subtrahiere die rationalen Zahlen.',
            formula='<mat>{{v1}}-(-{{v2}}) = ___ </mat>',
            correct='{{"%.1f"|format(v1+v2)}}',
            variables={
                'v1': (randdecimal, 11, 15),
                'v2': (randdecimal, 2, 5),
            }),
        Question(
            instruction='Subtrahiere die rationalen Zahlen.',
            formula='<mat>-{{v1}}-(-{{v2}}) = ___ </mat>',
            correct='{{"%.1f"|format(v2-v1)}}',
            variables={
                'v1': (randdecimal, 120, 125),
                'v2': (randdecimal, 130, 135),
            }),
        ]
)

rechenubungen_mit_rationalen_zahlen_2_mc = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit rationalen Zahlen',
    instruction='Setze das richtige Vergleichszeichen ein.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}} ___ {{"%.1f"|format(v2+v1)}}-{{v2}}</mat>',
            correct='=',
            wrong_1='>',
            wrong_2='<',
            variables={
                'v1': (randdecimal, 0.1, 0.9),
                'v2': (randdecimal, 45, 49),
            }),
        Question(
            formula='<mat>{{"%.1f"|format(v1+v2+v3)}}-{{v1}} ___ {{v2}}</mat>',
            correct='>',
            wrong_1='=',
            wrong_2='<',
            variables={
                'v1': (randdecimal, 2, 5),
                'v2': (randdecimal, 2, 5),
                'v3': (randdecimal, 0.1, 0.5),
            }),
        ]
)

rechenubungen_mit_bruchen_1_subtraktion = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit Brüchen (1)',
    instruction='Subtrahiere die rationalen Zahlen und wandle Brüche oder Dezimalzahlen um.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{"%.1f"|format(v1/v3)}}-{{v2}}/{{v3*v4}}'
                    '<br> = (___*{{v3*v4}})/___-{{v2}}/{{v3*v4}}'
                    '<br> = ___/{{v3*v4}}-{{v2}}/{{v3*v4}} = ___',
            correct='{{"%.1f"|format(v1/v3)}};{{v3*v4}};{{v1*v4}};{{v1*v4-v2}}/{{v3*v4}}</mat>',
            variables={
                'v1': (randint, 3, 7),
                'v2': (randint, 2, 9),
                'v3': (choice, [2, 5]),
                'v4': (choice, [2, 3, 4]),
            }),
        Question(
            formula='<mat>-{{v1}}/{{v2}}-{{v3}}<br> '
                    '= ___-{{v3}}<br> '
                    '= ___',
            correct='-{{"%.1f"|format(v1/v2)}};{{"%.1f"|format(v1/v2+v3)}}</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [2, 5, 10]),
                'v3': (randdecimal, 0.1, 1.5),
            }),
        ]
)

rechenubungen_mit_bruchen_2_subtraktion = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit Brüchen (2)',
    instruction='Subtrahiere die rationalen Zahlen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}/{{v2}}-{{v3}}/{{v2}} = ___</mat>',
            correct='-{{v3-v1}}/{{v2}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 9),
                'v3': (randint, 6, 9),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}-{{v3}}/{{v2}} = ___</mat>',
            correct='{{v1-v3}}/{{v2}}',
            variables={
                'v1': (randint, 11, 19),
                'v2': (randint, 2, 9),
                'v3': (randint, 5, 9),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und Subtrahiere die rationalen Zahlen',
            formula='<mat>{{v1}}/{{v2}}-{{v3}}/{{v2*v4}}<br> = ___/{{v2*v4}}-{{v3}}/{{v2*v4}}<br> = ___</mat>',
            correct='{{v1*v4}};{{v1*v4-v3}}/{{v2*v4}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 6),
                'v3': (randint, 11, 15),
                'v4': (randint, 3, 5),
            }),
        Question(
            instruction='Mache die Brüche gleichnamig und Subtrahiere die rationalen Zahlen',
            formula='<mat>{{v1}}/{{v2}}-{{v3}}/{{v4}}<br> = ___/{{v2*v4}}-___/{{v2*v4}}<br> = ___</mat>',
            correct='{{v1*v4}};{{v3*v2}};{{v1*v4-v3*v2}}/{{v2*v4}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 6),
                'v4': (randint, 6, 8),
            }),
        ]
)

rechenubungen_mit_bruchen_3_subtraktion = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit Brüchen (3)',
    instruction='Subtrahiere die rationalen Zahlen.<br> Wandle, wenn nötig, Brüche oder Dezimalzahlen um.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}} -(-{{v2}}/4)<br>= {{v1}}  - (___)<br> = ___</mat>',
            correct='{{"%.2f"|format(-v2/4)}};{{"%.2f"|format(v1+v2/4)}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (choice, [1, 3, 5]),
            }),
        Question(
            formula='<mat>{{v1}} -(-{{v2}}/{{v3}})<br>= {{v1}}  - (___)<br> = ___</mat>',
            correct='{{"%.1f"|format(-v2/v3)}};{{"%.1f"|format(v1+v2/v3)}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (choice, [3, 4, 6, 7, 8, 9]),
                'v3': (choice, [2, 5, 10])
            }),
        Question(
            formula='<mat>{{v1}}-(-{{v2}}/{{v3}})'
                    '<br> = (___*{{v3}})/___ - (-{{v2}}/{{v3}})'
                    '<br> = ___/{{v3}} -(-{{v2}}/{{v3}})'
                    '<br> = ___',
            correct='{{v1}};{{v3}};{{v1*v3}};{{v1*v3+v2}}/{{v3}}</mat>',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 1, 5),
                'v3': (randint, 6, 9)
            }),
        ]
)

rechenubungen_mit_bruchen_4_subtraktion = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Subtraktion rationaler Zahlen',
    title='Rechenübungen mit Brüchen (4)',
    instruction='Subtrahiere die rationalen Zahlen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}/{{v2}}-(-{{v3}}/{{v2}}) = ___</mat>',
            correct='{{v3+v1}}/{{v2}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 7, 15),
                'v3': (randint, 6, 9),
            }),
        ]
)

multiplikation_rationaler_zahlen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Multiplikation rationaler Zahlen',
    instruction='Wähle die korrekte Umformung aus.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}+{{v1}}+{{v1}} = ____________</mat>',
            correct='3*{{v1}}',
            wrong_1='{{v1}}^3',
            wrong_2='3/{{v1}}',
            variables={
                'v1': (randdecimal, 3, 6),
            }),
        Question(
            formula='<mat>{{v1}}+{{v1}}+{{v1}}+{{v1}} = ____________</mat>',
            correct='4*{{v1}}',
            wrong_1='{{v1}}^4',
            wrong_2='4/{{v1}}',
            variables={
                'v1': (randdecimal, 3, 6),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}+{{v1}}/{{v2}}+{{v1}}/{{v2}}+{{v1}}/{{v2}} = ___ * ___</mat>',
            correct='4;{{v1}}/{{v2}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 7),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}+{{v1}}/{{v2}}+{{v1}}/{{v2}}+{{v1}}/{{v2}}+{{v1}}/{{v2}} = = ___ * ___</mat>',
            correct='5;{{v1}}/{{v2}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 7),
            }),
        ]
)

rationale_zahlen_umwandeln_dragmatch = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Rationale Zahlen umwandeln',
    instruction='Ordne den Brüchen ihre Dezimaldarstellung zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='-1/2|-0.5;'
                    '0.75|3/4;'
                    '1/10|0.1;'
                    '-1/4|-0.25;'
                    '1/3|0.\\bar(3)',
            variables={}),
        ]
)

rationale_zahlen_umwandeln = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Rationale Zahlen umwandeln',
    instruction='Streiche alle Brüche, die zu einer inkorrekten Gleichung führen.',
    question_type='MC',
    hint='Der Bruchstrich ist eine andere Schreibweise für das Divisionszeichen. '
         'Daher lässt sich ein Bruch in eine Dezimalzahl umwandeln, indem der Zähler durch den Nenner geteilt wird.',
    questions=[
        Question(
            formula='<mat>___ = = {{"%.1f"|format(v1/2)}}</mat>',
            correct='{{v1}}/2;{{v1*2}}/4;{{v1*4}}/8',
            wrong_1='{{v1*2}}/6;{{v1*2+5}}/10',
            variables={
                'v1': (choice, [3, 5, 7, 9, 11])
            }),
        Question(
            formula='<mat>___ = = -{{"%.2f"|format(v1/4)}}</mat>',
            correct='-{{v1}}/4;-{{v1*2}}/8;-{{v1*25}}/100',
            wrong_1='-{{v1-2}}/2;-{{v1}}/10',
            variables={
                'v1': (choice, [3, 5, 7, 9, 11])
            }),
        ]
)

vorzeichen_bestimmen_multiplikation = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Vorzeichen bestimmen',
    instruction='Ergänze das fehlende Vorzeichen.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>(-{{v1}})*(-{{v2}})=__{{"%.1f"|format(v1*v2)}}</mat>',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randdecimal, 11, 19),
            }),
        Question(
            formula='<mat>{{v2}}*(-{{v1}})=__{{"%.1f"|format(v1*v2)}}</mat>',
            correct='-',
            wrong_1='+',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randdecimal, 0.1, 0.9),
            }),
        Question(
            formula='<mat>-{{v1}}/{{v2}} * {{v3}} = __{{v1*v3}}/{{v2}}</mat>',
            correct='-',
            wrong_1='+',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 3, 9),
                'v3': (randint, 2, 5),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}} * {{v3}}/{{v4}} = __{{v1*v3}}/{{v2*v4}}</mat>',
            correct='+',
            wrong_1='-',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 1, 5),
                'v4': (randint, 2, 5),
            }),
        Question(
            instruction='Setze den korrekten Faktor ein.',
            hint='Ist die Anzahl negativer Faktoren gerade, ist das Ergebnis positiv. '
                 'Bei ungerader Anzahl ist das Ergebnis negativ',
            formula='<mat>{{v1}} * (-{{v2}}) * (-{{v3}}) * 100 * ___ = {{(v1*v2*v3*v4*100)|round|int}}</mat>',
            correct='{{v4}}',
            wrong_1='-{{v4}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randdecimal, 0.1, 0.9),
                'v3': (randdecimal, 0.1, 0.5),
                'v4': (randint, 1, 3),
            }),
        Question(
            instruction='Setze den korrekten Faktor ein.',
            hint='Ist die Anzahl negativer Faktoren gerade, ist das Ergebnis positiv. '
                 'Bei ungerader Anzahl ist das Ergebnis negativ',
            formula='<mat>{{v1}}/{{v2}} * ___ * (-{{v5}}/{{v6}}) = {{v1*v3*v5}}/{{v2*v4*v6}}<br></mat>',
            correct='-{{v3}}/{{v4}}',
            wrong_1='{{v3}}/{{v4}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 1, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 1, 5),
                'v6': (randint, 2, 5),
            }),
        Question(
            instruction='Setze den korrekten Faktor ein.',
            hint='Ist die Anzahl negativer Faktoren gerade, ist das Ergebnis positiv. '
                 'Bei ungerader Anzahl ist das Ergebnis negativ',
            formula='<mat>___ * {{v2}} * (-{{v3}}) * {{v4}} = {{"%.2f"|format(v1*v2*v3*v4)}}</mat>',
            correct='-{{v1}}',
            wrong_1='{{v1}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randdecimal, 0.1, 0.9),
                'v3': (randdecimal, 0.1, 0.5),
                'v4': (randint, 2, 5),
            }),
        ]
)

rationale_dezimalzahlen_multiplizieren = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Rationale Dezimalzahlen multiplizieren',
    instruction='Wie lautet das Ergebnis mit dem richtigen Vorzeichen?',
    question_type='gap',
    hint='Sind die Vorzeichen beider Faktoren gleich, ist das Ergebnis positiv. '
         'Ist nur einer der beiden Faktoren negativ, ist das Ergebnis ebenfalls negativ.',
    questions=[
        Question(
            formula='<mat>(-{{v1}}) * (-{{v2}}) = ___</mat>',
            correct='+{{v1*v2}}',
            variables={
                'v1': (randint, 7, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='<mat>{{"%.1f"|format(v1/2)}} * (-{{v2*2}}) = ___</mat>',
            correct='-{{v1*v2}}',
            variables={
                'v1': (choice, [3, 5, 7, 9, 11]),
                'v2': (randint, 2, 6),
            }),
        ]
)

multiplikation_von_bruchen_1 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Multiplikation von Brüchen (1)',
    instruction='Löse die Aufgaben und gib auch den Zwischenschritt mit an.',
    question_type='gap',
    hint='Brüche werden mit rationalen Zahlen multipliziert, '
         'in dem die rationale Zahl mit dem Zähler multipliziert wird. Der Nenner bleibt gleich.',
    questions=[
        Question(
            formula='<mat>-{{v1}} * {{v2}}/{{v3}} = (___ * ___)/{{v3}} <br>= ___</mat>',
            correct='-{{v1}};{{v2}};-{{v1*v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='<mat>{{v1}} * -{{v2}}/{{v3}} = (___ * ___)/{{v3}} <br>= ___</mat>',
            correct='{{v1}};-{{v2}};-{{v1*v2}}/{{v3}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='<mat>(-{{v1}}) * (-{{v2}}/{{v3}}) = ((___) * (___))/(___)<br> = ___</mat>',
            correct='-{{v1}};-{{v2}};{{v3}};{{(v1*v2)|round|int}}/{{v3}}',
            variables={
                'v1': (choice, [1.5, 2.5, 3.5, 4.5]),
                'v2': (choice, [2, 4, 6, 8]),
                'v3': (randint, 2, 7),
            }),
        ]
)

multiplikation_von_bruchen_2 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Multiplikation von Brüchen (2)',
    instruction='Löse die Aufgaben und gib auch den Zwischenschritt mit an.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}/{{v2}} * {{v3}}/{{v4}} = (___ * ___)/(___ * ___) = ___</mat>',
            correct='{{v1}};{{v3}};{{v2}};{{v4}};{{v1*v3}}/{{v2*v4}}',
            variables={
                'v1': (randint, 1, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 1, 12),
                'v4': (randint, 2, 7),
            }),
        ]
)

multiplikation_von_summen_und_differenzen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Multiplikation rationaler Zahlen',
    title='Multiplikation von Summen und Differenzen',
    instruction='Löse die Aufgabe, indem du die Klammer auflöst und die Rechenzeichen bestimmst.',
    question_type='gap',
    hint='Faktoren dürfen vertauscht werden.',
    questions=[
        Question(
            formula='<mat>-{{v1}} * ({{v2}} + {{v3}}) <br> = ___ + ___<br> = ___</mat>',
            correct='-{{v1*v2}};{{"%.1f"|format(-v1*v3)}};{{"%.1f"|format(-v1*v2-v1*v3)}}',
            variables={
                'v1': (choice, [1.5, 2.5, 3.5, 4.5]),
                'v2': (randint, 2, 7),
                'v3': (randdecimal, 0.2, 0.8, 0.2),
            }),
        Question(
            formula='<mat>-{{v1}}/{{v2}} * ({{v2}}/{{v1}} - {{v2*v3}}) <br> = ___ + ___<br> = ___</mat>',
            correct='-1;{{v3}};{{v3-1}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
                'v3': (randint, 2, 5),
            }),
        ]
)

zahlen_zuordnen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Rationale Zahlen kennenlernen',
    title='Zahlen zuordnen',
    instruction='Ziehe gleiche Zahlenwerte aufeinander.',
    question_type='dragMatch',
    hint='Wenn du die zum Bruch gehörende Dezimalzahl nicht kennst, erweitere den Bruch zu einem Zehnerbruch, '
         'um ihn leicht in eine Dezimalzahl umwandeln zu können.<br>'
         '<i>Beispiel:</i><br> 4/5 = (4*<i>2</i>)/(5*<i>2</i>) = 8/10 = 0.8',
    questions=[
        Question(
            formula='',
            correct='1/2|0.5;'
                    '1/20|0.05;'
                    '1/5|0.2;'
                    '1/10|0.1;'
                    '1/8|0.125',
            variables={}),
        Question(
            formula='',
            correct='{{v1}}/10|0.{{v1}};'
                    '{{v2*v6}}/{{v2*4}}|{{"%.2f"|format(v6/4)}};'
                    '{{v3}}/5|{{"%.1f"|format(v3/5)}};'
                    '{{v4}}/8|{{"%.3f"|format(v4/8)}};'
                    '{{v5}}/10|0.{{v5}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 1, 5),
                'v3': (choice, [1, 2, 3, 4, 6, 7, 8]),
                'v4': (choice, [3, 5, 7, 9, 11, 13]),
                'v5': (randint, 6, 9),
                'v6': (randint, 1, 3),
            }),
        Question(
            formula='',
            correct='{{v1*10+v6}}/100|0.{{v1*10+v6}};'
                    '{{"%.2f"|format(v2/4)}}|{{v2}}/4;'
                    '{{v3}}/5|{{"%.1f"|format(v3/5)}};'
                    '{{v4}}/10|0.{{v4}};'
                    '{{v5}}/20|{{"%.2f"|format(v5/20)}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [1, 2, 3, 5, 6, 7]),
                'v3': (choice, [1, 2, 3, 4, 6, 7, 8]),
                'v4': (randint, 1, 9),
                'v5': (choice, [3, 5, 7, 9, 11, 13, 15, 17]),
                'v6': (choice, [1, 2, 3, 4, 6, 7, 8, 9]),
            }),
        ]
)

temperaturwerte_vergleichen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Rationale Zahlen kennenlernen',
    title='Temperaturwerte vergleichen',
    instruction='',
    question_type='dragGroup',
    questions=[
        Question(
            instruction='Welche Temperaturen sind höher und welche niedriger als {{v1}}°C?',
            formula='',
            correct='niedriger|{{"%.1f"|format(v1+v2)}}°C~{{"%.2f"|format(v1+v3)}}°C~{{"%.1f"|format(v1+v4)}}°C;'
                    'höher|{{"%.1f"|format(v1+v5)}}°C~{{"%.1f"|format(v1+v6)}}°C~{{"%.2f"|format(v1+v7)}}°C',
            variables={
                'v1': (randdecimal, -15, -4),
                'v2': (randdecimal, -0.9, -0.5),
                'v3': (randdecimal, -1.95, -1.15, 0.01, 2),
                'v4': (randdecimal, -0.4, -0.1),
                'v5': (randdecimal, 0.1, 0.5),
                'v6': (randdecimal, 3.6, 5.5),
                'v7': (randdecimal, 1.95, 3.55, 0.01, 2),
            }),
        ]
)

division_durch_0 = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Rechengesetze anwenden',
    title='Division durch 0',
    instruction='Hat dieser Term eine Lösung? Wenn ja, berechne diese anschließend.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}*{{v2}}:0</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randdecimal, 2, 5),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>({{v1}}/{{v2}}-{{"%.1f"|format(v1/v2)}}):({{v3}}*{{v4}})</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [2, 5, 10]),
                'v3': (randdecimal, 2, 5),
                'v4': (randint, 2, 5),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}*{{v2}}/{{v1}}:({{v3}}/{{v4}}-{{v3}}/{{v4}})</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 1, 5),
                'v4': (randint, 6, 9),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}-{{v3}}/{{v4}}:({{v5}}*0)</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 1, 5),
                'v4': (randint, 6, 9),
                'v5': (randdecimal, 2, 5),
            }),
        Question(
            formula='<mat>{{v1}}*1/{{v2}}:1/{{v3}}-{{v4}}/{{v5}}</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 1, 5),
                'v5': (randint, 6, 9),
            }),
        ]
)

vorteilhaftes_rechnen = QuestionSet(
    grade='7',
    capital='Rationale Zahlen',
    subcapital='Rechengesetze anwenden',
    title='Vorteilhaftes Rechnen',
    instruction='Entscheide, wie der Term vereinfacht werden kann.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}*{{v2}}/{{v3}}-{{v4}}/{{v5}}*{{v2}}/{{v3}}+{{v6}}/{{v7}}*{{v2}}/{{v3}}</mat>',
            correct='ausklammern',
            wrong_1='ausmultiplizieren',
            variables={
                'v1': (randdecimal, 2, 5),
                'v2': (randint, 1, 7),
                'v3': (randint, 2, 9),
                'v4': (randint, 1, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 1, 9),
                'v7': (randint, 2, 9),
            }),
        Question(
            formula='<mat>({{"%.2f"|format(v5/v1)}}+{{v2*v5}}-{{v5*v3}}/{{v4*v3}}):{{v5}}</mat>',
            correct='ausmultiplizieren',
            wrong_1='ausklammern',
            variables={
                'v1': (choice, [2, 4]),
                'v2': (randint, 1, 7),
                'v3': (randint, 1, 3),
                'v4': (randint, 2, 9),
                'v5': (choice, [3, 5, 6, 7, 9]),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}*{{v3}}-{{v4}}*{{v3}}+{{v5}}/{{v6}}*{{v3}}</mat>',
            correct='ausklammern',
            wrong_1='ausmultiplizieren',
            variables={
                'v1': (randint, 1, 7),
                'v2': (randint, 2, 9),
                'v3': (randdecimal, 5, 15, 0.01, 2),
                'v4': (randdecimal, 1, 9),
                'v5': (randint, 1, 9),
                'v6': (randint, 2, 9),
            }),
        ]
)

question_sets = [
    koordinaten_zuordnen,
    koordinaten_eintragen,
    rechenubungen_mit_rationalen_zahlen,
    rechenubungen_mit_bruchen_1_gap,
    rechenubungen_mit_bruchen_1_mc,
    rechenubungen_mit_bruchen_2,
    rechenubungen_mit_bruchen_3,
    rechenubungen_mit_bruchen_4,
    vorzeichen_bestimmen,
    divisionsaufgaben_dragmatch,
    divisionsaufgaben_dragsort,
    division_mir_bruchen,
    bruche_dividieren,
    umkehraufgaben_bilden_1_mc,
    umkehraufgaben_bilden_1_gap,
    umkehraufgaben_bilden_2_mc,
    umkehraufgaben_bilden_2_gap,
    rechenubungen_mit_rationalen_zahlen_2,
    rechenubungen_mit_rationalen_zahlen_2_mc,
    rechenubungen_mit_bruchen_1_subtraktion,
    rechenubungen_mit_bruchen_2_subtraktion,
    rechenubungen_mit_bruchen_3_subtraktion,
    rechenubungen_mit_bruchen_4_subtraktion,
    multiplikation_rationaler_zahlen,
    rationale_zahlen_umwandeln_dragmatch,
    rationale_zahlen_umwandeln,
    vorzeichen_bestimmen_multiplikation,
    rationale_dezimalzahlen_multiplizieren,
    multiplikation_von_bruchen_1,
    multiplikation_von_bruchen_2,
    multiplikation_von_summen_und_differenzen,
    zahlen_zuordnen,
    temperaturwerte_vergleichen,
    division_durch_0,
    vorteilhaftes_rechnen,
    ]
