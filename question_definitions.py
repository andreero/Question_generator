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
            formula='(x+y)/x+(x-y)/x',
            correct='(x+y+x-y)/x',
            wrong_1='(x+y+x-y)/x^2',
            wrong_2='(x+y-x+y)/x',
            variables={}),
        Question(
            formula='b/(a-b)-({{v1}}a+b)/(a-b)',
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

zahlen_ausklammern = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Zahlen ausklammern',
    instruction='Welche Zahl kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}a+{{v1*2}}b',
            correct='{{v1}}',
            wrong_1='{{v1*2}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{4*v1}}z-{{v1}}xy',
            correct='{{v1}}',
            wrong_1='{{4*v1}}',
            variables={
                'v1': (randint, 2, 5),
            }),
        Question(
            formula='{{2*v1}}uv^2+{{3*v1}}',
            correct='{{v1}}',
            wrong_1='{{2*v1}}',
            wrong_2='{{3*v1}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

zahl_richtig_ausgeklammert = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Zahlen ausklammern',
    instruction='Wird die Zahl richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1*3}}x^2y^2-{{v1*2}}z = {{v1}}(3x^2y^2-2z)',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{5*v1}}x+{{10*v1}}y+{{15*v1}}z = {{5*v1}}(3x+2y+z)',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 7),
            }),
        ]
)

bruchterme = QuestionSet(
    capital='Terme',
    subcapital='Bruchterme',
    title='Bruchterme',
    instruction='Ziehe die Terme in die richtige Kategorie.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='Bruchterm|{{v1}}/x~{{v2}}/(x+y)~({{v3}}xyz)/(x+{{v4}}y+z)~({{v4}}x)/(x^2-{{v5}});' +
                    'kein Bruchterm|(x+{{v6}})/{{v11}}~(x+y)/{{v7}}-1~1/{{v8}}y-{{v9}}~1/{{v10}}x+1/{{v10}}',
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
            }),
        ]
)

minusklammern_berechnen = QuestionSet(
    capital='Terme',
    subcapital='Subtrahieren einer Klammer',
    title='Minusklammern berechnen',
    instruction='Ziehe äquivalente Terme aufeinander.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='-({{v1}}x+{{v2}})|-{{v1}}x-{{v2}};' +
                    '-{{v3}}(p-{{v4}})|-{{v3}}p+{{v3*v4}};' +
                    '-{{v5}}(-{{v6}}+{{v7}}y)|{{v5*v6}}-{{v5*v7}}y;' +
                    '-{{v8}}(-{{v9}}-{{v10}}v)|{{v8*v9}}+{{v8*v10}}v;' +
                    '-({{v11}}-c)|-{{v11}}+c',
            variables={
                'v1': (randint, 2, 15),
                'v2': (randint, 2, 15),
                'v3': (randint, 2, 9),
                'v4': (randint, 2, 6),
                'v5': (randint, 2, 4),
                'v6': (randint, 2, 9),
                'v7': (randint, 2, 9),
                'v8': (randint, 2, 6),
                'v9': (randint, 2, 9),
                'v10': (randint, 2, 9),
                'v11': (randint, 2, 19),
            }),
        ]
)

terme_dividieren = QuestionSet(
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme dividieren',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}x:{{v2}}',
            correct='{{v1}}/3*{{v2}}',
            wrong_1='x/({{v1}}*{{v2}})',
            wrong_2='{{v1}}*{{v2}}*x',
            variables={
                'v1': (randint, 7, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='{{v1}}y:{{v2}}',
            correct='{{v1}}/{{v2}}y',
            wrong_1='({{v1}}*{{v2}})*y',
            wrong_2='{{v1}}/({{v2}}y)',
            variables={
                'v1': (randint, 7, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='-{{v1}}a:1/{{v2}}',
            correct='(-{{v1}}*{{v2}})*a',
            wrong_1='-{{v1}}/({{v2}}*a)',
            wrong_2='-{{v1}}/{{v2}}*a',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='1/({{v1}}b):1/{{v2}}',
            correct='{{v2}}/({{v1}}b)',
            wrong_1='({{v1}}b)/{{v2}}',
            wrong_2='1/({{v2}}*{{v1}}b)',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='({{v1}}a^2b)/{{v2}}:{{v3}}/{{v4}}',
            correct='(({{v4}}*{{v1}})a^2b)/({{v3}}*{{v2}})',
            wrong_1='({{v3}}*{{v2}})/(({{v4}}*{{v1}})a^2b)',
            wrong_2='(({{v3}}*{{v1}})a^2b)/({{v4}}*{{v2}})',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
                'v3': (randint, 16, 25),
                'v4': (randint, 10, 15),
            }),
        ]
)

terme_vereinfachen = QuestionSet(
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Terme vereinfachen',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='xy^2+x^2y-{{v1}}xy^2+{{v2}}x^2y',
            correct='{{v2+1}}x^2y-{{v1-1}}xy^2',
            wrong_1='{{v1+1}}x^2y-{{v2+1}}xy^2',
            wrong_2='x^2-{{v1}}y^2-xy^2-{{v2}}x^2y^2',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 3, 7),
            }),
        Question(
            formula='x^2y+xy+xy^2+{{v1}}xy',
            correct='x^2y+{{v1+1}}xy+xy^2',
            wrong_1='x^2y+{{v1}}xy+2xy^2',
            wrong_2='{{v1+1}}x^2y+{{v1+1}}xy^2',
            variables={
                'v1': (randint, 2, 8),
            }),
        Question(
            formula='xy^2-{{v1}}y^2+{{v2}}xy^2+xy',
            correct='{{v2+1}}xy^2+xy-{{v1}}y^2',
            wrong_1='{{v2+1}}x^2y-{{v1}}xy^2',
            wrong_2='x^2y+{{v1+v2}}xy+xy^2',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        ]
)

terme_vereinfachen_buttons = QuestionSet(
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Terme vereinfachen',
    instruction='Was muss zum Term A addiert werden, um Term B zu erhalten?',
    question_type='buttons',
    questions=[
        Question(
            formula='A: x^2+xy+y^2<br><br> B: x^2+{{v1}}xy+y^2',
            correct='{{v1-1}}xy',
            wrong_1='-{{v1}}xy',
            wrong_2='{{v1}}x+{{v1}}y',
            variables={
                'v1': (randint, 2, 6),
            }),
        Question(
            formula='A: {{v1}}uv+{{v2}}uv^2<br><br> B: {{v2}}(uv+uv^2)',
            correct='{{v2-v1}}uv',
            wrong_1='{{v2}}uv',
            wrong_2='{{v2}}uv^2',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
            }),
        Question(
            instruction='Was muss vom Term A subtrahiert werden, um Term B zu erhalten?',
            formula='A: a+b+c+a+b<br><br> B: a+b+c',
            correct='a+b',
            wrong_1='a',
            wrong_2='b',
            variables={}),
        Question(
            instruction='Was muss vom Term A subtrahiert werden, um Term B zu erhalten?',
            formula='x(1+x+x^2+x^3)<br><br> B: x+x^2+x^3',
            correct='x^4',
            wrong_1='x^3',
            wrong_2='1',
            variables={}),
        ]
)

minusklammern = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Minusklammern',
    instruction='Wo wurde die Zahl -1 richtig ausgeklammert? Klicke auf die korrekte Lösung.',
    question_type='lineCombineRight',
    questions=[
        Question(
            formula='-{{v1}}p+{{v2}}',
            correct='-({{v1}}p-{{v2}})',
            wrong_1='-(-{{v1}}p+{{v2}})',
            wrong_2='({{v1}}p-{{v2}})',
            wrong_3='-({{v1}}-{{v2}})',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}x-{{v2}}-y',
            correct='-(-{{v1}}x+{{v2}}+y)',
            wrong_1='-({{v1}}x+{{v2}}-y)',
            wrong_2='-(-{{v1}}x-{{v2}}-y)',
            wrong_3='-(-{{v1}}+{{v2}}+y)',
            variables={
                'v1': (randint, 10, 30),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='-{{v1}}-{{v2}}a+{{v3}}b',
            correct='-({{v1}}+{{v2}}a-{{v3}}b)',
            wrong_1='-({{v1}}-{{v2}}a+{{v3}}b)',
            wrong_2='-(-{{v1}}+{{v2}}a-{{v3}}b)',
            wrong_3='({{v1}}+{{v2}}a-{{v3}}b)',
            variables={
                'v1': (randint, 20, 50),
                'v2': (randint, 10, 19),
                'v3': (randint, 2, 9),
            }),
        ]
)

definitionsmenge_2 = QuestionSet(
    capital='Terme',
    subcapital='Bruchterme',
    title='Definitionsmenge (2)',
    instruction='Bestimme die richtige Definitionsmenge der folgenden Bruchterme.',
    question_type='MC',
    questions=[
        Question(
            formula='(x-{{v2}})/(x-{{v1}})',
            correct='ℝ \\ {{"{"}}{{v1}}{{"}"}}',
            wrong_1='ℝ \\ {{"{"}}{{v1}},{{v2}}{{"}"}}',
            wrong_2='ℝ \\ {{"{"}}{{v2}}{{"}"}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
            }),
        Question(
            formula='(({{v1}}x^2-x+{{v2}})/((x+{{v3}})(x-{{v4}}))',
            correct='ℝ \\ {{"{"}}-{{v3}}, {{v4}}{{"}"}}',
            wrong_1='ℝ \\ {{"{"}}{{v3}}{{"}"}}',
            wrong_2='ℝ \\ {{"{"}}{{v4}}{{"}"}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 6, 9),
            }),
        Question(
            formula='{{v2}}/(x^2-{{v1**2}})',
            correct='ℝ \\ {{"{"}}{{v1}}, -{{v1}}{{"}"}}',
            wrong_1='ℝ \\ {{"{"}}{{v1}}{{"}"}}',
            wrong_2='ℝ \\ {{"{"}}-{{v1}}{{"}"}}',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
            }),
        ]
)

rechengesetze_anwenden = QuestionSet(
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Rechengesetze anwenden',
    instruction='Forme den Term mithilfe des Distributivgesetzes um.',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}(x-{{v2}})',
            correct='{{v1}}*x+{{v1}}*(-{{v2}})',
            wrong_1='{{v1}}*x-{{v2}}',
            wrong_2='{{v1}}*x+{{v1}}*{{v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            instruction='Forme den Term mithilfe des Kommutativgesetzes um.',
            formula='x*{{v1}}+{{v2}}*y*{{v3}}',
            correct='{{v1}}*x+{{v2}}*{{v3}}*y',
            wrong_1='x+{{v2}}*{{v3}}*y',
            wrong_2='{{v1}}*x+{{v2}}*y',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 5),
                'v3': (randint, 6, 9),
            }),
        Question(
            instruction='Forme den Term mithilfe des Assoziativgesetzes um.',
            formula='{{v1}}*({{v2}}*x)',
            correct='({{v1}}*{{v2}})*x',
            wrong_1='{{v1}}+{{v2}}*x',
            wrong_2='{{v1}}*x',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
            }),
        ]
)

terme_vereinfachen_2_2 = QuestionSet(
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme vereinfachen (2)',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='-{{v1}}xy*({{v2}}xy)^3',
            correct='-{{v1}}*{{v2}}*{{v2}}*{{v2}}*x*x*x*x*y*y*y*y',
            wrong_1='-{{v1}}*{{v2}}*x*y*y*y*y',
            wrong_2='-{{v1}}*x*x*x*x*y*y*y*y',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='ab(-{{v1}}a^2b)*{{v2}}b^3',
            correct='-{{v1}}*{{v2}}*a*a*a*b*b*b*b*b',
            wrong_1='-{{v1}}*{{v2}}*a*a*a*b*b',
            wrong_2='-{{v1}}*a*a*a*b*b*b*b*b',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='x(-xy)^3*{{v1}}xy',
            correct='{{v1}}*x*(-x)*(-x)*(-x)*x*y*y*y*y',
            wrong_1='{{v1}}*x*x*x*x*x*y*y*y*y',
            wrong_2='{{v1}}*x*x*x*(-x)*x*y*y*(-y)*y',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

textaufgaben = QuestionSet(
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Textaufgaben',
    instruction='Welche dieser Terme passen zum Text?',
    question_type='MC',
    questions=[
        Question(
            formula='Multipliziere {{v1}} mit der Differenz aus {{v2}} und x.',
            correct='35*(11-x)',
            wrong_1='35*(x+11)',
            wrong_2='35*11*x',
            variables={
                'v1': (randint, 20, 40),
                'v2': (randint, 5, 19),
            }),
        Question(
            formula='Dividiere {{v1}} durch die Summe von {{v2}} und y.',
            correct='{{v1}}:({{v2}}+y)',
            wrong_1='{{v1}}:{{v2}}+y',
            wrong_2='{{v1}}:y+{{v2}}',
            variables={
                'v1': (randint, 20, 40),
                'v2': (randint, 5, 19),
            }),
        Question(
            formula='Quadriere die Summe von {{v1}}, a und b.',
            correct='({{v1}}+a+b)^2',
            wrong_1='{{v1}}^2+a+b',
            wrong_2='{{v1}}^2+a^2+b^2',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='Multipliziere die Summe von x und {{v1}} mit der Differenz von x und {{v2}}.',
            correct='(x+{{v1}})(x-{{v2}})',
            wrong_1='(x-{{v2}})(x+{{v1}})',
            wrong_2='(x+{{v1}})/(x-{{v2}})',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
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
            correct='1. binomische Formel|({{v1}}+x)^2~(b+{{v2}})^2;' +
                    '2. binomische Formel|(a-{{v3}})^2~({{v4}}-z)^2;' +
                    '3. binomische Formel|({{v5}}-b)({{v5}}+b)~(y+{{v6}})(y-{{v6}})',
            variables={
                'v1': (randint, 2, 19),
                'v2': (randint, 2, 19),
                'v3': (randint, 2, 19),
                'v4': (randdecimal, 0.3, 1.9),
                'v5': (randint, 2, 19),
                'v6': (randint, 2, 19),
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
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
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

vereinfachen_und_umformen = QuestionSet(
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Vereinfachen und umformen',
    instruction='Welcher Term ist wertgleich zu folgendem Term?',
    question_type='MC',
    questions=[
        Question(
            formula='{{v1}}*x*x*y*(-1)*x<br>+{{v2}}*y*x*x*x',
            correct='-{{v1}}x^3y+{{v2}}x^3y',
            wrong_1='{{v1}}x^3y+{{v2}}x^3y',
            wrong_2='-{{v1}}x^3y+{{v2}}x^2y',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='a*b*b*a*b*{{v1}}<br>-b*b*b*a*a<br>+a*a*a',
            correct='{{v1}}a^2b^3-a^2b^3+a^3',
            wrong_1='{{v1}}a^2b^3-a^2b^2+a^3',
            wrong_2='{{v1}}a^2b^3-a^2b^3',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}*x*y*y*y<br>+{{v2}}*y*y*x*y<br>-{{v3}}*y*y*y*x',
            correct='{{v1}}xy^3+{{v2}}xy^3-{{v3}}xy^3',
            wrong_1='{{v1}}xy^3+{{v2}}xy^3-{{2*v3}}xy^3',
            wrong_2='{{v1*v3}}xy^3-{{2*v3}}xy^3',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        ]
)

faktorisierung_kennenlernen = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Faktorisierung kennenlernen',
    instruction='Welche Zahl kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}b-{{v1*v2}}x',
            correct='{{v1}}',
            wrong_1='{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='{{v1*4}}x+{{v1}}a',
            correct='{{v1}}',
            wrong_1='{{v1*2}}',
            wrong_2='{{v1*4}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='{{v1}}c-{{v1*v2}}d',
            correct='{{v1}}',
            wrong_1='1{{v1}}',
            wrong_2='{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        ]
)

subtrahieren_einer_klammer = QuestionSet(
    capital='Terme',
    subcapital='Subtrahieren einer Klammer',
    title='Minusklammern kennenlernen',
    instruction='Wurde die Minusklammer korrekt berechnet?',
    question_type='buttons',
    questions=[
        Question(
            formula='-(x+{{v1}})=-x+{{v1}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='-(-{{v1}}+{{v2}}p)={{v1}}-{{v2}}p',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 10, 30),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='-({{v1}}z-{{v2}})=-{{v1}}z-{{v2}}',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 30),
            }),
        Question(
            formula='-(-{{v1}}-v)={{v1}}+v',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

summen_und_differenzen_ausklammern = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Summen und Differenzen ausklammern',
    instruction='Was kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}*(b-d)+c*(b-d)',
            correct='(b-d)',
            wrong_1='{{v1}}',
            wrong_2='c',
            wrong_3='b',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='({{v1}}f+{{v2}})*{{v1}}-f*({{v1}}f+{{v2}})',
            correct='({{v1}}f+{{v2}})',
            wrong_1='{{v1}}',
            wrong_2='{{v2}}',
            wrong_3='f',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 10),
            }),
        ]
)

gemischte_ubungen = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Gemischte Übungen',
    instruction='Wird die Zahl richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='{{v1}}xy+{{v1*v2}}x={{v1}}(xy+{{v2-1}}x)',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 3, 9),
            }),
        Question(
            instruction='Welche Faktoren kann man ausklammern?',
            formula='{{v1*10}}cv-{{v1*4}}cd',
            correct='{{v1*2}}c',
            wrong_1='{{v1*4}}c',
            wrong_2='c',
            wrong_3='{{v1*2}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            instruction='Was kann man ausklammern?',
            formula='{{v2}}(c-{{v1}})-(c-{{v1}})*c^2',
            correct='(c-{{v1}})',
            wrong_1='(c+{{v1}})',
            wrong_2='c',
            wrong_3='c^2',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 20),
            }),
        ]
)

gemischte_ubungen_lineCombineRight = QuestionSet(
    capital='Terme',
    subcapital='Ausklammern',
    title='Gemischte Übungen',
    instruction='Wo wurde richtig ausgeklammert? Klicke auf die richtige Lösung.',
    question_type='lineCombineRight',
    questions=[
        Question(
            formula='{{v1*v3}}z-{{v2*v3}}zy',
            correct='({{v1}}-{{v2}}y)*{{v3}}z',
            wrong_1='{{v3}}z*({{v2}}-y)',
            wrong_2='z*({{v3}}-{{v2}}y)',
            wrong_3='{{v3}}z*({{v2}}-{{v1}}y)',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 7),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='{{v1*v2}}-{{v1}}b-{{v1}}c',
            correct='{{v1}}*({{v2}}-b-c)',
            wrong_1='{{v1*v2}}*(1-2b)',
            wrong_2='{{v1}}*(b-c)',
            wrong_3='{{v1}}*(1-b-c)',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 4),
            }),
        ]
)

gleichartige_terme = QuestionSet(
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Gleichartige Terme',
    instruction='Ordne gleichartige Terme einander zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='{{v1}}xy|-{{v2}}xy;'
                    '{{v3}}x*x*y*y|{{v4}}x^2y^2;'
                    '{{v5}}x^2yz|-{{v6}}x*x*y*z;'
                    '{{v7}}xy^2+xy^2|-{{v8}}xy^2;'
                    '{{v9}}x*y*x*y*x*y|{{v10}}x^3y^3',
            variables={
                'v1': (randint, 2, 20),
                'v2': (randint, 2, 20),
                'v3': (randint, 2, 20),
                'v4': (randint, 2, 20),
                'v5': (randint, 2, 20),
                'v6': (randint, 2, 20),
                'v7': (randint, 2, 20),
                'v8': (randint, 2, 20),
                'v9': (randint, 2, 20),
                'v10': (randint, 2, 20),
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
    zahlen_ausklammern,
    zahl_richtig_ausgeklammert,
    bruchterme,
    minusklammern_berechnen,
    terme_dividieren,
    terme_vereinfachen,
    terme_vereinfachen_buttons,
    minusklammern,
    definitionsmenge_2,
    rechengesetze_anwenden,
    terme_vereinfachen_2_2,
    terme_zuordnen_dragGroup,
    terme_zuordnen_dragMatch,
    vereinfachen_und_umformen,
    faktorisierung_kennenlernen,
    subtrahieren_einer_klammer,
    summen_und_differenzen_ausklammern,
    gemischte_ubungen,
    gemischte_ubungen_lineCombineRight,
    gleichartige_terme,
]
