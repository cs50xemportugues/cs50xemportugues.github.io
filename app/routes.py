from flask import render_template
from . import app as bp
from flask import send_file, send_from_directory

@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('redirect.html')

@bp.route('/estilo')
@bp.route('/estilo.html')
def estilo():
    return render_template('estilo.html')
