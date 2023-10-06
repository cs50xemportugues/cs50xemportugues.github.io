from flask import Blueprint
from .manual import manual_bp

app = Blueprint(
    'app',
    __name__,
    template_folder='templates'
)

app.register_blueprint(manual_bp, url_prefix="/manual")

from . import routes
