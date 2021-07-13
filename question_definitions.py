import random

from questions import Question, QuestionSet
from random import randint


def randdecimal(a, b):
    """ Return random decimal between a and b with 1 digit precision."""
    return round(random.uniform(a, b), 1)


terme_potenzen_q1 = Question(
    formula='{{v1}} + x * y + {{v2}} * z',
    correct='{{v1}} + xy + {{v2}}z',
    wrong_1='{{v1}}x + {{v1}}y + {{v2}}z',
    variables={
        'v1': (randint, 2, 10),
        'v2': (randint, 2, 10),
    })

terme_potenzen_q2 = Question(
    formula='{{v1}} * a * b : c',
    correct='({{v1}}ab) / c',
    wrong_1='{{v1}} + (ab) / c',
    wrong_2='{{v1}}abc',
    variables={
        'v1': (randint, 2, 20),
    })

terme_potenzen_q3 = Question(
    formula='{{v1}} * ( {{v2}} * x + {{v3}} )',
    correct='{{v1 * v2}}x + {{v1*v3}}',
    wrong_1='{{(v1+1) * v2}}x + {{(v1-1)*v3}}',
    wrong_2='{{v1+v2+v3}}x',
    variables={
        'v1': (randint, 2, 20),
        'v2': (randint, 2, 10),
        'v3': (randint, 5, 12),
    })

terme_potenzen_q4 = Question(
    formula='({{v1}}x)^2',
    correct='{{v1}}*{{v1}}*x*x',
    wrong_1='{{v1}}*{{v1}}*x',
    wrong_2='{{v1}}*x*x',
    variables={
        'v1': (randint, 2, 9),
    })

terme_mit_potenzen = QuestionSet(
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme mit Potenzen',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        terme_potenzen_q1,
        terme_potenzen_q2,
        terme_potenzen_q3,
        terme_potenzen_q4,
        ]
)

variablen_ausklammern = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Variablen ausklammern',
    instruction='Welche Variable kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}a+ab',
            correct='a',
            wrong_1='b',
            variables={
                'v1': (randint, 2, 10),
            }),
        Question(
            formula='{{v1}}xz-{{v2}}xy',
            correct='x',
            wrong_1='y',
            wrong_2='z',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 10),
            }),
        ]
)

variable_richtig_ausgeklammert = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Variablen ausklammern',
    instruction='Wird die Variable richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}xy-xz = x({{v1}}y-z)',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 10),
            }),
        Question(
            formula='{{v1}}xyz-{{v2}}x^2 = x({{v1}}yz-{{v2}})',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 10),
            }),
        ]
)

terme_zuordnen = QuestionSet(
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Ordne jedem Term die Formel zu, mit der der Term ausgerechnet werden kann.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='1. binomische Formel|({{v1}}+x)^2~(b+{{v2}})^2, '  # strings will be automatically joined
                    '2. binomische Formel|(a-{{v3}})^2~({{v4}}-z)^2, '
                    '3. binomische Formel|({{v5}}-b)({{v5}}+b)~(y+{{v6}})(y-{{v6}})',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 10),
                'v3': (randint, 2, 10),
                'v4': (randdecimal, 0.5, 0.9),
                'v5': (randint, 2, 10),
                'v6': (randint, 2, 10),
            }),
    ]
)

question_sets = [
    terme_mit_potenzen,
    variablen_ausklammern,
    variable_richtig_ausgeklammert,
    terme_zuordnen,
]
