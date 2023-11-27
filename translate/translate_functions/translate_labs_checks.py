from .translate import translate
import os
from ..types import TypeCourse
from ..constants import LABS_CHECKS

def get_checks(course: TypeCourse):
    checks = [check for check in os.listdir(f'{course}/content/english/{LABS_CHECKS}')]
    return checks

def translate_labs_checks(course, language):
    checks = get_checks(course)
    translate(course, checks, LABS_CHECKS, language, "py", "Python code")
