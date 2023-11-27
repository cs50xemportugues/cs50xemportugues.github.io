from flask import render_template
from . import app as bp
import os
import marko

@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('redirect.html')

@bp.route('/estilo')
@bp.route('/estilo.html')
def estilo():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/style.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
