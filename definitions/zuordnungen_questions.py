from questions import Question, QuestionSet
from random import randint, choice
from definitions.common import female_names, male_names

sachaufgaben = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Dreisatzes',
    title='Sachaufgaben',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='{{name}} möchte sich im Modehaus drei gleich teure Hosen für zusammen {{v1*v2}} € kaufen. '
                'Sie hat {{v1*v3}} € Bargeld in ihrem Portemonnaie. <br><br> '
                '<b>Frage: </b>Wie viele Hosen zu diesem Preis könnte sie sich von ihrem Bargeld eigentlich kaufen?',
            formula='{{v2}} Hosen kosten ___ <br> Somit kostet eine Hose <br><mat>___ €:___ = ___ €. </mat> <br> '
                    'Für {{v1*v3}} € kann sich {{name}} also <br>'
                    '<mat>___</mat> €: <mat>___ </mat> € = <mat>___</mat><br> Hosen kaufen.',
            correct='{{v1*v2}};{{v1*v2}};{{v2}};{{v1}};{{v1*v3}};{{v1}};{{v3}}',
            variables={
                'name': (choice, female_names),
                'v1': (randint, 15, 28),
                'v2': (randint, 2, 4),
                'v3': (randint, 5, 9),
            }),
        ]
)

zuordnungsvorschriften_finden = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Lineare Funktionen',
    title='Zuordnungsvorschriften finden',
    instruction='Bestimme die Zuordnungsvorschrift mithilfe der abgebildeten linearen Funktion.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>P_1 = (x_1|y_1) = (___|___)</mat> <br><mat>P_2 = (x_2|y_2) = (___|___)</mat><br>'
                    'Nutze nun die Formel <br><mat>m = (y_2 - y_1)/(x_2 - x_1)</mat> <br> um die Steigung zu berechnen.'
                    '<br><mat>m = (___ - ___)/(___ - ___) = ___/___ = ___</mat><br>'
                    'Wie lautet die Zuordnungsvorschrift? <br><mat>y = ___*x</mat>',
            correct='{{x1}};{{x1*v1}};{{x2}};{{x2*v1}};'
                    '{{x2*v1}};{{x1*v1}};{{x2}};{{x1}};{{(x2-x1)*v1}};{{x2-x1}};{{v1}};{{v1}}',
            variables={
                'x2': 1,
                'x1': 2,
                'v1': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '-4',
                                'ymax': '{{x1*v1+2}}'},
                'dots': [
                    {'x': '{{x1}}', 'y': '{{x1*v1}}', 'color': 'orange', 'text': 'P1'},
                    {'x': '{{x2}}', 'y': '{{x2*v1}}', 'color': 'orange', 'text': 'P2'},
                ],
                'charts': [
                    {'chart': '{{v1}}*x'},
                ]},
        )]
)

y_achsenabschnitt_ablesen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Lineare Funktionen',
    title='y-Achsenabschnitt ablesen',
    instruction='Wie lautet der yAchsenabschnitt <mat>b</mat>?',
    question_type='gap',
    questions=[
        Question(
            formula='b = ___',
            correct='{{v2}}',
            variables={
                'v1': (randint, 1, 3),
                'v2': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-6}}',
                                'ymax': '{{v2+2}}'},
                'charts': [
                    {'chart': '{{v1}}*x+{{v2}}'},
                ]},
        ),
        Question(
            formula='b = ___',
            correct='{{v2}}',
            variables={
                'v1': (randint, -3, -1),
                'v2': (randint, -5, -1),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-2}}',
                                'ymax': '{{v2+6}}'},
                'charts': [
                    {'chart': '{{v1}}*x+{{v2}}'},
                ]},
        ),
    ]
)

zuordnen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Lineare Funktionen',
    title='Zuordnen',
    instruction='Welche Funktionsvorschrift gehört zu dieser linearen Funktion?',
    question_type='MC',
    questions=[
        Question(
            formula='',
            correct='y={{v1}}*x+({{v2}})',
            wrong_1='y={{(-v1)}}*x+({{(2*v2)|round|int}})',
            wrong_2='y={{(2*v1)|round|int}}*x+({{v2}})',
            variables={
                'v1': (choice, [-2, -1, -0.5, 0.5, 1, 2]),
                'v2': (choice, [-3, -2, -1, 1, 2, 3]),
            },
            image={
                'axis_limits': {'xmin': '-4',
                                'xmax': '4',
                                'ymin': '{{v2-4}}',
                                'ymax': '{{v2+4}}'},
                'charts': [
                    {'chart': '{{v1}}*x+{{v2}}'},
                ]},
        ),
    ]
)

berechne_im_kopf = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Lineare Funktionen',
    title='Berechne im Kopf',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Gegeben sei die Funktionsvorschrift <br> <mat>y = {{v1}}*x</mat>. <br>'
                        'Ergänze zum <mat>x</mat>-Wert den dazugehörigen <mat>y</mat>-Wert.',
            formula='x = {{v3}} <br> y = ___',
            correct='{{v1*v3}}',
            variables={
                'v1': (choice, [-3, -2, -1, 1, 2, 3]),
                'v3': (choice, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
            }),
        Question(
            instruction='Gegeben sei die Funktionsvorschrift <br> <mat>y = {{v1}}*x+({{v2}})</mat>. <br>'
                        'Ergänze zum <mat>x</mat>-Wert den dazugehörigen <mat>y</mat>-Wert.',
            formula='x = {{v3}} <br> y = ___',
            correct='{{v1*v3+v2}}',
            variables={
                'v1': (choice, [-3, -2, -1, 1, 2, 3]),
                'v2': (choice, [-3, -2, -1, 1, 2, 3]),
                'v3': (choice, [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]),
            }),
        ]
)

wertepaare_prufen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Antiproportionale Zuordnungen',
    title='Wertepaare prüfen',
    instruction='Prüfe, ob die beiden Wertepaare zueinander antiproportional sind.',
    question_type='MC',
    questions=[
        Question(
            instruction='Fülle die Lücke',
            formula='Zuordnungen sind antiproportional, wenn alle Wertepaare ____________ sind.',
            correct='produktgleich',
            wrong_1='quotientengleich',
            variables={}),
        Question(
            formula='{{v1}} ⟼ {{v2*v2}} <br> {{v1*v2}} ⟼ {{v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='antiproportional',
            wrong_1='nicht antiproportional',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 8),
            }),
        Question(
            formula='{{v1+1}} ⟼ {{v2*v3}} <br> {{v1*v3}} ⟼ {{v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht antiproportional',
            wrong_1='antiproportional',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        Question(
            formula='{{v1}} ⟼ {{v2*(v3-2)}} <br> {{v1*v3}} ⟼ {{v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht antiproportional',
            wrong_1='antiproportional',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 4),
                'v3': (randint, 7, 15),
            }),
        Question(
            formula='{{v1*v3}} ⟼ {{v2*v3}} <br> {{v1*(v3+1)}} ⟼ {{v2*(v3+1)}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht antiproportional',
            wrong_1='antiproportional',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 6),
                'v3': (randint, 1, 3),
            }),
        Question(
            formula='{{v1}} ⟼ {{v2*v3}} <br> {{v1*v3}} ⟼ {{v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='antiproportional',
            wrong_1='nicht antiproportional',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 7),
            }),
        ]
)

zuordnungen_verstehen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Antiproportionale Zuordnungen',
    title='Zuordnungen verstehen',
    instruction='Ordne dem x-Wert seinen zugehörigen y-Wert zu.',
    question_type='gap',
    questions=[
        Question(
            formula='x = 1 <br> y = ___',
            correct='{{v1}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [1]),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '{{v1+2}}',
                                'ymin': '1',
                                'ymax': '{{v1+2}}'},
                'charts': [
                    {'chart': '{{v1}}/x'},
                ]},
        ),
        Question(
            formula='x = {{v1}} <br> y = ___',
            correct='1',
            variables={
                'v1': (randint, 2, 9),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '{{v1+2}}',
                                'ymin': '1',
                                'ymax': '{{v1+2}}'},
                'charts': [
                    {'chart': '{{v1}}/x'},
                ]},
        ),
        Question(
            formula='x = {{v2}} <br> y = ___',
            correct='{{(v1/v2)|round|int}}',
            variables={
                'v1': (choice, [4, 6, 8, 10, 12]),
                'v2': (choice, [2])
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '{{v1+2}}',
                                'ymin': '1',
                                'ymax': '{{v1+2}}'},
                'charts': [
                    {'chart': '{{v1}}/x'},
                ]},
        ),
        Question(
            formula='x = {{v2}} <br> y = ___',
            correct='{{(v1/v2)|round|int}}',
            variables={
                'v1': (choice, [6, 9, 12]),
                'v2': (choice, [3])
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '{{v1+2}}',
                                'ymin': '1',
                                'ymax': '{{v1+2}}'},
                'charts': [
                    {'chart': '{{v1}}/x'},
                ]},
        ),
    ]
)

zuordnungen_verstehen_mc = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Antiproportionale Zuordnungen',
    title='Zuordnungen verstehen',
    instruction='Welcher Graph stellt eine antiproportionale Zuordnung dar?',
    question_type='MC',
    questions=[
        Question(
            formula='',
            correct='lila',
            wrong_1='gelb',
            wrong_2='blau',
            variables={
                'v1': (randint, 1, 9),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '8',
                                'ymin': '1',
                                'ymax': '8'},
                'charts': [
                    {'chart': '{{v1}}/x', 'color': 'purple'},
                    {'chart': '{{v2}}*x*x', 'color': 'gold'},
                    {'chart': '{{v3}}+2-0.5*x', 'color': 'tab:blue'},
                ]},
        ),
        Question(
            formula='',
            correct='blau',
            wrong_1='lila',
            wrong_2='gelb',
            variables={
                'v1': (randint, 1, 9),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '8',
                                'ymin': '1',
                                'ymax': '8'},
                'charts': [
                    {'chart': '{{v1}}/x', 'color': 'tab:blue'},
                    {'chart': '-x+2+{{v2}}', 'color': 'purple'},
                    {'chart': 'x**2', 'color': 'gold'},
                ]},
        ),
        Question(
            formula='',
            correct='gelb',
            wrong_1='lila',
            wrong_2='blau',
            variables={
                'v1': (randint, 1, 9),
                'v2': (randint, 1, 5),
                'v3': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '8',
                                'ymin': '1',
                                'ymax': '8'},
                'charts': [
                    {'chart': '{{v1}}/x', 'color': 'gold'},
                    {'chart': 'x+2-{{v2}}', 'color': 'purple'},
                    {'chart': '0.5*x', 'color': 'tab:blue'},
                ]},
        ),
        ]
)

sachaufgaben_umgekehrter_dreisatz = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Umgekehrter Dreisatz',
    title='Sachaufgaben',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Eine Tippgemeinschaft aus {{v1}} Leuten hat im Lotto gewonnen. '
                        'Jeder von ihnen erhält {{v2*v3}} €. <br><br>Wie viel hätte jeder von ihnen gewonnen, '
                        'wenn die Tippgemeinschaft aus {{v3}} Personen bestünde und jeder gleich viel bekommt?',
            formula='{{v1}} Tipper haben je <mat>___</mat> € gewonnen. <br> <br> Ein einzelner Tipper hat '
                    '<mat>___</mat> € <mat>*___</mat> = <mat>___</mat> € gewonnen. <br> <br> '
                    'Wären 9 Personen in der Tippgemeinschaft, hätte jeder von ihnen '
                    '<mat>___</mat> € : <mat>___</mat> = <mat>___</mat> € gewonnen.',
            correct='{{v2*v3}};{{v2*v3}};{{v1}};{{v1*v2*v3}};{{v1*v2*v3}};{{v3}};{{v1*v2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (choice, [5, 10, 20, 40, 50, 100]),
                'v3': (randint, 7, 12),
            }),
        Question(
            instruction='Um eine Baugrube auszuheben, benötigen {{v1}} gleich schnelle Bagger {{(v1-1)*v2}} Tage. '
                        '<br><br> Wie viele Tage werden benötigt, wenn ein Bagger ausfällt?',
            formula='Für das Ausheben der Baugrube benötigen {{v1}} Bagger <mat>___</mat> Tage. <br><br> '
                    'Ein einzelner Bagger benötigt <mat>___</mat> d <mat>*___</mat> = <mat>___</mat> d. <br><br> '
                    'Die {{v1-1}} noch funktionsfähigen Bagger benötigen für das Ausheben <mat>___</mat> d : '
                    '<mat>___</mat> = <mat>___</mat> d',
            correct='{{(v1-1)*v2}};{{(v1-1)*v2}};{{v1}};{{v1*(v1-1)*v2}};{{v1*(v1-1)*v2}};{{(v1-1)}};{{v1*v2}}',
            wrong_1='nicht antiproportional',
            variables={
                'v1': (randint, 3, 7),
                'v2': (choice, [5, 10, 20, 40, 50]),
            }),
    ]
)

wertepaare_prufen_proportionale = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Proportionale Zuordnungen',
    title='Wertepaare prüfen',
    instruction='Prüfe, ob die beiden Wertepaare zueinander proportional sind.',
    question_type='MC',
    hint='Wertepaare einer Zuordnung sind zueinander proportional, wenn der Quotient aus vorgegebenen und '
         'zugeordnetem Wert immer gleich ist. Man nennt sie dann quotientengleich.',
    questions=[
        Question(
            instruction='Fülle die Lücke',
            hint='',
            formula='Zuordnungen sind proportional, wenn alle Wertepaare ____________ sind.',
            correct='quotientengleich',
            wrong_1='produktgleich',
            variables={}),
        Question(
            formula='{{v1}} ⟼ {{v1*v2}} <br>{{v3}} ⟼ {{v3*v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='proportional',
            wrong_1='nicht proportional',
            variables={
                'v1': (randint, 4, 8),
                'v2': (randint, 2, 11),
                'v3': (randint, 9, 15)
            }),
        Question(
            formula='{{v1}} ⟼ {{v1*v2}} <br>{{v3}} ⟼ {{v3*v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='proportional',
            wrong_1='nicht proportional',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 11),
                'v3': (randint, 5, 9)
            }),
        Question(
            formula='{{v1}} ⟼ {{v1*v2*2}} <br>{{v3}} ⟼ {{v3*v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht proportional',
            wrong_1='proportional',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 11),
                'v3': (randint, 5, 9)
            }),
        Question(
            formula='{{v1}} ⟼ {{v1*10}} <br>{{v3}} ⟼ {{v3*5}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht proportional',
            wrong_1='proportional',
            variables={
                'v1': (randint, 5, 9),
                'v3': (randint, 9, 15)
            }),
        Question(
            formula='{{v1}} ⟼ {{v1*v2}} <br>{{v3}} ⟼ {{(v3+1)*v2}} <br> '
                    'Die beiden Wertepaare sind zueinander ____________.',
            correct='nicht proportional',
            wrong_1='proportional',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 11),
                'v3': (randint, 5, 9)
            }),
        ]
)

bremsweg_berechnen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Zuordnungen und Schaubilde',
    title='Bremsweg berechnen',
    instruction='Wähle aus, welcher Term im Text beschrieben wird.',
    question_type='MC',
    questions=[
        Question(
            formula='Um den Bremsweg eines Autos zu berechnen wird die Geschwindigkeit x des Autos (in km je h) '
                    'durch {{v1}} geteilt und der Quotient mit sich selber multipliziert.',
            correct='y=(x:{{v1}})^2',
            wrong_1='y=({{v1}}:x)^2',
            wrong_2='y=x^2:{{v1}}',
            variables={
                'v1': (randint, 5, 15)
            }),
        ]
)

bremsweg_berechnen_gap = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Zuordnungen und Schaubilde',
    title='Bremsweg berechnen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Berechne den Bremswerg mit Hilfe des Terms <mat>y=(x:{{v2}})^2</mat> für die folgende Geschwindigkeit.',
            formula='Geschwindigkeit [km/h] = {{v1*v2}} <br> Bremsweg [m] = ___',
            correct='{{(v1**2)|round|int}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (choice, [5, 10, 15, 20]),
            }),
        ]
)

tabelle_ausfullen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Zuordnungen und Schaubilder',
    title='Tabelle ausfüllen',
    instruction='Ordne dem x-Wert seinen zugehörigen y-Wert zu.',
    question_type='gap',
    questions=[
        Question(
            formula='x = {{v2+v1}} <br> y = ___',
            correct='{{v3 - (v1)**2}}',
            variables={
                'v1': (randint, -3, 3),
                'v2': (randint, 1, 5),
                'v3': (randint, 8, 12),
            },
            image={
                'axis_limits': {'xmin': '{{v2-5}}',
                                'xmax': '{{v2+3}}',
                                'ymin': '{{v3-12}}',
                                'ymax': '{{v3+1}}'},
                'charts': [
                    {'chart': '-(x-{{v2}})**2+{{v3}}'},
                ]},
        ),
        Question(
            formula='x = {{v2+v1}} <br> y = ___',
            correct='{{(v1)**2}}',
            variables={
                'v1': (choice, [-3, -2, -1, 1, 2, 3]),
                'v2': (randint, 1, 5),
            },
            image={
                'axis_limits': {'xmin': '{{v2-5}}',
                                'xmax': '{{v2+3}}',
                                'ymin': '-1',
                                'ymax': '9'},
                'charts': [
                    {'chart': '(x-{{v2}})**2'},
                ]},
        ),
        ]
)

hohenprofil_auswerten = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Zuordnungen und Schaubilder',
    title='Höhenprofil ausfüllen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Hier siehst du das Höhenprofil der Wanderung von {{fname}} und {{mname}}. '
                        'Auf welcher Höhe befinden sich die Wanderer nach folgender zurückgelegter Strecke.',
            formula='Strecke [km] = {{v1}} Höhe [m] = ___',
            correct='{{heights[v1]*30}}',
            variables={
                'fname': (choice, female_names),
                'mname': (choice, male_names),
                'v1': (randint, 1, 9),
                'heights': [4, 5, 4, 6, 7, 7, 8, 6, 5, 3, 4],
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '9',
                                'ymin': '0',
                                'ymax': '10'},
                'charts': [
                    {'chart_xs': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     'chart_ys': '{{heights}}',
                     }],
                'dots': [
                    {'x': '0', 'y': '{{heights[0]}}', 'color': 'tab:blue'},
                    {'x': '1', 'y': '{{heights[1]}}', 'color': 'tab:blue'},
                    {'x': '2', 'y': '{{heights[2]}}', 'color': 'tab:blue'},
                    {'x': '3', 'y': '{{heights[3]}}', 'color': 'tab:blue'},
                    {'x': '4', 'y': '{{heights[4]}}', 'color': 'tab:blue'},
                    {'x': '5', 'y': '{{heights[5]}}', 'color': 'tab:blue'},
                    {'x': '6', 'y': '{{heights[6]}}', 'color': 'tab:blue'},
                    {'x': '7', 'y': '{{heights[7]}}', 'color': 'tab:blue'},
                    {'x': '8', 'y': '{{heights[8]}}', 'color': 'tab:blue'},
                    {'x': '9', 'y': '{{heights[9]}}', 'color': 'tab:blue'},
                ],
                'y_scale': 30,
            },
        ),
        Question(
            instruction='Hier siehst du das Höhenprofil der Wanderung von {{fname}} und {{mname}}. '
                        'Auf welcher Höhe befinden sich die Wanderer nach folgender zurückgelegter Strecke.',
            formula='Strecke [km] = {{v1}} Höhe [m] = ___',
            correct='{{heights[v1]*30}}',
            variables={
                'fname': (choice, female_names),
                'mname': (choice, male_names),
                'v1': (randint, 1, 9),
                'heights': [8, 7, 7, 6, 4, 5, 5, 3, 2, 3, 3],
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '9',
                                'ymin': '0',
                                'ymax': '10'},
                'charts': [
                    {'chart_xs': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
                     'chart_ys': '{{heights}}',
                     }],
                'dots': [
                    {'x': '0', 'y': '{{heights[0]}}', 'color': 'tab:blue'},
                    {'x': '1', 'y': '{{heights[1]}}', 'color': 'tab:blue'},
                    {'x': '2', 'y': '{{heights[2]}}', 'color': 'tab:blue'},
                    {'x': '3', 'y': '{{heights[3]}}', 'color': 'tab:blue'},
                    {'x': '4', 'y': '{{heights[4]}}', 'color': 'tab:blue'},
                    {'x': '5', 'y': '{{heights[5]}}', 'color': 'tab:blue'},
                    {'x': '6', 'y': '{{heights[6]}}', 'color': 'tab:blue'},
                    {'x': '7', 'y': '{{heights[7]}}', 'color': 'tab:blue'},
                    {'x': '8', 'y': '{{heights[8]}}', 'color': 'tab:blue'},
                    {'x': '9', 'y': '{{heights[9]}}', 'color': 'tab:blue'},
                ],
                'y_scale': 30,
            },
        ),
        ]
)

preise_vergleichen = QuestionSet(
    grade='7',
    capital='Zuordnungen',
    subcapital='Zuordnungen und Schaubilder',
    title='Zuordnungen verstehen',
    instruction='Mit welchem Term lassen sich die Preise berechnen? X steht für die Menge in Kilogramm',
    question_type='MC',
    questions=[
        Question(
            formula='Kartoffeln',
            correct='x*{{v1}}',
            wrong_1='{{v1}}:x',
            variables={
                'v1': (choice, [0.25, 0.5, 1, 1.5]),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '9',
                                'ymin': '1',
                                'ymax': '9'},
                'dots': [
                    {'x': '4', 'y': '{{4*v1}}', 'color': 'purple', 'text': 'Kartoffeln'},
                    {'x': '2.5', 'y': '{{5*v1}}', 'color': 'tab:brown', 'text': 'Erdbeeren'},
                    {'x': '1', 'y': '{{4*v1}}', 'color': 'green', 'text': 'Äpfel'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}', 'color': 'purple'},
                    {'chart': 'x*2*{{v1}}', 'color': 'tab:brown'},
                    {'chart': 'x*4*{{v1}}', 'color': 'green'},
                ]},
        ),
        Question(
            formula='Erdbeeren',
            correct='x*{{2*v1}}',
            wrong_1='{{2*v1}}:x',
            wrong_2='{{4*v1}}:x',
            variables={
                'v1': (choice, [0.25, 0.5, 1, 1.5]),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '9',
                                'ymin': '1',
                                'ymax': '9'},
                'dots': [
                    {'x': '4', 'y': '{{4*v1}}', 'color': 'purple', 'text': 'Kartoffeln'},
                    {'x': '2.5', 'y': '{{5*v1}}', 'color': 'tab:brown', 'text': 'Erdbeeren'},
                    {'x': '1', 'y': '{{4*v1}}', 'color': 'green', 'text': 'Äpfel'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}', 'color': 'purple'},
                    {'chart': 'x*2*{{v1}}', 'color': 'tab:brown'},
                    {'chart': 'x*4*{{v1}}', 'color': 'green'},
                ]},
        ),
        Question(
            formula='Äpfel',
            correct='x*{{4*v1}}',
            wrong_1='{{4*v1}}:x',
            wrong_2='x+{{v1}}',
            variables={
                'v1': (choice, [0.25, 0.5, 1, 1.5]),
            },
            image={
                'axis_limits': {'xmin': '1',
                                'xmax': '9',
                                'ymin': '1',
                                'ymax': '9'},
                'dots': [
                    {'x': '4', 'y': '{{4*v1}}', 'color': 'purple', 'text': 'Kartoffeln'},
                    {'x': '2.5', 'y': '{{5*v1}}', 'color': 'tab:brown', 'text': 'Erdbeeren'},
                    {'x': '1', 'y': '{{4*v1}}', 'color': 'green', 'text': 'Äpfel'},
                ],
                'charts': [
                    {'chart': 'x*{{v1}}', 'color': 'purple'},
                    {'chart': 'x*2*{{v1}}', 'color': 'tab:brown'},
                    {'chart': 'x*4*{{v1}}', 'color': 'green'},
                ]},
        ),
        ]
)

question_sets = [
    sachaufgaben,
    zuordnungsvorschriften_finden,
    y_achsenabschnitt_ablesen,
    zuordnen,
    berechne_im_kopf,
    wertepaare_prufen,
    zuordnungen_verstehen,
    zuordnungen_verstehen_mc,
    sachaufgaben_umgekehrter_dreisatz,
    wertepaare_prufen_proportionale,
    bremsweg_berechnen,
    bremsweg_berechnen_gap,
    tabelle_ausfullen,
    hohenprofil_auswerten,
    preise_vergleichen,
    ]
