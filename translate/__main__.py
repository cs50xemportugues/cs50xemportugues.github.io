import sys
from translate_functions.translate_notes import translate_notes
from translate_functions.translate_specifications import translate_specifications, translate_specifications_part1, translate_specifications_part2, translate_specifications_divided_part1, translate_specifications_divided_part2
from translate_functions.translate_psets import translate_psets
from translate_functions.translate_labs_code import translate_labs_code
from translate_functions.translate_psets_code import translate_psets_code
from translate_functions.translate_labs_checks import translate_labs_checks
from translate_functions.translate_psets_checks import translate_psets_checks
from translate_functions.translate_manual import translate_manual
from .types import TypeCourse, TypeLanguage, TypeContent
from .constants import COURSES, CONTENT_TYPES, LANGUAGES, NOTES, SPECIFICATIONS, MANUAL, PSETS, PSETS_CODE, LABS_CODE, PSETS_CHECKS, LABS_CHECKS

COURSE: TypeCourse = sys.argv[1]
CONTENT_TYPE: TypeContent = sys.argv[2]
LANGUAGE: TypeLanguage = sys.argv[3]

if len(sys.argv)!=4:
    print("Usage: python translate COURSE CONTENT_TYPE LANGUAGE")
    print("COURSE can be: ", COURSES)
    print("CONTENT_TYPE can be: ", CONTENT_TYPES)
    print("LANGUAGE can be: ", LANGUAGES)
    sys.exit()
elif not CONTENT_TYPE in COURSES:
    raise Exception("Error: Invalid course")
elif not CONTENT_TYPE in CONTENT_TYPES:
    raise Exception("Error: Invalid content type")
elif not LANGUAGE in LANGUAGES:
    raise Exception("Error: Invalid language")
else:
    if CONTENT_TYPE == PSETS:
        translate_psets(LANGUAGE)
    elif CONTENT_TYPE == PSETS_CODE:
        translate_psets_code(LANGUAGE)
    elif CONTENT_TYPE == PSETS_CHECKS:
        translate_psets_checks(COURSE, LANGUAGE)
    elif CONTENT_TYPE == LABS_CODE:
        translate_labs_code(LANGUAGE)
    elif CONTENT_TYPE == LABS_CHECKS:
        translate_labs_checks(LANGUAGE)
    elif CONTENT_TYPE == NOTES:
        translate_notes(LANGUAGE)
    elif CONTENT_TYPE == MANUAL:
        translate_manual(LANGUAGE)
    elif CONTENT_TYPE == SPECIFICATIONS:
        translate_specifications(LANGUAGE)
        translate_specifications_part1(LANGUAGE)
        translate_specifications_part2(LANGUAGE)
        translate_specifications_divided_part1(LANGUAGE)
        translate_specifications_divided_part2(LANGUAGE)
