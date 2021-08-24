from definitions.funktionen_questions import question_sets as funktionen_question_sets
from definitions.terme_questions import question_sets as terme_question_sets
from definitions.gleichungen_questions import question_sets as gleichungen_question_sets
from definitions.prozente_zinzen_questons import question_sets as prozente_question_sets
from definitions.wahrscheinlichkeit_questions import question_sets as wahrscheinlichkeit_question_sets
from definitions.rationale_zahlen_questions import question_sets as rationale_zahlen_question_sets
from definitions.zuordnungen_questions import question_sets as zuordnungen_question_sets

question_sets = [
    *prozente_question_sets,
    *wahrscheinlichkeit_question_sets,
    *terme_question_sets,
    *funktionen_question_sets,
    *gleichungen_question_sets,
    *rationale_zahlen_question_sets,
    *zuordnungen_question_sets,
]
