from flask import render_template
from . import app as bp
from flask import send_file, send_from_directory

@bp.route('/')
@bp.route('/index.html')
def index():
    return render_template('redirect.html')

@bp.route('/estilo')
@bp.route('/estilo.html')
def manual():
    return render_template('estilo.html')

@bp.route('/download/<path:filename>')
@bp.route('/download/<path:filename>.html')
def return_file(filename):
	try:
		return send_from_directory("download_files", filename, as_attachment=True)
	except Exception as e:
		return str(e)