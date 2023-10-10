from flask import render_template
from . import web as bp
import os
import marko

@bp.route('/')
@bp.route('/index.html')
def index():
    with open(f"web/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'web/index.html',
        markdown_text=marko.convert(markdown_text)
    )