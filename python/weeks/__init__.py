from flask import Blueprint, render_template

weeks_bp = Blueprint(
    'weeks',
    __name__,
    template_folder='templates'
)

from . import routes