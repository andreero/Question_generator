from questions import Question, QuestionSet
from random import randint
from definitions.common import randdecimal


terme_mit_potenzen = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme mit Potenzen',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>({{v1}}x)^2</mat>',
            correct='<mat>{{v1}}*{{v1}}*x*x</mat>',
            wrong_1='<mat>{{v1}}*{{v1}}*x</mat>',
            wrong_2='<mat>{{v1}}*x*x</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>({{v1}}a)^2</mat>',
            correct='<mat>{{v1}}*{{v1}}*a*a</mat>',
            wrong_1='<mat>{{v1}}*{{v1}}*a</mat>',
            wrong_2='<mat>{{v1}}*a*a</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>({{v1}}y)^3</mat>',
            correct='<mat>{{v1}}*{{v1}}*{{v1}}*y*y*y</mat>',
            wrong_1='<mat>{{v1}}*{{v1}}*{{v1}}*y</mat>',
            wrong_2='<mat>{{v1}}*{{v1}}*y*y*y</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>(-b)^3</mat>',
            correct='<mat>(-1)*(-1)*(-1)*b*b*b</mat>',
            wrong_1='b',
            wrong_2='<mat>b*b*b</mat>',
            variables={}),
        Question(
            formula='<mat>(-{{v1}}xy)^2</mat>',
            correct='<mat>(-{{v1}})*(-{{v1}})*x*x*y*y</mat>',
            wrong_1='<mat>(-{{v1}})*(-{{v1}})*x*x*y</mat>',
            wrong_2='<mat>(-{{v1}})*(-{{v1}})*x*y*y</mat>',
            variables={
                'v1': (randint, 2, 9)
            }),
        ]
)

variablen_ausklammern = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Variablen ausklammern',
    instruction='Welche Variable kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}a+ab</mat>',
            correct='a',
            wrong_1='b',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}xz-{{v2}}xy</mat>',
            correct='x',
            wrong_1='y',
            wrong_2='z',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}u^2-{{v2}}uv</mat>',
            correct='u',
            wrong_1='v',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        ]
)

variable_richtig_ausgeklammert = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Variablen ausklammern',
    instruction='Wird die Variable richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}xy-xz = x({{v1}}y-z)</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}xyz-{{v2}}x^2 = x({{v1}}yz-{{v2}})</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}a^2b+{{v2}}ac^2 = a({{v1}}ab+{{v2}}ac^2)</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>abc-ab-ac = a(bc-b-c)</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={}),
        ]
)

nennergleiche_bruchterme_addieren = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Bruchterme',
    title='Nennergleiche Bruchterme addieren',
    instruction='Zu welchem Bruchterm ist der folgende Bruchterm äquivalent?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>(x+y)/x+(x-y)/x</mat>',
            correct='<mat>(x+y+x-y)/x</mat>',
            wrong_1='<mat>(x+y+x-y)/x^2</mat>',
            wrong_2='<mat>(x+y-x+y)/x</mat>',
            variables={}),
        Question(
            formula='<mat>b/(a-b)-({{v1}}a+b)/(a-b)</mat>',
            correct='<mat>(b-{{v1-1}}a-b)/(a-b)</mat>',
            wrong_1='<mat>(b-{{v1-1}}a-b)/(a-b)^3</mat>',
            wrong_2='<mat>(b-{{v1-1}}a+b)/(a-b)</mat>',
            variables={
                'v1': (randint, 3, 9),
            }),
        Question(
            formula='<mat>({{v1}}x(x+1))/(x+y) - (x(y+1))/(x+y)</mat>',
            correct='<mat>({{v1}}x^2+{{v1}}x-xy-x)/(x+y)</mat>',
            wrong_1='<mat>({{v1}}x^2+{{v1}}x-xy-x)/({{v1+1}}x+{{v1+1}}y)</mat>',
            wrong_2='<mat>({{v1}}x^2+{{v1}}x-xy+x)/(x+y)</mat>',
            variables={
                'v1': (randint, 3, 8),
            }),
        Question(
            formula='<mat>(a^2-{{v1}}ab)/(a+b)^2 - (a(a-{{v2}}b))/(a+b)^2</mat>',
            correct='<mat>(a^2-{{v1}}ab-a^2+{{v2}}ab)/(a+b)^2</mat>',
            wrong_1='<mat>(a^2-{{v1}}ab-a^2-{{v2}}ab)/(a+b)^2</mat>',
            wrong_2='<mat>(a^2-{{v1}}ab+a^2-{{v2}}ab)/(a+b)^2</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        ]
)

terme_vereinfachen_2 = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme mit Variablen',
    title='Terme vereinfachen (2)',
    instruction='Vereinfache den folgenden Term.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}+{{v2}}*y+{{v3}}*y</mat>',
            correct='<mat>{{v1}}+{{v2+v3}}y</mat>',
            wrong_1='<mat>{{v1+v2}}+{{v3}}y</mat>',
            wrong_2='<mat>{{v1+v2}}+{{v2+v3}}y</mat>',
            variables={
                'v1': (randint, 11, 20),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}*{{v2}}*a*b:c</mat>',
            correct='<mat>({{v1*v2}}ab)/c</mat>',
            wrong_1='<mat>{{v1*v2}}abc</mat>',
            wrong_2='<mat>({{v1}}{{v2}}ab)/c</mat>',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 3, 6),
            }),
        Question(
            formula='<mat>{{v1}}*({{v2}}*x+(-1)*y)</mat>',
            correct='<mat>{{v1*v2}}x-{{v1}}y</mat>',
            wrong_1='<mat>{{v1}}{{v2}}x-{{v1}}y</mat>',
            wrong_2='<mat>{{v1*v2}}x+{{v1}}y</mat>',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        ]
)

multiplizieren_und_dividieren = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Bruchterme',
    title='Multiplizieren und dividieren',
    instruction='Zu welchem Bruchterm ist der folgende Bruchterm äquivalent?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>(xy^2)/({{v1}}z)*({{v2}}x)/({{v3}}yz)</mat>',
            correct='<mat>({{v2}}x^2y^2)/({{v1*v3}}yz^2)</mat>',
            wrong_1='<mat>({{v1}}xy^3z)/({{v2*v3}}xz)</mat>',
            wrong_2='<mat>({{v2}}x^2y^2)/({{v1}}z)</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='<mat>({{v1}}a+bc)/({{v2}}ab)*a/(a+b)</mat>',
            correct='<mat>({{v1}}a^2+abc)/({{v2}}a^2b+{{v2}}ab^2)</mat>',
            wrong_1='<mat>({{v1}}a^2+bc)/(a+b)</mat>',
            wrong_2='<mat>({{v1}}a^2+abc+{{v1}}ab+b^2c)/({{v2}}a^2b)</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>(x^2y)/({{v1}}z^3):(xy)/({{v2}}z^2)</mat>',
            correct='<mat>({{v1}}x^2yz^2)/({{v2}}xyz^3)</mat>',
            wrong_1='<mat>(x^3y^2)/({{v1*v2}}z^5)</mat>',
            wrong_2='<mat>(x^2y)/({{v2}}xyz^3)</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>((a+b)(a-b))/c:(a+b)/c^2</mat>',
            correct='<mat>((a+b)(a-b)c^2)/(c(a+b))</mat>',
            wrong_1='<mat>((a+b)^2(a-b))/(c^3)</mat>',
            wrong_2='<mat>((a+b)^2(a-b))/(c^2)</mat>',
            variables={}),
        ]
)

produkte_ausklammern = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Produkte ausklammern',
    instruction='Welche Faktoren kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}ab+abc</mat>',
            correct='ab',
            wrong_1='{{v1}}b',
            wrong_2='ac',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}cd+{{v1}}fc</mat>',
            correct='{{v1}}c',
            wrong_1='cd',
            wrong_2='{{v1}}d',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1*2}}m+{{v1*5}}m^2</mat>',
            correct='{{v1}}m',
            wrong_1='2m',
            wrong_2='5m',
            variables={
                'v1': (randint, 1, 4),
            }),
        Question(
            formula='<mat>((a+b)(a-b))/c:(a+b)/c^2</mat>',
            correct='<mat>((a+b)(a-b)c^2)/(c(a+b))</mat>',
            wrong_1='<mat>((a+b)^2(a-b))/(c^3)</mat>',
            wrong_2='<mat>((a+b)^2(a-b))/(c^2)</mat>',
            variables={}),
        ]
)

produkt_richtig_ausgeklammert = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Produkte ausklammern',
    instruction='Wo wurde das Produkt richtig ausgeklammert?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}ab+abc</mat>',
            correct='<mat>ab*({{v1}}+c)</mat>',
            wrong_1='<mat>ab*({{v1}}+a)</mat>',
            wrong_2='<mat>ac*({{v1}}+b)</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1*2}}m+{{v1*5}}m^2</mat>',
            correct='<mat>{{v1}}m*(2+5m)</mat>',
            wrong_1='<mat>{{v1}}m*(5+2m)</mat>',
            wrong_2='<mat>{{v1}}m*(5m)</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

terme_multiplizieren = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme multiplizieren',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}*({{v2}}x)</mat>',
            correct='<mat>({{v1}}*{{v2}})*x</mat>',
            wrong_1='<mat>({{v1}}*{{v2}})*x*x</mat>',
            wrong_2='<mat>({{v1}}*{{v2}}*{{v1}})*x</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>-{{v1}}a*({{v2}})</mat>',
            correct='<mat>(-{{v1}}*{{v2}})*a</mat>',
            wrong_1='<mat>({{v1}}*{{v2}})*a</mat>',
            wrong_2='<mat>(-{{v1}}*{{v2}})*a*{{v2}}</mat>',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randdecimal, 0.2, 0.9),
            }),
        Question(
            formula='<mat>{{v1}}y*{{v2}}y</mat>',
            correct='<mat>({{v1}}*{{v2}})*y*y</mat>',
            wrong_1='<mat>{{v1}}*y*y</mat>',
            wrong_2='<mat>({{v1}}*{{v2}})*y</mat>',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
            }),
        Question(
            formula='<mat>1/{{v1}}b^2*1/{{v2}}b</mat>',
            correct='<mat>(1/{{v1}}*1/{{v2}})*b^2*b</mat>',
            wrong_1='<mat>(1/{{v1}}*1/{{v2}})*b^2</mat>',
            wrong_2='<mat>(1/{{v1}}*1/{{v2}})*b^2*b^2</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}xy*1/{{v2}}y^2</mat>',
            correct='<mat>({{v1}}*1/{{v2}})*x*y*y^2</mat>',
            wrong_1='<mat>({{v1}}*1/{{v2}})*x*y^2</mat>',
            wrong_2='<mat>({{v1}}*1/{{v2}})*y*y^2</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}/{{v2}}a^2b*1/{{v1}}ab^2</mat>',
            correct='<mat>({{v1}}/{{v2}}*1/{{v1}})*a^2*a*b*b^2</mat>',
            wrong_1='<mat>({{v1}}/{{v2}}*{{v1}})*a^2*a*b*b^2</mat>',
            wrong_2='<mat>({{v1}}/{{v2}}*1/{{v1}})*a*a*b*b</mat>',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 2, 4),
            }),
        ]
)

vorrangregeln = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Vorrangregeln',
    instruction='Welche Rechnung muss zuerst durchgeführt werden?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}*(2*{{v2}}+1)</mat>',
            correct='<mat>2*{{v2}}</mat>',
            wrong_1='<mat>{{v2}}+1</mat>',
            wrong_2='<mat>{{v1}}*2</mat>',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 3, 5),
            }),
        Question(
            formula='<mat>({{v1}}-{{v2}})*{{v3}}^2</mat>',
            correct='<mat>{{v1}}-{{v2}}</mat>',
            wrong_1='<mat>{{v3}}^2</mat>',
            wrong_2='<mat>-{{v2}}*{{v3}}</mat>',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 5, 9),
                'v3': (randint, 2, 4),
            }),
        Question(
            formula='<mat>({{v1}}-{{v2}})^2:{{v3}}^2</mat>',
            correct='<mat>{{v1}}-{{v2}}</mat>',
            wrong_1='<mat>{{v3}}^2</mat>',
            wrong_2='<mat>-{{v2}}^2</mat>',
            variables={
                'v1': (randint, 5, 9),
                'v2': (randint, 4, 5),
                'v3': (randint, 2, 3),
            }),
        ]
)

faktorisieren_2 = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Faktorisieren (2)',
    instruction='Welche binomische Formel musst du für die Faktorisierung anwenden?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>x^2+{{2*v1}}x+{{v1**2}}</mat>',
            correct='1. binomische Formel',
            wrong_1='2. binomische Formel',
            wrong_2='3. binomische Formel',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1**2}}-y^2',
            correct='3. binomische Formel',
            wrong_1='1. binomische Formel',
            wrong_2='2. binomische Formel',
            variables={
                'v1': (randint, 5, 15),
            }),
        Question(
            formula='<mat>{{v1**2}}-{{2*v1}}z+z^2</mat>',
            correct='2. binomische Formel',
            wrong_1='1. binomische Formel',
            wrong_2='3. binomische Formel',
            variables={
                'v1': (randint, 3, 9),
            }),
        ]
)

wertgleiche_terme_zuordnen = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Wertgleiche Terme zuordnen',
    instruction='Ordne wertgleiche Terme zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='<mat>{{v1+v2}}x+{{v3-v4}}|{{v1}}x+{{v2}}x+{{v3}}-{{v4}};</mat>' +
                    '<mat>{{v5-v6}}x-{{v8-v7}}|{{v5}}x-{{v6}}x+{{v7}}-{{v8}};</mat>' +
                    '<mat>-{{v10-v9}}x|{{v9}}x-{{v10}}x</mat>;' +
                    '<mat>{{v12}}|x-{{v11}}x+{{v11-1}}x+{{v12}}</mat>',
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
            correct='<mat>1/{{v1}}a|a-{{v1-1}}/{{v1}}a</mat>;' +
                    '<mat>a+{{v2-v3}}|{{v2}}-{{v3}}+a</mat>;' +
                    '<mat>{{v4-v5}}-a|{{v4}}-({{v5}}+a)</mat>;' +
                    '<mat>{{v7}}a|{{v6}}-({{v6}}-{{v7}}a)</mat>',
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
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Zahlen ausklammern',
    instruction='Welche Zahl kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}a+{{v1*2}}b</mat>',
            correct='<mat>{{v1}}</mat>',
            wrong_1='<mat>{{v1*2}}</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{4*v1}}z-{{v1}}xy</mat>',
            correct='<mat>{{v1}}</mat>',
            wrong_1='<mat>{{4*v1}}</mat>',
            variables={
                'v1': (randint, 2, 5),
            }),
        Question(
            formula='<mat>{{2*v1}}uv^2+{{3*v1}}</mat>',
            correct='<mat>{{v1}}</mat>',
            wrong_1='<mat>{{2*v1}}</mat>',
            wrong_2='<mat>{{3*v1}}</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

zahl_richtig_ausgeklammert = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Zahlen ausklammern',
    instruction='Wird die Zahl richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1*3}}x^2y^2-{{v1*2}}z = {{v1}}(3x^2y^2-2z)</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{5*v1}}x+{{10*v1}}y+{{15*v1}}z = {{5*v1}}(3x+2y+z)</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 7),
            }),
        ]
)

bruchterme = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Bruchterme',
    title='Bruchterme',
    instruction='Ziehe die Terme in die richtige Kategorie.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='Bruchterm|<mat>{{v1}}/x~{{v2}}/(x+y)</mat>~<mat>({{v3}}xyz)/(x+{{v4}}y+z)</mat>~<mat>({{v4}}x)/(x^2-{{v5}})</mat>;' +
                    'kein Bruchterm|<mat>(x+{{v6}})/{{v11}}</mat>~<mat>(x+y)/{{v7}}-1~1/{{v8}}y-{{v9}}</mat>~<mat>1/{{v10}}x+1/{{v10}}</mat>',
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
    grade='8',
    capital='Terme',
    subcapital='Subtrahieren einer Klammer',
    title='Minusklammern berechnen',
    instruction='Ziehe äquivalente Terme aufeinander.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='<mat>-({{v1}}x+{{v2}})|-{{v1}}x-{{v2}}</mat>;' +
                    '<mat>-{{v3}}(p-{{v4}})|-{{v3}}p+{{v3*v4}}</mat>;' +
                    '<mat>-{{v5}}(-{{v6}}+{{v7}}y)|{{v5*v6}}-{{v5*v7}}y</mat>;' +
                    '<mat>-{{v8}}(-{{v9}}-{{v10}}v)|{{v8*v9}}+{{v8*v10}}v</mat>;' +
                    '<mat>-({{v11}}-c)|-{{v11}}+c',
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
    grade='8',
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme dividieren',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}x:{{v2}}</mat>',
            correct='<mat>{{v1}}/3*{{v2}}</mat>',
            wrong_1='<mat>x/({{v1}}*{{v2}})</mat>',
            wrong_2='<mat>{{v1}}*{{v2}}*x</mat>',
            variables={
                'v1': (randint, 7, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='<mat>{{v1}}y:{{v2}}</mat>',
            correct='<mat>{{v1}}/{{v2}}y</mat>',
            wrong_1='<mat>({{v1}}*{{v2}})*y</mat>',
            wrong_2='<mat>{{v1}}/({{v2}}y)</mat>',
            variables={
                'v1': (randint, 7, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='<mat>-{{v1}}a:1/{{v2}}</mat>',
            correct='<mat>(-{{v1}}*{{v2}})*a</mat>',
            wrong_1='<mat>-{{v1}}/({{v2}}*a)</mat>',
            wrong_2='<mat>-{{v1}}/{{v2}}*a</mat>',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>1/({{v1}}b):1/{{v2}}</mat>',
            correct='<mat>{{v2}}/({{v1}}b)</mat>',
            wrong_1='<mat>({{v1}}b)/{{v2}}</mat>',
            wrong_2='<mat>1/({{v2}}*{{v1}}b)</mat>',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
            }),
        Question(
            formula='<mat>({{v1}}a^2b)/{{v2}}:{{v3}}/{{v4}}</mat>',
            correct='<mat>(({{v4}}*{{v1}})a^2b)/({{v3}}*{{v2}})</mat>',
            wrong_1='<mat>({{v3}}*{{v2}})/(({{v4}}*{{v1}})a^2b)</mat>',
            wrong_2='<mat>(({{v3}}*{{v1}})a^2b)/({{v4}}*{{v2}})</mat>',
            variables={
                'v1': (randint, 6, 9),
                'v2': (randint, 2, 5),
                'v3': (randint, 16, 25),
                'v4': (randint, 10, 15),
            }),
        ]
)

terme_vereinfachen = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Terme vereinfachen',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>xy^2+x^2y-{{v1}}xy^2+{{v2}}x^2y</mat>',
            correct='<mat>{{v2+1}}x^2y-{{v1-1}}xy^2</mat>',
            wrong_1='<mat>{{v1+1}}x^2y-{{v2+1}}xy^2</mat>',
            wrong_2='<mat>x^2-{{v1}}y^2-xy^2-{{v2}}x^2y^2</mat>',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 3, 7),
            }),
        Question(
            formula='<mat>x^2y+xy+xy^2+{{v1}}xy</mat>',
            correct='<mat>x^2y+{{v1+1}}xy+xy^2</mat>',
            wrong_1='<mat>x^2y+{{v1}}xy+2xy^2</mat>',
            wrong_2='<mat>{{v1+1}}x^2y+{{v1+1}}xy^2</mat>',
            variables={
                'v1': (randint, 2, 8),
            }),
        Question(
            formula='<mat>xy^2-{{v1}}y^2+{{v2}}xy^2+xy</mat>',
            correct='<mat>{{v2+1}}xy^2+xy-{{v1}}y^2</mat>',
            wrong_1='<mat>{{v2+1}}x^2y-{{v1}}xy^2</mat>',
            wrong_2='<mat>x^2y+{{v1+v2}}xy+xy^2</mat>',
            variables={
                'v1': (randint, 2, 6),
                'v2': (randint, 2, 6),
            }),
        ]
)

terme_vereinfachen_buttons = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Terme vereinfachen',
    instruction='Was muss zum Term A addiert werden, um Term B zu erhalten?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>A: x^2+xy+y^2<br><br> B: x^2+{{v1}}xy+y^2</mat>',
            correct='<mat>{{v1-1}}xy</mat>',
            wrong_1='<mat>-{{v1}}xy</mat>',
            wrong_2='<mat>{{v1}}x+{{v1}}y</mat>',
            variables={
                'v1': (randint, 2, 6),
            }),
        Question(
            formula='<mat>A: {{v1}}uv+{{v2}}uv^2<br><br> B: {{v2}}(uv+uv^2)</mat>',
            correct='<mat>{{v2-v1}}uv</mat>',
            wrong_1='<mat>{{v2}}uv</mat>',
            wrong_2='<mat>{{v2}}uv^2</mat>',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
            }),
        Question(
            instruction='Was muss vom Term A subtrahiert werden, um Term B zu erhalten?',
            formula='<mat>A: a+b+c+a+b<br><br> B: a+b+c</mat>',
            correct='<mat>a+b</mat>',
            wrong_1='a',
            wrong_2='b',
            variables={}),
        Question(
            instruction='Was muss vom Term A subtrahiert werden, um Term B zu erhalten?',
            formula='<mat>x(1+x+x^2+x^3)<br><br> B: x+x^2+x^3</mat>',
            correct='<mat>x^4</mat>',
            wrong_1='<mat>x^3</mat>',
            wrong_2='1',
            variables={}),
        ]
)

minusklammern = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Minusklammern',
    instruction='Wo wurde die Zahl -1 richtig ausgeklammert? Klicke auf die korrekte Lösung.',
    question_type='lineCombineRight',
    questions=[
        Question(
            formula='<mat>-{{v1}}p+{{v2}}</mat>',
            correct='<mat>-({{v1}}p-{{v2}})</mat>',
            wrong_1='<mat>-(-{{v1}}p+{{v2}})</mat>',
            wrong_2='<mat>({{v1}}p-{{v2}})</mat>',
            wrong_3='<mat>-({{v1}}-{{v2}})</mat>',
            variables={
                'v1': (randint, 10, 20),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}x-{{v2}}-y</mat>',
            correct='<mat>-(-{{v1}}x+{{v2}}+y)</mat>',
            wrong_1='<mat>-({{v1}}x+{{v2}}-y)</mat>',
            wrong_2='<mat>-(-{{v1}}x-{{v2}}-y)</mat>',
            wrong_3='<mat>-(-{{v1}}+{{v2}}+y)</mat>',
            variables={
                'v1': (randint, 10, 30),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>-{{v1}}-{{v2}}a+{{v3}}b</mat>',
            correct='<mat>-({{v1}}+{{v2}}a-{{v3}}b)</mat>',
            wrong_1='<mat>-({{v1}}-{{v2}}a+{{v3}}b)</mat>',
            wrong_2='<mat>-(-{{v1}}+{{v2}}a-{{v3}}b</mat>',
            wrong_3='<mat>({{v1}}+{{v2}}a-{{v3}}b)</mat>',
            variables={
                'v1': (randint, 20, 50),
                'v2': (randint, 10, 19),
                'v3': (randint, 2, 9),
            }),
        ]
)

definitionsmenge_2 = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Bruchterme',
    title='Definitionsmenge (2)',
    instruction='Bestimme die richtige Definitionsmenge der folgenden Bruchterme.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>(x-{{v2}})/(x-{{v1}})</mat>',
            correct='<mat>ℝ \\ {{"{"}}{{v1}}{{"}"}}</mat>',
            wrong_1='<mat>ℝ \\ {{"{"}}{{v1}},{{v2}}{{"}"}}</mat>',
            wrong_2='<mat>ℝ \\ {{"{"}}{{v2}}{{"}"}}</mat>',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
            }),
        Question(
            formula='<mat>(({{v1}}x^2-x+{{v2}})/((x+{{v3}})(x-{{v4}}))</mat>',
            correct='<mat>ℝ \\ {{"{"}}-{{v3}}, {{v4}}{{"}"}}</mat>',
            wrong_1='<mat>ℝ \\ {{"{"}}{{v3}}{{"}"}}</mat>',
            wrong_2='<mat>ℝ \\ {{"{"}}{{v4}}{{"}"}}</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 5),
                'v4': (randint, 6, 9),
            }),
        Question(
            formula='<mat>{{v2}}/(x^2-{{v1**2}})</mat>',
            correct='<mat>ℝ \\ {{"{"}}{{v1}}, -{{v1}}{{"}"}}</mat>',
            wrong_1='<mat>ℝ \\ {{"{"}}{{v1}}{{"}"}}</mat>',
            wrong_2='<mat>ℝ \\ {{"{"}}-{{v1}}{{"}"}}</mat>',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 2, 5),
            }),
        ]
)

rechengesetze_anwenden = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Rechengesetze anwenden',
    instruction='Forme den Term mithilfe des Distributivgesetzes um.',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}(x-{{v2}})</mat>',
            correct='<mat>{{v1}}*x+{{v1}}*(-{{v2}})</mat>',
            wrong_1='<mat>{{v1}}*x-{{v2}}</mat>',
            wrong_2='<mat>{{v1}}*x+{{v1}}*{{v2}}</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            instruction='Forme den Term mithilfe des Kommutativgesetzes um.',
            formula='<mat>x*{{v1}}+{{v2}}*y*{{v3}}</mat>',
            correct='<mat>{{v1}}*x+{{v2}}*{{v3}}*y</mat>',
            wrong_1='<mat>x+{{v2}}*{{v3}}*y</mat>',
            wrong_2='<mat>{{v1}}*x+{{v2}}*y</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 5),
                'v3': (randint, 6, 9),
            }),
        Question(
            instruction='Forme den Term mithilfe des Assoziativgesetzes um.',
            formula='<mat>{{v1}}*({{v2}}*x)</mat>',
            correct='<mat>({{v1}}*{{v2}})*x</mat>',
            wrong_1='<mat>{{v1}}+{{v2}}*x</mat>',
            wrong_2='<mat>{{v1}}*x</mat>',
            variables={
                'v1': (randint, 2, 5),
                'v2': (randint, 6, 9),
            }),
        ]
)

terme_vereinfachen_2_2 = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme multiplizieren und dividieren',
    title='Terme vereinfachen (2)',
    instruction='Welcher Term ist wertgleich?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>-{{v1}}xy*({{v2}}xy)^3</mat>',
            correct='<mat>-{{v1}}*{{v2}}*{{v2}}*{{v2}}*x*x*x*x*y*y*y*y</mat>',
            wrong_1='<mat>-{{v1}}*{{v2}}*x*y*y*y*y</mat>',
            wrong_2='<mat>-{{v1}}*x*x*x*x*y*y*y*y</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>ab(-{{v1}}a^2b)*{{v2}}b^3</mat>',
            correct='<mat>-{{v1}}*{{v2}}*a*a*a*b*b*b*b*b</mat>',
            wrong_1='<mat>-{{v1}}*{{v2}}*a*a*a*b*b</mat>',
            wrong_2='<mat>-{{v1}}*a*a*a*b*b*b*b*b</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>x(-xy)^3*{{v1}}xy</mat>',
            correct='<mat>{{v1}}*x*(-x)*(-x)*(-x)*x*y*y*y*y</mat>',
            wrong_1='<mat>{{v1}}*x*x*x*x*x*y*y*y*y</mat>',
            wrong_2='<mat>{{v1}}*x*x*x*(-x)*x*y*y*(-y)*y</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

textaufgaben = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Textaufgaben',
    instruction='Welche dieser Terme passen zum Text?',
    question_type='MC',
    questions=[
        Question(
            formula='Multipliziere {{v1}} mit der Differenz aus {{v2}} und x.',
            correct='<mat>35*(11-x)</mat>',
            wrong_1='<mat>35*(x+11)</mat>',
            wrong_2='<mat>35*11*x</mat>',
            variables={
                'v1': (randint, 20, 40),
                'v2': (randint, 5, 19),
            }),
        Question(
            formula='Dividiere {{v1}} durch die Summe von {{v2}} und y.',
            correct='<mat>{{v1}}:({{v2}}+y)</mat>',
            wrong_1='<mat>{{v1}}:{{v2}}+y</mat>',
            wrong_2='<mat>{{v1}}:y+{{v2}}</mat>',
            variables={
                'v1': (randint, 20, 40),
                'v2': (randint, 5, 19),
            }),
        Question(
            formula='Quadriere die Summe von {{v1}}, a und b.',
            correct='<mat>({{v1}}+a+b)^2</mat>',
            wrong_1='<mat>{{v1}}^2+a+b</mat>',
            wrong_2='<mat>{{v1}}^2+a^2+b^2</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='Multipliziere die Summe von x und {{v1}} mit der Differenz von x und {{v2}}.',
            correct='<mat>(x+{{v1}})(x-{{v2}})</mat>',
            wrong_1='<mat>(x-{{v2}})(x+{{v1}})</mat>',
            wrong_2='<mat>(x+{{v1}})/(x-{{v2}})</mat>',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 9),
            }),
        ]
)

terme_zuordnen_dragGroup = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Ordne jedem Term die Formel zu, mit der der Term ausgerechnet werden kann.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='1. binomische Formel|<mat>({{v1}}+x)^2)</mat>~<mat>(b+{{v2}})^2</mat>;' +
                    '2. binomische Formel|<mat>(a-{{v3}})^2)</mat>~<mat>({{v4}}-z)^2</mat>;' +
                    '3. binomische Formel|<mat>({{v5}}-b)({{v5}}+b))</mat>~<mat>(y+{{v6}})(y-{{v6}})</mat>',
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
    grade='8',
    capital='Terme',
    subcapital='Binomische Formeln',
    title='Terme zuordnen',
    instruction='Füge äquivalente Terme zusammen.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='<mat>({{v1}}+x)^2|{{v1**2}}+{{2*v1}}x+x^2</mat>;' +
                    '<mat>(x-{{v2}})^2|x^2-{{2*v2}}x+{{v2**2}}</mat>;' +
                    '<mat>({{v3}}-x)({{v3}}+x)|{{v3**2}}-x^2</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='',
            correct='<mat>(v+{{v1}})^2|v^2+{{2*v1}}v+{{v1**2}}</mat>;' +
                    '<mat>({{v2}}-v)^2|{{v2**2}}-{{2*v2}}v+v^2</mat>;' +
                    '<mat>(v+{{v3}})(v-{{v3}})|v^2-{{v3**2}}</mat>',
            variables={
                'v1': (randint, 3, 9),
                'v2': (randint, 3, 9),
                'v3': (randint, 5, 15),
            }),
    ]
)

vereinfachen_und_umformen = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme vereinfachen und umformen',
    title='Vereinfachen und umformen',
    instruction='Welcher Term ist wertgleich zu folgendem Term?',
    question_type='MC',
    questions=[
        Question(
            formula='<mat>{{v1}}*x*x*y*(-1)*x<br>+{{v2}}*y*x*x*x</mat>',
            correct='<mat>-{{v1}}x^3y+{{v2}}x^3y</mat>',
            wrong_1='<mat>{{v1}}x^3y+{{v2}}x^3y</mat>',
            wrong_2='<mat>-{{v1}}x^3y+{{v2}}x^2y</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>a*b*b*a*b*{{v1}}<br>-b*b*b*a*a<br>+a*a*a</mat>',
            correct='<mat>{{v1}}a^2b^3-a^2b^3+a^3</mat>',
            wrong_1='<mat>{{v1}}a^2b^3-a^2b^2+a^3</mat>',
            wrong_2='<mat>{{v1}}a^2b^3-a^2b^3</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}*x*y*y*y<br>+{{v2}}*y*y*x*y<br>-{{v3}}*y*y*y*x</mat>',
            correct='<mat>{{v1}}xy^3+{{v2}}xy^3-{{v3}}xy^3</mat>',
            wrong_1='<mat>{{v1}}xy^3+{{v2}}xy^3-{{2*v3}}xy^3</mat>',
            wrong_2='<mat>{{v1*v3}}xy^3-{{2*v3}}xy^3</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 9),
                'v3': (randint, 2, 9),
            }),
        ]
)

faktorisierung_kennenlernen = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Faktorisierung kennenlernen',
    instruction='Welche Zahl kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}b-{{v1*v2}}x</mat>',
            correct='{{v1}}',
            wrong_1='{{v1*v2}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 4),
            }),
        Question(
            formula='<mat>{{v1*4}}x+{{v1}}a</mat>',
            correct='{{v1}}',
            wrong_1='{{v1*2}}',
            wrong_2='{{v1*4}}',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1}}c-{{v1*v2}}d</mat>',
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
    grade='8',
    capital='Terme',
    subcapital='Subtrahieren einer Klammer',
    title='Minusklammern kennenlernen',
    instruction='Wurde die Minusklammer korrekt berechnet?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>-(x+{{v1}})=-x+{{v1}}</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>-(-{{v1}}+{{v2}}p)={{v1}}-{{v2}}p</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 10, 30),
                'v2': (randint, 2, 9),
            }),
        Question(
            formula='<mat>-({{v1}}z-{{v2}})=-{{v1}}z-{{v2}}</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 30),
            }),
        Question(
            formula='<mat>-(-{{v1}}-v)={{v1}}+v</mat>',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randint, 2, 9),
            }),
        ]
)

summen_und_differenzen_ausklammern = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Summen und Differenzen ausklammern',
    instruction='Was kann man ausklammern?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}*(b-d)+c*(b-d)</mat>',
            correct='<mat>(b-d)</mat>',
            wrong_1='{{v1}}',
            wrong_2='c',
            wrong_3='b',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            formula='<mat>({{v1}}f+{{v2}})*{{v1}}-f*({{v1}}f+{{v2}})</mat>',
            correct='<mat>({{v1}}f+{{v2}})</mat>',
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
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Gemischte Übungen',
    instruction='Wird die Zahl richtig ausgeklammert?',
    question_type='buttons',
    questions=[
        Question(
            formula='<mat>{{v1}}xy+{{v1*v2}}x={{v1}}(xy+{{v2-1}}x)</mat>',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 3, 9),
            }),
        Question(
            instruction='Welche Faktoren kann man ausklammern?',
            formula='<mat>{{v1*10}}cv-{{v1*4}}cd</mat>',
            correct='<mat>{{v1*2}}c</mat>',
            wrong_1='<mat>{{v1*4}}c</mat>',
            wrong_2='c',
            wrong_3='<mat>{{v1*2}}</mat>',
            variables={
                'v1': (randint, 2, 9),
            }),
        Question(
            instruction='Was kann man ausklammern?',
            formula='<mat>{{v2}}(c-{{v1}})-(c-{{v1}})*c^2</mat>',
            correct='<mat>(c-{{v1}})</mat>',
            wrong_1='<mat>(c+{{v1}})</mat>',
            wrong_2='c',
            wrong_3='<mat>c^2</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 10, 20),
            }),
        ]
)

gemischte_ubungen_lineCombineRight = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Ausklammern',
    title='Gemischte Übungen',
    instruction='Wo wurde richtig ausgeklammert? Klicke auf die richtige Lösung.',
    question_type='lineCombineRight',
    questions=[
        Question(
            formula='<mat>{{v1*v3}}z-{{v2*v3}}zy</mat>',
            correct='<mat>({{v1}}-{{v2}}y)*{{v3}}z</mat>',
            wrong_1='<mat>{{v3}}z*({{v2}}-y)</mat>',
            wrong_2='<mat>z*({{v3}}-{{v2}}y)</mat>',
            wrong_3='<mat>{{v3}}z*({{v2}}-{{v1}}y)</mat>',
            variables={
                'v1': (randint, 2, 4),
                'v2': (randint, 5, 7),
                'v3': (randint, 2, 9),
            }),
        Question(
            formula='<mat>{{v1*v2}}-{{v1}}b-{{v1}}c</mat>',
            correct='<mat>{{v1}}*({{v2}}-b-c)</mat>',
            wrong_1='<mat>{{v1*v2}}*(1-2b)</mat>',
            wrong_2='<mat>{{v1}}*(b-c)</mat>',
            wrong_3='<mat>{{v1}}*(1-b-c)</mat>',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 2, 4),
            }),
        ]
)

gleichartige_terme = QuestionSet(
    grade='8',
    capital='Terme',
    subcapital='Terme addieren und subtrahieren',
    title='Gleichartige Terme',
    instruction='Ordne gleichartige Terme einander zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='<mat>{{v1}}xy|-{{v2}}xy</mat>;'
                    '<mat>{{v3}}x*x*y*y|{{v4}}x^2y^</mat>2;'
                    '<mat>{{v5}}x^2yz|-{{v6}}x*x*y*z</mat>;'
                    '<mat>{{v7}}xy^2+xy^2|-{{v8}}xy^2</mat>;'
                    '<mat>{{v9}}x*y*x*y*x*y|{{v10}}x^3y^3</mat>',
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
