from flask import Blueprint
from .weeks import weeks_bp
from .psets import psets_bp
from .notes import notes_bp
from .labs import labs_bp
import os

cs50x = Blueprint(
    'cs50x',
    __name__,
    template_folder='templates'
)

routes_weeks = {
    "english": "weeks",
    "portuguese": "semanas",
    "french": "semaines",
    "spanish": "semanas"
}

routes_notes = {
    "english": "notes",
    "portuguese": "anotacoes",
    "french": "notes",
    "spanish": "notas"
}

routes_psets = {
    "english": "psets",
    "portuguese": "problemas",
    "french": "problemes",
    "spanish": "problemas"
}

routes_labs = {
    "english": "labs",
    "portuguese": "laboratorios",
    "french": "laboratoires",
    "spanish": "laboratorios"
}


cs50x.register_blueprint(weeks_bp, url_prefix=f"/{routes_weeks[os.environ['COURSE_LANGUAGE']]}")
cs50x.register_blueprint(notes_bp, url_prefix=f"/{routes_notes[os.environ['COURSE_LANGUAGE']]}")
cs50x.register_blueprint(psets_bp, url_prefix=f"/{routes_psets[os.environ['COURSE_LANGUAGE']]}")
cs50x.register_blueprint(labs_bp, url_prefix=f"/{routes_labs[os.environ['COURSE_LANGUAGE']]}")

from . import routes