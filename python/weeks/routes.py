import os
from flask import Blueprint, render_template
from . import weeks_bp as bp

from cs50x.content.english.language import (
    week_page as english_week_page,
    week_0 as english_week_0,
    week_1 as english_week_1,
    week_2 as english_week_2,
    week_3 as english_week_3,
    week_4 as english_week_4,
    week_5 as english_week_5,
    week_6 as english_week_6,
    week_7 as english_week_7,
    week_8 as english_week_8,
    week_9 as english_week_9,
    week_10 as english_week_10,
    cibersecurity as english_cibesecurity
)


from cs50x.content.spanish.language import (
    week_page as spanish_week_page,
    week_0 as spanish_week_0,
    week_1 as spanish_week_1,
    week_2 as spanish_week_2,
    week_3 as spanish_week_3,
    week_4 as spanish_week_4,
    week_5 as spanish_week_5,
    week_6 as spanish_week_6,
    week_7 as spanish_week_7,
    week_8 as spanish_week_8,
    week_9 as spanish_week_9,
    week_10 as spanish_week_10,
    cibersecurity as spanish_cibesecurity
)

from cs50x.content.portuguese.language import (
    week_page as portuguese_week_page,
    week_0 as portuguese_week_0,
    week_1 as portuguese_week_1,
    week_2 as portuguese_week_2,
    week_3 as portuguese_week_3,
    week_4 as portuguese_week_4,
    week_5 as portuguese_week_5,
    week_6 as portuguese_week_6,
    week_7 as portuguese_week_7,
    week_8 as portuguese_week_8,
    week_9 as portuguese_week_9,
    week_10 as portuguese_week_10,
    cibersecurity as portuguese_cibesecurity
)

from cs50x.content.french.language import (
    week_page as french_week_page,
    week_0 as french_week_0,
    week_1 as french_week_1,
    week_2 as french_week_2,
    week_3 as french_week_3,
    week_4 as french_week_4,
    week_5 as french_week_5,
    week_6 as french_week_6,
    week_7 as french_week_7,
    week_8 as french_week_8,
    week_9 as french_week_9,
    week_10 as french_week_10,
    cibersecurity as french_cibesecurity
)

from cs50x.content.spanish.language import (
    week_page as spanish_week_page,
    week_0 as spanish_week_0,
    week_1 as spanish_week_1,
    week_2 as spanish_week_2,
    week_3 as spanish_week_3,
    week_4 as spanish_week_4,
    week_5 as spanish_week_5,
    week_6 as spanish_week_6,
    week_7 as spanish_week_7,
    week_8 as spanish_week_8,
    week_9 as spanish_week_9,
    week_10 as spanish_week_10,
    cibersecurity as spanish_cibesecurity
)

if os.environ["COURSE_LANGUAGE"] == "portuguese":
    weeks_content = {
        "week_page": portuguese_week_page,
        "week0": portuguese_week_0,
        "week1": portuguese_week_1,
        "week2": portuguese_week_2,
        "week3": portuguese_week_3,
        "week4": portuguese_week_4,
        "week5": portuguese_week_5,
        "week6": portuguese_week_6,
        "week7": portuguese_week_7,
        "week8": portuguese_week_8,
        "week9": portuguese_week_9,
        "week10": portuguese_week_10,
        "cibersecurity": portuguese_cibesecurity,
    }
elif os.environ["COURSE_LANGUAGE"] == "spanish":
    weeks_content = {
        "week_page": spanish_week_page,
        "week0": spanish_week_0,
        "week1": spanish_week_1,
        "week2": spanish_week_2,
        "week3": spanish_week_3,
        "week4": spanish_week_4,
        "week5": spanish_week_5,
        "week6": spanish_week_6,
        "week7": spanish_week_7,
        "week8": spanish_week_8,
        "week9": spanish_week_9,
        "week10": spanish_week_10,
        "cibersecurity": spanish_cibesecurity,
    }
elif os.environ["COURSE_LANGUAGE"] == "french":
    weeks_content = {
        "week_page": french_week_page,
        "week0": french_week_0,
        "week1": french_week_1,
        "week2": french_week_2,
        "week3": french_week_3,
        "week4": french_week_4,
        "week5": french_week_5,
        "week6": french_week_6,
        "week7": french_week_7,
        "week8": french_week_8,
        "week9": french_week_9,
        "week10": french_week_10,
        "cibersecurity": french_cibesecurity,
    }
elif os.environ["COURSE_LANGUAGE"] == "english":
    weeks_content = {
        "week_page": english_week_page,
        "week0": english_week_0,
        "week1": english_week_1,
        "week2": english_week_2,
        "week3": english_week_3,
        "week4": english_week_4,
        "week5": english_week_5,
        "week6": english_week_6,
        "week7": english_week_7,
        "week8": english_week_8,
        "week9": english_week_9,
        "week10": english_week_10,
        "cibersecurity": english_cibesecurity,
    }
    
weeks_content = {
    "week_page": portuguese_week_page,
    "week0": portuguese_week_0,
    "week1": portuguese_week_1,
    "week2": portuguese_week_2,
    "week3": portuguese_week_3,
    "week4": portuguese_week_4,
    "week5": portuguese_week_5,
    "week6": portuguese_week_6,
    "week7": portuguese_week_7,
    "week8": portuguese_week_8,
    "week9": portuguese_week_9,
    "week10": portuguese_week_10,
    "cibersecurity": portuguese_cibesecurity,
}

@bp.route('/')
@bp.route('/index.html')
def weeks():
    return render_template('weeks/index.html')


@bp.route('/0')
@bp.route('/0.html')
def week0():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week0"]
    )


@bp.route('/1')
@bp.route('/1.html')
def week1():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week1"]
    )


@bp.route('/2')
@bp.route('/2.html')
def week2():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week2"]
    )


@bp.route('/3')
@bp.route('/3.html')
def week3():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week3"]
    )


@bp.route('/4')
@bp.route('/4.html')
def week4():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week4"]
    )


@bp.route('/5')
@bp.route('/5.html')
def week5():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week5"]
    )


@bp.route('/6')
@bp.route('/6.html')
def week6():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week6"]
    )


@bp.route('/7')
@bp.route('/7.html')
def week7():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week7"]
    )


@bp.route('/8')
@bp.route('/8.html')
def week8():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week8"]
    )


@bp.route('/9')
@bp.route('/9.html')
def week9():
    return render_template(
        'weeks/layout.html',
        week_page=weeks_content["week_page"],
        week=weeks_content["week9"]
    )
