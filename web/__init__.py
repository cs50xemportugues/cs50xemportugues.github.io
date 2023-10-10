from flask import Blueprint
import os

web = Blueprint(
    'web',
    __name__,
    template_folder="templates"
)

from . import routes
