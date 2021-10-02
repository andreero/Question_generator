from questions import Question, QuestionSet
from random import randint, choice
from definitions.common import randdecimal, male_names, female_names, get_fakultaet, numbers

baumdiagramme = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Baumdiagramme und Pfadregeln',
    title='Baumdiagramme',
    instruction='Wähle die richtige Antwort aus.',
    question_type='MC',
    questions=[
        Question(
            formula='Die Reißzwecke wird nun zweimal geworfen. Die Reihenfolge spielt keine Rolle. '
                    'Das heißt, es ist egal, ob zuerst Kopf und dann Seite oder umgekehrt geworfen wurde. '
                    '<br>Wie sieht eine mögliche Ergebnismenge aus?',
            correct='{{"{"}}KK;_SS;_KS{{"}"}}',
            wrong_1='{{"{"}}K;_S;_K;_S{{"}"}}',
            wrong_2='{{"{"}}KS;_SK;_KK{{"}"}}',
        )
    ]
)

pfadregel_1 = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Baumdiagramme und Pfadregeln',
    title='1. Pfadregel',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Die erste Pfadregel besagt, dass nur entlang eines Pfades ________ wird. '
                        'Deswegen wird die erste Pfadregel auch ________ genannt.',
            formula='',
            correct='multipliziert|dividiert;Produktregel|Divisionsregel',
        ),
        Question(
            instruction='Ein <b>Pfad</b> ist der Weg entlang der _____ zum Ergebnis.',
            formula='',
            correct='Äste',
            wrong_1='Wahrscheinlichkeiten',
            wrong_2='Startpunnkte',
        )
    ]
)

ur_und_ranglisten_unterscheiden = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Diagramme und Tabellen',
    title='Ur- und Ranglisten unterscheiden ',
    instruction='Handelt es sich um eine Rangliste?',
    question_type='MC',
    questions=[
        Question(
            formula='1 cm; {{v2}} cm; {{v3}} cm; {{v4}} cm; {{v5}} cm; {{v6}} cm; {{v7}} cm; {{v8}} cm',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v2': (randint, 1, 3),
                'v3': (randint, 3, 5),
                'v4': (randint, 6, 9),
                'v5': (randint, 10, 13),
                'v6': (randint, 14, 17),
                'v7': (randint, 17, 20),
                'v8': (randint, 21, 25),
            },
        ),
        Question(
            formula='{{v1}} m; {{v2}} m; {{v3}} m; {{v4}} m; {{v5}} m; {{v6}} m; {{v7}} m; {{v7}} m',
            correct='correct',
            wrong_1='wrong',
            variables={
                'v1': (randdecimal, 55, 58),
                'v2': (randint, 58, 60),
                'v3': (randint, 60, 62),
                'v4': (randint, 62, 65),
                'v5': (randint, 66, 69),
                'v6': (randint, 70, 75),
                'v7': (randint, 75, 80),
            },
        ),
        Question(
            formula='{{v1}} °C; {{v2}} °C; {{v3}} °C; {{v4}} °C; {{v5}} °C; {{v6}} °C; {{v7}} °C; {{v8}} °C',
            correct='wrong',
            wrong_1='correct',
            variables={
                'v1': (randdecimal, 11.5, 12),
                'v2': (randdecimal, 11.0, 11.4),
                'v3': (randdecimal, 11, 12),
                'v4': (randdecimal, 11, 12),
                'v5': (randdecimal, 12, 12.5),
                'v6': (randdecimal, 12, 13),
                'v7': (randdecimal, 12.5, 13),
                'v8': (randdecimal, 12, 13),
            },
        ),
    ]
)

ur_und_ranglisten_unterscheiden_dragsort = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Diagramme und Tabellen',
    title='Ur- und Ranglisten unterscheiden ',
    instruction='',
    question_type='dragSort',
    questions=[
        Question(
            instruction='{{name}} hat 10 Tage lang morgens die Temperatur gemessen. Erstelle die Rangliste.',
            formula='',
            correct='{{v1}} °C; {{v2}} °C; {{v3}} °C; {{v4}} °C; {{v5}} °C; {{v6}} °C; {{v7}} °C; {{v8}} °C',
            variables={
                'name': (choice, female_names),
                'v1': (randint, 16, 18),
                'v2': (randint, 18, 20),
                'v3': (randint, 20, 22),
                'v4': (randint, 22, 23),
                'v5': (randint, 23, 24),
                'v6': (randint, 24, 25),
                'v7': (randint, 25, 26),
                'v8': (randint, 27, 28),
            }),
    ]
)

sachaufgaben_gap = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Häufigkeiten',
    title='Sachaufgaben',
    instruction='Wie groß ist die Stichprobe?',
    question_type='gap',
    questions=[
        Question(
            formula='In einer Stichprobe betrug der Anteil der schlechten Äpfel <mat>{{v1*5}}/{{v2*15}}</mat>. '
                    'Die Stichprobe enthielt {{v1*5}} schlechte Äpfel.'
                    'Die Stichprobe bestand aus <mat>___</mat> Äpfeln.',
            correct='{{v2*15}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 11, 25),
            }
        ),
        Question(
            formula='Eine Stichprobe enthielt {{v1*10}} defekte Lampen. Sie machten einen Anteil von '
                    '<mat>{{v1*10}}/{{v2*10}}</mat> der Stichprobe aus.'
                    'Die Stichprobe bestand aus <mat>___</mat> Lampen.',
            correct='{{v2*10}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (randint, 11, 25),
            }
        ),
        Question(
            formula='Bei einer Stichprobe trugen <mat>{{v1}}/{{v2*10}}</mat> der Fahrradfahrer keinen Helm. '
                    'In der Stichprobe waren {{v1}} Fahrradfahrer ohne Helm.'
                    'Die Stichprobe bestand aus <mat>___</mat> Fahrradfahrern.',
            correct='{{v2*10}}',
            variables={
                'v1': (randint, 11, 25),
                'v2': (randint, 11, 25),
            }
        ),
    ]
)

sachaufgaben_mc = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Häufigkeiten',
    title='Sachaufgaben',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Die Firma Thiele möchte die Qualität ihrer Blumentöpfe überprüfen. Dazu wurde von den '
                        '{{v1*v2*100}} produzierten Blumentöpfen eine Stichprobe von {{v1*100}} Blumentöpfen entnommen.'
                        ' Bei der Kontrolle der Stichprobe fand man heraus, dass {{v1*v3}} davon einen Sprung hatten. '
                        'Schätze, wie viel Blumentöpfe in der Gesamtproduktion beschädigt sein könnten.',
            formula='{{v1*v3}} von {{v1*100}} Blumentöpfen hatten einen Sprung. Das ist ein Anteil von ____________.',
            correct='1/{{(100/v3)|round|int}}',
            wrong_1='1/{{(200/v3)|round|int}}',
            wrong_2='1/30',
            wrong_3='1/{{v3}}',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [10, 20, 40, 100]),
                'v3': (choice, [2, 4, 5]),
            }
        ),
        Question(
            instruction='Die Klirr GmbH kontrolliert in einer Stichprobe, wie viele ihrer produzierten Glasflaschen '
                        'einen Riss haben. Sie entnehmen zur Überprüfung {{v1*v2}} Glasflaschen aus der Gesamtproduktion '
                        'und finden heraus, dass {{v1}} dieser Glasflaschen einen Riss haben. <br> '
                        'Wie viele der insgesamt 100000 produzierten Glasflaschen haben vermutlich einen Riss?',
            formula='{{v1}} von {{v1*v2}} Glasflaschen hatten einen Riss. '
                    'Der Anteil von Glasflaschen mit Riss beträgt also ____________.',
            correct='1/{{v2}}',
            wrong_1='1/{{v2+10}}',
            wrong_2='1/{{(v2/10)|round|int}}',
            wrong_3='3/50',
            variables={
                'v1': (randint, 2, 9),
                'v2': (choice, [20, 25, 40, 50]),
            }
        ),
    ]
)

gemischte_aufgaben_dragmatch = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Gemischte Aufgaben',
    instruction='Ein Würfel wird einmal geworfen. Schiebe Ereignisse mit gleicher Wahrscheinlichkeit zusammen.',
    question_type='dragMatch',
    hint='Überlege, wie viele günstige Ergebnisse es zu jedem Ereignis gibt.',
    questions=[
        Question(
            formula='',
            correct='Die Augenzahl ist gerade.|Die Augenzahl ist ungerade.;'
                    'Die Augenzahl ist genau 4.|Die Augenzahl ist genau 2.;'
                    'Die Augenzahl ist größer als 0.|Die Augenzahl ist kleiner als 7.',
        ),
    ]
)

gemischte_aufgaben = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Gemischte Aufgaben',
    instruction='Wähle die richtige Antwort aus.',
    question_type='MC',
    questions=[
        Question(
            formula='Die Wahrscheinlichkeit, dass beim Werfen einer Münze die {{v1}} nach oben zeigt, beträgt:',
            correct='1/2',
            wrong_1='1/3',
            wrong_2='2/2',
            variables={
                'v1': (choice, ['Zahlseite', 'Kopfseite'])
            }
        ),
        Question(
            formula='Die Wahrscheinlichkeit an einem Sonntag Geburtstag zu haben, beträgt',
            correct='1/7',
            wrong_1='1/4',
            wrong_2='2/7',
            variables={
                'v1': (choice, ['Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag', 'Sonntag']),
            }
        ),
    ]
)

laplace_experimente_1 = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Laplace-Experimente (1)',
    instruction='Handelt es sich um Laplace-Experimente? Entscheide',
    question_type='MC',
    questions=[
        Question(
            formula='Werfen eines Würfels',
            correct='correct',
            wrong_1='wrong',
        ),
        Question(
            formula='Ein Münzwurf',
            correct='correct',
            wrong_1='wrong',
        ),
        Question(
            formula='Ziehen eines Loses aus einem Topf mit 50 Gewinnen und 50 Nieten',
            correct='correct',
            wrong_1='wrong',
        ),
        Question(
            formula='Werfen einer Reißzwecke',
            correct='wrong',
            wrong_1='correct',
        ),
        Question(
            formula='Ziehen von Gummibärchen aus einer Tüte mit 14 grünen, 8 roten, '
                    '4 gelben und 18 orangen Gummibärchen.',
            correct='wrong',
            wrong_1='correct',
        ),
    ]
)

laplace_experimente_1_dragmatch = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Laplace-Experimente (1)',
    instruction='Wähle die Wahrscheinlichkeite n der einzelnen Ergebnisse zu den passenden Laplace-Experimenten aus.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='Wurf eines sechsseitigen Würfels|<mat>1/6</mat>;'
                    'Ziehen einer Kugel aus einer Urne mit zwölf gleichen Kugeln| <mat>1/12</mat>;'
                    'Ziehen eines Loses aus einem Hut mit 3 verschiedenen Losen|<mat>1/3</mat>;'
                    'Glücksrad mit sieben gleich großen Feldern| <mat>1/7</mat>',
        ),
    ]
)

laplace_experimente_2 = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Laplace-Experimente (2)',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Wie lautet die Formel zur Berechnung der Wahrscheinlichkeit eines '
                        '<b>einzelnen</b> Ergebnisses in Laplace-Experimenten?',
            formula='',
            correct='<mat>1/(Anzahl der möglichen Ergebnisse)</mat>',
            wrong_1='<mat>(Anzahl der möglichen Ergebnisse)/1</mat>',
            wrong_2='<mat>(Anzahl der möglichen Ergebnisse)/(Anzahl der günstigen Ergebnisse)</mat>',
        ),
        Question(
            formula='Ein Würfel hat {{v1*2}} Seiten und <mat>___</mat> Augenzahlen sind gerade. '
                    'Mit der Formel ergibt sich:'
                    '<br><br><mat>P(E) =|(günstige Ergebnisse)/(mögliche Ergebnisse)<br> =___/___ = ___</mat>',
            correct='{{v1}}|{{v1-1}}|{{v1-2}};{{v1}}|{{v1+1}}|{{v1+2}};{{v1*2}}|{{v1*2-2}}|{{v1*2-4}};0.5|1|0.25',
            variables={
                'v1': (choice, [6, 8, 12, 20])
            }
        ),
    ]
)

relative_haufigkeit_und_wahrscheinlichkeit_1_dragmatch = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Relative Häufigkeit und Wahrscheinlichkeit (1)',
    instruction='Mit einem gewöhnlichen Würfel wirft man bei ungefähr jedem sechsten Wurf eine 6.<br>'
                'Ordne die Schreibweisen für die Wahrscheinlichkeit ihren Bezeichnungen zu.',
    question_type='dragMatch',
    questions=[
        Question(
            formula='',
            correct='1/6|Bruch;'
                    '0.1 bar{6}|Dezimalzahl;'
                    '16.bar{6}%|Prozentzahl',
        ),
    ]
)

relative_haufigkeit_und_wahrscheinlichkeit_1_draggroup = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Relative Häufigkeit und Wahrscheinlichkeit (1)',
    instruction='Ordne die Begriffe ihren Definitionen zu.',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='absolute Häufigkeit|Die Zahl, die angibt, wie oft ein Ergebnis aufgetreten ist.;'
                    'relative Häufigkeit|Die Zahl, wie oft ein bestimmtes Ergebnis aufgetreten ist im Verhältnis zur Versuchszahl.',
        ),
    ]
)

relative_haufigkeit_und_wahrscheinlichkeit_2 = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeiten',
    title='Relative Häufigkeit und Wahrscheinlichkeit (2)',
    question_type='gap',
    instruction='',
    questions=[
        Question(
            instruction='Berechne für {{name}}s Versuch die relativen Häufigkeiten, '
                        'indem du die absoluten Häufigkeiten durch die Gesamtzahl teilst.',
            formula='{{name}} erzielte in {{v1}} Versuchen {{v2}} mal Kopf und {{v1-v2}} mal Seite. <br><br> '
                    'P(Kopf) = ___/{{v1}} = ___<br>'
                    'P(Seite) = {{v1-v2}}/___ = ___',
            correct='{{v2}};{{"%.3f"|format(v2/v1)}};{{v1}};{{"%.3f"|format((v1-v2)/v1)}}',
            variables={
                'name': (choice, female_names),
                'v1': (randdecimal, 100, 400, 100),
                'v2': (randdecimal, 20, 80, 10),
            }
        ),
        Question(
            instruction='Berechne für {{name}}s Versuch die Prozentzahl, '
                        'indem du die Dezimalzahl mit dem Faktor 100 multiplizierst.',
            formula='{{name}} erzielte in {{v1}} Versuchen {{v2}} mal Kopf und {{v1-v2}} mal Seite. <br><br> '
                    'P(Kopf) = {{v2}}/{{v1}} = {{"%.3f"|format(v2/v1)}} = ___% <br> '
                    'P(Seite) = {{v1-v2}}/{{v2}} = {{"%.3f"|format(v2/v1)}} = ___ %',
            correct='{{"%.1f"|format(v2/v1*100)}};{{"%.1f"|format((v1-v2)/v1*100)}}',
            variables={
                'name': (choice, female_names),
                'v1': (randdecimal, 100, 400, 100),
                'v2': (randdecimal, 20, 80, 10),
            }
        ),
    ]
)

ereignisse = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Ereignisse',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            formula='Welche günstigen Ergebnisse gehören zum Ereignis „Die Augenzahl ist ungerade“?',
            correct='1;3;5',
            wrong_1='2;4;6',
            wrong_2='2',
            wrong_3='6',
        ),
        Question(
            formula='Welche günstigen Ergebnisse gehören zum Ereignis „Die Augenzahl ist gerade“?',
            correct='2;4;6',
            wrong_1='1;3;5',
            wrong_2='3',
            wrong_3='5',
        ),
        Question(
            instruction='Welches der Ergebnisse passt <b>nicht</b> zum Ereignis?',
            formula='Die Summe der beiden Kugeln ist kleiner als 3',
            correct='12;13;21;22;23;31;32;33',
            wrong_1='11;33',
            wrong_2='12;21;23;32',
            image='images/zufallsexperimente1.svg'
        ),
        Question(
            instruction='Welches der Ergebnisse passt <b>nicht</b> zum Ereignis?',
            formula='Die Summe der beiden Kugeln ist ungerade',
            correct='11;13;22;31;33',
            wrong_1='12;21;23;32;33',
            wrong_2='21;22;32',
            image='images/zufallsexperimente1.svg',
        ),
    ]
)

ergebnissmengen = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Ergebnissmengen',
    instruction='Im einem Ort wird in diesem Jahr eine Statistik geführt, in welcher Jahreszeit Kinder geboren werden. '
                'Dort gibt es Familien mit ein, zwei oder drei Kindern. '
                'Es wird unterschieden in Sommer (S) und in Winter (W).',
    question_type='MC',
    questions=[
        Question(
            formula='Wie sieht die jeweilige Ergebnismenge bei Familien mit einem Kind aus? {___;___}?',
            correct='{{"{"}}S;W{{"}"}}',
            wrong_1='{{"{"}}SW;WS{{"}"}}',
        ),
        Question(
            formula='Wie sieht die jeweilige Ergebnismenge bei Familien mit zwei Kindern aus? {___;___;___;___}',
            correct='{{"{"}}SS;WW;SW;WS{{"}"}}',
            wrong_1='{{"{"}}S;W;WW;SW{{"}"}}',
        ),
        Question(
            formula='Wie sieht die jeweilige Ergebnismenge bei Familien mit drei Kindern aus?',
            correct='{{"{"}}SSS;SSW;SWW;SWS;WSS;WWS;WSW;WWW{{"}"}}',
            wrong_1='{{"{"}}SSS;WWW;SWW;WSS{{"}"}}',
            wrong_2='{{"{"}}S;W;SSS;WWW;SS;WW;SWS{{"}"}}',
        ),
    ]
)

spezielle_ereignisse = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Zufallsexperimente',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Welche Gegenereignisse gehören zum Ereignis „Die Münze zeigt Kopf“?',
            formula='',
            correct='Die Münze zeigt nicht Kopf;Die Münze zeigt Zahl',
            wrong_1='Die Münze zeigt Kopf;Die Münze zeigt nicht Zahl',
        ),
        Question(
            instruction='Welche Gegenereignisse gehören zum Ereignis „Die Münze zeigt Kopf“?',
            formula='',
            correct='Die Münze zeigt Kopf;Die Münze zeigt nicht Zahl',
            wrong_1='Die Münze zeigt nicht Kopf;Die Münze zeigt Zahl',
        ),
        Question(
            instruction='Es wird mit einem gewöhnlichem Würfel geworfen. Was ist dazu ein sicheres Ereignis?',
            formula='',
            correct='Die Augenzahl ist kleiner als 7',
            wrong_1='Die Augenzahl ist gerade',
            wrong_2='Die Augenzahl ist größer als 2',
        ),
    ]
)

spezielle_ereignisse_draggroup = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Spezielle Ereignisse',
    instruction='',
    question_type='dragGroup',
    questions=[
        Question(
            instruction='In einem Behälter befinden sich {{v1}} Kugeln, die von 1 bis {{v1}} nummeriert sind. '
                        'Es wird eine Kugel gezogen. Entscheide, ob es sich bei den gegebenen '
                        'Ereignissen um sichere oder unmögliche Ereignisse handelt?',
            formula='',
            correct='sicheres Ereignis|Die Zahl auf der Kugel ist kleiner als {{v1+1}}~Die Zahl auf der Kugel ist eine natürliche Zahl '
                    'unmögliches Ereignis|Auf der Kugel steht eine {{v1+v2}}~Die Zahl auf der Kugel ist größer als {{v1+1}}',
            variables={
                'v1': (randint, 4, 7),
                'v2': (randint, 2, 4)
            }
        ),
    ]
)

spezielle_ereignisse_dragmatch = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Spezielle Ereignisse',
    instruction='',
    question_type='dragGroup',
    questions=[
        Question(
            instruction='Ein gewöhnlicher Würfel wird geworfen. Ordne jedem Ereignis sein Gegenereignis zu.',
            formula='',
            correct='Die Augenzahl ist kleiner als 4.|Die Augenzahl ist eine 4, 5 oder 6.;'
                    'Die Augenzahl ist durch 2 teilbar.|Die Augenzahl ist ungerade.;'
                    'Die Augenzahl ist eine 1 oder eine 2.|Die Augenzahl ist eine 3, 4, 5 oder 6.;'
                    'Die Augenzahl ist größer als 1.|Die Augenzahl ist genau 1.;'
                    'Die Augenzahl ist eine 6.|Die Augenzahl ist eine 1,2,3,4 oder 5.',
        ),
    ]
)

zufallsexperimente_draggroup = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Zufallsexperimente',
    instruction='Handelt es sich um ein Zufallsexperiment?',
    question_type='dragGroup',
    questions=[
        Question(
            formula='',
            correct='Zufallsexperiment|Mit einem gewöhnlichen Würfel würfeln~'
                    'Eine gewöhnliche Münze werfen~Ziehen eines Loses aus einem Hut;'
                    'kein Zufallsexperiment|Wette über den Wochentag am 01.01.2021~'
                    'Das Messen der Gefriertemperatur von Wasser',
        ),
        Question(
            instruction='Zufallsexperimente werden mithilfe von Zufallsgeräten durchgeführt. '
                        'Was könnten Zufallsgeräte sein?',
            formula='',
            correct='Zufallsgerät|Würfel~Münze~Kartenspiel;'
                    'kein Zufallsgerät|Taschenrechner~Taschenuhr~Thermometer',
        )
    ]
)

zufallsexperimente = QuestionSet(
    grade='7',
    capital='Wahrscheinlichkeit',
    subcapital='Zufallsexperimente',
    title='Zufallsexperimente',
    instruction='Überlege, was sinnvolle Eigenschaften eines Zufallsexperimentes sein können',
    question_type='MC',
    questions=[
        Question(
            formula='Ein Zufallsexperiment muss in der Theorie beliebig oft durchführbar sein.',
            correct='correct',
            wrong_1='wrong',
        ),
        Question(
            formula='Man weiß im Voraus, welches Ergebnis eintreten wird.',
            correct='wrong',
            wrong_1='correct',
        ),
        Question(
            formula='Es müssen mindestens zwei verschiedene Ergebnisse eintreten können.',
            correct='correct',
            wrong_1='wrong',
        ),
        Question(
            formula='Es können verschiedene Ergebnisse gleichzeitig eintreffen.',
            correct='wrong',
            wrong_1='correct',
        ),
    ]
)

kombinatorik_fakultaet = QuestionSet(
    grade='8',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeit',
    title='Kombinatorik und Fakultät',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Wähle die richtige Antwort aus.',
            formula='In einer Polit-Talkshow sollen {{numbers[v1]}} Gäste auf Sitzplätzen platziert werden. Wie viele Möglichkeiten gibt es, die Gäste anzuordnen?',
            correct='{{"%.0d"|format(get_fakultaet(v1))}}', # only the calculated field itself is surrounded by {{ }}, the variable v1 is passed normally
            wrong_1='{{"%.0d"|format(get_fakultaet(v1)/2)}}',
            wrong_2='{{v1**v1}}',
            hint='Da jeder Gast nur einen Platz benötigt, berechnet sich die Anzahl der Möglichkeiten wie folgt: <br> Beispielhaft gehen wir von 6 Gästen aus<mat>6! = 6*5*4*3*2*1 =720</mat>',
            variables={
                'v1': (randint, 2, 10),
                'get_fakultaet': get_fakultaet, # also need to pass the function in the variables, so jinja2 can substitute the string "get_fakultaet" with the actual function
                'numbers': numbers
            }
        ),
        
    ]
)

laplace_niete = QuestionSet(
    grade='8',
    capital='Wahrscheinlichkeit',
    subcapital='Wahrscheinlichkeit',
    title='Laplace Experimente (2)',
    instruction='',
    question_type='MC',
    questions=[
        Question(
            instruction='Wähle die richtige Antwort aus.',
            formula='Aus einer Box mit {{v1}} Hauptpreisen, {{v2}} zweiten Preisen, {{v4}} Trostpreisen und {{v3}} Nieten wird ein Los gezogen. '
                    'Was ist die Wahrscheinlichkeit vom Ereignis E=„Es wird eine Niete gezogen“?',
            correct='{{v3}}/{{"%.0d"|format(v1+v2+v3+v4)}}', # only the calculated field itself is surrounded by {{ }}, the variable v1 is passed normally
            wrong_1='{{v3-50}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            wrong_2='{{v3-75}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            hint='',
            variables={
                'v1': (randint, 5, 25),
                'v2': (choice, [30,40,50,60,70,80, 90, 100]),
                'v3': (randint, 650, 1050),
                'v4': (choice, [30,40,50,60,70,80, 90, 100]),
            }
        ),
        Question(
            instruction='Wähle die richtige Antwort aus.',
            formula='Aus einer Box mit {{v1}} Hauptpreisen, {{v2}} zweiten Preisen, {{v4}} Trostpreisen und {{v3}} Nieten wird ein Los gezogen. '
                    'Was ist die Wahrscheinlichkeit vom Ereignis E=„Es wird eine Trostpreis gezogen“?',
            correct='{{v4}}/{{"%.0d"|format(v1+v2+v3+v4)}}', # only the calculated field itself is surrounded by {{ }}, the variable v1 is passed normally
            wrong_1='{{v3-50}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            wrong_2='{{v3-75}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            hint='',
            variables={
                'v1': (randint, 5, 25),
                'v2': (choice, [30,40,50,60,70,80, 90, 100]),
                'v3': (randint, 650, 1050),
                'v4': (choice, [30,40,50,60,70,80, 90, 100]),
            }
        ),
        Question(
            instruction='Wähle die richtige Antwort aus.',
            formula='Aus einer Box mit {{v1}} Hauptpreisen, {{v2}} zweiten Preisen, {{v4}} Trostpreisen und {{v3}} Nieten wird ein Los gezogen. '
                    'Was ist die Wahrscheinlichkeit vom Ereignis E=„Es wird eine Hauptpreis gezogen“?',
            correct='{{v1}}/{{"%.0d"|format(v1+v2+v3+v4)}}', # only the calculated field itself is surrounded by {{ }}, the variable v1 is passed normally
            wrong_1='{{v3-50}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            wrong_2='{{v3-75}}/{{"%.0d"|format(v1+v2+v3+v4)}}',
            hint='',
            variables={
                'v1': (randint, 5, 25),
                'v2': (choice, [30,40,50,60,70,80, 90, 100]),
                'v3': (randint, 650, 1050),
                'v4': (choice, [30,40,50,60,70,80, 90, 100]),
            }
        ),
    ]
)

baumdiagramme_8 = QuestionSet(
    grade='8',
    capital='Wahrscheinlichkeit',
    subcapital='Baumdiagramme und Pfadregeln',
    title='Einführung Baumdiagramme',
    instruction='Wähle die richtige Antwort aus.',
    question_type='MC',
    questions=[
        Question(
            formula='Die Münze wird nun zweimal geworfen. Dabei spielt die Reihenfolge keine Rolle. Also ist es egal ob zuerst Kopf und dann Zahl oder umgekehrt geworfen wird. <br><br>'
                    'Wie sieht eine mögliche Ergebnismenge aus? '
                    'Der Einfachheit halber bezeichnet man jetzt das Ergebnis Kopf mit einem K und das Ergebnis Zahl mit einem Z.',
            correct='{{"{"}}KK;ZZ;KZ{{"}"}}',
            wrong_1='{{"{"}}K;Z;K;Z{{"}"}}',
            wrong_2='{{"{"}}KZ;ZK;KK{{"}"}}',
        ),
        Question(
            formula='Die Münze wird nun zweimal geworfen. Dabei spielt die Reihenfolge keine Rolle. Also ist es egal ob zuerst Kopf und dann Zahl oder umgekehrt geworfen wird. <br><br>'
                    'Wie viele mögliche Ergebnisse gibt es somit insgesamt? '
                    'Der Einfachheit halber bezeichnet man jetzt das Ergebnis Kopf mit einem K und das Ergebnis Zahl mit einem Z.',
            correct='3',
            wrong_1='2',
            wrong_2='4',
        )
    ]
)


# Add newly created question sets in that list, so the script can use them
question_sets = [
    laplace_niete,
    baumdiagramme_8,
    kombinatorik_fakultaet,
    baumdiagramme,
    pfadregel_1,
    ur_und_ranglisten_unterscheiden,
    ur_und_ranglisten_unterscheiden_dragsort,
    sachaufgaben_gap,
    sachaufgaben_mc,
    gemischte_aufgaben_dragmatch,
    gemischte_aufgaben,
    laplace_experimente_1,
    laplace_experimente_1_dragmatch,
    laplace_experimente_2,
    relative_haufigkeit_und_wahrscheinlichkeit_1_dragmatch,
    relative_haufigkeit_und_wahrscheinlichkeit_1_draggroup,
    relative_haufigkeit_und_wahrscheinlichkeit_2,
    ereignisse,
    ergebnissmengen,
    spezielle_ereignisse,
    spezielle_ereignisse_draggroup,
    spezielle_ereignisse_dragmatch,
    zufallsexperimente_draggroup,
    zufallsexperimente,
]
