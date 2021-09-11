from questions import Question, QuestionSet
from random import randint
from definitions.common import randdecimal


sachsituationen_zuordnen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Sachsituationen zuordnen',
    instruction='Ordne der Sachsituation die korrekte Funktionsvorschrift zu',
    question_type='buttons',
    questions=[
        Question(
            formula='Eine Taxifahrt kostet pro Kilometer {{v1}} €. Der Grundpreis beträgt {{v2}} €.',
            correct='<mat>y={{v1}}*x+{{v2}}</mat>',
            wrong_1='<mat>y={{v1+1}}*x+{{v2-2}}</mat>',
            wrong_2='<mat>y={{v2*3}}-{{v1}}*x</mat>',
            variables={
                'v1': (randdecimal, 1.5, 5, 0.5),
                'v2': (randint, 2, 9)
            }),
        Question(
            formula='Ein Paar Socken kostet im Internet {{v1}} €. Der Versand kostet {{v2}} €.',
            correct='<mat>y={{v1}}*x+{{v2}}</mat>',
            wrong_1='<mat>y={{v1*2}}*x+{{v2}}</mat>',
            wrong_2='<mat>y={{10*v1}}*x-{{v2}}</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='Ein Kilogramm Kartoffeln kostet im Supermarkt {{v1}} €.',
            correct='<mat>y={{v1}}*x</mat>',
            wrong_1='<mat>y={{v1*2}}*x+{{v2}}</mat>',
            wrong_2='<mat>y={{v1*5}}-{{v2}}*x</mat>',
            variables={
                'v1': (randdecimal, 1, 5, 0.5),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='Ein Auto mit einem {{10*v1}} Liter Tank verbraucht {{v2}} Liter Benzin pro km.',
            correct='<mat>y={{10*v1}}-{{v2}}*x</mat>',
            wrong_1='<mat>y={{v2}}*x+{{v1}}</mat>',
            wrong_2='<mat>y={{v1}}*x</mat>',
            variables={
                'v1': (randint, 3, 15),
                'v2': (randdecimal, 0.1, 0.8, 0.1),
            }),
        ]
)

allgemeine_und_scheitelform = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='Allgemeine und Scheitelform',
    instruction='Welche der Funktionsvorschrift en stehen in der allgemeinen Form und welche in der Scheitelform? '
                'Ziehe in die richtige Kategorie.',
    question_type='dragGroup',
    hint='Allgemeine Form: <mat>f(x) = ax^2+bx+c <br>Scheitelform: f(x) = a(x-d)^2+e</mat>',
    questions=[
        Question(
            formula='',
            correct='allgemeine Form|<mat>f(x) = {{v1}}x^2+{{v2}}x-{{v3}}</mat>~<mat>f(x) = {{v4}}x^2-x+{{v5}}</mat>~<mat>f(x) = -{{v6}}x^2+{{v7}}x-{{v8}}</mat>;' +
                    'Scheitelform|<mat>f(x) = -(x-{{v9}})^2+{{v10}}</mat>~<mat>f(x) = {{v11}}(x+{{v12}})^2-{{v13}}</mat>~<mat>f(x) = -{{v14}}(x+{{v15}})^2 - {{v16}}</mat>',
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
    grade='8',
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
    grade='8',
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Punkte prüfen',
    instruction='Überprüfe, ob der Punkt P(x|y) auf dem jeweiligen Graphen liegt. '
                'Setze dazu den x-Wert in die Gleichung ein.',
    question_type='gap',
    hint='Jeder Punkt hat einen x und einen y-Wert. Wenn man überprüfen möchte, ob ein Punkt auf einem Graphen liegt, '
         'muss der x-Wert eingesetzt werden. Kommt der gleiche y-Wert heraus, so liegt der Punkt auf dem Graphen. '
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
    grade='8',
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionswerte bestimmen (1)',
    instruction='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>y = {{v1}}x - {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 - v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='<mat>y = {{v1}}x + {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 + v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='<mat>y = {{v1}} - {{v2}}x</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1 - v2*v3}}',
            variables={
                'v1': (randint, 15, 30),
                'v2': (randint, 2, 7),
                'v3': (randint, 1, 5),
            }),
        Question(
            formula='<mat>y = {{v1}}x - {{v2}}</mat><br><br><math>x = {{v3}}<br>y = ___</mat>',
            correct='{{v1*v3 - v2}}',
            variables={
                'v1': (randint, -7, -2),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        ]
)

funktionswerte_bestimmen_2 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionswerte bestimmen (2)',
    instruction='Setze die x-Werte in die Funktionsgleichung ein und bestimme so die dazugehörigen y-Werte.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>y = x^2 - {{v1}}</mat><br><br><math>x = {{v2}}<br>y = ___</mat>',
            correct='{{v2**2 - v1}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (randint, -5, -1),
            }),
        Question(
            formula='<mat>>y = ({{v1}} + x)x</mat><br><br><math>x = {{v2}}<br>y = ___</mat>',
            correct='{{v1*v2 + v2**2}}',
            variables={
                'v1': (randint, 3, 15),
                'v2': (randint, -5, -1),
            }),
        Question(
            formula='<mat>y = x^3</mat><br><br><math>x = {{v1}}<br>y = ___</mat>',
            correct='{{v1**3}}',
            variables={
                'v1': (randint, -4, -1),
            }),
        ]
)

funktionsvorschrift_erkennen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Funktionsgleichungen',
    title='Funktionsvorschrift erkennen',
    instruction='Welche Funktionsvorschrift gehört zu dem Graphen? ',
    question_type='MC',
    hint='Setze in jede Funktionsvorschrift den x-Wert des eingezeichneten Punktes ein und überprüfe, '
         'ob der berechnete y-Wert mit dem y-Wert aus dem Graphen übereinstimmt.',
    questions=[
        Question(
            formula='Der eingezeichnete Punkt kann dir helfen.',
            correct='<mat>y = x^2 + {{v1}}</mat>',
            wrong_1='<mat>y = -x(x - {{v1}})</mat>',
            wrong_2='<mat>y = {{v2}}x + {{v1}}</mat>',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 6),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v1-4}}',
                                'ymax': '{{v1+4}}'},
                'dots': [
                    {'x': '1', 'y': '{{1+v1}}', 'color': 'orange'},
                ],
                'charts': [
                    {'chart': 'x**2 + {{v1}}'},
                ],
            },
        ),
        Question(
            formula='Der eingezeichnete Punkt kann dir helfen.',
            correct='<mat>y = -x(x - {{v1}})</mat>',  # -x^2 + {{v1}}
            wrong_1='<mat>y = {{v2}}x + {{v1}}</mat>',
            wrong_2='<mat>y = x^2 + {{v1}}</mat>',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 2, 6),
            },
            image={
                'axis_limits': {'xmin': '{{v1/2-4}}',
                                'xmax': '{{v1/2+4}}',
                                'ymin': '{{v1**2/4-4}}',
                                'ymax': '{{v1**2/4+4}}'},
                'dots': [
                    {'x': '1', 'y': '{{v1-1}}', 'color': 'orange'},
                ],
                'charts': [
                    {'chart': '-x*(x - {{v1}})'},
                ],
            },
        ),
        Question(
            formula='Der eingezeichnete Punkt kann dir helfen.',
            correct='<mat>y = {{v1}}/x</mat>',
            wrong_1='<mat>y = x^2 + {{v1}}</mat>',
            wrong_2='<mat>y = -x(x - {{v1}})</mat>',
            variables={
                'v1': (randint, 1, 3),
            },
            image={
                'dots': [
                    {'x': '1', 'y': '{{v1}}', 'color': 'orange'},
                ],
                'charts': [
                    {'chart': '{{v1}}/x'},
                ],
            },
        ),
        Question(
            formula='Der eingezeichnete Punkt kann dir helfen.',
            correct='<mat>y = {{v1}}x+{{v2}}</mat>',
            wrong_1='<mat>y = x^2 + {{v1}}</mat>',
            wrong_2='<mat>y = {{v1}}/x</mat>',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randint, 1, 4),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-4}}',
                                'ymax': '{{v2+4}}'},
                'dots': [
                    {'x': '1', 'y': '{{v1+v2}}', 'color': 'orange'},
                ],
                'charts': [
                    {'chart': '{{v1}}*x+{{v2}}'},
                ],
            },
        ),
    ]
)

lineare_zuordnen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Lineare Funktionen',
    title='Funktionsvorschrift erkennen',
    instruction='Welche Funktionsvorschrift gehört zu der angezeigten linearen Funktion?',
    question_type='MC',
    questions=[
        Question(
            formula='',
            correct='<mat>y = -x + {{v1}}</mat>',
            wrong_1='<mat>y = {{v2}} * x - {{v1}}</mat>',
            wrong_2='<mat>y = {{v3}} * x + {{v4}}</mat>',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 4),
                'v3': (randdecimal, 0.5, 2.5, 0.5),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v1-4}}',
                                'ymax': '{{4+v1}}'},
                'charts': [
                    {'chart': '-x + {{v1}}'},
                ],
            },
        ),
        Question(
            formula='',
            correct='<mat>y = -{{v1}} * x - {{v2}}</mat>',
            wrong_1='<mat>y = {{v2}} * x + {{v3}}</mat>',
            wrong_2='<mat>y = -x + {{v4}}</mat>',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{5*(-1)-v2}}',
                                'ymax': '{{5-v2}}'},
                'charts': [
                    {'chart': '{{v1}} * x - {{v2}}'},
                ],
            },
        ),
        Question(
            formula='',
            correct='<mat>y = {{v1}} * x + {{v2}}</mat>',
            wrong_1='<mat>y = {{v2}} * x - {{v3}}</mat>',
            wrong_2='<mat>y = -x + {{v4}}</mat>',
            variables={
                'v1': (randdecimal, 0.5, 1.5, 0.5),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{5*(-1)+v2}}',
                                'ymax': '{{5+v2}}'},
                'charts': [
                    {'chart': '{{v1}} * x + {{v2}}'},
                ],
            },
        ),
        Question(
            formula='',
            correct='<mat>y = {{v1}} * x - {{v2}}</mat>',
            wrong_1='<mat>y = {{v2}} * x + {{v3}}</mat>',
            wrong_2='<mat>y = -x + {{v4}}</mat>',
            variables={
                'v1': (randdecimal, 0.5, 1.5, 0.5),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 7),
                'v4': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{5*(-1)-v2}}',
                                'ymax': '{{5-v2}}'},
                'charts': [
                    {'chart': '{{v1}} * x - {{v2}}'},
                ],
            },
        ),
    ]
)

proportionale_funktionen_gap_2 = QuestionSet(
    grade='8',
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

quotientengleichheit = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Proportionale Funktionen',
    title='Quotientengleichheit',
    instruction='Rechne den Quotienten <mat>y/x</mat> für das folgende Wertepaare aus.',
    question_type='gap',
    hint='Beispiel: Um den Quotienten <mat>y/x</mat> für das Wertepaar <mat>x=-3</mat> und <mat>y=-7.5</mat> '
         'zu berechnen, muss folgende Gleichung gelöst werden: <br><mat>(-7.5)/(-3)</mat>',
    questions=[
        Question(
            formula='<mat>x = {{v1}}   y = {{v1*v2}}</mat>',
            correct='{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randdecimal, 1.5, 4, 0.5),
            }),
        Question(
            formula='<mat>x = {{v1}}   y = {{v1*v2}}</mat>',
            correct='{{v2}}',
            variables={
                'v1': (randint, -9, -2),
                'v2': (randdecimal, 1.5, 4, 0.5),
            }),
        ]
)

steigungsdreieck = QuestionSet(
    grade='8',
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
                'axis_limits': {'xmin': '-2',
                                'xmax': '6',
                                'ymin': '-2',
                                'ymax': '{{v1*2+4}}'},
                'charts': [
                    {'chart': '{{v1}} * x'},
                ],
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
                'axis_limits': {'xmin': '-2',
                                'xmax': '6',
                                'ymin': '-2',
                                'ymax': '{{v1*2+4}}'},
                'charts': [
                    {'chart': '{{v1}} * x'},
                ],
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
                'axis_limits': {'xmin': '-2',
                                'xmax': '6',
                                'ymin': '{{v1*2-4}}',
                                'ymax': '2'},
                'charts': [
                    {'chart': '{{v1}} * x'},
                ],
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
                'axis_limits': {'xmin': '-2',
                                'xmax': '6',
                                'ymin': '{{v1*2-4}}',
                                'ymax': '2'},
                'charts': [
                    {'chart': '{{v1}} * x'},
                ],
                'arrows': [
                    ('1; {{v1}}; 1; 0; +1'),
                    ('2; {{v1}}; 0; {{v1}}; y'),
                ],
            },
        ),
    ]
)

antiproportionale_funktionen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Antiproportionale Funktionen',
    title='Antiproportionale Funktionen',
    instruction='Rechne das Produkt <mat>x * y</mat> für das folgende Wertepaare aus.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>x = {{v1}} <br> y = {{v2}}</mat>',
            correct='{{v1*v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 11, 25),
            }),
        Question(
            formula='<mat>x = {{v1}} <br> y = {{v1*v2}}</mat>',
            correct='{{v2}}',
            variables={
                'v1': (randint, -9, -2),
                'v2': (randdecimal, 1.5, 4, 0.5),
            }),
        ]
)

schnittpunkte_berechnen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Lineare Funktion',
    title='Schnittpunkte berechnen',
    instruction='Bestimme für jede Funktionsvorschrift den y-Achsenabschnitt.',
    hint='Der <b>y-Achsenabschnitt</b> b kann der Funktionsvorschrift <mat>f(x) = m*x + b</mat> direktentnommen werden.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>f(x) = {{v1}}*x - {{v2}}<br>b = ___</mat>',
            correct='{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            instruction='Bestimme für jede Funktionsvorschrift die Nullstelle.',
            hint='Die Formel für die Nullstelle <mat>x_0</mat>, also den Schnittpunkt mit der x-Achse, '
                 'lautet: <br> <mat>x = -b/m</mat>.',
            formula='<mat>f(x) = {{v1}}*x - {{v1*v2}} <br> x_0 = - ___/___ = ___</mat>',
            correct='{{(-v1*v2)}};{{v1}};{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 3),
            }),
        Question(
            formula='f(x) = {{v1}}*x + {{v2}} <br> b = ___',
            correct='{{v2}}',
            variables={
                'v1': (randint, -9, -2),
                'v2': (randint, 2, 9),
            }),
        Question(
            instruction='Bestimme für jede Funktionsvorschrift die Nullstelle.',
            hint='Die Formel für die Nullstelle <mat>x_0</mat>, also den Schnittpunkt mit der x-Achse, '
                 'lautet: <br> <mat>x = -b/m</mat>.',
            formula='<mat>f(x) = {{v1}}*x + {{v1*v2}} <br> x_0 = - ___/___ = ___</mat>',
            correct='{{v1*v2}};{{v1}};{{v2}}',
            variables={
                'v1': (randint, -8, -2),
                'v2': (randint, -3, -1),
            }),
        ]
)

funktionswerte_bestimmen_1_2 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Geraden durch Punkte',
    title='Funktionswerte bestimmen (1)',
    instruction='Bestimme den y-Achsenabschnitt b mit der Steigung m und dem Punkt P.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>m = {{v1}}<br>P = ({{v2}}|{{v3}})<br><br>b = ___ - ___ * ___ = ___</mat>',
            correct='{{v3}};{{v1}};{{v2}};{{v3-v1*v2}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 4),
            }),
        Question(
            instruction='Bestimme die gesamte Funktionsvorschrift an.',
            formula='<mat>m = {{v1}}<br>P = ({{v2}}|{{v3}})<br><br>f(x) = ___ * ___ + ___</mat>',
            correct='x;{{v1}};{{v3-v1*v2}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 4),
            }),
        Question(
            formula='<mat>m = {{v1}}<br>P = ({{v2}}|{{v3}})<br><br>b = ___ - ___ * ___ = ___</mat>',
            correct='{{v3}};{{v1}};{{v2}};{{v3-v1*v2}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, -4, -1),
                'v3': (randint, -4, -1),
            }),
        Question(
            instruction='Bestimme die gesamte Funktionsvorschrift an.',
            formula='<mat>m = {{v1}}<br>P = ({{v2}}|{{v3}})<br><br>f(x) = ___ * ___ + ___</mat>',
            correct='x;{{v1}};{{v3-v1*v2}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, -4, -1),
                'v3': (randint, -4, -1),
            }),
        ]
)

funktionswerte_bestimmen_2_2 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Geraden durch Punkte',
    title='Funktionswerte bestimmen (2)',
    instruction='Bestimme den y-Achsenabschnitt b mit der Steigung m und dem Punkt P.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>b = {{v1}}<br>P = ({{v2}}|{{v2*v3+v1}})<br><br>m = ( ___ - ___ ) / ___ = ___</mat>',
            correct='{{v2*v3-v1}};{{v1}};{{v2}};{{v3}}',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 3),
            }),
        Question(
            instruction='Bestimme die gesamte Funktionsvorschrift an.',
            formula='<mat>b = {{v1}}<br>P = ({{v2}}|{{v2*v3+v1}})<br><br>f(x) = ___ * ___ + ___ </mat>',
            correct='x;{{v3}};{{v1}}',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 3),
            }),
        ]
)

funktionswerte_bestimmen_3 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Geraden durch Punkte',
    title='Funktionswerte bestimmen (2)',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Wie lauten die Koordinaten der Punkte <mat>P_1</mat> und <mat>P_2</mat>?',
            formula='<mat>P_1 = (x_1|y_1) = ( ___ | ___ )</mat><br><mat>P_2 = (x_2|y_2) = ( ___| ___ )</mat>',
            correct='{{v3}};{{v1*v3+v2}};{{v4}};{{v1*v4+v2}}',
            variables={
                'v1': (randint, 1, 2),
                'v2': (randint, -2, 2),
                'v3': (randint, -3, -1),
                'v4': (randint, 1, 3),
            },
            image={
                'axis_limits': {'xmin': '{{v3-1}}',
                                'xmax': '{{v4+1}}',
                                'ymin': '{{v1*v3+v2-1}}',
                                'ymax': '{{v1*v4+v2+1}}'},
                'dots': [
                    {'x': '{{v3}}', 'y': '{{v1*v3+v2}}', 'color': 'orange', 'text': 'P1'},
                    {'x': '{{v4}}', 'y': '{{v1*v4+v2}}', 'color': 'orange', 'text': 'P2'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}+({{v2}})'},
                ],
            },
        ),
        Question(
            instruction='Berechne die Steigung anhand der folgenden Formel.<br><br><mat>m = y_2 - y_1 / x_2 - x_1</mat>',
            formula='<mat>m = ( ___ -  ___ ) / ( ___ -  ___ ) = ___ / ___ = ___</mat>',
            correct='{{v1*v4+v2}};{{v1*v3+v2}};{{v4}};{{v3}};{{v1*(v4-v3)}};{{v4-v3}};{{v1}}',
            variables={
                'v1': (randint, 1, 2),
                'v2': (randint, -2, 2),
                'v3': (randint, -3, -1),
                'v4': (randint, 1, 3),
            },
            image={
                'axis_limits': {'xmin': '{{v3-1}}',
                                'xmax': '{{v4+1}}',
                                'ymin': '{{v1*v3+v2-1}}',
                                'ymax': '{{v1*v4+v2+1}}'},
                'dots': [
                    {'x': '{{v3}}', 'y': '{{v1*v3+v2}}', 'color': 'orange', 'text': 'P1'},
                    {'x': '{{v4}}', 'y': '{{v1*v4+v2}}', 'color': 'orange', 'text': 'P2'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}+({{v2}})'},
                ],
            },
        ),
        Question(
            instruction='Wie lautet der y-Achsenabschnitt b?',
            formula='<mat>b = ___ </mat>',
            correct='{{v2}}',
            variables={
                'v1': (randint, 1, 2),
                'v2': (randint, -2, 2),
                'v3': (randint, -3, -1),
                'v4': (randint, 1, 3),
            },
            image={
                'axis_limits': {'xmin': '{{v3-1}}',
                                'xmax': '{{v4+1}}',
                                'ymin': '{{v1*v3+v2-1}}',
                                'ymax': '{{v1*v4+v2+1}}'},
                'dots': [
                    {'x': '{{v3}}', 'y': '{{v1*v3+v2}}', 'color': 'orange', 'text': 'P1'},
                    {'x': '{{v4}}', 'y': '{{v1*v4+v2}}', 'color': 'orange', 'text': 'P2'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}+({{v2}})'},
                ],
            },
        ),
        Question(
            instruction='Wie lautet die dazugehörige Zuordnungsvorschrift?',
            formula='<mat>y = ___ * x + ___</mat>',
            correct='{{v1}};{{v2}}',
            variables={
                'v1': (randint, 1, 2),
                'v2': (randint, -2, 2),
                'v3': (randint, -3, -1),
                'v4': (randint, 1, 3),
            },
            image={
                'axis_limits': {'xmin': '{{v3-1}}',
                                'xmax': '{{v4+1}}',
                                'ymin': '{{v1*v3+v2-1}}',
                                'ymax': '{{v1*v4+v2+1}}'},
                'dots': [
                    {'x': '{{v3}}', 'y': '{{v1*v3+v2}}', 'color': 'orange', 'text': 'P1'},
                    {'x': '{{v4}}', 'y': '{{v1*v4+v2}}', 'color': 'orange', 'text': 'P2'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}+({{v2}})'},
                ],
            },
        ),
    ]
)

punkte_prufen_2 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Geraden durch Punkte',
    title='Punkte prüfen',
    instruction='Überprüfe, ob der Punkt P(x|y) auf dem jeweiligen Graphen liegt. '
                'Setze dazu den x-Wert in die Gleichung ein.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>f(x) = {{v1}} * x + {{v2}}</mat><br><br>P({{v3}}|{{v1*v3+v2}})'
                    '<br><br><mat>y = ___ * ___ + ___ = ____ </mat>',
            correct='{{v1}};{{v3}};{{v2}};{{v1*v3+v2}}',
            variables={
                'v1': (randint, -4, -1),
                'v2': (randint, 2, 7),
                'v3': (randint, 1, 4),
            }),
        Question(
            formula='<mat>f(x) = {{v1}} * x + {{v2}}</mat><br><br>P({{v3}}|{{v1*v3+v2}})'
                    '<br><br><mat>y = ___ * ___ + ___ = ____ </mat>',
            correct='{{v1}};{{v3}};{{v2}};{{v1*v3+v2}}',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randint, 2, 7),
                'v3': (randint, 1, 4),
            }),
    ]
)

parabeln_erkennen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='Parabeln erkennen',
    question_type='MC',
    instruction='',
    questions=[
        Question(
            instruction='Ist der Betrag von a kleiner, gleich oder größer als {{v2}}?',
            hint='Allgemeine Form: <mat>f(x) = ax^2 + bx + c</mat><br>Scheitelform: <mat>f(x) = a(xd)^2+e</mat>',
            formula='',
            correct='<mat>|a| > {{v2}}</mat>',
            wrong_1='<mat>|a| < {{v2}}</mat>',
            wrong_2='<mat>|a| = {{v2}}</mat>',
            variables={
                'v1': (randdecimal, 0.5, 2, 0.5),
                'v2': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-4}}',
                                'ymax': '{{v2+4}}'},
                'charts': [
                    {'chart': '{{v1}}*x**2 + {{v2}}'},
                ],
            },
        ),
        Question(
            instruction='Welche Formel gehört zu der Parabel?',
            formula='',
            correct='<mat>y = {{v1}}x^2+{{v2}}</mat>',  # -x^2 + {{v1}}
            wrong_1='<mat>y = -{{v1}}x^2+{{v2}}</mat>',
            variables={
                'v1': (randdecimal, 0.5, 2, 0.5),
                'v2': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-4}}',
                                'ymax': '{{v2+4}}'},
                'charts': [
                    {'chart': '{{v1}}*x**2 + {{v2}}'},
                ],
            },
        ),
    ]
)

scheitelpunkt_ablesen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='Scheitelpunkt ablesen',
    question_type='gap',
    instruction='Wie lautet der Scheitelpunkt?',
    questions=[
        Question(
            hint='Die Scheitelform lautet <br><mat>f(x) = a*(xd)^2+e</mat>.<br> Dabei ist d die Verschiebung auf der '
                 'x-Achse und e die Verschiebung auf der y-Achse. Bei Normalparabeln hat a entweder den Wert 1 oder -1.',
            formula='<mat>S = ( ___ | ___ )</mat>',
            correct='{{v1}};{{v2}}',
            variables={
                'v1': (randint, -4, -1),
                'v2': (randint, 1, 4),
            },
            image={
                'axis_limits': {'xmin': '{{v1-4}}',
                                'xmax': '{{v1+4}}',
                                'ymin': '{{v2-6}}',
                                'ymax': '{{v2+2}}'},
                'charts': [
                    {'chart': '-(x-{{v1}})**2 + {{v2}}'},
                ],
            },
        ),
        Question(
            instruction='Wie lautet die Funktionsvorschrift?',
            formula='<mat>f(x) = ___ ( x - ___ )^2 + ___</mat>',
            correct='-;{{(-v1)}};{{v2}}',
            variables={
                'v1': (randint, -4, -1),
                'v2': (randint, 1, 4),
            },
            image={
                'axis_limits': {'xmin': '{{v1-4}}',
                                'xmax': '{{v1+4}}',
                                'ymin': '{{v2-6}}',
                                'ymax': '{{v2+2}}'},
                'charts': [
                    {'chart': '-(x-{{v1}})**2 + {{v2}}'},
                ],
            },
        ),
    ]
)

funktionsvorschrift_erkennen_2 = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='Funktionsvorschrift erkennen',
    question_type='MC',
    instruction='Welche Funktionsvorschrift passt zu der angezeigten Parabel?',
    questions=[
        Question(
            formula='',
            correct='<mat>f(x) = -{{v1}}*(x - {{v2}})^2 + {{v3}}</mat>',
            wrong_1='<mat>f(x) = 4*(x + 3)^2 - 2</mat>',
            wrong_2='<mat>f(x) = -0,5*(x - {{v2}})^2 - {{v3}}</mat>',
            wrong_3='<mat>f(x) = 1,5*(x - 2)^2 + 2</mat>',
            variables={
                'v1': (randdecimal, 0.5, 1.5, 0.5),
                'v2': (randint, 1, 3),
                'v3': (randint, 1, 3),
            },
            image={
                'axis_limits': {'xmin': '{{v2-4}}',
                                'xmax': '{{v2+4}}',
                                'ymin': '{{v3-6}}',
                                'ymax': '{{v3+2}}'},
                'charts': [
                    {'chart': '-{{v1}}*(x - {{v2}})**2 + {{v3}}'},
                ],
            },
        ),
    ]
)

in_die_allgemeine_form_umrechnen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Quadratische Funktionen',
    title='In die allgemeine Form umrechnen',
    question_type='MC',
    instruction='Rechne die Scheitelform in die allgemeine Form um. '
                'Rechne in kleinen Schritten und benutze die binomischen Formeln.',
    hint='Die ersten beiden binomischen Formeln lauten: <br>'
         '<mat>(a+b)^2 = a^2 + 2ab + b^2</mat>,<br><mat>(ab)^2 = a^2 - 2ab + b^2</mat>.',
    questions=[
        Question(
            formula='<mat>f(x) = {{v1}}(x-{{v2}})^2+{{v3}}</mat><br>'
                    '<mat>f(x) = {{v1}}( ___ ) + {{v3}}</mat><br>'
                    '<mat>f(x)= ___ + {{v3}}</mat><br>'
                    '<mat>f(x)= ___</mat>',
            correct='<mat>x^2-{{2*v2}}x+{{v2**2}}</mat>;'
                    '<mat>{{v1}}x^2-{{v1*2*v2}}x+{{v1*v2**2}}</mat>;'
                    '<mat>{{v1}}x^2-{{v1*2*v2}}x+{{v1*v2**2+v3}}</mat>',
            variables={
                'v1': (randint, 2, 3),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
            },
        ),
    ]
)

wertetabelle_auslesen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Potenzfunktionen',
    title='Wertetabelle auslesen',
    question_type='gap',
    instruction='Berechne für die Funktionsvorschrift für den vorgegebenen x-Wert den dazugehörigen Funktionswert.',
    questions=[
        Question(
            formula='<mat>f(x) = {{v1}}*x^{{v2}} <br> x = {{v3}}</mat>',
            correct='{{v1*v3**v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 3, 3),
                'v3': (randint, 1, 3),
            },
        ),
        Question(
            formula='<mat>f(x) = {{v1}}*x^{{v2}} <br> x = {{v3}}</mat>',
            correct='{{v1*v3**v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 3, 3),
                'v3': (randint, -3, -1),
            },
        ),
        Question(
            formula='<mat>f(x) = {{v1}}*x^{{v2}} <br> x = {{v3}}</mat>',
            correct='{{v1*v3**v2}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 4, 4),
                'v3': (randint, 1, 2),
            },
        ),
        Question(
            formula='<mat>f(x) = {{v1}}*x^{{v2}} <br> x = {{v3}}</mat>',
            correct='{{v1*v3**v2}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 3, 4),
                'v3': (randint, -2, -1),
            },
        ),
    ]
)

funktionvorschriften_zuordnen = QuestionSet(
    grade='8',
    capital='Funktionen',
    subcapital='Potenzfunktionen',
    title='Funktionvorschriften zuordnen',
    question_type='MC',
    instruction='Ordne dem Graph die richtige Funktionsvorschrift zu.',
    questions=[
        Question(
            formula='Welche Funktionsvorschrift gehört zum lila Graph?',
            correct='<mat>f(x) = -{{v1}}x^3</mat>',
            wrong_1='<mat>f(x) = x^5</mat>',
            wrong_2='<mat>f(x) = {{v2}}x^4</mat>',
            wrong_3='<mat>f(x) = -{{v3}}x^2</mat>',
            variables={
                'v1': (randdecimal, 0.1, 0.5, 0.1),
                'v2': (randint, 1, 3),
                'v3': (randdecimal, 0.2, 0.8, 0.2),
            },
            image={
                'charts': [
                    {'chart': '-{{v1}}*(x**3)', 'color': 'purple'},
                    {'chart': 'x**5', 'color': 'C0'},
                    {'chart': '{{v2}}*(x**4)', 'color': 'orange'},
                    {'chart': '-{{v3}}*(x**2)', 'color': 'green'},
                ],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zum blau Graph?',
            correct='<mat>f(x) = -x^5</mat>',
            wrong_1='<mat>f(x) = {{v1}}x^3</mat>',
            wrong_2='<mat>f(x) = -{{v3}}x^2</mat>',
            wrong_3='<mat>f(x) = {{v2}}x^4</mat>',
            variables={
                'v1': (randdecimal, 0.1, 0.5, 0.1),
                'v2': (randint, 1, 3),
                'v3': (randdecimal, 0.1, 0.5, 0.1),
            },
            image={
                'charts': [
                    {'chart': '{{v1}}*(x**3)', 'color': 'purple'},
                    {'chart': '-x**5', 'color': 'C0'},
                    {'chart': '{{v2}}*(x**4)', 'color': 'orange'},
                    {'chart': '-{{v3}}*(x**2)', 'color': 'green'},
                ],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zum orange Graph?',
            correct='<mat>f(x) = -{{v2}}x^4</mat>',
            wrong_1='<mat>f(x) = -x^5</mat>',
            wrong_2='<mat>f(x) = {{v1}}x^3</mat>',
            wrong_3='<mat>f(x) = {{v3}}x^2</mat>',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randdecimal, 0.2, 0.8, 0.2),
                'v3': (randint, 1, 3),
            },
            image={
                'charts': [
                    {'chart': '{{v1}}*(x**3)', 'color': 'purple'},
                    {'chart': '-x**5', 'color': 'C0'},
                    {'chart': '-{{v2}}*(x**4)', 'color': 'orange'},
                    {'chart': '{{v3}}*(x**2)', 'color': 'green'},
                ],
            },
        ),
        Question(
            formula='Welche Funktionsvorschrift gehört zum grün Graph?',
            correct='<mat>f(x) = {{v3}}x^2</mat>',
            wrong_1='<mat>f(x) = x^5</mat>',
            wrong_2='<mat>f(x) = -{{v2}}x^4</mat>',
            wrong_3='<mat>f(x) = -{{v1}}x^3</mat>',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randdecimal, 0.2, 0.6, 0.2),
                'v3': (randdecimal, 0.2, 0.5, 0.1),
            },
            image={
                'charts': [
                    {'chart': '-{{v1}}*(x**3)', 'color': 'purple'},
                    {'chart': 'x**5', 'color': 'C0'},
                    {'chart': '-{{v2}}*(x**4)', 'color': 'orange'},
                    {'chart': '{{v3}}*(x**2)', 'color': 'green'},
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
    quotientengleichheit,
    steigungsdreieck,
    schnittpunkte_berechnen,
    funktionswerte_bestimmen_1_2,
    funktionswerte_bestimmen_2_2,
    funktionswerte_bestimmen_3,
    punkte_prufen_2,
    parabeln_erkennen,
    scheitelpunkt_ablesen,
    funktionsvorschrift_erkennen_2,
    in_die_allgemeine_form_umrechnen,
    wertetabelle_auslesen,
    funktionvorschriften_zuordnen,
]
