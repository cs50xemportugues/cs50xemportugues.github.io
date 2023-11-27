from flask import Blueprint
from .weeks import weeks_bp
from .psets import psets_bp
from .notes import notes_bp
import os

python = Blueprint(
    'python',
    __name__,
    template_folder="templates"
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
    "french": "problemas",
    "spanish": "problemas"
}

python.register_blueprint(weeks_bp, url_prefix=f"/{routes_weeks[os.environ['COURSE_LANGUAGE']]}")
python.register_blueprint(notes_bp, url_prefix=f"/{routes_notes[os.environ['COURSE_LANGUAGE']]}")
python.register_blueprint(psets_bp, url_prefix=f"/{routes_psets[os.environ['COURSE_LANGUAGE']]}")

from . import routes
