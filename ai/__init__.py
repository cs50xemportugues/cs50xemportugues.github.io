from flask import Blueprint
import os

ai = Blueprint(
    'ai',
    __name__,
    template_folder="templates"
)

from . import routes
