from flask import Blueprint, render_template

manual_bp = Blueprint(
    'manual',
    __name__,
    template_folder='templates'
)

from . import routes