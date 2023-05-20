from flask import Blueprint, render_template

labs_bp = Blueprint(
    'labs',
    __name__,
    template_folder='templates'
)

from . import routes