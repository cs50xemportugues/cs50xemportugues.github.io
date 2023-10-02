from flask import Blueprint, render_template
from . import labs_bp as bp
import os
import marko

@bp.route('/1')
@bp.route('/1.html')
def lab1():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/population.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/2')
@bp.route('/2.html')
def lab2():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/scrabble.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
@bp.route('/3')
@bp.route('/3.html')
def lab3():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/sort.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/4')
@bp.route('/4.html')
def lab4():
    return render_template('labs/4.html')

@bp.route('/4/smiley')
@bp.route('/4/smiley.html')
def smiley():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/smiley.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/4/volume')
@bp.route('/4/volume.html')
def volume():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/volume.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/5')
@bp.route('/5.html')
def lab5():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/inheritance.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6')
@bp.route('/6.html')
def lab6():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/worldcup.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/7')
@bp.route('/7.html')
def lab7():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/songs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/8')
@bp.route('/8.html')
def lab8():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/trivia.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/9')
@bp.route('/9.html')
def lab9():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/birthdays.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

