from .translate import translate
from ..constants import LABS_CODE

def translate_labs_code(language):
    code = ["inheritance", "scrabble", "volume"]
    translate(code, LABS_CODE, language, "c", "C code")
   