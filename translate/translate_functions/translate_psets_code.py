from .translate import translate
from ..files_names.text.psets_code import psets_code

def translate_psets_code(language):
    translate(psets_code, "psets_code", language, "c", "C language code")
