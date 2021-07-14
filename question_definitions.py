import random

from questions import Question, QuestionSet
from random import randint


def randdecimal(a, b):
    """ Return random decimal between a and b with 1 digit precision."""
    return round(random.uniform(a, b), 1)


terme_mit_potenzen = QuestionSet(
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme mit Potenzen',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='({{v1}}x)^2',
            correct='{{v1}}*{{v1}}*x*x',
            wrong_1='{{v1}}*{{v1}}*x',
            wrong_2='{{v1}}*x*x',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='({{v1}}a)^2',
            correct='{{v1}}*{{v1}}*a*a',
            wrong_1='{{v1}}*{{v1}}*a',
            wrong_2='{{v1}}*a*a',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='({{v1}}y)^3',
            correct='{{v1}}*{{v1}}*{{v1}}*y*y*y',
            wrong_1='{{v1}}*{{v1}}*{{v1}}*y',
            wrong_2='{{v1}}*{{v1}}*y*y*y',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='(-b)^3',
            correct='(-1)*(-1)*(-1)*b*b*b',
            wrong_1='b',
            wrong_2='b*b*b',
            variables={}),
        Question(
            formula='(-{{v1}}xy)^2',
            correct='(-{{v1}})*(-{{v1}})*x*x*y*y',
            wrong_1='(-{{v1}})*(-{{v1}})*x*x*y',
            wrong_2='(-{{v1}})*(-{{v1}})*x*y*y',
            variables={}),
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
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}xz-{{v2}}xy',
            correct='x',
            wrong_1='y',
            wrong_2='z',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}u^2-{{v2}}uv',
            correct='u',
            wrong_1='v',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
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
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}xyz-{{v2}}x^2 = x({{v1}}yz-{{v2}})',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}a^2b+{{v2}}ac^2 = a({{v1}}ab+{{v2}}ac^2)',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='abc-ab-ac = a(bc-b-c)',
            correct='correct',
            wrong_1='wrong',
            variables={}),
        ]
)

nennergleiche_bruchterme_addieren = QuestionSet(
    capital='Terme',
    subcapital='Bruchterme',
    title='Nennergleiche Bruchterme addieren',
    instruction='Zu welchem Bruchterm ist der folgende Bruchterm äquivalent?',
    question_type='MC',
    questions=[
        Question(
            formula='(x+y)/x + (x-y)/x',
            correct='(x+y+x-y)/x',
            wrong_1='(x+y+x-y)/x^2',
            wrong_2='(x+y-x+y)/x',
            variables={}),
        Question(
            formula='b/(a-b) - ({{v1}}a+b)/(a-b)',
            correct='(b-{{v1-1}}a-b)/(a-b)',
            wrong_1='(b-{{v1-1}}a-b)/(a-b)^3',
            wrong_2='(b-{{v1-1}}a+b)/(a-b)',
            variables={
                'v1': (randint, 3, 9),
            }),
        Question(
            formula='({{v1}}x(x+1))/(x+y) - (x(y+1))/(x+y)',
            correct='({{v1}}x^2+{{v1}}x-xy-x)/(x+y)',
            wrong_1='({{v1}}x^2+{{v1}}x-xy-x)/({{v1+1}}x+{{v1+1}}y)',
            wrong_2='({{v1}}x^2+{{v1}}x-xy+x)/(x+y)',
            variables={
                'v1': (randint, 3, 8),
            }),
        Question(
            formula='(a^2-{{v1}}ab)/(a+b)^2 - (a(a-{{v2}}b))/(a+b)^2',
            correct='(a^2-{{v1}}ab-a^2+{{v2}}ab)/(a+b)^2',
            wrong_1='(a^2-{{v1}}ab-a^2-{{v2}}ab)/(a+b)^2',
            wrong_2='(a^2-{{v1}}ab+a^2-{{v2}}ab)/(a+b)^2',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        ]
)

terme_vereinfachen_2 = QuestionSet(
    capital='Terme',
    subcapital='Terme mit Variablen',
    title='Terme vereinfachen (2)',
    instruction='Vereinfache den folgenden Term.',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}+{{v2}}*y+{{v3}}*y',
            correct='{{v1}}+{{v2+v3}}y',
            wrong_1='{{v1+v2}}+{{v3}}y',
            wrong_2='{{v1+v2}}+{{v2+v3}}y',
            variables={
                'v1': (randint, 11, 20),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}*{{v2}}*a*b:c',
            correct='({{v1*v2}}ab)/c',
            wrong_1='{{v1*v2}}abc',
            wrong_2='({{v1}}{{v2}}ab)/c',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 3, 6),
            }),
        Question(
            formula='{{v1}}*({{v2}}*x+(-1)*y)',
            correct='{{v1*v2}}x-{{v1}}y',
            wrong_1='{{v1}}{{v2}}x-{{v1}}y',
            wrong_2='{{v1*v2}}x+{{v1}}y',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        ]
)

terme_zuordnen_dragGroup = QuestionSet(
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Ordne jedem Term die Formel zu, mit der der Term ausgerechnet werden kann.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='1. binomische Formel|({{v1}}+x)^2~(b+{{v2}})^2, ' +
                    '2. binomische Formel|(a-{{v3}})^2~({{v4}}-z)^2, ' +
                    '3. binomische Formel|({{v5}}-b)({{v5}}+b)~(y+{{v6}})(y-{{v6}})',
            variables={
                'v1': (randint, 2, 10),
                'v2': (randint, 2, 10),
                'v3': (randint, 2, 10),
                'v4': (randdecimal, 0.3, 0.9),
                'v5': (randint, 2, 10),
                'v6': (randint, 2, 10),
            }),
    ]
)

terme_zuordnen_dragMatch = QuestionSet(
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Füge äquivalente Terme zusammen.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='({{v1}}+x)^2|{{v1**2}}+{{2*v1}}x+x^2,' +
                    '(x-{{v2}})^2|x^2-{{2*v2}}x+{{v2**2}},' +
                    '({{v3}}-x)({{v3}}+x)|{{v3**2}}-x^2',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
            }),
        Question(
            formula='',
            correct='(v+{{v1}})^2|v^2+{{2*v1}}v+{{v1**2}},' +
                    '({{v2}}-v)^2|{{v2**2}}-{{2*v2}}v+v^2,' +
                    '(v+{{v3}})(v-{{v3}})|v^2-{{v3**2}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 3, 9),
                'v3': (randint, 5, 15),
            }),
    ]
)


# Add newly created question sets in that list, so the script can use them
question_sets = [
    terme_mit_potenzen,
    variablen_ausklammern,
    variable_richtig_ausgeklammert,
    terme_zuordnen_dragGroup,
    terme_zuordnen_dragMatch,
]

# #        Question(
#             formula='{{v1}} + x * y + {{v2}} * z',
#             correct='{{v1}} + xy + {{v2}}z',
#             wrong_1='{{v1}}x + {{v1}}y + {{v2}}z',
#             variables={
#                 'v1': (randint, 2, 10),
#                 'v2': (randint, 2, 10),
#             }),
#         Question(
#             formula='{{v1}} * a * b : c',
#             correct='({{v1}}ab) / c',
#             wrong_1='{{v1}} + (ab) / c',
#             wrong_2='{{v1}}abc',
#             variables={
#                 'v1': (randint, 2, 20),
#             }),
#         Question(
#             formula='{{v1}} * ( {{v2}} * x + {{v3}} )',
#             correct='{{v1 * v2}}x + {{v1*v3}}',
#             wrong_1='{{(v1+1) * v2}}x + {{(v1-1)*v3}}',
#             wrong_2='{{v1+v2+v3}}x',
#             variables={
#                 'v1': (randint, 2, 20),
#                 'v2': (randint, 2, 10),
#                 'v3': (randint, 5, 12),
#             }),