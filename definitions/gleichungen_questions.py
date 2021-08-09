from questions import Question, QuestionSet
from random import randint
from definitions.common import randdecimal


definitionsmenge_2_dragmatch = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Bruchgleichungen',
    title='Definitionsmenge (2)',
    instruction='Ordne die Bruchgleichungen ihrer Definitionsmenge zu. Die Grundmenge sind die reellen Zahlen ℝ.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='1/(x-{{v0}})={{v1}}|ℝ \\ {{"{"}}{{v0}}{{"}"}};'
                    '({{v2}}x)/(x-{{v3}})={{v4}}/x|ℝ \\ {{"{"}}0, {{v3}}{{"}"}};'
                    '1/(x+{{v5}})=1/(x+{{v6}})|ℝ \\ {{"{"}}-{{v5}}, -{{v6}}{{"}"}};'
                    '{{v9}}/(x^2-{{v7**2}})=3/(x^2-{{v8**2}})|ℝ \\ {{"{"}}-{{v8}}, -{{v7}}, {{v7}}, {{v8}}{{"}"}}',
            variables={
                'v0': (randint, 2, 19),
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 5),
                'v6': (randint, 6, 9),
                'v7': (randint, 1, 3),
                'v8': (randint, 4, 7),
                'v9': (randint, 1, 5),
            }),
        Question(
            instruction='Ordne die Bruchgleichungen ihrer Definitionsmenge zu. Die Grundmenge sind die rationalen Zahlen ℚ.',
            formula='',
            correct='{{v1}}/(x-{{v2}})={{v3}}|ℚ \\ {{"{"}}{{v2}}{{"}"}};'
                    'x/(x-{{v4}})=x^2/({{v5}}-x)|ℚ \\ {{"{"}}{{v4}}, {{v5}}{{"}"}};'
                    '{{v8}}/(x+{{v7}})=({{v9}}x)/(x+{{v7}})|ℚ \\ {{"{"}}-{{v7}}{{"}"}};'
                    '{{v10}}/(x^2-{{v11**2}})={{v13}}/(x^2+{{v12}})|ℚ \\ {{"{"}}-{{v11}}, {{v11}}{{"}"}};',
            variables={
                'v0': (randint, 2, 9),
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 19),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 19),
                'v8': (randint, 1, 9),
                'v9': (randint, 2, 9),
                'v10': (randint, 1, 9),
                'v11': (randint, 2, 9),
                'v12': (randint, 2, 9),
                'v13': (randint, 2, 9),
            }),
    ]
)

null_als_produkt_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen lösen',
    title='Null als Produkt (1)',
    instruction='Von welchen Gleichungen ist L nicht die Lösungsmenge?',
    question_type='MC',
    questions=[
        Question(
            formula='L = {{"{"}}0;-{{v1}}{{"}"}};',
            correct='(x-{{v1}})*({{v1}}-x)=0',
            wrong_1='(x+{{v1}})*x=0',
            wrong_2='(x/{{v1}}+1)*{{v1}}x=0',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='L = {{"{"}}-{{v1}};{{v2}}{{"}"}}',
            correct='({{v3}}x-{{v3*v2}})*(x-{{v1}})=0',
            wrong_1='({{v4}}x+{{v4*v1}})*(x-{{v2}})=0',
            wrong_2='(x+{{v1}})*(x-{{v2}})=0',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
            }),
        ]
)

null_als_produkt_dragmatch = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen lösen',
    title='Null als Produkt (1)',
    instruction='Ordne den Lösungsmengen die passende Gleichung zu.',
    question_type='dragMatch',
    hint='Um die richtige Gleichung zu finden, kannst du die Werte aus der Lösungsmenge in die Gleichungen einsetzen. '
         '<br>Die Lösungsmenge L=ℝ umfasst die Menge der reellen Zahlen. '
         'Das bedeutet, dass für x jeder reelle Zahle eingesetzt werden kann.',
    questions=[
        Question(
            formula='',
            correct='L={{"{"}}0,-{{v1}}{{"}"}}|(x+{{v1}})*x=0;'
                    'L=ℝ|(x+{{v2}})*0=0;'
                    'L={{"{"}}{{v3}},{{v4}}{{"}"}}|({{v3}}-x)*({{v4}}-x)=0;'
                    'L={{"{"}}-{{v5}},{{v6}}{{"}"}}|({{v5}}+x)*({{v6}}-x)=0',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 30),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 5, 20),
            }),
    ]
)

ruckwartsrechnen_mit_probe_1_dragmatch = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen lösen',
    title='Rückwärtsrechnen mit Probe (1)',
    instruction='Ziehe die entsprechenden Umkehroperationen zueinander.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='Multiplikation ⋅|Division :;'
                    'Addition +|Subtraktion -',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 30),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 5, 20),
            }),
    ]
)

ruckwartsrechnen_mit_probe_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen lösen',
    title='Rückwärtsrechnen mit Probe (1)',
    instruction='Löse die Gleichung, indem du rückwärts rechnest. Führe danach die Probe durch.',
    question_type='gap',
    questions=[
        Question(
            formula='x + {{v1}} = {{10*v2}} | ___    x = ___',
            correct='-{{v1}};{{10*v2-v1}}',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 7),
            }),
        Question(
            formula='x : {{v1}} = {{v2}} | ___    x = ___',
            correct='*{{v1}};{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 10),
            }),
        Question(
            formula='-{{v1}}x = {{v1*v2}} | ___    x = ___',
            correct=':-{{v1}};-{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 10),
            }),
        Question(
            instruction='Führe die Probe für diese Gleichung durch.',
            formula='x + {{v1}} = {{10*v2}} x = {{10*v2-v1}}    ___ + {{v1}} = {{10*v2}}    ___ = {{10*v2}}',
            correct='{{10*v2-v1}};{{10*v2}}',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 7),
            }),
        Question(
            instruction='Führe die Probe für diese Gleichung durch.',
            formula='x : {{v1}} = {{v2}}  x = {{v1*v2}}   '
            '___ : {{v1}} = {{v2}}   ___ = {{v2}}',
            correct='{{v1*v2}};{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 10),
            }),
        Question(
            instruction='Führe die Probe für diese Gleichung durch.',
            formula='-{{v1}}x = {{v1*v2}}   x = ___   '
            '-{{v1}} * ___ = {{v1*v2}}    ___ = {{v1*v2}}',
            correct='-{{v2}};{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 10),
            }),
    ]
)

verhaltnisgleichungen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen lösen',
    title='Verhältnisgleichungen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Kevin kann bei seiner Handykamera unterschiedliche Bildformate auswählen. Er wählt das '
                        'Format <b>4:3</b> und macht ein hochkant ausgerichtetes Foto. Das Handy zeigt an, dass das '
                        'entstehende Bild eine Breite von {{v1*1000}} Pixeln hat. <br><br>Stelle die Verhätnisgleichung '
                        'auf und löse sie.',
            formula='Die Höhe a verhält sich zur Breite b ({{v1*1000}} Pixel) wie 4 zu 3.<br><br> '
                    'a / b = c / d<br> a / ____ px = ___ / ___',
            correct='{{v1*1000}};4;3',
            variables={
                'v1': (randint, 1, 6),
            }),
        Question(
            instruction='Kevin kann bei seiner Handykamera unterschiedliche Bildformate auswählen. Er wählt das '
                        'Format <b>4:3</b> und macht ein hochkant ausgerichtetes Foto. Das Handy zeigt an, dass das '
                        'entstehende Bild eine Breite von {{v1*1000}} Pixeln hat. <br><br>Runde die Höhe auf eine ganze Zahl.',
            formula='a / {{v1*1000}} px = 4 / 3   | ___ px'
                    '<br> ___ = 4 / 3 * ___ px<br> ≈ ___ px',
            correct='*{{v1*1000}};a;{{v1*1000}};{{(v1*1000*4/3)|round|int}}',
            variables={
                'v1': (randint, 1, 6),
            }),
        Question(
            instruction='Löse die Aufgabe mit einer Verhältnisgleichung.',
            formula='{{v1}} kg Reis kosten {{v2*v1}} €. Der Preis für {{v3}} kg Reis beträgt x.  a / b = c / d '
                    '<br> {{v1}} kg / ___ = ___ / ___',
            correct='{{v2*v1}} €;{{v3}} kg;x',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 2, 5),
                'v3': (randint, 16, 30),
            }),
        Question(
            instruction='Bilde den Kehrwert, um nach x aufzulösen.',
            formula='{{v1}} kg / {{v2*v1}} € = {{v3}} kg / x  | Kehrwert'
                    '<br> {{v2*v1}} € / ___ = ___ / ___<br> ___ € = x',
            correct='{{v1}} kg;x;{{v3}} kg;{{v3*v2}}',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 2, 5),
                'v3': (randint, 16, 30),
            }),
        ]
)

aussagen_und_aussageformen_draggroup = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Aussagen und Aussageformen',
    instruction='Ordne die mathematischen Ausdrücke der richtigen Kategorie zu.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='Aussage|{{v1}}+{{v2}}={{v1+v2}}~{{v3}}-{{v4}}={{v3-v4}}~{{v5}}+{{v6}}>{{v5+v6-5}};'
                    'Aussageform|{{v7}}+x={{v8}}~{{v9}}+x>{{v10}}~{{v11}}+x=y',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 15),
                'v4': (randint, 2, 15),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 15),
                'v7': (randint, 2, 15),
                'v8': (randint, 2, 15),
                'v9': (randint, 2, 15),
                'v10': (randint, 10, 19),
                'v11': (randint, 2, 15),
            }),
    ]
)

gleichungen_aufstellen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Gleichungen aufstellen',
    instruction='Welche dieser Gleichungen passt zum Text?',
    question_type='MC',
    questions=[
        Question(
            formula='Marcos Vater ist heute dreimal so alt wie sein Sohn, in {{v1}} Jahren aber nur noch zweimal so alt. Wie alt sind Marco und Marcos Vater heute?',
            correct='3x+{{v1}}=2(x+{{v1}})',
            wrong_1='3x=2(x+{{v1}})',
            wrong_2='3x+{{v1}}=2x',
            variables={
                'v1': (randint, 10, 15),
            }),
        Question(
            formula='Angie hat x Stücke Schokolade. Rolf hat nur ein Viertel davon. Rolf klaut {{v1*2}} Stücke von Angie, wodurch sich die Anzahl von Rolfs Stücken verdreifacht. Wie viele Stücke Schokolade gibt es insgesamt?',
            correct='x/4+{{v1*2}}=(3x)/4',
            wrong_1='(x/4=(3x)/4',
            wrong_2='x/4=(3x)/4+{{v1*2}}',
            variables={
                'v1': (randint, 2, 6),
            }),
        ]
)


ungleichungen_draggroup = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Ungleichungen',
    instruction='Ordne die Aussageformen der richtigen Kategorie zu.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='Gleichung|{{v1}}x+{{v2}}=-{{v3}}~x^2-x={{v4}}y-{{v5}}y^2~x/{{v6}} + {{v7}} = 0;'
                    'Ungleichung|{{v8}}-{{v9}}x > 0~x^2-{{v10}}x + {{v1}} < -x^3~{{v12}}+x>={{v13}}y+{{v14}}',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 15),
                'v4': (randint, 2, 15),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 15),
                'v7': (randint, 2, 15),
                'v8': (randint, 2, 15),
                'v9': (randint, 2, 15),
                'v10': (randint, 2, 15),
                'v11': (randint, 2, 15),
                'v12': (randint, 2, 15),
                'v13': (randint, 2, 15),
                'v14': (randint, 2, 15),
            }),
    ]
)

losungen_der_gleichung_mc = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Lösungen der Gleichung',
    instruction='Prüfe ob die Zahl Lösung der Gleichung ist',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}x - {{v2}} = {{v1+1}}x + {{v3}}  x = {{v3-v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x - {{v2}} = {{v1+1}}x + {{v3}}  x = -{{v3+v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
            }),
        Question(
            formula='{{v1}}x^2 = {{(v2+1)*v1}}x - {{v1}}x  x = {{v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 3),
            }),
        ]
)

losungen_der_gleichung_gap = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Lösungen der Gleichung',
    instruction='Löse die Gleichung durch Einsetzen.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}x - {{v2}} = {{v1+1}}x + {{v3}}  x = {{v3-v2}}  ___ = ___',
            correct='{{v1*(v3-v2)-v2}};{{(v1+1)*(v3-v2) + v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x - {{v2}} = {{v1+1}}x + {{v3}}  x = -{{v3+v2}}  ___ = ___',
            correct='{{v1*(-v3-v2) - v2}};{{(v1+1)*(-v3-v2) + v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
            }),
        Question(
            formula='{{v1}}x^2 = {{(v2+1)*v1}}x - {{v1}}x  x = {{v2}}  ___ = ___',
            correct='{{v1*v2**2}};{{(v2+1)*v1*v2 - v1*v2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 3),
            }),
        ]
)

ungleichungen_dragmatch = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Gleichungen und Ungleichungen aufstellen',
    title='Ungleichungen',
    instruction='Ordne die Gleichungen ihrer Lösungsmenge zu. Der Variablengrundbereich sind die natürlichen Zahlen.',
    question_type='dragMatch',
    hint='L = {} wird leere Lösungsmenge genannt. Gleichungen haben leere Lösungsmengen, wenn für die Variablen kein '
         'Element des Variablengrundbereichs eingesetzt werden kann.',
    questions=[
        Question(
            formula='',
            correct='{{v1}}x-{{v2*v1}}=0|{{"{"}}{{v2}}{{"}"}};'
                    '{{v3}}x-{{v4*v5}}={{v3+v4}}x|{{"{"}}{{v5}}{{"}"}};'
                    '{{v7}}x^2={{v7*v8**2}}|{{"{"}}{{v8}}{{"}"}};'
                    '(x+{{v9}})(x-{{v10}})=0|{{"{"}}{{v10}}{{"}"}};',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 9),
                'v4': (randint, 1, 4),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 15),
                'v7': (randint, 2, 15),
                'v8': (randint, 1, 3),
                'v9': (randdecimal, 0.25, 1, 0.25),
                'v10': (randint, 2, 15),
            }),
        Question(
            formula='',
            correct='x-{{v1}}=0|{{"{"}}{{v1}}{{"}"}};'
                    '-{{v2}}x+{{v3*v2}}=-{{v2+1}}x+{{(v3+1)*v2}}|{{"{"}}{{v3}}{{"}"}};'
                    '{{v4}}x-{{v5}}={{v4}}x-{{v5}}|ℤ;'
                    '{{v6}}x=1|{}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 9),
                'v4': (randint, 1, 4),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 15),
            }),
    ]
)

aquivalenzumformungen_mit_mehreren_variablen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen mit mehreren Variablen',
    instruction='Fülle die Lücken.',
    question_type='gap',
    questions=[
        Question(
            formula='Äquivalenzumformungen können auch bei Gleichungen mit mehreren Variablen angewandt werden. '
                    'Das heißt, wenn man Äquivalenzumformungen an einer Gleichung mit mehreren Variablen durchführt, '
                    'ändert sich ____________ der Gleichung nicht.',
            correct='die Lösungsmenge',
            wrong_1='der Koeffizient',
            variables={}),
        Question(
            formula='Wenn man eine Gleichung mit mehreren Variablen nach einer der Variablen auflösen will, muss man '
                    '____________ auf einer Seite der Gleichung isolieren. Die andere Seite der Gleichung '
                    'darf alle anderen Variablen der Gleichung enthalten.',
            correct='die Variable',
            wrong_1='alle Variablen',
            variables={}),
    ]
)

aquivalenzumformungen_mit_klammern = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen mit Klammern',
    instruction='Fülle die Lücken, um die richtigen Äquivalenzumformungen '
                'durchzuführen und dadurch die Gleichung zu lösen.',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}(x - 1) = {{v1*v2}}  '
                    '{{v1}}x ___ = {{v1*v2}}  '
                    '{{v1}}x = {{v1*v2}} ___  '
                    'x = ___ ___  '
                    'x = ___',
            correct='-{{v1}}|+{{v1}}|*{{v1}};'
                    '+{{v1}}|-{{v1}}|*{{v1}};'
                    '{{v1*(v2+1)}}|{{v1*(v2-1)}}|{{v1*(v2+3)}};'
                    ':{{v1}}|-{{v1}}|*{{v1}};'
                    '{{v2+1}}|{{(v2+1)**2}}|{{v2-1}}',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 8),
            }),
    ]
)

aquivalenzumformungen_mit_klammern_gap = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen mit Klammern',
    instruction='Löse die Klammern auf.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}(x - {{v2}}) = ___',
            correct='{{v1}}x - {{v1*v2}}',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 8),
            }),
        Question(
            formula='{{v1}}(x + {{v2}}) = ___',
            correct='{{v1}}x + {{v1*v2}}',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 8),
            }),
        Question(
            formula='({{v1}}x + {{v2*v1}})/{{v1}} = ___',
            correct='x + {{v2}}',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 8),
            }),
        Question(
            formula='({{v1}}x - {{v2*v1}})/{{v1}} = ___',
            correct='x - {{v2}}',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 8),
            }),
    ]
)

aquivalenzumformungen_erkennen_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen erkennen (1)',
    instruction='Durch welche Äquivalenzumformungen erhält man aus der ersten Gleichung die zweite Gleichung?',
    question_type='MC',
    questions=[
        Question(
            formula='x:{{v1}} = {{v2}} | ___   x = {{v1*v2}}',
            correct='*{{v1}}',
            wrong_1=':{{v1}}',
            wrong_2='*{{v2}}',
            wrong_3=':{{v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 10),
            }),
        Question(
            formula='-1/{{v1}}x = {{v2}} | ___   x = -{{v1*v2}}',
            correct='*{{v1}}',
            wrong_1=':{{v1}}',
            wrong_2='*{{v2}}',
            wrong_3=':{{v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 10),
            }),
        Question(
            formula='{{v1}}x = {{v1*v2}} | ___   x = {{v2}}',
            correct=':{{v1}}',
            wrong_1='*{{v1}}',
            wrong_2=':{{v2}}',
            wrong_3='*{{v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 10),
            }),
    ]
)

aquivalenzumformungen_erkennen_1_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen erkennen (1)',
    instruction='Welche Äquivalenzumformungen wurden durchgeführt?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1+v3}}x + {{v2}} = {{v1}}x - {{v3*v2-v2}} | ___  '
                    '{{v1+v3}}x = {{v1}}x - {{v3*v2}} | ___ '
                    '{{v3}}x = -{{v3*v2}} | ___   '
                    'x = -{{v2}}',
            correct='-{{v2}}|+{{v2}}|-{{v3}}|*{{v2}};'
                    '-{{v1}}x|+{{v1}}x|:{{v1}}|*{{v2}};'
                    ':{{v3}}|*{{v3}}|:-{{v3}}|*-{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 4),
            }),
        Question(
            formula='{{v3+v4}}x - {{v2*(v3-v4)}} = {{v4}}*({{v2}} + x) | ___   '
                    '{{v3+v4}}x - {{v2*(v3-v4)}} = {{v2*v4}} + {{v4}}x | ___  '
                    '{{v3+v4}}x = {{v2*v3}} + {{v4}}x | ___  '
                    '{{v3}}x = {{v2*v3}} | ___  '
                    'x = {{v2}}',
            correct='TU|-{{v2}}|+{{v3}}|+{{v4}}x;'
                    '+{{v2*(v3-v4)}}|-{{v2*(v3-v4)}}|-{{v2}}x|+{{v2}}x;'
                    '-{{v4}}x|+{{v4}}x|*{{v2}}|-{{v2}};'
                    ':{{v3}}|*{{v3}}|*-{{v3}}|+{{v2}}',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 1, 4),
                'v3': (randint, 5, 9),
                'v4': (randint, 2, 4),
            }),
    ]
)

aquivalenzumformungen_erkennen_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Äquivalenzumformungen erkennen (2)',
    instruction='Kann man die zweite Gleichung aus der ersten Gleichung durch Äquivalenzumformungen erhalten?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}x = x + {{(v1-1)*v2}}   x = {{v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='x : 2 = x - {{v1}}    x = {{2*v1}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}({{v3}} - x) = {{v2}}(x - {{v3}})   x = -{{v3}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
    ]
)

lineare_gleichungen_mit_zwei_variablen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Lineare Gleichungen mit zwei Variablen',
    instruction='Rechne den Wert für y aus, indem du für x die Zahl einsetzt.',
    question_type='gap',
    questions=[
        Question(
            formula='y = {{v1}} + {{v2}}x   x = -{{v3}}',
            correct='{{v1-v2*v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='y = {{v2}}x - {{v1}}   x = -{{v3}}',
            correct='{{v2*v3-v1}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),

        ]
)

zahlenpaare_prufen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Zahlenpaare prüfen',
    instruction='Löse die Gleichung nach y auf.',
    question_type='gap',
    hint='Setze den x-Wert in die Gleichung ein und überprüfe, ob der y-Wert mit dem Ergebnis übereinstimmt.',
    questions=[
        Question(
            formula='{{v3}}y + {{v2*v3}} = {{v1*v3}}x  {{v3}}y = ___  y = ___',
            correct='{{v1*v3}}x-{{v2*v3}};{{v1}}x-{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v3}}y - {{v2*v3}} = {{v1*v3}}x  {{v3}}y = ___  y = ___',
            correct='{{v1*v3}}x+{{v2*v3}};{{v1}}x+{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            instruction='Prüfe, ob das Zahlenpaar ({{v1}};{{v1*v2-v3}}) die Gleichung löst. Setze dazu den x-Wert in '
                        'die Gleichung ein und überprüfe, ob der y-Wert mit dem Ergebnis übereinstimmt.',
            hint='',
            formula='y = {{v2}}x - {{v3}}  y = {{v2}} * ___ - {{v3}} = ___ - {{v3}} = ___',
            correct='{{v1}};{{v1*v2}};{{v1*v2-v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 10, 19),
            }),
        ]
)

zahlenpaare_berechnen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Zahlenpaare berechnen',
    instruction='Setzt den Wert für x in die Gleichung ein, um die Zahlenpaare zu berechnen.',
    question_type='gap',
    questions=[
        Question(
            formula='x = {{v1}}  y = {{v2}}x + {{v3}}  y = ___',
            correct='{{v1*v2+v3}}',
            variables={
                'v1': (randint, -6, -1),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='x = {{v1}}  y = {{v2}}x + {{v3}}  y = ___',
            correct='{{v1*v2+v3}}',
            variables={
                'v1': (randint, -6, -1),
                'v2': (randint, -6, -1),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='x = {{v1}}  y = {{v2}}x - {{v3}}  y = ___',
            correct='{{v1*v2-v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 10, 19),
            }),
        ]
)

gleichungen_aufstellen_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Gleichungen aufstellen',
    instruction='Schreibe die Aufgabe als Gleichung.',
    question_type='gap',
    questions=[
        Question(
            formula='Das {{v1}}-fache einer Zahl (x) addiert zu dem {{v2}}-fachen einer anderen Zahl (y) soll {{v3}} ergeben. <br> '
                    '___ = ___',
            correct='{{v1}}x+{{v1}}y;{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 20, 50),
            }),
        Question(
            formula='{{10*v1}} ist gleich das Doppelte einer Zahl (x) subtrahiert von dem {{v2}}-fachen einer anderen Zahl (y). <br> '
                    '___ = ___',
            correct='100;{{v2}}y-2x',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='Das {{v1}}-fache einer Zahl (x) addiert zu dem {{v1*v2}}-fachen einer anderen Zahl (y) ergibt {{v1**2}}. <br> '
                    '___ = ___',
            correct='{{v1}}x+{{v1*v2}}y;{{v1**2}}',
            variables={
                'v1': (randint, 4, 9),
                'v2': (randint, 1, 3),
            }),
        Question(
            formula='Das {{v1}}-fache einer Zahl (x) subtrahiert von dem {{v2}}-fachen einer anderen Zahl (y) ergibt {{v3}} <br> '
                    '___ = ___',
            correct='{{v2}}y-{{v1}}x;{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 20),
                'v3': (randint, 50, 99),
            }),
        ]
)

gleichsetzungsverfahren_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Gleichsetzungsverfahren (1)',
    instruction='Löse mit Hilfe des Gleichsetzungsverfahren.',
    question_type='gap',
    questions=[
        Question(
            formula='(1) y = {{v1+1}}x - {{v2}} (2) y = {{v1}}x + {{v3}} <br>'
                    '{{v1+1}}x - {{v2}} = {{v1}}x + {{v3}} | +{{v2}}  <br>'
                    '___ = ___ | -{{v1}}x  <br>'
                    'x = ___',
            correct='{{v1}}x;{{v1+1}}x+{{v2+v3}};{{v2+v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 4),
            }),
        Question(
            instruction='Führe die Probe durch',
            formula='P({{v2+v3}}|{{(v1+1)*(v2+v3)-v2}}) (1) {{v1+1}}x - y = {{v2}}  (2) {{v1}}x - y = -{{v3}}  '
                    'Für Gleichung (1): {{v1+1}} * ___ - ___ = {{(v1+1)*(v2+v3)-((v1+1)*(v2+v3)-v2)}}    ___ = {{v2}}  <br> '
                    'Für Gleichung (2): {{v1}} * ___ - ___ = {{(v1)*(v2+v3)-(v1+1)*(v2+v3)+v2}}   ___ = {{(v1)*(v2+v3)-(v1+1)*(v2+v3)+v2}}',
            correct='{{v2+v3}};{{(v1+1)*(v2+v3)-v2}};{{(v1+1)*(v2+v3)-((v1+1)*(v2+v3)-v2)}};{{v2+v3}};{{(v1+1)*(v2+v3)-v2}};{{(v1)*(v2+v3)-(v1+1)*(v2+v3)+v2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 4),
                'v3': (randint, 1, 4),
            }),
        ]
)

gleichsetzungsverfahren_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Gleichsetzungsverfahren (2)',
    instruction='Löse mit Hilfe des Gleichsetzungsverfahren.',
    question_type='gap',
    questions=[
        Question(
            formula='(1) y = {{v1}}x + {{v3-v1*v4}}   '  # y = v3; x=v4;
                    '(2) y = {{v2}}x + {{v3-v2*v4}}   '
                    '{{v1}}x + {{v3-v1*v4}} = ___ | -{{v3-v1*v4}}   '
                    '___ = ___ | :{{v1-v2}}  '
                    'x = ___',
            correct='{{v2}}x - {{v3-v2*v4}};'
                    '{{v1-v2}}x;{{v4*(v1-v2)}};'
                    '{{v4}}',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
                'v3': (randdecimal, 50, 70, 5),
                'v4': (randint, 2, 5),
            }),
        Question(
            instruction='Führe die Probe durch',
            formula='(1) y = {{v1}}x + {{v2}}   (2) x = {{v3}}   y = {{v1}} * ( ___ ) + {{v2}}  = ___ + {{v2}}  = ___',
            correct='{{v3}};{{v1*v3}};{{v1*v3+v2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 1, 9),
                'v3': (randint, -10, -1),
            }),
        ]
)

Einsetzungsverfahren_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Einsetzungsverfahren (1)',
    instruction='Was ist die korrekte Umformung für die Gleichung 2 nach x',
    question_type='MC',
    questions=[
        Question(
            formula='(1) {{v1}}x - {{v2}}y = 0  (2) x + y = {{v3}}',
            correct='x = {{v3}} - y',
            wrong_1='x = y - {{v3}}',
            wrong_2='y = {{v3}} - x',
            wrong_3='x = y + {{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='(1) {{v1}}x - {{v2}}y = 0  (2) {{v4}}x + y = {{v3}}',
            correct='x = ({{v3}} - y)/{{v4}}',
            wrong_1='x = (y - {{v3}})/{{v4}}',
            wrong_2='y = {{v3}} - {{v4}}x',
            wrong_3='x = (y + {{v3}})/{{v4}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
            }),
        ]
)

einsetzungsverfahren_1_gap = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Einsetzungsverfahren (1)',
    instruction='Löse die Gleichung nach x auf.',
    question_type='gap',
    questions=[
        Question(
            formula='(1) {{v1}}x + {{v2}}y = 0   '
                    '(2) x = {{v1-v2}} - y   '
                    '{{v1}}({{v1-v2}} - y) + {{v2}}y = 0   '
                    '{{v1*(v1-v2)}} - ___ + {{v2}}y = 0   '
                    '{{v1*(v1-v2)}} - ___ = 0 | + ___   '
                    '___ = ___ | :___   '
                    '___ = ___ ',
            correct='{{v1}}y;{{v1-v2}}y;{{v1-v2}}y;{{v1*(v1-v2)}};{{v1-v2}}y;{{v1-v2}};{{v1}};y',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 1, 4),
            }),
        Question(
            instruction='Löse die Gleichung indem du den folgenden Wert für y einsetzt.',
            formula='y = {{v1}}   '
                    '(1) {{v1}}x + {{v2}}y = 0   '
                    '(2) x = {{v1-v2}} - y    '
                    'x = {{v1-v2}} - ___    '
                    'x = ___',
            correct='{{v1}}; {{-v2}}',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 1, 4),
            }),
        ]
)

additionsverfahren_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Additionsverfahren (1)',
    instruction='Addiere Gleichung 1 mit Gleichung 2',
    question_type='gap',
    questions=[
        Question(
            hint='Durch die Addition ist die Variable y weggefallen. Die neu entstandene Gleichung nennt man 1a',
            formula='{{v1}}x - {{v2}}y = {{v1*v4 - v2*v5}} (1)    '
                    '{{v3}}x + {{v2}}y = {{v3*v4 + v2*v5}} (2)    '
                    '___ = ___ (1a)',
            correct='{{v1+v3}}x;{{v1*v4+v3*v4}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 2, 5),
            }),
        Question(
            instruction='Stelle die Gleichung nach x um.',
            formula='(1) {{v1}}x - {{v2}}y = {{v1*v4 - v2*v5}}    '
                    '(2) {{v3}}x + {{v2}}y = {{v3*v4 + v2*v5}}    '
                    '(1a) {{v1+v3}}x = {{(v1+v3)*v4}} | ___     '
                    'x = ____',
            correct=':{{v1+v3}};{{v4}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 2, 5),
            }),
        Question(
            instruction='Setze den Wert für x in Gleichung zwei und löse.',
            formula='(1) {{v1}}x - {{v2}}y = {{v1*v4 - v2*v5}}    '
                    '(2) {{v3}}x + {{v2}}y = {{v3*v4 + v2*v5}}    '
                    'x = {{v4}}    '
                    '{{v3}}x + {{v2}}y = {{v3*v4 + v2*v5}}     '
                    '{{v3}}*___ + {{v2}}y = {{v3*v4 + v2*v5}}    '
                    '___ + {{v2}}y = {{v3*v4 + v2*v5}} | ___    '
                    '{{v2}}y = ___ | ___    '
                    'y = ___',
            correct='{{v4}};{{v3*v4}};-{{v3*v4}};{{v2*v5}};:{{v2}};{{v5}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 2, 5),
            }),
        ]
)

additionsverfahren_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Lineare Gleichungen und Ungleichungen',
    title='Additionsverfahren (2)',
    instruction='Mit welchem Wert musst die eine Gleichung multiplizieren, '
                'damit die Vorfaktoren gleich sind und wir das Additionsverfahren anwenden können?',
    question_type='MC',
    questions=[
        Question(
            formula='(1) {{v1}}x + {{v2}}y = {{v1*v3+v2*v4}}   (2) x + {{v5}}y = {{v3+v5*v4}}',
            correct='{{(-v1)}}',
            wrong_1='{{v1}}',
            wrong_2='{{v2}}',
            wrong_3='{{(-v2)}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 1, 5),
            }),
        ]
)

allgemeine_form = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Quadratische Gleichungen',
    title='Allgemeine Form',
    instruction='Bestimme, ob die folgende quadratische Gleichung in allgemeiner Form steht.',
    question_type='buttons',
    hint='Allgemeine Form einer quadratischen Gleichung: ax^2+bx+c=0.',
    questions=[
        Question(
            formula='{{v1}}x^2+{{v2}}x+{{v3}}=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='(x+{{v1**2}})^2=0',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 1, 7),
            }),
        Question(
            formula='x^2+{{v1**2}}=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 1, 7),
            }),
        Question(
            formula='x^2={{v1}}x-{{v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='-x^2+1/{{v1}}x-{{v2}}/{{v3}}=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 4),
                'v3': (randint, 5, 9),
            }),
        Question(
            formula='{{v1}}(x^2+{{v2}}x-{{v3}})={{v1*v4}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 4),
                'v3': (randint, 5, 9),
                'v4': (randint, 1, 7),
            }),
        ]
)

normalform = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Quadratische Gleichungen',
    title='Normalform',
    instruction='Sind die folgenden quadratischen Gleichungen in Normalform oder nicht?',
    question_type='buttons',
    hint='Die Normalform für eine quadratische Gleichung ist <br><br> x^2+px+q=0. <br><br> '
         'Die Koeffizienten <i>p</i> und <i>q</i> können beliebige reelle Zahlen sein.',
    questions=[
        Question(
            formula='x^2+{{v1}}x+{{v2}}=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x^2-x-{{v2}}=0',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
            }),
        Question(
            formula='x^2=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 1, 7),
            }),
        Question(
            formula='-x^2+{{v1}}x+{{v2}}=0',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='x^2+1/{{v1}}x-1/{{v2}}=0',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='(x+{{v1}})^2=0',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

quadratische_gleichungen = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Quadratische Gleichungen',
    title='Quadratische Gleichungen',
    instruction='Ziehe die Gleichungen in die richtigen Kategorien.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='quadratische Gleichung|{{v1}}x^2+{{v2}}x+{{v3}}=0~{{v4}}x^2+y^2={{v5}}~(x-{{v6}})^2={{v7**2}};'
                    'nicht-quadratische Gleichung|{{v8}}x+{{v9}}=0~x+y=-{{v10}}~{{v12}}/x={{v13}}',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 9),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 9),
                'v12': (randint, 2, 9),
                'v13': (randint, 2, 9),
            }),
        ]
)

ungleichungen_losen_1 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Ungleichungen lösen',
    title='Ungleichungen lösen (1)',
    instruction='Betrachte die folgenden Schritte und bestimme, welches Zeichen in die Lücke passt.',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}*x > {{v1*v2}}   x ___ {{v2}}',
            hint='Wenn durch eine positive Zahl dividiert wird, bleibt das Größer-als-Zeichen gleich.',
            correct='>',
            wrong_1='<',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='{{v1}} - x < {{v1}}   x ___ 0',
            hint='Wenn durch eine negative Zahl dividiert wird, dreht sich das Kleiner-als-Zeichen um.',
            correct='>',
            wrong_1='<',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x + {{v2}} < x + {{v3}}   {{v1+1}}x + {{v2-v3}} ___ 0',
            hint='Wenn Zahlen und Variablen zu und von beiden Seiten addiert und subtrahiert werden, bleibt das Kleiner-als-Zeichen gleich.',
            correct='<',
            wrong_1='>',
            wrong_2='x > {{v3+v1*v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 5, 9),
                'v3': (randint, 1, 4),
            }),
        Question(
            formula='-1/{{v1}} x < 1   x ___ -{{v1}}',
            hint='Wenn mit einer negativen Zahl multipliziert wird, dreht sich das Kleiner-als-Zeichen um.',
            correct='>',
            wrong_1='<',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 4),
            }),
        Question(
            formula='{{v1}}*x > {{v1*v2}}   x > {{v2}}',
            hint='Wenn mit einer negativen Zahl multipliziert wird, dreht sich das Kleiner-als-Zeichen um.',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='{{v1}} - x < {{v1}}   x < 0',
            hint='Wenn durch eine negative Zahl dividiert wird, dreht sich das Kleiner-als-Zeichen um.',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x + {{v2}} < x + {{v3}}   {{v1+1}}x + {{v2-v3}} < 0',
            hint='Wenn Zahlen und Variablen zu und von beiden Seiten addiert und subtrahiert werden, '
                 'bleibt das Kleiner-als-Zeichen gleich.',
            correct='correct',
            wrong_1='wrong',
            wrong_2='x > {{v3+v1*v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 5, 9),
                'v3': (randint, 1, 4),
            }),
        Question(
            formula='-1/{{v1}} x < 1   x > -{{v1}}',
            hint='Wenn mit einer negativen Zahl multipliziert wird, dreht sich das Kleiner-als-Zeichen um.',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 4),
            }),
        ]
)

ungleichungen_losen_2 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Ungleichungen lösen',
    title='Ungleichungen lösen (2)',
    instruction='Löse die Ungleichung.',
    question_type='MC',
    questions=[
        Question(
            formula='x + {{v1}} < {{v2}}',
            correct='x < {{v2-v1}}',
            wrong_1='x > {{v2-v1}}',
            wrong_2='x < {{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 19),
            }),
        Question(
            formula='{{v1}}a + {{v1*v2}} > {{v3*v1}}',
            correct='a > {{v3-v2}}',
            wrong_1='a < {{v3-v2}}',
            wrong_2='a > {{v3*v1}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 1, 4),
                'v3': (randint, 5, 9),
            }),
        Question(
            formula='{{v1}} - x/{{v2}} < {{v3}}',
            correct='x > -{{v3+v1*v2}}',
            wrong_1='x < -{{v3+v1*v2}}',
            wrong_2='x > {{v3+v1*v2}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='-z/{{v1}} < {{v2}}',
            correct='z > -{{v2*v1}}',
            wrong_1='z > {{v2*v1}}',
            wrong_2='z < {{v1}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 1, 4),
            }),
        ]
)

ungleichungen_losen_3 = QuestionSet(
    grade='8',
    capital='Gleichungen und Ungleichungen',
    subcapital='Ungleichungen lösen',
    title='Ungleichungen lösen (3)',
    instruction='Löse die Ungleichung.',
    hint='Ungleichungen mit &ge; bzw. &le; werden genauso behandelt wie Ungleichungen mit > bzw. < Zeichen.',
    question_type='MC',
    questions=[
        Question(
            formula='x + {{v1}} ≤ {{v1+v2}}',
            correct='x ≤ {{v2}}',
            wrong_1='x ≥ {{v2}}',
            wrong_2='x < {{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='2a - {{v1}} ≥ {{v1}}',
            correct='a ≥ {{v1}}',
            wrong_1='a ≤ {{v1}}',
            wrong_2='a > {{v1}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='x - x/{{v1}} ≤ {{v1-1}}',
            correct='x ≤ {{v1}}',
            wrong_1='x ≥ {{v1}}',
            wrong_2='x > {{v1}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1-1}}/{{v1}} - z/{{v1}} ≤ 1/{{v1}}',
            correct='z ≥ {{v1-2}}',
            wrong_1='z > {{v1-2}}',
            wrong_2='z ≤ {{v1-2}}',
            variables={
                'v1': (randint, 3, 9),
            }),
        ]
)

question_sets = [
    definitionsmenge_2_dragmatch,
    null_als_produkt_1,
    null_als_produkt_dragmatch,
    ruckwartsrechnen_mit_probe_1_dragmatch,
    ruckwartsrechnen_mit_probe_1,
    verhaltnisgleichungen,
    aussagen_und_aussageformen_draggroup,
    gleichungen_aufstellen,
    ungleichungen_draggroup,
    losungen_der_gleichung_mc,
    losungen_der_gleichung_gap,
    ungleichungen_dragmatch,
    aquivalenzumformungen_mit_mehreren_variablen,
    aquivalenzumformungen_mit_klammern,
    aquivalenzumformungen_mit_klammern_gap,
    aquivalenzumformungen_erkennen_1,
    aquivalenzumformungen_erkennen_1_2,
    aquivalenzumformungen_erkennen_2,
    lineare_gleichungen_mit_zwei_variablen,
    zahlenpaare_prufen,
    zahlenpaare_berechnen,
    gleichungen_aufstellen_2,
    gleichsetzungsverfahren_1,
    gleichsetzungsverfahren_2,
    einsetzungsverfahren_1_gap,
    additionsverfahren_1,
    additionsverfahren_2,
    allgemeine_form,
    normalform,
    quadratische_gleichungen,
    ungleichungen_losen_1,
    ungleichungen_losen_2,
    ungleichungen_losen_3,
]
