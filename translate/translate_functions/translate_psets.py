from .translate import translate

def translate_psets(language):
    psets = ["2", "3", "4", "5", "6", "7", "8", "9"]
    translate(psets, "psets", language, "html", "HTML file")
