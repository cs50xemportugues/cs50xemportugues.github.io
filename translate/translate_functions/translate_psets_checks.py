from .translate import translate
import os
from ..types import TypeCourse

def get_checks(course: TypeCourse):
    checks = [check for check in os.listdir(f'{course}/content/english/psets_checks')]
    return checks

def translate_psets_checks(course, language):
    checks = get_checks(course)
    translate(course, checks, "psets_checks", language, "py", "Python code")
