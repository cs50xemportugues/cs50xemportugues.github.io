from flask import Blueprint

psets_bp = Blueprint(
    'psets',
    __name__,
    template_folder='templates'
)

from . import routes