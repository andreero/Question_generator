from math import ceil, floor
from questions import Question, QuestionSet
from random import randint
from images import Image


def randdecimal(low, high, step=0.1):
    low_scaled = ceil(float(low)/step)
    high_scaled = floor(float(high)/step)
    result = round(randint(low_scaled, high_scaled) * step, 1)
    return int(result) if float(result).is_integer() else result


sachsituationen_zuordnen = QuestionSet(
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Sachsituationen zuordnen',
    instruction='Ordne der Sachsituation die korrekte Funktionsvorschrift zu',
    question_type='buttons',
    questions=[
        Question(
            formula='Eine Taxifahrt kostet pro Kilometer {{v1}} €. Der Grundpreis beträgt {{v2}} €.',
            correct='y={{v1}}*x+{{v2}}',
            wrong_1='y={{v1+1}}*x+{{v2-2}}',
            wrong_2='y={{v2*3}}-{{v1}}*x',
            variables={
                'v1': (randdecimal, 1.5, 5, 0.5),
                'v2': (randint, 2, 9)
            }),
        Question(
            formula='Ein Paar Socken kostet im Internet {{v1}} €. Der Versand kostet {{v2}} €.',
            correct='y={{v1}}*x+{{v2}}',
            wrong_1='y={{v1*2}}*x+{{v2}}',
            wrong_2='y={{10*v1}}*x-{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='Ein Kilogramm Kartoffeln kostet im Supermarkt {{v1}} €.',
            correct='y={{v1}}*x',
            wrong_1='y={{v1*2}}*x+{{v2}}',
            wrong_2='y={{v1*5}}-{{v2}}*x',
            variables={
                'v1': (randdecimal, 1, 5, 0.5),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='Ein Auto mit einem {{10*v1}} Liter Tank verbraucht {{v2}} Liter Benzin pro km.',
            correct='y={{10*v1}}-{{v2}}*x',
            wrong_1='y={{v2}}*x+{{v1}}',
            wrong_2='y={{v1}}*x',
            variables={
                'v1': (randint, 3, 15),
                'v2': (randdecimal, 0.1, 0.8, 0.1),
            }),
        ]
)

allgemeine_und_scheitelform = QuestionSet(
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='Allgemeine und Scheitelform',
    instruction='Welche der Funktionsvorschrift en stehen in der allgemeinen Form und welche in der Scheitelform? '
                'Ziehe in die richtige Kategorie.',
    question_type='dragGroup',
    hint='Allgemeine Form: f(x) = ax^2+bx+c <br>Scheitelform: f(x) = a(x-d)^2+e',
    questions=[
        Question(
            formula='',
            correct='allgemeine Form|f(x) = {{v1}}x^2+{{v2}}x-{{v3}}~f(x) = {{v4}}x^2-x+{{v5}}~f(x) = -{{v6}}x^2+{{v7}}x-{{v8}};' +
                    'Scheitelform|f(x) = -(x-{{v9}})^2+{{v10}}~f(x) = {{v11}}(x+{{v12}})^2-{{v13}}~f(x) = -{{v14}}(x+{{v15}})^2 - {{v16}}',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 15),
                'v4': (randdecimal, 0.1, 0.9, 0.1),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 15),
                'v7': (randint, 2, 15),
                'v8': (randint, 2, 15),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 9),
                'v12': (randint, 2, 9),
                'v13': (randdecimal, 0.1, 0.9, 0.1),
                'v14': (randint, 2, 9),
                'v15': (randint, 2, 15),
                'v16': (randint, 2, 15),
            }),
        ]
)

proportionale_funktionen_gap = QuestionSet(
    capital='Funktionen',
    subcapital='Proportionale Funktionen',
    title='Proportionale Funktionen',
    instruction='Fülle die Lücke.',
    question_type='gap',
    questions=[
        Question(
            formula='Eine Zuordnung zweier Größen A und B ist proportional, wenn gilt:<br> '
                    'Wird die Größe A mit einer Zahl multipliziert, '
                    'so wird auch die Größe B mit dieser Zahl ____________. Dasselbe gilt auch für die Division.',
            correct='multipliziert',
            wrong_1='addiert',
            variables={}),
        ]
)

punkte_prufen = QuestionSet(
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Punkte prüfen',
    instruction='Überprüfe, ob der Punkt P(x|y) auf dem jeweiligen Graphen liegt. '
                'Setze dazu den xWert in die Gleichung ein.',
    question_type='gap',
    hint='Jeder Punkt hat einen x und einen y-Wert. Wenn man überprüfen möchte, ob ein Punkt auf einem Graphen liegt, '
         'muss der xWert eingesetzt werden. Kommt der gleiche y-Wert heraus, so liegt der Punkt auf dem Graphen. '
         'Wenn der y-Wert nicht gleich ist, liegt er nicht auf dem Graphen.',
    questions=[
        Question(
            formula='<mat>y = {{v1}}x</mat> <br><br>P({{v2}}|{{v1*v2}})<br><br><mat>y = ___ * ____ = ____ </mat>',
            correct='{{v1}};{{v2}};{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>y = x^2 + {{v1}}</mat> <br><br>P({{v2}}|{{v2**2+v1}})<br><br><mat>y = ___^2 + ___ =___</mat>',
            correct='{{v2}};{{v1}};{{v2**2+v1}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 7),
            }),
        Question(
            formula='<mat>y = x/{{v1}} + {{v2}}</mat> <br><br>P({{v3*v1}}|{{v3+v2}})<br><br><mat>y =  ___/{{v1}} + ___ =___</mat>',
            correct='{{v3*v1}};{{v2}};{{v3+v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 5),
            }),
        Question(
          formula='<mat>y = {{v1}}x + {{v2}}</mat><br><br>P({{v3}}|{{v1*v3+v2}})<br><br><mat>y = {{v1}}*___ + ___ = ___</mat>',
          correct='{{v3}};{{v2}};{{v1*v3+v2}}',
          variables={
              'v1': (randint, 2, 7),
              'v2': (randint, 2, 15),
              'v3': (randint, 1, 5),
          }),
        ]
)

funktionswerte_bestimmen_1 = QuestionSet(
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionswerte bestimmen (1)',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = {{v1}}x - {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 - v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = {{v1}}x + {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 + v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = {{v1}} - {{v2}}x</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1 - v2*v3}}',
            variables={
                'v1': (randint, 15, 30),
                'v2': (randint, 2, 7),
                'v3': (randint, 1, 5),
            }),
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = {{v1}}x - {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 - v2}}',
            variables={
                'v1': (randint, -7, -2),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        ]
)

funktionswerte_bestimmen_2 = QuestionSet(
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionswerte bestimmen (2)',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = x^2 - {{v1}}</mat><br><br><math>x = {{v2}}<br>y = ___</mat>',
            correct='{{v2**2 - v1}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (randint, -5, -1),
            }),
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>>y = ({{v1}} + x)x</mat><br><br><math>x = {{v2}}<br>y = ___</mat>',
            correct='{{v1*v2 + v2**2}}',
            variables={
                'v1': (randint, 3, 15),
                'v2': (randint, -5, -1),
            }),
        Question(
            formula='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.<br><br>'
                    '<mat>y = x^3</mat><br><br><math>x = {{v1}}<br>y = ___</mat>',
            correct='{{v1**3}}',
            variables={
                'v1': (randint, -4, -1),
            }),
        ]
)

funktionsvorschrift_erkennen = QuestionSet(
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionsvorschrift erkennen',
    instruction='',
    question_type='MC',
    hint='Setze in jede Funktionsvorschrift den x-Wert des eingezeichneten Punktes ein und überprüfe, '
         'ob der berechnete y-Wert mit dem y-Wert aus dem Graphen übereinstimmt.',
    questions=[
        Question(
            formula='Welche Funktionsvorschrift gehört zu dem Graphen? Der eingezeichnete Punkt kann dir helfen.',
            correct='y = x^2 + {{v1}}',
            wrong_1='y = -x(x - {{v1}})',
            wrong_2='y = {{v2}}x + {{v1}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 6),
            },
            image={
                'axis_limits': ['-4', '4', '{{v1-4}}', '{{v1+4}}'],
                'dots': ['1;{{1+v1}}'],
                'charts': ['x**2 + {{v1}}'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu dem Graphen? Der eingezeichnete Punkt kann dir helfen.',
            correct='y = -x(x - {{v1}})',  # -x^2 + {{v1}}
            wrong_1='y = {{v2}}x + {{v1}}',
            wrong_2='y = x^2 + {{v1}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 2, 6),
            },
            image={
                'axis_limits': ['{{v1/2-4}}', '{{v1/2+4}}', '{{v1**2/4-4}}', '{{v1**2/4+4}}'],
                'dots': ['1;{{v1-1}}'],
                'charts': ['-x*(x - {{v1}})'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu dem Graphen? Der eingezeichnete Punkt kann dir helfen.',
            correct='y = {{v1}}/x',
            wrong_1='y = x^2 + {{v1}}',
            wrong_2='y = -x(x - {{v1}})',
            variables={
                'v1': (randint, 1, 3),
            },
            image={
                'dots': ['1;{{v1}}'],
                'charts': ['{{v1}}/x'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu dem Graphen? Der eingezeichnete Punkt kann dir helfen.',
            correct='y = {{v1}}x+{{v2}}',
            wrong_1='y = x^2 + {{v1}}',
            wrong_2='y = {{v1}}/x',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randint, 1, 4),
            },
            image={
                'axis_limits': ['-4', '4', '{{v2-4}}', '{{v2+4}}'],
                'dots': ['1;{{v1+v2}}'],
                'charts': ['{{v1}}*x+{{v2}}'],
            },
        ),
    ]
)

lineare_zuordnen = QuestionSet(
    capital='Funktionen',
    subcapital='Lineare Funktionen',
    title='Funktionsvorschrift erkennen',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            formula='Welche Funktionsvorschrift gehört zu der angezeigten linearen Funktion?',
            correct='y = -x + {{v1}} ',
            wrong_1='y = {{v2}} * x - {{v1}}',
            wrong_2='y = {{v3}} * x + {{v4}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 4),
                'v3': (randdecimal, 0.5, 2.5, 0.5),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': ['-4', '4', '{{v1-4}}', '{{4+v1}}'],
                'charts': ['-x + {{v1}}'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu der angezeigten linearen Funktion?',
            correct='y = -{{v1}} * x - {{v2}}',
            wrong_1='y = {{v2}} * x + {{v3}}',
            wrong_2='y = -x + {{v4}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': ['-4', '4', '{{5*(-1)-v2}}', '{{5-v2}}'],
                'charts': ['{{v1}} * x - {{v2}}'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu der angezeigten linearen Funktion?',
            correct='y = {{v1}} * x + {{v2}}',
            wrong_1='y = {{v2}} * x - {{v3}}',
            wrong_2='y = -x + {{v4}}',
            variables={
                'v1': (randdecimal, 0.5, 1.5, 0.5),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': ['-4', '4', '{{5*(-1)+v2}}', '{{5+v2}}'],
                'charts': ['{{v1}} * x + {{v2}}'],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zu der angezeigten linearen Funktion?',
            correct='y = {{v1}} * x - {{v2}}',
            wrong_1='y = {{v2}} * x + {{v3}}',
            wrong_2='y = -x + {{v4}}',
            variables={
                'v1': (randdecimal, 0.5, 1.5, 0.5),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': ['-4', '4', '{{5*(-1)-v2}}', '{{5-v2}}'],
                'charts': ['{{v1}} * x - {{v2}}'],
            },
        ),
    ]
)

proportionale_funktionen_gap_2 = QuestionSet(
    capital='Funktionen',
    subcapital='Proportionale Funktionen',
    title='Proportionale Funktionen',
    instruction='Fülle die Lücke.',
    question_type='gap',
    questions=[
        Question(
            instruction='Martins ältere Schwester fährt auf der Autobahn unverändert mit einer Geschwindigkeit '
                        'von 2,5 km/min von Hamburg nach Berlin. Genau ab dem Zeitpunkt, an dem sie die Grenze '
                        'von Hamburg überqueren, fängt Martin an, die Zeit und die gefahrenen Kilometer aufzuschreiben.'
                        '<br><br> In einer Minute legt Sieeinen Weg von 2,5 km zurück.',
            formula='Wieviel Kilometer fährt Sie in {{v1}} Minuten?',
            correct='{{v1*2.5}}',
            variables={
                'v1': (randdecimal, 5, 30, 5),
            }),
        ]
)

steigungsdreieck = QuestionSet(
    capital='Funktionen',
    subcapital='Proportionale Funktionen',
    title='Steigungsdreieck',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Schaue dir den Graphen der proportionalen Funktion an. '
                        'Nutze das eingezeichnete Steigungsdreieck, um die Steigung <mat>m</mat> zu bestimmen.',
            formula='<mat>m = y/x = ___/___ = ___</mat>',
            correct='{{v1}};1;{{v1}}',
            variables={
                'v1': (randint, 1, 4),
            },
            image={
                'axis_limits': ['-2', '6', '-2', '{{v1*2+4}}'],
                'charts': ['{{v1}} * x'],
                'arrows': [
                    ('1; {{v1}}; 1; 0; x'),
                    ('2; {{v1}}; 0; {{v1}}; y'),
                ],
            },
        ),
        Question(
            instruction='Schaue dir den Graphen der proportionalen Funktion an. '
                        'Nutze das eingezeichnete Steigungsdreieck, um die Funktionsgleichung  zu bestimmen.',
            formula='<mat>y = ___*___</mat>',
            correct='{{v1}};x',
            variables={
                'v1': (randint, 1, 4),
            },
            image={
                'axis_limits': ['-2', '6', '-2', '{{v1*2+4}}'],
                'charts': ['{{v1}} * x'],
                'arrows': [
                    ('1; {{v1}}; 1; 0; x'),
                    ('2; {{v1}}; 0; {{v1}}; y'),
                ],
            },
        ),
        Question(
            instruction='Schaue dir den Graphen der proportionalen Funktion an. '
                        'Nutze das eingezeichnete Steigungsdreieck, um die Steigung <mat>m</mat> zu bestimmen.',
            formula='<mat>m = y/x = ___/___ = ___</mat>',
            correct='{{v1}};1;{{v1}}',
            variables={
                'v1': (randint, -4, -1),
            },
            image={
                'axis_limits': ['-2', '6', '{{v1*2-4}}', '2'],
                'charts': ['{{v1}} * x'],
                'arrows': [
                    ('1; {{v1}}; 1; 0; +1'),
                    ('2; {{v1}}; 0; {{v1}}; y'),
                ],
            },
        ),
        Question(
            instruction='Schaue dir den Graphen der proportionalen Funktion an. '
                        'Nutze das eingezeichnete Steigungsdreieck, um die Funktionsgleichung  zu bestimmen.',
            formula='<mat>__ = ___*___</mat>',
            correct='y;{{v1}};x',
            variables={
                'v1': (randint, -4, -1),
            },
            image={
                'axis_limits': ['-2', '6', '{{v1*2-4}}', '2'],
                'charts': ['{{v1}} * x'],
                'arrows': [
                    ('1; {{v1}}; 1; 0; +1'),
                    ('2; {{v1}}; 0; {{v1}}; y'),
                ],
            },
        ),
    ]
)

question_sets = [
    sachsituationen_zuordnen,
    allgemeine_und_scheitelform,
    proportionale_funktionen_gap,
    punkte_prufen,
    funktionswerte_bestimmen_1,
    funktionswerte_bestimmen_2,
    funktionsvorschrift_erkennen,
    lineare_zuordnen,
    proportionale_funktionen_gap_2,
    steigungsdreieck,
]
