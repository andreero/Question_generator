from questions import Question, QuestionSet
from random import randint, choice, randrange
from definitions.common import randdecimal, measurement_units


naherungswert_bestimmen = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Mit Wurzeln rechnen',
    title='Näherungswert bestimmen',
    instruction='Wurde richtig vereinfacht?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>sqrt({{v1**2}}) - sqrt({{v2**2}}) <br> = {{v1}} - {{v2}} <br> = {{v1-v2}}</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 10, 16),
                'v2': (randint, 5, 9)
            }),
        Question(
            formula='<mat>sqrt({{(v1**2)-(v2**2)}}) + sqrt({{v2**2}}) <br> = sqrt({{v1**2}}) <br> = {{v1}}</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 10, 16),
                'v2': (randint, 5, 9)
            }),
        Question(
            formula='<mat>sqrt({{v1}}) + sqrt({{v2}}) <br> '
                    '= {{"%.2f"|format(v1**0.5)}} + {{"%.2f"|format(v2**0.5)}} <br> '
                    '≈ {{"%.2f"|format(round(v1**0.5, 2)+round(v2**0.5, 2))}}</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randrange, 20, 50, 5),
                'v2': (randrange, 50, 90, 5),
                'round': round,
            }),
        Question(
            formula='<mat>sqrt({{(v1**2)*3}}) <br> = sqrt({{v1**2}}+{{v1**2}}+{{v1**2}}) <br> = {{v1*3}}</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 5, 9),
            }),
        ]
)

wurzeln_mit_variablen_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Mit Wurzeln rechnen',
    title='Wurzeln mit Variablen',
    instruction='Schiebe die Aufgaben und die zugehörigen Lösungen zusammen. '
                'Alle Variablen sind positive reelle Zahlen, sodass Betragsstriche vernachlässigt werden können.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='sqrt((x-{{v1}})^2) = ?|x-{{v1}};'
                    'sqrt(x^2)-sqrt({{v2}}) = ?|x-sqrt({{v2}});'
                    'root3({{v3**3}}x^{{3*v4}}) = ?|{{v3}}x^{{v4}}',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 7),
            }),
    ]
)

wurzeln_mit_variablen_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Mit Wurzeln rechnen',
    title='Wurzeln mit Variablen',
    instruction='Vereinfache die Terme.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>root2(x^{{v1}})=x^(___)</mat>',
            correct='{{v1}}/2',
            variables={
                'v1': (choice, [3, 5, 7, 9]),
            }),
        Question(
            formula='<mat>root{{v1}}(x)=x^(___)</mat>',
            correct='1/{{v1}}',
            variables={
                'v1': (randint, 3, 9),
            }),
        Question(
            formula='<mat>root2({{v1**2}}x^{{v2*2}})=___</mat>',
            correct='{{v1}}x^{{v2}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='<mat>root2({{v1**2}}x^{{v2*2}}y^{{v3*2}})=___</mat>',
            correct='{{v1}}x^{{v2}}y^{{v3}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 2, 4),
                'v3': (randint, 2, 4),
            }),
        ]
)

mit_variablen_in_wurzeln_rechnen = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Mit Wurzeln rechnen',
    title='Mit Variablen in Wurzeln rechnen',
    instruction='Ziehe teilweise die Wurzel. Alle Variablen sind positive reelle Zahlen.',
    question_type='gap',
    questions=[
        Question(
            instruction='Wende das Distributivgesetz mit Wurzeln an',
            formula='<mat>(sqrt({{v1*(v2**2)}}x) + sqrt({{v1}}x)) * sqrt({{v1}}x)<br>'
                    '= sqrt({{v1*(v2**2)}}x) * sqrt(___) + sqrt({{v1}}x) * sqrt(___)<br>'
                    '= sqrt(___) + sqrt(___)<br>=___ + ___<br>= ___</mat>',
            correct='{{v1}}x;{{v1}}x;{{(v1*v2)**2}}x^2;{{v1**2}}x^2;{{v1*v2}}x;{{v1}}x;{{v1*v2+v1}}x',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>sqrt({{v1}}x^2) + sqrt({{v1*(v2**2)}}x^2)<br>'
                    '= sqrt({{v1}}x^2) + sqrt({{v1}} * ___ * x^2)<br>'
                    '= ___ * sqrt({{v1}}) + ___ * ___ * sqrt({{v1}})<br>'
                    '= ___ * sqrt({{v1}})</mat>',
            correct='{{v2**2}};x;{{v2}};x;{{v2+1}}x',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>sqrt({{"%.2f"|format(v1**2)}}w) = ___ * sqrt(___)</mat>',
            correct='{{v1}};w',
            variables={
                'v1': (randdecimal, 0.2, 0.9),
            }),
        Question(
            formula='<mat>sqrt({{v1*(v2**2)}}a^3)<br>'
                    '= sqrt({{v1}} * ___ * a * ___)<br>'
                    '= ___ * ___ sqrt(___)</mat>',
            correct='{{v2**2}};a^2;{{v2}};a;{{v1}}a',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 5),
            }),
        ]
)

potenzen_mit_bruch_als_basis_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch als Basis',
    instruction='Ordne die gleichwertigen Terme einander zu.',
    question_type='dragMatch',
    hint="Beispiel: <mat center='true'>(4/3)^3=(4^3)/(3^3)=64/27",
    questions=[
        Question(
            formula='',
            correct='({{v1}}/{{v2}})^2|{{v1**2}}/{{v2**2}};'
                    '({{v3*v5}}/{{v4*v5}})^2|{{v3}}^2/{{v4}}^2;'
                    '({{v6}}/{{v7}})^3|{{v6}}/{{v7}}*{{v6}}/{{v7}}*{{v6}}/{{v7}};'
                    '({{v8}}/{{v9}})^4|{{v8}}^4/{{v9}}^4',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 4),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 9),
                'v9': (randint, 2, 9),
            }),
    ]
)

potenzen_mit_bruch_als_basis_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch als Basis',
    instruction='Berechne die Potenz.',
    question_type='gap',
    hint='Denke daran, dass die Basis auch gekürzt werden kann. Nutze, wenn nötig, den Taschenrechner.',
    questions=[
        Question(
            formula='<mat>({{v1}}/{{v1*v2}})^2 = ___</mat>',
            correct='1/{{v2**2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='<mat>-({{v1}}/{{v2}})^0 = ___</mat>',
            correct='-1',
            variables={
                'v1': (randint, 5, 50),
                'v2': (randint, 5, 50),
            }),
        Question(
            formula='<mat>({{v1}}/{{v2}})^2 = ___</mat>',
            correct='{{v1**2}}/{{v2**2}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 11, 15),
            }),
        Question(
            formula='<mat>({{v1*v3}}/{{v2*v3}})^3 = ___</mat>',
            correct='{{v1**3}}/{{v2**3}}',
            variables={
                'v1': (randint, 1, 2),
                'v2': (choice, [3, 5]),
                'v3': (randint, 2, 6),
            }),
    ]
)

potenzen_mit_bruch_im_exponenten_1_mc = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch im Exponenten (1)',
    instruction='Ordne dem Wurzelterm den richtigen Potenzausdruck zu',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>root{{v1}}({{v2}}) = ___</mat>',
            correct='<mat>{{v2}}^(1/{{v1}})</mat>',
            wrong_1='<mat>{{v1}}^({{v2}}/1)</mat>',
            wrong_2='<mat>1^({{v2}}/{{v1}})</mat>',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='<mat>{{v2}}^(1/{{v1}}) = ___</mat>',
            correct='<mat>root{{v1}}({{v2}})</mat>',
            wrong_1='<mat>root{{v2}}({{v1}})</mat>',
            wrong_2='<mat>root1({{v2}}^{{v1}})</mat>',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='<mat>{{v1}}^(1/{{v2}}) = ___</mat>',
            correct='<mat>root{{v2}}({{v1}})</mat>',
            wrong_1='<mat>root{{v1}}({{v2}})</mat>',
            wrong_2='<mat>root1({{v1}}^{{v2}})</mat>',
            variables={
                'v1': (randint, 11, 49),
                'v2': (randint, 2, 4),
            }),
        ]
)

potenzen_mit_bruch_im_exponenten_1_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch im Exponenten (1)',
    instruction='Schreibe den Wurzelterm als Potenz.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>root{{v2}}({{v1}}) = ___</mat>',
            correct='{{v1}}^(1/{{v2}})',
            variables={
                'v1': (randint, 5, 50),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>root{{v2}}({{v1}}) = ___</mat>',
            correct='{{v1}}^(1/{{v2}})',
            variables={
                'v1': (randrange, 500, 5000, 500),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>root{{v1}}({{v1}}) = ___</mat>',
            correct='{{v1}}^(1/{{v1}})',
            variables={
                'v1': (randint, 5, 10),
            }),
        Question(
            formula='<mat>root3({{v1**3}}) = ___</mat>',
            correct='{{v1**3}}^(1/3)',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>root{{v2}}({{v1*111}}) = ___</mat>',
            correct='{{v1*111}}^(1/{{v2}})',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 5),
            }),
        Question(
            instruction='Schreibe die Potenz als Wurzelterm',
            formula='<mat>{{v1}}^(1/{{v2}}) = ___</mat>',
            correct='<mat>root{{v2}}({{v1}})</mat>',
            variables={
                'v1': (randint, 5, 50),
                'v2': (randint, 3, 7),
            }),
        Question(
            instruction='Schreibe die Potenz als Wurzelterm',
            formula='<mat>{{v1}}^(1/2) = ___</mat>',
            correct='<mat>sqrt({{v1}})</mat>',
            variables={
                'v1': (randint, 5, 50),
            }),
        ]
)

potenzen_mit_bruch_im_exponenten_2_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch im Exponenten (2)',
    instruction='Ordne die gleichwertigen Terme einander zu',
    question_type='dragMatch',
    hint='Beispiel:<br>rootn(x^m)=x^(m/n)<br>',
    questions=[
        Question(
            formula='',
            correct='root{{v1}}({{v2}}^{{v3}})=|{{v2}}^({{v3}}/{{v1}});'
                    'root{{v4}}({{v5}}^{{v6}})=|{{v5}}^({{v6}}/{{v4}});'
                    'root{{v7}}({{v8}}^{{v9}})=|{{v8}}^({{v9}}/{{v7}});'
                    '{{v10}}^({{v11}}/{{v12}})=|root{{v12}}({{v10}}^{{v11}});'
                    '{{v13}}^({{v14}}/{{v15}})=|root{{v15}}({{v13}}^{{v14}});'
                    '{{v16}}^({{v17}}/{{v18}})=|root{{v18}}({{v16}}^{{v17}})',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 15),
                'v6': (randint, 10, 15),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 15),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 15),
                'v11': (randint, 2, 9),
                'v12': (randint, 2, 9),
                'v13': (randint, 2, 15),
                'v14': (randint, 2, 9),
                'v15': (randint, 2, 9),
                'v16': (randint, 2, 15),
                'v17': (randint, 2, 9),
                'v18': (randint, 2, 9),
            }),
    ]
)

potenzen_mit_bruch_im_exponenten_2_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit Bruch im Exponenten (2)',
    instruction='Schreibe den Wurzelterm als Potenz.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>sqrt({{v1}}^{{v2}}) = ___</mat>',
            correct='{{v1}}^({{v2}}/2)',
            variables={
                'v1': (randint, 15, 50),
                'v2': (randint, 3, 9),
            }),
        Question(
            formula='<mat>root{{v1}}({{v2}}^{{v3}}) = ___</mat>',
            correct='{{v2}}^({{v3}}/{{v1}})',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 19),
                'v3': (randint, 2, 9),
            }),
        Question(
            instruction='Schreibe die Potenz als Wurzelterm.',
            formula='<mat>{{v1}}^({{v2}}/{{v3}}) = ___</mat>',
            correct='{{v2}}^({{v3}}/{{v1}})',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 0, 9),
                'v3': (randint, 2, 9),
            }),
        ]
)

potenzen_mit_negativem_exponenten_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit negativem Exponenten',
    instruction='Ordne die gleichwertigen Terme einander zu',
    question_type='dragMatch',
    hint="Beispiel:<br>"
         "<mat align='rcl'>x^(-n)||=||1/x^(n)<br> "
         "(1/x)^(-n)||=||x^n <br>"
         "1/x^(-n)||=||x^n",
    questions=[
        Question(
            formula='',
            correct='1/{{v1}}^(-1)|{{v1}};'
                    '1/{{v2}}^(-{{v3}})|{{v2}}^{{v3}};'
                    '(1/{{v4}})^(-{{v5}})|{{v4}}^{{v5}};'
                    '{{v6}}^(-{{v7}})|1/{{v6}}^({{v7}});'
                    '{{v8}}^(-{{v9}})|1/{{v8}}^({{v9}})',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 10),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 10),
                'v5': (randint, 2, 15),
                'v6': (randint, 2, 10),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 10),
                'v9': (randint, 2, 9),
            }),
    ]
)

potenzen_mit_negativem_exponenten_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit negativem Exponenten',
    instruction='Forme den Term so um, dass der Exponent positiv ist.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}^(-{{v2}}) = ___</mat>',
            correct='1/{{v1}}^{{v2}}',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>(1/{{v1}})^(-{{v2}}) = ___</mat>',
            correct='{{v1}}^{{v2}}',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}^(-1) = ___</mat>',
            correct='1/{{v1}}',
            variables={
                'v1': (randint, 5, 50),
            }),
        ]
)

potenzen_mit_negativer_basis_berechnen_draggroup = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit negativer Basis berechnen',
    instruction='Ist der Potenzwert positiv oder negativ? Ziehe die Potenzen in die entsprechenden Kategorien.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            hint="Beispiel:<br> "
                 "<mat align='rclcl'>(-3)^3||=||(-3)*(-3)*(-3) ||=||-27<br>"
                 "(-3)^4||=||(-3)*(-3)*(-3)*(-3)||=||81<br>"
                 "<br>Der Potenzwert ist jeweils das Ergebnis der Rechnung.",
            correct='positiver Potenzwert|(-{{v1}})^{{v2}}~(-{{v3}})^{{v4}}~(-{{v5}})^{{v6}}~(-{{v7}})^{{v8}};'
                    'negativer Potenzwert|(-{{v9}})^{{v10}}~(-{{v11}})^{{v12}}~(-{{v13}})^{{v14}}~(-{{v15}})^{{v16}}',
            variables={
                'v1': (randint, 2, 12),
                'v2': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v3': (randint, 2, 9),
                'v4': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v5': (randint, 2, 15),
                'v6': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v7': (randint, 2, 9),
                'v8': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v9': (randint, 2, 9),
                'v10': (choice, [1, 3, 5, 7, 9, 11, 13, 15]),
                'v11': (randint, 2, 9),
                'v12': (choice, [1, 3, 5, 7, 9, 11, 13, 15]),
                'v13': (randint, 2, 15),
                'v14': (choice, [1, 3, 5, 7, 9, 11, 13, 15]),
                'v15': (randint, 2, 9),
                'v16': (choice, [1, 3, 5, 7, 9, 11, 13, 15]),
            }),
        Question(
            formula='',
            hint="Beispiel:<br> "
                 "<mat align='rclcl'>-3^4||=||-(3*3*3*3) ||=||-81<br>"
                 "(-3)^4||=||(-3)*(-3)*(-3)*(-3)||=||81",
            correct='positiver Potenzwert|(-{{v1}})^{{v2}}~(-{{v3}})^{{v4}}~(-{{v5}})^{{v6}}~(-{{v7}})^{{v8}};'
                    'negativer Potenzwert|-{{v9}}^{{v10}}~-{{v11}}^{{v12}}~-{{v13}}^{{v14}}~-{{v15}}^{{v16}}',
            variables={
                'v1': (randint, 2, 12),
                'v2': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v3': (randint, 2, 9),
                'v4': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v5': (randint, 2, 15),
                'v6': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v7': (randint, 2, 9),
                'v8': (choice, [2, 4, 6, 8, 10, 12, 14, 16]),
                'v9': (randint, 2, 9),
                'v10': (choice, [0, 2, 4, 6, 8, 10, 12, 14, 16]),
                'v11': (randint, 2, 9),
                'v12': (choice, [0, 2, 4, 6, 8, 10, 12, 14, 16]),
                'v13': (randint, 2, 15),
                'v14': (choice, [0, 2, 4, 6, 8, 10, 12, 14, 16]),
                'v15': (randint, 2, 9),
                'v16': (choice, [0, 2, 4, 6, 8, 10, 12, 14, 16]),
            }),
    ]
)

potenzen_mit_negativer_basis_berechnen_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Potenzen mit negativer Basis berechnen',
    instruction='Berechne den Potenzwert. Nutze, wenn nötig, den Taschenrechner.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>(-{{v1}})^{{v2}} = ___</mat>',
            correct='{{(-v1)**v2}}',
            variables={
                'v1': (choice, [2, 3, 4, 5, 10]),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>-{{v1}}^{{v2}} = ___</mat>',
            correct='-{{v1**v2}}',
            variables={
                'v1': (choice, [2, 3, 4, 5, 10]),
                'v2': (randint, 2, 5),
            }),
        ]
)

wiederholung_potenzen_berechnen = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzen kennenlernen',
    title='Wiederholung: Potenzen berechnen',
    instruction='Ordne die gleichwertigen Terme einander zu.',
    question_type='dragMatch',
    hint='Beispiel: <br> 3⁴=3*3*3*3',
    questions=[
        Question(
            formula='',
            correct='{{v1}}^3|{{v1}}*{{v1}}*{{v1}};'
                    '{{v2}}^2|{{v2}}*{{v2}};'
                    '{{v3}}^5|{{v3}}*{{v3}}*{{v3}}*{{v3}}*{{v3}};'
                    '{{v4}}^4|{{v4}}*{{v4}}*{{v4}}*{{v4}};'
                    '{{v5}}^7|{{v5}}*{{v5}}*{{v5}}*{{v5}}*{{v5}}*{{v5}}*{{v5}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
            }),
        ]
)

potenzfunktionen_kennenlernen = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzfunktionen',
    title='Potenzfunktionen kennenlernen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            instruction='Berechne das Ergebnis der Funktion <mat>f(x)=x^4</mat>',
            formula='<mat>x = {{v1}}</mat><br><br>'
                    '<mat>f(x) = ___</mat>.',
            correct='{{v1**4}}',
            variables={
                'v1': (randint, -5, 5),
            }),
        Question(
            instruction='Berechne das Ergebnis der Funktion <mat>f(x)=x^3</mat>',
            formula='<mat>x = {{v1}}</mat><br><br>'
                    '<mat>f(x) = ___</mat>.',
            correct='{{v1**3}}',
            variables={
                'v1': (randint, -5, 5),
            }),
        ]
)

der_vorfaktor = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzfunktionen',
    title='Der Vorfaktor',
    instruction='Ordne die Funktionsterme den Kategorien zu.',
    question_type='dragGroup',
    hint='Streckung: Vorfaktor |a|>1 <br> Stauchung: Vorfaktor |a|<1',
    questions=[
        Question(
            formula='',
            correct='Streckung|f(x)={{v1}}*x^{{v2}}~f(x)={{v3}}*x^{{v4}};'
                    'Stauchung|f(x)=1/{{v5}}*x^{{v6}}~f(x)=1/{{v7}}*x^{{v8}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randdecimal, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 9),
                'v9': (randint, 2, 9),
            }),
        ]
)

eigenschaften_zuordnen = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzfunktionen',
    title='Eigenschaften zuordnen',
    instruction='Entscheide anhand des Funktionsterms, ob der Graph gestreckt oder gestaucht wird.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>f(x)={{v1}}^{{v2}}</mat>',
            correct='gestreckt',
            wrong_1='gestaucht',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>f(x)={{v1}}^{{v2}}</mat>',
            correct='gestreckt',
            wrong_1='gestaucht',
            variables={
                'v1': (randdecimal, 1.1, 1.9),
                'v2': (randint, 2, 19),
            }),
        Question(
            formula='<mat>f(x)={{v1}}^{{v2}}</mat>',
            correct='gestaucht',
            wrong_1='gestreckt',
            variables={
                'v1': (randdecimal, 0.1, 0.9),
                'v2': (randint, 2, 19),
            }),
        ]
)

division_von_potenzen_mit_gleicher_basis_1 = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Division von Potenzen mit gleicher Basis (1)',
    instruction='Fasse die Potenzen so weit wie möglich zusammen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>x^{{v1*v3}}/x^{{v2*v3}} = x^(___ - ___) = ___</mat>',
            correct='{{v1*v3}};{{v2*v3}};x^{{v3}}',
            variables={
                'v1': (choice, [1, 3, 5, 7, 9]),
                'v2': (choice, [2, 4, 8]),
                'v3': (choice, [11, 111, 1111]),
            }),
        Question(
            formula='<mat>x^{{v1}}/y^{{v2}}+y^{{v3}}/y = x^___/y^{{v2}}+y^(___ - ___) = ___</mat>',
            correct='{{v1}};{{v3}};1;x^{{v1}}/y^{{v2}}+y^{{v3-1}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 3, 9),
            }),
        Question(
            formula='<mat>a^{{v1}}/a^(-{{v2}})=a^(___ - ___) = ___</mat>',
            correct='{{v1}};-{{v2}};a^{{v1+v2}}',
            variables={
                'v1': (randint, 11, 50),
                'v2': (randint, 11, 50),
            }),
        ]
)

division_von_potenzen_mit_gleicher_basis_2_mc = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Division von Potenzen mit gleicher Basis (2)',
    instruction='Wurden die Potenzen richtig oder falsch vereinfacht?',
    question_type='MC',
    questions=[
        Question(
            formula='y^(-{{v1}})/y^{{v2}}=y^({{v1}}-{{v2}})=y^(-{{v2-v1}})',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 8, 15),
            }),
        Question(
            formula='m^{{v1*2}}/m^{{v1}}:d^{{v1}}=(m/d)^{{v1}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 7),
            }),
        Question(
            formula='({{v1}}^{{v2}}/{{v2}}^{{v2**2}})/{{v3}}^(-{{v4}})={{v1}}^{{v2}}/{{v3}}^(-{{v4}})',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 31, 49),
                'v2': (randint, 3, 7),
                'v3': (randint, 15, 30),
                'v4': (randint, 2, 9),
            }),
        ]
)

division_von_potenzen_mit_gleicher_basis_2_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Division von Potenzen mit gleicher Basis (2)',
    instruction='Ordne den Potenzprodukten ihre äquivalenten Vereinfachungen zu. Beispiel:',
    question_type='dragMatch',
    hint="Beispiel:<br>"
         "<mat align='rcl'><c-green>(6x^3)/(2x^2)</c-green>||=||3x^(3-2)<br>"
         "||=||<cgreen>(1/2)x</c-green>",
    questions=[
        Question(
            formula='',
            correct='(x^{{v1+v3}}*y^{{v2+v3}})/(x^{{v3}}*y^{{v3}})|x^{{v1}}*y^{{v2}};'
                    '({{v4}}x^{{v5}})/({{v6}}x^{{v7}})|{{v4}}/{{v6}}x^{{v5-v7}};'
                    'y^{{v7+1}}/y|y^{{v7}};'
                    '(x^{{v8+1}}*y^{{v9+1}})/(x*y^{{v9}})|x^{{v8}}*y;'
                    '(y^{{v10}}*z^{{v11+1}})/(y^{{v10}}*z)|z^{{v11}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 7, 15),
                'v6': (randint, 2, 6),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 9),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 9),
            }),
        ]
)

division_von_potenzen_mit_gleicher_basis_2_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Division von Potenzen mit gleicher Basis (2)',
    instruction='Fasse die Potenzen zusammen und berechne den Potenzwert. Nutze, wenn nötig, den Taschenrechner.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>({{v1}}^{{v2+v3+v4}}/{{v1}}^{{v3}})/{{v1}}^{{v4}} = {{v1}}^___/{{v1}}^{{v4}} = ___</mat>',
            correct='{{v2+v4}};{{v1**v2}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 1, 3),
                'v3': (randint, 11, 19),
                'v4': (randint, 11, 19),
            }),
        Question(
            formula='<mat>c^(-{{v1}})/c^(-{{v1}}) = ___^___ = ___</mat>',
            correct='c;0;1',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}^{{v2}}/{{v1}}^{{v2+1}}={{v1}}^___ = ___/___^1 = ___</mat>',
            correct='-1;1;{{v1}};{{"%.1f"|format(1/v1)}}',
            variables={
                'v1': (choice, [2, 2.5, 5]),
                'v2': (randint, 2, 9),
            }),
        ]
)

multiplikation_von_potenzen_mit_gleicher_basis_1_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Multiplikation von Potenzen mit gleicher Basis (1)',
    instruction='Fasse die Potenzen so weit wie möglich zusammen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>y^{{v1}}*y^{{v2}}*y^{{v3}} = ___</mat>',
            correct='y^{{v1+v2+v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='<mat>a^{{v1}}*a^{{v2}}*a^{{v3}} = ___</mat>',
            correct='a^{{v1+v2+v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 11, 19),
                'v3': (randint, 2, 6),
            }),
        Question(
            formula='<mat>c^{{v1}}*c^{{v2}}*d^{{v3}}*d^{{v4}} = ___</mat>',
            correct='c^{{v1+v2}}*d^{{v3+v4}}',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 5, 15),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
            }),
        Question(
            instruction='Vereinfache den Term richtig.',
            formula='<mat>{{v1}}x^{{v2}}*{{v3}}x^{{v4}} = ___</mat>',
            correct='{{v1*v3}}x^{{v2+v4}}',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
            }),
        ]
)

multiplikation_von_potenzen_mit_gleicher_basis_1_mc = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Multiplikation von Potenzen mit gleicher Basis (1)',
    instruction='Wurden die Potenzen richtig oder falsch vereinfacht?',
    question_type='MC',
    questions=[
        Question(
            formula='c^{{v1}}*c^{{v2}}=c^({{v1}}+{{v2}})=c^{{v1+v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='y^{{v1}}*y^{{v2}}*y^{{v3}}=y^{{v1+v3-v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 2, 5),
                'v3': (randint, 3, 9),
            }),
        Question(
            formula='{{v1}}k^{{v2}}*{{v3}}k^{{v4}}={{v1*v3}}k^{{v2+v4}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}y^{{v2}}*y^{{v3}}*z^{{v4}}*{{v5}}z^{{v6}}={{v1*v3}}zy^{{v2+v5+v6}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 2, 5),
                'v6': (randint, 2, 5),
            }),
        Question(
            formula='{{v1}}x^{{v2}}*{{v1}}x^{{v3}}={{v1}}x^{{v2+v3}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
            }),
        ]
)

multiplikation_von_potenzen_mit_gleicher_basis_2_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Multiplikation von Potenzen mit gleicher Basis (2)',
    instruction='Ordne den Potenzprodukten ihre äquivalenten Vereinfachungen zu.',
    hint="<u>Beispiel:</u><br>"
         "<mat align='rcl'><c-green>2x^7*4x^2</c-green>||=||2*4*x^7*x^2<br>"
         "||=||8*x^(7+2)<br>||=||<c-green>8x^9</c-green>",
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1}}z^{{v2}}*{{v3}}z^{{v4}}|{{v1*v3}}z^{{v2+v4}};'
                    'x^{{v5}}*y^{{v5+v6}}*x^{{v6}}|(x*y)^{{v5+v6}};'
                    '{{v7}}x^{{v8}}*{{v9}}x^{{v10}}|{{v7*v9}}x^{{v8+v10}};'
                    'x^{{v11}}*x*x^({{v12}})|x^{{v11+v12+1}};'
                    'z^{{v13}}*x^{{v14}}*z^{{v15}}|x^{{v14}}*z^{{v13+v15}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 6),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 6),
                'v7': (randint, 2, 6),
                'v8': (randint, 2, 9),
                'v9': (randint, 2, 6),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 9),
                'v12': (randint, 2, 9),
                'v13': (randint, 2, 9),
                'v14': (randint, 2, 9),
                'v15': (randint, 2, 9),
            }),
        ]
)

multiplikation_von_potenzen_mit_gleicher_basis_2_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Multiplikation von Potenzen mit gleicher Basis (2)',
    instruction='Fasse die Potenzen zusammen und berechne den Potenzwert. Nutze, wenn nötig, den Taschenrechner.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>{{v1}}^{{v2}}*{{v1}}^{{v3}} = ___^___ = ___</mat>',
            correct='{{v1}};{{v2}}+{{v3}};{{v1**(v2+v3)}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 1, 3),
                'v3': (randint, 1, 3),
            }),
        Question(
            formula='<mat>(-{{v1}})^{{v2}}*(-{{v2}})^{{v3}} = (___)^___ = ___</mat>',
            correct='-{{v1}};{{v2}}+{{v3}};{{(-v1)**(v2+v3)}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 1, 3),
                'v3': (randint, 1, 3),
            }),
    ]
)

potenzen_mit_gleichen_exponenten_1_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen mit gleichen Exponenten (1)',
    instruction='Ordne den Potenzen ihre äquivalenten Vereinfachungen zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1}}x^{{v2}}*{{v3}}y^{{v2}}*{{v4}}z^{{v2}}|{{v1*v3*v4}}(x*y*z)^{{v2}};'
                    'x^{{v5}}*y^{{v5}}*x^{{v5}}*y^{{v5}}|(x*y)^{{2*v5}};'
                    '{{v6}}x^{{v7}}*{{v8}}y^{{v7}}|{{v6*v8}}(x*y)^{{v7}};'
                    'x^(-{{v9}})*y^(-{{v9}})|(x*y)^(-{{v9}});'
                    '-{{v10}}x^{{v11}}*y^{{v11}}|-{{v10}}(x*y)^{{v11}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 5),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 6),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 6),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 9),
            }),
        ]
)

potenzen_mit_gleichen_exponenten_1_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen mit gleichen Exponenten (1)',
    instruction='Fasse die Potenzen so weit wie möglich zusammen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>a^{{v1+v2}}*y^{{v1}}*y^{{v2}} = ___</mat>',
            correct='(a*y)^{{v1+v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>c^{{v1}}*d^{{v2}}*c^{{v3}}*d^{{v4}} = ___</mat>',
            correct='c^{{v1+v3}}*d^{{v2+v4}}',
            variables={
                'v1': (randint, 5, 15),
                'v2': (randint, 5, 15),
                'v3': (randint, 5, 15),
                'v4': (randint, 5, 15),
            }),
        Question(
            formula='<mat>(x*y)^{{v1}}/a^{{v1}} = ___</mat>',
            correct='((x*y)/a)^{{v1}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>a^(m+n)*(a^(-n)/b^m) = ___</mat>',
            correct='(a/b)^m',
            variables={
                'v1': (randint, 2, 7),
                'v2': (randint, 2, 7),
            }),
    ]
)

potenzen_mit_gleichen_exponenten_2_mc = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen mit gleichen Exponenten (2)',
    instruction='Wurden die Potenzen richtig oder falsch vereinfacht?',
    question_type='MC',
    questions=[
        Question(
            formula='x^{{v1}}*y^{{v1}}*z^{{v1}}=(x*y*z)^{{v1}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='c^{{v1}}*d^{{v1}}=cd^({{v1}}+{{v1}})=cd^{{v1*2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}m^{{v2+v3}}*{{v4}}n^{{v2}}*n^{{v3}}={{v1*v4}}(m*n)^{{v2+v3}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 6),
            }),
        Question(
            formula='f^{{v1}}*g^{{v1}}*h^{{v1}}=(f+g+h)^{{v1}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='(b^{{v1+v2}}*c^{{v1}}*c^{{v2}})/d^{{v1+v2}}=((b*c)/d)^{{v1+v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='(a^{{v1}}*b^{{v1}})/c^{{v1}}=((a*b*c)/c)^{{v1}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

potenzen_mit_gleichen_exponenten_2_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen mit gleichen Exponenten (2)',
    instruction='Ordne den Potenzen ihre äquivalenten Vereinfachungen zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='(a*b)^{{v1}}/a^{{v1}}|b^{{v1}};'
                    'a^{{v2}}/(b^{{v2+v3}}*b^(-{{v3}}))|(a/b)^{{v2}};'
                    'x^{{v4}}/(1/y^(-{{v4}}))|(x/y)^{{v4}};'
                    'x^(-{{v5}})/(y^(-{{v5+v6}})*y^{{v6}})|(x/y)^(-{{v5}});'
                    '(a^{{v7}}*b^{{v7}})/x^{{v7}}|((a*b)/x)^{{v7}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
            }),
        ]
)

potenzen_potenzieren_1 = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen potenzieren (1)',
    instruction='Wurden die Potenzen richtig oder falsch vereinfacht?',
    question_type='MC',
    questions=[
        Question(
            formula='(b^{{v1}})^{{v2}}=b^({{v1}}*{{v2}})=b^{{v1*v2}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='(y^(-{{v1+1}})*y^{{v1}})^{{v2}}=y^{{v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 8),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='(n^{{v1}})^{{v2}}=n^({{v1}}+{{v2}})=n^{{v1+v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='((e^{{v1}}*e^{{v2}})/(e^{{v3}}*f^{{v4}}))^{{v5}}='
                    '(e^{{v1+v2}}/(e^{{v3}}*f^{{v4}}))^{{v5}}=(e^{{v1+v2-v3}}/(1*f^{{v4}}))^{{v5}}='
                    'e^{{(v1+v2-v3)*v5}}/f^{{v4*v5}}',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 3, 7),
                'v2': (randint, 3, 7),
                'v3': (randint, 2, 5),
                'v4': (randint, 2, 6),
                'v5': (randint, 2, 3),
            }),
        Question(
            formula='({{v1}}y^{{v2}})^{{v3}}={{v1}}y^({{v2}}*{{v3}})={{v1}}y^{{v2*v3}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
            }),
        ]
)

potenzen_potenzieren_2_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen potenzieren (2)',
    instruction='Ordne den Potenzprodukten ihre äquivalenten Vereinfachungen zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='(p^(-{{v1}}))^{{v2}}|p^(-{{v1*v2}});'
                    '(p^{{v3*v4}})^(1/{{v3}})|p^{{v4}};'
                    '1/(p^{{v5*v6}})|(p^{{v5}})^(-{{v6}});'
                    '(x^r)^(r+{{v7}})|x^(r^2+{{v7}}r)',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
                'v4': (randint, 2, 9),
                'v5': (randint, 2, 6),
                'v6': (randint, 2, 6),
                'v7': (randint, 2, 9),
            }),
        ]
)

potenzen_potenzieren_2_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen potenzieren (2)',
    instruction='Fasse die Potenzen so weit wie möglich zusammen.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>((-x)^{{v1}})^{{v2}}/y^{{v1*v2}} = ___</mat>',
            correct='(-x/y)^{{v1*v2}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='<mat>(c^{{v1+v2}}/c^{{v2}})^{{v3}} = ___</mat>',
            correct='c^{{v1*v3}}',
            variables={
                'v1': (randint, 1, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 4),
            }),
        Question(
            formula='<mat>(((a^{{v1}})^(-{{v2}}))^{{v3}})^(-{{v4}})=a^(___*___*___*___) = ___</mat>',
            correct='{{v1}};-{{v2}};{{v3}};-{{v4}};a^{{v1*v2*v3*v4}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 1, 3),
                'v3': (randint, 2, 4),
                'v4': (randint, 1, 3),
            }),
        Question(
            formula='<mat>(x^{{v1*v2}})^{{v3}}*(y^{{v1}})^{{v2*v3}} = ___</mat>',
            correct='(x*y)^{{v1*v2*v3}}',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 4),
                'v3': (randint, 2, 4),
            }),
        ]
)

potenzen_potenzieren_2_gap_2 = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Potenzgesetze',
    title='Potenzen potenzieren (2)',
    instruction='Fasse die Potenzen zusammen und berechne den Potenzwert. Nutze, wenn nötig, den Taschenrechner.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>({{v1}}^(a))^({{v2}}*1/a) = {{v1}}^(___*___*___) = {{v1}}^___ = ___</mat>',
            correct='a;{{v2}};1/a;{{v2}};{{v1**v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='<mat>({{v1}}^(a+{{v2}})/{{v1}}^a)^2=({{v1}}^(___ - ___))^2 = {{v1}}^(___*___) = ___</mat>',
            correct='a+{{v2}};a;{{v2}};2;{{v1**(v2*2)}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 1, 2),
            }),
        Question(
            formula='<mat>({{v1}}*{{v2}}^2)^{{v3}} = ___</mat>',
            correct='{{(v1*(v2**2))**v3}}',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 2, 3),
                'v3': (randint, 2, 4),
            }),
        ]
)

hohere_wurzeln_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Wurzeln',
    title='Höhere Wurzeln',
    instruction='Schiebe die Terme zusammen, welche die Umkehrfunktion darstellen.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1}}^{{v2}} = {{v1**v2}}|root{{v2}}({{v1**v2}}) = {{v1}};'
                    '2^{{v3}} = {{2**v3}}|root{{v3}}({{2**v3}}) = 2;'
                    '1^{{v4}} = 1|root{{v4}}(1)= 1;'
                    'root{{v5}}({{v6**v5}}) = {{v6}}|{{v6}}^{{v5}} = {{v6**v5}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
                'v3': (randint, 2, 8),
                'v4': (randint, 9, 29),
                'v5': (randint, 2, 4),
                'v6': (randint, 2, 5),
            }),
        ]
)

hohere_wurzeln_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Wurzeln',
    title='Höhere Wurzeln',
    instruction='Berechne die Seitenlänge des Würfels.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>V = a^___<br>'
                    'a = root3(___m^3) = ___m</mat>',
            correct='3;{{v1**3}};{{v1}}',
            variables={
                'v1': (randint, 2, 7),
            },
            image={
                'draw_grid': False,
                'draw_axes': False,
                'axis_limits': {'xmin': '0',
                                'xmax': '3',
                                'ymin': '0',
                                'ymax': '3'},
                'polygons': [
                    {'xy': [(0, 0), (0, 2), (2, 2), (2, 0)],
                     'closed': True,
                     'facecolor': '#C5CBE8',
                     'edgecolor': '#8B8F9F',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(0, 2), (1, 2.5), (3, 2.5), (2, 2)],
                     'closed': True,
                     'facecolor': '#D3D8EE',
                     'edgecolor': '#8B8F9F',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(2, 0), (3, 0.5), (3, 2.5), (2, 2)],
                     'closed': True,
                     'facecolor': '#9EA2BA',
                     'edgecolor': '#8B8F9F',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                ],
                'texts': [
                    {'x': '1',
                     'y': '1',
                     's': 'V = {{v1**3}} m³',
                     'fontsize': 'x-large',
                     'color': '#4352A5',
                     'ha': 'center',
                     'va': 'center',
                     },
                    {'x': '1',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': '#4352A5',
                     'ha': 'center',
                     'va': 'top',
                     },
                    {'x': '2.6',
                     'y': '0.2',
                     's': 'a',
                     'fontsize': 'large',
                     'color': '#4352A5',
                     'ha': 'left',
                     'va': 'center',
                     },
                    {'x': '3.1',
                     'y': '1.5',
                     's': 'a',
                     'fontsize': 'large',
                     'color': '#4352A5',
                     'ha': 'left',
                     'va': 'center',
                     },
                ]
            },
        ),
        ]
)

quadratwurzeln = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Wurzeln',
    title='Quadratwurzeln',
    instruction='Löse diese Aufgabe.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>sqrt({{v1**2}}) = ____</mat>',
            correct='{{v1}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>sqrt(___) = {{v1}}</mat>',
            correct='{{v1**2}}',
            variables={
                'v1': (randint, 11, 16),
            }),
        Question(
            formula='<mat>sqrt(___) = {{v1}}</mat>',
            correct='{{v1**2}}',
            variables={
                'v1': (randrange, 1100, 1600, 100),
            }),
        Question(
            formula='<mat>sqrt({{v1**2}}) = ____</mat>',
            correct='{{v1}}',
            variables={
                'v1': (randrange, 20, 90, 10),
            }),
        Question(
            instruction='Löse diese Gleichung.',
            hint="Forme die Gleichungen um, indem du auf beiden Seiten Rechenschritte durchführst "
                 "und die Variable so isolierst. Hier ein Beispiel:<br> <mat>2x=4 || :2<br>x=2</mat>",
            formula='<mat>(x^2)/2 = {{v1*v1*2}}<br>'
                    'x^2 = ___<br>x = ± sqrt(___)<br>'
                    'x_1 = ___<br>x_2 = ___</mat>',
            correct='{{4*v1**2}};{{4*v1**2}};{{4*v1*2}};-{{4*v1*2}}',
            variables={
                'v1': (randint, 2, 6),
            }),
        Question(
            instruction='Löse diese Gleichung.',
            hint="Forme die Gleichungen um, indem du auf beiden Seiten Rechenschritte durchführst "
                 "und die Variable so isolierst. Hier ein Beispiel:<br> <mat>2x=4 || :2<br>x=2</mat>",
            formula='<mat>{{v1}}x^2 = {{v1*(v2**2)}}<br>'
                    'x^2 = ___<br>x = ± sqrt(___)<br>'
                    'x_1 = ___<br>x_2 = ___</mat>',
            correct='{{v2**2}};{{v2**2}};{{v2}};-{{v2}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 8),
            }),
        ]
)

sachaufgaben = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Wurzeln',
    title='Sachaufgaben',
    instruction='Berechne die Seitenlänge a der Quadrate und den Umfang U der Figur',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>A = {{5*(v1**2)}} m^2</mat>'
                    '<mat>A_Quadrat = {{5*(v1**2)}} m^2 : ___ = ___ m^2<br>'
                    'a = sqrt( ___ m^2) = ___ m<br>'
                    'U = n * a = ___ *___<br>→ U = ___ m</mat>',
            correct='5;{{v1**2}};{{v1**2}};{{v1}};12;{{v1}};{{12*v1}}',
            variables={
                'v1': (randint, 2, 8),
            },
            image={
                'draw_grid': False,
                'draw_axes': False,
                'axis_limits': {'xmin': '0',
                                'xmax': '5',
                                'ymin': '0',
                                'ymax': '1'},
                'polygons': [
                    {'xy': [(0, 0), (0, 1), (1, 1), (1, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(1, 0), (1, 1), (2, 1), (2, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(2, 0), (2, 1), (3, 1), (3, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(3, 0), (3, 1), (4, 1), (4, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(4, 0), (4, 1), (5, 1), (5, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                ],
                'texts': [
                    {'x': '0.5',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'va': 'top',
                     },
                    {'x': '1.5',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'va': 'top',
                     },
                    {'x': '2.5',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'va': 'top',
                     },
                    {'x': '3.5',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'va': 'top',
                     },
                    {'x': '4.5',
                     'y': '-0.1',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'va': 'top',
                     },
                ]
            },
        ),
        Question(
            formula='<mat>A = {{8*(v1**2)}} m^2</mat>'
                    '<mat>A_Quadrat = {{8*(v1**2)}} m^2 : ___ = ___ m^2<br>'
                    'a = sqrt(___ m^2) = ___ m<br>'
                    'U = n * a = ___ * ___<br>→U = ___ m</mat>',
            correct='8;{{v1**2}};{{v1**2}};{{v1}};18;{{v1}};{{18*v1}}',
            variables={
                'v1': (randint, 2, 8),
            },
            image={
                'draw_grid': False,
                'draw_axes': False,
                'axis_limits': {'xmin': '0',
                                'xmax': '5',
                                'ymin': '-1',
                                'ymax': '2'},
                'polygons': [
                    {'xy': [(0, 0), (0, 1), (1, 1), (1, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(0, 1), (0, 2), (1, 2), (1, 1)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(1, 0), (1, 1), (2, 1), (2, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(2, 0), (2, 1), (3, 1), (3, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(2, -1), (2, 0), (3, 0), (3, -1)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(3, 0), (3, 1), (4, 1), (4, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(4, 0), (4, 1), (5, 1), (5, 0)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                    {'xy': [(4, 1), (4, 2), (5, 2), (5, 1)],
                     'closed': True,
                     'edgecolor': 'black',
                     'facecolor': 'None',
                     'linewidth': 2,
                     'zorder': 3,
                     },
                ],
                'texts': [
                    {'x': '1.1',
                     'y': '1.5',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'ha': 'left',
                     },
                    {'x': '3.9',
                     'y': '1.5',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'ha': 'right',
                     },
                    {'x': '3.1',
                     'y': '-0.5',
                     's': 'a',
                     'fontsize': 'large',
                     'color': 'tab:blue',
                     'ha': 'left',
                     },
                ]
            },
        )
    ]
)

einheitenprafixe = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Zehnerpotenzen kennenlernen',
    title='Einheitenpräfixe',
    instruction='Ordne Potenz und entsprechendes Einheitenpräfix einander zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='Kilo|10^3;'
                    'Mega|10^6;'
                    'Zenti|10^(-2);'
                    'Milli|10^(-3);'
                    'Giga|10^9',
            variables={
            }),
        ]
)

schreibweisen_1_draggroup = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Zehnerpotenzen kennenlernen',
    title='Schreibweisen (1)',
    instruction='Ordne die Angaben der wissenschaftlichen und der technischen Schreibweise zu.',
    question_type='dragGroup',
    hint='Bei der wissenschaftlichen Schreibweise darf die Dezimalzahl nur eine Stelle vor dem Komma haben. '
         'Die Ziffer vor dem Komma darf dabei nicht 0 sein.<br>'
         'Bei der technischen Schreibweise ist der Exponent der Zehnerpotenz immer ein Vielfaches von drei.',
    questions=[
        Question(
            formula='',
            correct='wissenschaftliche Schreibweise|{{v1}}*10^{{v5}} m~{{v2}}*10^{{v11}}W~{{v3}}*10^{{v12}} kg~{{v4}}*10^{{v13}} m;'
                    'technische Schreibweise|{{v6}}*10^{{v10}} m~{{v7}} MW~{{v8}}*10^{{v14}} kg~{{v9}}*10^{{v15}} m',
            variables={
                'v1': (randdecimal, 2, 8),
                'v2': (randint, 2, 10),
                'v3': (randdecimal, 2, 8, 0.01, 2),
                'v4': (randdecimal, 2, 8, 0.001, 3),
                'v5': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v11': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v12': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v13': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v6': (randdecimal, 2, 8),
                'v7': (randdecimal, 0.1, 0.9),
                'v8': (randdecimal, 20, 80, 0.01, 2),
                'v9': (randint, 20, 80),
                'v10': (choice, [3, 6, 9, 12, 15, 18, 21]),
                'v14': (choice, [3, 6, 9, 12, 15, 18, 21]),
                'v15': (choice, [3, 6, 9, 12, 15, 18, 21]),
            }),
        ]
)

schreibweisen_2_draggroup = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Zehnerpotenzen kennenlernen',
    title='Schreibweisen (2)',
    instruction='Ordne die Angaben der wissenschaftlichen und der technischen Schreibweise zu.',
    question_type='dragGroup',
    hint='Bei der wissenschaftlichen Schreibweise darf die Dezimalzahl nur eine Stelle vor dem Komma haben. '
         'Die Ziffer vor dem Komma darf dabei nicht 0 sein.<br>Bei der technischen Schreibweise ist '
         'der Exponent der Zehnerpotenz immer ein Vielfaches von drei.',
    questions=[
        Question(
            formula='',
            correct='wissenschaftliche Schreibweise|{{v1}}*10^(-{{v5}}) m~{{v2}}*10^(-{{v6}})m~{{v3}}*10^(-{{v7}}) g~{{v4}}*10^(-{{v8}}) g;'
                    'technische Schreibweise|{{v9}}*10^(-{{v13}}) m~{{v10}}*10^(-{{v14}}) m~{{v11}}*10^(-{{v15}}) g~{{v12}}*10^(-{{v16}}) g',
            variables={
                'v1': (randdecimal, 2, 8),
                'v2': (randdecimal, 2, 8),
                'v3': (randdecimal, 2, 8, 0.01, 2),
                'v4': (randdecimal, 2, 8, 0.001, 3),
                'v5': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v6': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v7': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v8': (choice, [2, 4, 5, 7, 10, 13, 16, 17, 22, 23]),
                'v9': (randdecimal, 2, 8),
                'v10': (randint, 2, 10),
                'v11': (randdecimal, 20, 80, 0.01, 2),
                'v12': (randdecimal, 0.1, 0.9),
                'v13': (choice, [3, 6, 9, 12, 15, 18, 21]),
                'v14': (choice, [3, 6, 9, 12, 15, 18, 21]),
                'v15': (choice, [3, 6, 9, 12, 15, 18, 21]),
                'v16': (choice, [3, 6, 9, 12, 15, 18, 21]),
            }),
        ]
)

zehnerpotenzen_berechnen_dragmatch = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Zehnerpotenzen kennenlernen',
    title='Zehnerpotenzen berechnen',
    instruction='Ordne Potenz und gleichwertigen Potenzwert einander zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            hint='Bei Zehnerpotenzen entspricht ein positiver Exponent der Anzahl der Nullen im Potenzwert.',
            correct='{{10**v1}}|10^{{v1}};'
                    '{{10**v2}}|10^{{v2}};'
                    '{{10**v3}}|10^{{v3}};'
                    '{{10**v4}}|10^{{v4}}',
            variables={
                'v1': (randint, 1, 10),
                'v2': (randint, 1, 10),
                'v3': (randint, 1, 10),
                'v4': (randint, 1, 10),
            }),
        Question(
            formula='',
            hint='Bei Zehnerpotenzen entspricht der Betrag eines negativen Exponenten '
                 'der Anzahl der Nachkommastellen im Potenzwert.',
            correct='0.{{"0"*(v1-1)}}1|10^(-{{v1}});'
                    '0.{{"0"*(v2-1)}}1|10^(-{{v2}});'
                    '0.{{"0"*(v3-1)}}1|10^(-{{v3}});'
                    '0.{{"0"*(v4-1)}}1|10^(-{{v4}})',
            variables={
                'v1': (randint, 1, 10),
                'v2': (randint, 1, 10),
                'v3': (randint, 1, 10),
                'v4': (randint, 1, 10),
            }),
        ]
)

zehnerpotenzen_berechnen_gap = QuestionSet(
    grade='9',
    capital='Wurzeln und Potenzen',
    subcapital='Zehnerpotenzen kennenlernen',
    title='Zehnerpotenzen berechnen',
    instruction='Schreibe den Potenzwert der Zehnerpotenz.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>10^{{v1}} = ___</mat>',
            correct='{{10**v1}}',
            variables={
                'v1': (randint, 4, 10),
            }),
        Question(
            formula='<mat>10^(-{{v1}}) = ___</mat>',
            correct='0.{{"0"*(v1-1)}}1',
            variables={
                'v1': (randint, 3, 10),
            }),
        ]
)

question_sets = [
    naherungswert_bestimmen,
    wurzeln_mit_variablen_dragmatch,
    wurzeln_mit_variablen_gap,
    mit_variablen_in_wurzeln_rechnen,
    potenzen_mit_bruch_als_basis_dragmatch,
    potenzen_mit_bruch_als_basis_gap,
    potenzen_mit_bruch_im_exponenten_1_mc,
    potenzen_mit_bruch_im_exponenten_1_gap,
    potenzen_mit_bruch_im_exponenten_2_dragmatch,
    potenzen_mit_bruch_im_exponenten_2_gap,
    potenzen_mit_negativem_exponenten_dragmatch,
    potenzen_mit_negativem_exponenten_gap,
    potenzen_mit_negativer_basis_berechnen_draggroup,
    potenzen_mit_negativer_basis_berechnen_gap,
    wiederholung_potenzen_berechnen,
    potenzfunktionen_kennenlernen,
    der_vorfaktor,
    eigenschaften_zuordnen,
    division_von_potenzen_mit_gleicher_basis_1,
    division_von_potenzen_mit_gleicher_basis_2_mc,
    division_von_potenzen_mit_gleicher_basis_2_dragmatch,
    division_von_potenzen_mit_gleicher_basis_2_gap,
    multiplikation_von_potenzen_mit_gleicher_basis_1_gap,
    multiplikation_von_potenzen_mit_gleicher_basis_1_mc,
    multiplikation_von_potenzen_mit_gleicher_basis_2_dragmatch,
    multiplikation_von_potenzen_mit_gleicher_basis_2_gap,
    potenzen_mit_gleichen_exponenten_1_dragmatch,
    potenzen_mit_gleichen_exponenten_1_gap,
    potenzen_mit_gleichen_exponenten_2_mc,
    potenzen_mit_gleichen_exponenten_2_dragmatch,
    potenzen_potenzieren_1,
    potenzen_potenzieren_2_dragmatch,
    potenzen_potenzieren_2_gap,
    potenzen_potenzieren_2_gap_2,
    hohere_wurzeln_dragmatch,
    hohere_wurzeln_gap,
    quadratwurzeln,
    sachaufgaben,
    einheitenprafixe,
    schreibweisen_1_draggroup,
    schreibweisen_2_draggroup,
    zehnerpotenzen_berechnen_dragmatch,
    zehnerpotenzen_berechnen_gap,
    ]
