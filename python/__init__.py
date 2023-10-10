from flask import Blueprint
import os

python = Blueprint(
    'python',
    __name__,
    template_folder="templates"
)

from . import routes
