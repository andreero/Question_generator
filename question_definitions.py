import random

from questions import Question, QuestionSet
from random import randint


def randdecimal(a, b):
    """ Return random decimal between a and b with 1 digit precision."""
    return round(random.uniform(a, b), 1)


terme_zuordnen_dragGroup = QuestionSet(
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Ordne jedem Term die Formel zu, mit der der Term ausgerechnet werden kann.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='1. binomische Formel|({{v1}}+x)^2~(b+{{v2}})^2;' +
                    '2. binomische Formel|(a-{{v3}})^2~({{v4}}-z)^2;' +
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
            correct='({{v1}}+x)^2|{{v1**2}}+{{2*v1}}x+x^2;' +
                    '(x-{{v2}})^2|x^2-{{2*v2}}x+{{v2**2}};' +
                    '({{v3}}-x)({{v3}}+x)|{{v3**2}}-x^2',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
                'v3': (randint, 2, 6),
            }),
        Question(
            formula='',
            correct='(v+{{v1}})^2|v^2+{{2*v1}}v+{{v1**2}};' +
                    '({{v2}}-v)^2|{{v2**2}}-{{2*v2}}v+v^2;' +
                    '(v+{{v3}})(v-{{v3}})|v^2-{{v3**2}}',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 3, 9),
                'v3': (randint, 5, 15),
            }),
    ]
)

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
            variables={
                'v1': (randint, 2, 9)
            }),
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

multiplizieren_und_dividieren = QuestionSet(
    capital='Terme',
    subcapital='Bruchterme',
    title='Multiplizieren und dividieren',
    instruction='Zu welchem Bruchterm ist der folgende Bruchterm äquivalent?',
    question_type='MC',
    questions=[
        Question(
            formula='(xy^2)/({{v1}}z)*({{v2}}x)/({{v3}}yz)',
            correct='({{v2}}x^2y^2)/({{v1*v3}}yz^2)',
            wrong_1='({{v1}}xy^3z)/({{v2*v3}}xz)',
            wrong_2='({{v2}}x^2y^2)/({{v1}}z)',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='({{v1}}a+bc)/({{v2}}ab)*a/(a+b)',
            correct='({{v1}}a^2+abc)/({{v2}}a^2b+{{v2}}ab^2)',
            wrong_1='({{v1}}a^2+bc)/(a+b)',
            wrong_2='({{v1}}a^2+abc+{{v1}}ab+b^2c)/({{v2}}a^2b)',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='(x^2y)/({{v1}}z^3):(xy)/({{v2}}z^2)',
            correct='({{v1}}x^2yz^2)/({{v2}}xyz^3)',
            wrong_1='(x^3y^2)/({{v1*v2}}z^5)',
            wrong_2='(x^2y)/({{v2}}xyz^3)',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='((a+b)(a-b))/c:(a+b)/c^2',
            correct='((a+b)(a-b)c^2)/(c(a+b))',
            wrong_1='((a+b)^2(a-b))/(c^3)',
            wrong_2='((a+b)^2(a-b))/(c^2)',
            variables={}),
        ]
)

produkte_ausklammern = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Produkte ausklammern',
    instruction='Welche Faktoren kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}ab+abc',
            correct='ab',
            wrong_1='{{v1}}b',
            wrong_2='ac',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}cd+{{v1}}fc',
            correct='{{v1}}c',
            wrong_1='cd',
            wrong_2='{{v1}}d',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1*2}}m+{{v1*5}}m^2',
            correct='{{v1}}m',
            wrong_1='2m',
            wrong_2='5m',
            variables={
                'v1': (randint, 1, 4),
            }),
        Question(
            formula='((a+b)(a-b))/c:(a+b)/c^2',
            correct='((a+b)(a-b)c^2)/(c(a+b))',
            wrong_1='((a+b)^2(a-b))/(c^3)',
            wrong_2='((a+b)^2(a-b))/(c^2)',
            variables={}),
        ]
)

produkt_richtig_ausgeklammert = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Produkte ausklammern',
    instruction='Wo wurde das Produkt richtig ausgeklammert?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}ab+abc',
            correct='ab*({{v1}}+c)',
            wrong_1='ab*({{v1}}+a)',
            wrong_2='ac*({{v1}}+b)',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1*2}}m+{{v1*5}}m^2',
            correct='{{v1}}m*(2+5m)',
            wrong_1='{{v1}}m*(5+2m)',
            wrong_2='{{v1}}m*(5m)',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

terme_multiplizieren = QuestionSet(
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme multiplizieren',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}*({{v2}}x)',
            correct='({{v1}}*{{v2}})*x',
            wrong_1='({{v1}}*{{v2}})*x*x',
            wrong_2='({{v1}}*{{v2}}*{{v1}})*x',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='-{{v1}}a*({{v2}})',
            correct='(-{{v1}}*{{v2}})*a',
            wrong_1='({{v1}}*{{v2}})*a',
            wrong_2='(-{{v1}}*{{v2}})*a*{{v2}}',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randdecimal, 0.2, 0.9),
            }),
        Question(
            formula='{{v1}}y*{{v2}}y',
            correct='({{v1}}*{{v2}})*y*y',
            wrong_1='{{v1}}*y*y',
            wrong_2='({{v1}}*{{v2}})*y',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
            }),
        Question(
            formula='1/{{v1}}b^2*1/{{v2}}b',
            correct='(1/{{v1}}*1/{{v2}})*b^2*b',
            wrong_1='(1/{{v1}}*1/{{v2}})*b^2',
            wrong_2='(1/{{v1}}*1/{{v2}})*b^2*b^2',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}xy*1/{{v2}}y^2',
            correct='({{v1}}*1/{{v2}})*x*y*y^2',
            wrong_1='({{v1}}*1/{{v2}})*x*y^2',
            wrong_2='({{v1}}*1/{{v2}})*y*y^2',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}/{{v2}}a^2b*1/{{v1}}ab^2',
            correct='({{v1}}/{{v2}}*1/{{v1}})*a^2*a*b*b^2',
            wrong_1='({{v1}}/{{v2}}*{{v1}})*a^2*a*b*b^2',
            wrong_2='({{v1}}/{{v2}}*1/{{v1}})*a*a*b*b',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 2, 4),
            }),
        ]
)

vorrangregeln = QuestionSet(
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Vorrangregeln',
    instruction='Welche Rechnung muss zuerst durchgeführt werden?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}*(2*{{v2}}+1)',
            correct='2*{{v2}}',
            wrong_1='{{v2}}+1',
            wrong_2='{{v1}}*2',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 3, 5),
            }),
        Question(
            formula='({{v1}}-{{v2}})*{{v3}}^2',
            correct='{{v1}}-{{v2}}',
            wrong_1='{{v3}}^2',
            wrong_2='-{{v2}}*{{v3}}',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 5, 9),
                'v3': (randint, 2, 4),
            }),
        Question(
            formula='({{v1}}-{{v2}})^2:{{v3}}^2',
            correct='{{v1}}-{{v2}}',
            wrong_1='{{v3}}^2',
            wrong_2='-{{v2}}^2',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 4, 5),
                'v3': (randint, 2, 3),
            }),
        ]
)

faktorisieren_2 = QuestionSet(
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Faktorisieren (2)',
    instruction='Welche binomische Formel musst du für die Faktorisierung anwenden?',
    question_type='MC',
    questions=[
        Question(
            formula='x^2+{{2*v1}}x+{{v1**2}}',
            correct='1. binomische Formel',
            wrong_1='2. binomische Formel',
            wrong_2='3. binomische Formel',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1**2}}-y^2',
            correct='3. binomische Formel',
            wrong_1='1. binomische Formel',
            wrong_2='2. binomische Formel',
            variables={
                'v1': (randint, 5, 15),
            }),
        Question(
            formula='{{v1**2}}-{{2*v1}}z+z^2',
            correct='2. binomische Formel',
            wrong_1='1. binomische Formel',
            wrong_2='3. binomische Formel',
            variables={
                'v1': (randint, 3, 9),
            }),
        ]
)

wertgleiche_terme_zuordnen = QuestionSet(
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Wertgleiche Terme zuordnen',
    instruction='Ordne wertgleiche Terme zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1+v2}}x+{{v3-v4}}|{{v1}}x+{{v2}}x+{{v3}}-{{v4}};' +
                    '{{v5-v6}}x-{{v8-v7}}|{{v5}}x-{{v6}}x+{{v7}}-{{v8}};' +
                    '-{{v10-v9}}x|{{v9}}x-{{v10}}x;' +
                    '{{v12}}|x-{{v11}}x+{{v11-1}}x+{{v12}}',
            variables={
                'v1': (randint, 1, 4),
                'v2': (randint, 5, 9),
                'v3': (randint, 5, 9),
                'v4': (randint, 2, 9),
                'v5': (randint, 10, 20),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
                'v8': (randint, 10, 20),
                'v9': (randint, 2, 4),
                'v10': (randint, 5, 9),
                'v11': (randint, 2, 9),
                'v12': (randint, 3, 9),
            }),
        Question(
            formula='',
            correct='1/{{v1}}a|a-{{v1-1}}/{{v1}}a;' +
                    'a+{{v2-v3}}|{{v2}}-{{v3}}+a;' +
                    '{{v4-v5}}-a|{{v4}}-({{v5}}+a);' +
                    '{{v7}}a|{{v6}}-({{v6}}-{{v7}}a)',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 20),
                'v3': (randint, 2, 9),
                'v4': (randint, 10, 20),
                'v5': (randint, 2, 9),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
            }),
        ]
)

# Add newly created question sets in that list, so the script can use them
question_sets = [
    terme_mit_potenzen,
    variablen_ausklammern,
    variable_richtig_ausgeklammert,
    nennergleiche_bruchterme_addieren,
    terme_vereinfachen_2,
    multiplizieren_und_dividieren,
    produkte_ausklammern,
    produkt_richtig_ausgeklammert,
    terme_multiplizieren,
    vorrangregeln,
    faktorisieren_2,
    wertgleiche_terme_zuordnen,
    terme_zuordnen_dragGroup,
    terme_zuordnen_dragMatch,
]
