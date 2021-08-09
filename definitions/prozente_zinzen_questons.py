from questions import Question, QuestionSet
from random import randint, choice
from definitions.common import randdecimal, male_names, female_names


anteile_vergleichen = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Vergleichen mit Prozenten',
    title='Anteile vergleichen',
    instruction='Ordne die Anteile der Größe nach. Beginne mit dem Kleinsten.',
    question_type='dragSort',
    questions=[
        Question(
            formula='',
            correct='0,{{v1}}%;1/{{v8}};0,{{v2}};1/{{v3}};{{v4}}%;0,{{v5}};3/{{v6}};{{v7}}%',
            variables={
                'v1': (randint, 1, 90),
                'v8': (randdecimal, 20, 50, 5),
                'v2': (randint, 10, 12),
                'v3': (randint, 5, 8),
                'v4': (randdecimal, 21, 24),
                'v5': (randint, 25, 40),
                'v6': (randint, 4, 5),
                'v7': (randint, 81, 99),
            }),
        ]
)

umwandlung_von_bruchen_und_dezimalzahlen = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Vergleichen mit Prozenten',
    title='Umwandlung von Brüchen und Dezimalzahlen',
    instruction='Wandle den Bruch zu einem Zehnerbruch um. Schreibe dann als Prozentangabe.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}/50 = ___/100 = ___ %',
            correct='{{v1*2}}; {{v1*2}}',
            variables={
                'v1': (randint, 2, 40),
            }),
        Question(
            formula='{{v1}}/25 = ___/100 = ___ %',
            correct='{{v1*4}}; {{v1*4}}',
            variables={
                'v1': (randint, 2, 24),
            }),
        Question(
            instruction='Schreibe die Dezimalzahl zuerst als Zehnerbruch mit 100 im Nenner und dann als Prozentangabe.',
            formula='0,{{v1}} = ___/100 = ___ %',
            correct='{{v1}}; {{v1}}',
            variables={
                'v1': (randint, 10, 99),
            }),
        Question(
            instruction='Schreibe die Dezimalzahl zuerst als Zehnerbruch mit 100 im Nenner und dann als Prozentangabe.',
            formula='0,0{{v1}} = ___/100 = ___ %',
            correct='{{v1}}; {{v1}}',
            variables={
                'v1': (randint, 1, 9),
            }),
        Question(
            instruction='Wandle die Prozentangabe zuerst in einen Zehnerbruch um. Kürze dann so weit wie möglich.',
            formula='{{v1*20}}% = ___/100 = ___/___',
            correct='{{v1*20}}; {{v1*20}}',
            variables={
                'v1': (randint, 1, 4),
            }),
        ]
)

anteile_in_prozent = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Vergleichen mit Prozenten',
    title='Anteile in Prozent',
    instruction='Gib die Anteile in Prozent an.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1*10}} g sind <mat>___</mat>% von 1 kg.',
            correct='{{v1}}',
            variables={
                'v1': (randint, 2, 95),
            }),
        Question(
            formula='{{v1*10}} m sind <mat>___</mat>% von 1 km.',
            correct='{{v1}}',
            variables={
                'v1': (randint, 2, 95),
            }),
        Question(
            formula='{{v1*6}} min sind <mat>___</mat>% von 1 h.',
            correct='{{v1*10}}',
            variables={
                'v1': (randint, 1, 9),
            }),
        Question(
            formula='{{v1*v2}} ct sind <mat>___</mat>% von {{v2}} €.',
            correct='{{v1}}',
            variables={
                'v1': (randint, 1, 8),
                'v2': (randint, 2, 5),
            }),
        ]
)

gangige_prozentangaben = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Vergleichen mit Prozenten',
    title='Gängige Prozentangaben',
    instruction='Schreibe den Bruch als Prozentzahl. Runde, wenn nötig, auf eine Nachkommastelle.',
    question_type='gap',
    questions=[
        Question(
            formula='<mat>1/{{v1}} = ___%</mat>',
            correct='{{(100/v1)|round|int}}',
            variables={
                'v1': (choice, [2, 4, 5, 10, 20, 25, 50]),
            }),
        Question(
            formula='<mat>1/{{v1}} ≈ ___%</mat>',
            correct='{{"%.1f"|format(100/v1)}}',
            variables={
                'v1': (choice, [3, 6, 8, 30, 40]),
            }),
        ]
)

prozentzahlen_erkennen = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Vergleichen mit Prozenten',
    title='Prozentzahlen erkennen',
    instruction='Gib den im Text beschriebenen Anteil als Bruch und in Prozent an.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}} von hundert Hamburgern waren im Jahr 2017 zwischen 10 und 20 Jahre alt. '
                    '<br><br> <mat>___ = ___%</mat>',
            correct='{{v1}}/100;{{v1}}',
            variables={
                'v1': (randint, 8, 15),
            }),
        Question(
            formula='An {{v1*v2}} Verkehrsunfällen waren {{v1}} RadfahrerInnen beteiligt. '
                    '<br><br> <mat>___ = ___%</mat>',
            correct='{{v1}}/{{v1*v2}};{{(100/v2)|round|int}}',
            variables={
                'v1': (randdecimal, 10, 50, 10),
                'v2': (choice, [5, 10, 20])
            }),
        Question(
            formula='ABeim Elfmeterschießen haben die Torschützinnen bei {{v1}} von fünf Schüssen das Tor getroffen. '
                    '<br><br> <mat>___ = ___%</mat>',
            correct='{{v1}}/5;{{v1*20}}',
            variables={
                'v1': (randint, 1, 5),
            }),
        Question(
            formula='Am Donnerstag waren {{v1}} von {{v1*v2}} Kinder krank. <br><br> <mat>___ = ___%</mat>',
            correct='{{v1}}/{{v1*v2}};{{(100/v2)|round|int}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [5, 10, 20])
            }),
        ]
)

prozentsatz = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Prozentsatz, Prozentwert, Grundwert',
    title='Prozentsatz',
    instruction='Berechne den Prozentsatz',
    hint='Um den Prozentsatz auszurechnen, teilst du den Prozentwert durch den Grundwert, '
         'und multiplizierst das Ergebnis mit 100.',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}} € von 100 € <br><br> <mat>___</mat> %',
            correct='{{v1}}',
            variables={
                'v1': (randdecimal, 10, 50, 5),
            }),
        Question(
            formula='{{v1}} m von {{v1*v2}} m <br><br> <mat>___</mat> %',
            correct='{{(100/v2)|round|int}}',
            variables={
                'v1': (randint, 11, 30),
                'v2': (choice, [5, 10, 20, 50])
            }),
        Question(
            formula='{{v1}} kg von {{v1*v2}} kg <br><br> <mat>___</mat> %',
            correct='{{(100/v2)|round|int}}',
            variables={
                'v1': (randdecimal, 10, 50, 5),
                'v2': (choice, [2, 4, 5, 10, 20])
            }),
        Question(
            formula='{{v1}} g von {{v1*v2}} g <br><br> <mat>___</mat> %',
            correct='{{(100/v2)|round|int}}',
            variables={
                'v1': (randint, 1, 9),
                'v2': (choice, [2, 4, 5, 10])
            }),
        Question(
            formula='{{v1}} Minuten von 60 Minuten <br><br> <mat>___</mat> %',
            correct='{{(60/v1)|round|int}}',
            variables={
                'v1': (choice, [3, 6, 12, 15, 30]),
            }),
        ]
)

prozentwert = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Prozentsatz, Prozentwert, Grundwert',
    title='Prozentwert',
    instruction='Berechne den Prozentwert im Kopf mit der Formel <mat>W = G * p%</mat>',
    question_type='gap',
    questions=[
        Question(
            formula='Grundwert: {{v1*100}} <br> Prozentsatz: {{v2*10}}% <br> Prozentwert = ___',
            correct='{{v1*v2*10}}',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 1, 9),
            }),
        Question(
            formula='Grundwert: {{v1}} <br> Prozentsatz: {{v2}}% <br> Prozentwert = ___',
            correct='{{(v1*v2/100)|round|int}}',
            variables={
                'v1': (randdecimal, 15, 40, 5),
                'v2': (randdecimal, 20, 80, 20),
            })
        ]
)

grundwert = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Prozentsatz, Prozentwert, Grundwert',
    title='Prozentwert',
    instruction='Berechne den Grundwert mit der Formel <mat>G = W / p%</mat>',
    question_type='gap',
    questions=[
        Question(
            formula='{{v1}}% sind {{v2}} kg. <br> 100 % sind <mat>___</mat> kg.',
            correct='{{(v2*100/v1)|round|int}}',
            variables={
                'v1': (choice, [4, 10, 20, 25, 50]),
                'v2': (randint, 2, 8),
            }),
        Question(
            formula='{{v1}}% sind {{v2}} cm. <br> 100 % sind <mat>___</mat> cm.',
            correct='{{(v2*100/v1)|round|int}}',
            variables={
                'v1': (choice, [4, 10, 20, 25, 50]),
                'v2': (randint, 2, 8),
            }),
        Question(
            formula='{{v1}}% sind {{v2*100}} €. <br> 100 % sind <mat>___</mat> €.',
            correct='{{(v2*10000/v1)|round|int}}',
            variables={
                'v1': (choice, [10, 20, 25, 40, 50]),
                'v2': (randint, 1, 4),
            }),
        ]
)

prozentsatz_erkennen_und_darstellen = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Prozentsatz, Prozentwert, Grundwert',
    title='Prozentsatz erkennen und darstellen',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            formula='Wieviele Felder sind blau? <br> ___ <br> '
                    'Wieviele Felder gibt es insgesamt? <br> ___ <br> '
                    'Wieviele Prozent ist das? <br> ___ %',
            correct='{{v1}}; 20; {{v1*5}}',
            variables={
                'v1': (randint, 2, 18),
            },
            image={
                'table': {
                    'nrows': 4,
                    'ncols': 5,
                    'cells_filled': '{{v1}}',
                },
                'draw_grid': False,
            }
        ),
        Question(
            formula='Wieviele Felder sind blau? <br> ___ <br> '
                    'Wieviele Felder gibt es insgesamt? <br> ___ <br> '
                    'Wieviele Prozent ist das? <br> ___ %',
            correct='{{v1}}; 10; {{v1*10}}',
            variables={
                'v1': (randint, 2, 9),
            },
            image={
                'pie_chart': {
                    'nsegments': 10,
                    'segments_filled': '{{v1}}',
                },
                'draw_grid': False,
            }
        ),
        ]
)

zinsen = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Zinsrechnung',
    title='Zinsen',
    instruction='Berechne die Zinsen.',
    question_type='gap',
    questions=[
        Question(
            formula='{{name}}s Vater hat ihm erzählt, dass er dieses Jahr <mat>K={{v1*10000}}€</mat> '
                    'zu einem Zinssatz von <mat>p={{"%.1f"|format(v2*100)}}%</mat> angelegt hat.<br><br> '
                    'Wie viel Zinsen bekommt sein Vater jährlich? '
                    '<br><br> Rechnung</b>:<mat>Z = ___ € * ___%<br>=___€ * ____<br>=___€</mat>',
            correct='{{v1*10000}};{{"%.1f"|format(v2*100)}};{{v1*10000}};{{v2}};{{(v1*v2)|round|int}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 1, 5),
                'v2': (randdecimal, 0.02, 0.06, 0.005, 3),
            }),
        Question(
            formula='{{name}} hat dieses Jahr <mat>K={{v1}}€</mat> gespart und von der Bank ein gutes '
                    'Angebot für einen Sparvertrag bekommen, der ihr einen Zinssatz von <mat>p=10%</mat> verspricht.'
                    '<br><b>Frage</b>:<br>Wie viel Zinsen bekommt sie am Ende des Jahres? <br><br> '
                    '<mat>Z = ___ € * ___% <br>=___ € * ___<br>=___€</mat>',
            correct='{{v1}};{{(v2*100)|round|int}};{{v1}};{{v2}};{{(v1*v2)|round|int}}',
            variables={
                'name': (choice, female_names),
                'v1': (randdecimal, 500, 1000, 100),
                'v2': (choice, [0.05, 0.06, 0.08, 0.1]),
            }),
        Question(
            formula='{{name}} hat sich von der Bank <mat>K={{v1*10000}}€</mat> für ein Auto geliehen. '
                    'Auf dieses Geld muss er jährlich <mat>p={{"%.1f"|format(v2*100)}}%</mat> Zinsen bezahlen.'
                    '<br><b>Frage</b>:<br> Wenn er noch nichts abbezahlt hat, erhöhen sich seine Schulden um wie '
                    'viel Euro? <br><br> '
                    '<mat>Z = ___ € * ___% <br>=___ € * ___<br>=___€</mat>',
            correct='{{v1*10000}};{{"%.1f"|format(v2*100)}};{{v1*10000}};{{v2}};{{(v1*v2)|round|int}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 1, 6),
                'v2': (randdecimal, 0.02, 0.06, 0.005, 3),
            }),
        Question(
            formula='{{name}} fragt sich, wie viel Zinsen ein Millionär mit einem Kapital von <mat>K=1000000€</mat> '
                    'bekommt, wenn er sein Vermögen auf einem Konto mit <mat>p={{"%.1f"|format(v2*100)}}%</mat> Zinsen '
                    'hat.<br><b>Frage</b>:<br>Wie viel Zinsen würde der Millionär bekommen?'
                    '<mat>Z = ___ € * ___% <br>=___ € * ___<br>=___€</mat>',
            correct='1000000;{{"%.1f"|format(v2*100)}};1000000;{{v2}};{{(1000000*v2)|round|int}}',
            variables={
                'name': (choice, female_names),
                'v1': (randint, 1, 6),
                'v2': (randdecimal, 0.02, 0.06, 0.005, 3),
            }),
        ]
)

bankjahr = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Zinsrechnung',
    title='Bankjahr',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            formula='{{name}} hat ein Kapital von <mat>K={{v1*1000}}€</mat> bei der Bank angelegt. '
                    'Er bekommt von der Bank einen Zinssatz p = {{v2}}%. <br> '
                    'Das Geld hat er nur {{v3}} Monate, also laut der Bank <mat>t={{30*v3}}</mat> Tage, auf dem Konto.'
                    '<br><br><b>Frage</b>:<br>Wie viel Geld bekommt er von der Bank? <mat>Z = Z_(J)*t/360 '
                    '<br>= K*p*t/360 '
                    '<br>=___€*___%*___/360 '
                    '<br>=___€</mat>',
            correct='{{v1*1000}};{{v2}};{{30*v3}};{{(v1*10*v2*v3/12)|round|int}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 1, 5),
                'v2': (choice, [2, 4, 6, 8]),
                'v3': (choice, [3, 6, 9]),
            }),
        Question(
            formula='{{name}} hat ein Kapital von <mat>K={{v1*1000}}€</mat> bei der Bank angelegt. '
                    'Er bekommt von der Bank einen Zinssatz p = {{v2}}%. <br> '
                    'Das Geld hat er <mat>t={{v3}}</mat> Tage auf dem Konto.<br><br><b>Frage</b>:<br>'
                    'Wie viel Geld bekommt er von der Bank? <mat>Z = Z_(J)*t/360 '
                    '<br>=K*p*t/360 '
                    '<br>=___€*___%*___/360 '
                    '<br>=___€</mat>',
            correct='{{v1*1000}};{{v2}};{{v3}};{{(v1*10*v2*v3/360)|round|int}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 1, 5),
                'v2': (choice, [2, 4, 6, 8]),
                'v3': (choice, [36, 72, 108, 144]),
            }),
        ]
)

tageszins = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Zinsrechnung',
    title='Tageszins',
    instruction='',
    question_type='gap',
    questions=[
        Question(
            formula='Berechne die Tageszinsen bei einem Jahreszins von <mat>Z={{v1*360}}€</mat>. <br><br> '
                    '<mat>Z=1/360 * ___€=___€</mat>',
            correct='{{v1*360}};{{v1}}',
            variables={
                'v1': (randint, 3, 9),
            }),
        Question(
            formula='Berechne die Monatszinsen bei einem Jahreszins von <mat>Z={{v1*60}}€</mat>. '
                    'Monatszinsen sind Zinsen für 30 Tage. <br><br> <mat>Z=___/360 * ___€ = ___€</mat>',
            correct='30;{{v1*60}};{{v1*5}}',
            variables={
                'v1': (randint, 3, 9),
            }),
        Question(
            instruction='Berechne die Zinsen.',
            hint="Um die Zinsen Z einer beliebigen Dauer zu berechnen, multipliziere die Jahreszinsen "
                 "<mat>Z_J=K*p</mat> mit dem Verhältnis der Tage zum Jahr:<mat center='true'>Z = K*p*t/360</mat>",
            formula='Guthaben: {{1200*v1}} € <br> '
                    'Zinssatz: {{v2}} % <br> '
                    'Tage: {{30*v3}}  <br> '
                    'Zinsen: ____ € <br><br> ',
            correct='{{v2*v3}}',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 2, 5),
                'v3': (randint, 1, 6),
            }),
        Question(
            instruction='Berechne die Zinsen.',
            hint="Um die Zinsen Z einer beliebigen Dauer zu berechnen, multipliziere die Jahreszinsen "
                 "<mat>Z_J=K*p</mat> mit dem Verhältnis der Tage zum Jahr:<mat center='true'>Z = K*p*t/360</mat>",
            formula='Guthaben: {{10000*v1}} € <br> '
                    'Zinssatz: {{v2}} % <br> '
                    'Tage: {{36*v3}}  <br> '
                    'Zinsen: ____ € <br><br> ',
            correct='{{(v1*100*v2*v3/360)|round|int}}',
            variables={
                'v1': (randint, 1, 6),
                'v2': (randint, 2, 5),
                'v3': (randint, 1, 6),
            }),
        ]
)

zinssatz = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Zinsrechnung',
    title='Zinssatz',
    instruction='Wie hoch ist der Zinssatz p %?',
    question_type='gap',
    questions=[
        Question(
            formula='{{name}} hat ein Kapital von <mat>K={{v1*100}}€</mat> und hat nach einem Jahr '
                    '<mat>Z={{v1*v2}}€</mat> Zinsen bekommen. <br><br> <mat>p=(___€)/(___€) = ___%</mat>',
            correct='{{v1*v2}};{{v1*100}};{{v2}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 10, 15),
                'v2': (randint, 2, 6),
            }),
        Question(
            formula='Mit einem Kapital von <mat>K={{v1*100}}€</mat> hat {{name}} von der Bank '
                    '<mat>Z={{v1*v2}}€</mat> Jahreszinsen bekommen.  <br><br> <mat>p=(___€)/(___€) = ___%</mat>',
            correct='30;{{v1*60}};{{v1*5}}',
            variables={
                'name': (choice, female_names),
                'v1': (randint, 5, 9),
                'v2': (randint, 2, 6),
            }),
        ]
)

kapital = QuestionSet(
    grade='7',
    capital='Prozente, Zinsen',
    subcapital='Zinsrechnung',
    title='Kapital',
    instruction='',
    question_type='gap',
    hint="Um eine Dezimalzahl in eine Prozentzahl umzuwandeln, verschiebe das Komma um zwei Stellen nach rechts."
         "<br><mat center='true'><b>0.05 = 5%</b></mat>",
    questions=[
        Question(
            instruction='Wie hoch war der Gewinn?',
            formula='{{name}} hat im Lotto gewonnen und ihr Geld für ein Jahr bei der Bank angelegt. '
                    'Da sie eine große Summe Geld angelegt hat, hat sie einen guten Zinssatz von '
                    '<mat>{{v1}}%</mat> bekommen. Ihre Jahreszinsen sind <mat>{{(v1*v2*1000)|round|int}}€</mat>. '
                    '<br><b>Frage:</b><br> <mat>K = Z/(p) '
                    '<br>= (___€)/(___%) <br>= ___€</mat>',
            correct='{{(v1*v2*1000)|round|int}};{{v1}};{{(v2*100000)|round|int}}',
            variables={
                'name': (choice, female_names),
                'v1': (randdecimal, 6, 9, 0.5),
                'v2': (randint, 2, 9),
            }),
        Question(
            instruction='Wie viel Geld hat {{name}} auf seinem Konto?',
            formula="{{name}} bekommt von der Bank <mat>Z={{v1*v2}}€</mat> Zinsen bei einem Zinssatz von "
                    "<mat>p={{v2}}%</mat>. <br><br> <mat center='true' align='rl'>K = Z/(p) "
                    "<br>= (___€)/(___%) <br>=___€</mat>",
            correct='{{v1*v2}};{{v2}};{{v1*100}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 11, 19),
                'v2': (randint, 2, 5),
            }),
        Question(
            instruction='Wie viel Geld haben seine Eltern angelegt?',
            formula="{{name}}' Eltern haben für ihn ein Konto eingerichtet, von welchem Max die Zinsen bekommt. "
                    "Im Jahr sind das <mat>Z={{v1*v2*5}}€</mat>, bei einem Zinssatz von <mat>p={{v2}}%</mat>."
                    "<br><br><mat>K = Z/(p) <br>= (___€)/(___%) <br>=___€</mat>",
            correct='{{v1*v2*5}};{{v2}};{{v1*500}}',
            variables={
                'name': (choice, male_names),
                'v1': (randint, 11, 19),
                'v2': (randint, 2, 5),
            }),
        ]
)

# Add newly created question sets in that list, so the script can use them
question_sets = [
    anteile_vergleichen,
    umwandlung_von_bruchen_und_dezimalzahlen,
    anteile_in_prozent,
    gangige_prozentangaben,
    prozentzahlen_erkennen,
    prozentsatz,
    prozentwert,
    grundwert,
    prozentsatz_erkennen_und_darstellen,
    zinsen,
    bankjahr,
    tageszins,
    zinssatz,
    kapital,
    ]
