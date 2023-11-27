from .translate import translate
import os
from ..types import TypeCourse, TypeLanguage

def get_notes(course: TypeCourse):
    notes = [note for note in os.listdir(f'{course}/content/english/notes')]
    return notes

def translate_notes(course: TypeCourse, language: TypeLanguage):
    notes = get_notes(course)
    translate(course, notes, "notes", language, "md", "Markdown file")