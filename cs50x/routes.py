from flask import render_template
from . import cs50x as bp
import os
import marko


@bp.route('/')
@bp.route('/index.html')
def index():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'index.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/honestidade')
@bp.route('/honestidade.html')
def honesty():
        
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/honesty.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/perguntas_frequentes')
@bp.route('/perguntas_frequentes.html')
def faqs():
        
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/faqs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/certificado')
@bp.route('/certificado.html')
def certificate():
        
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/certificate.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/curriculo')
@bp.route('/curriculo.html')
def syllabus():

    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/syllabus.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/equipe')
@bp.route('/equipe.html')
def staff():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/staff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/obrigado')
@bp.route('/obrigado.html')
def thanks():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/thanks.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/seminarios')
@bp.route('/seminarios.html')
def seminars():

    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/seminars.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/projeto_final')
@bp.route('/projeto_final.html')
def project():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/project.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/secoes')
@bp.route('/secoes.html')
def sections():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/sections.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/tutorias')
@bp.route('/tutorias.html')
def office_hours():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/office_hours.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

