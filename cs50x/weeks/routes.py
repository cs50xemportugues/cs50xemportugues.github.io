from flask import Blueprint, render_template
from . import weeks_bp as bp
from cs50x.content.english.language import week_0, week_page, week_1, week_2, week_3, week_4, week_5, week_6, week_7, week_8, week_9, week_10, cibersecurity



@bp.route('/')
@bp.route('/index.html')
def weeks():
    return render_template('weeks/index.html')


@bp.route('/0')
@bp.route('/0.html')
def week0():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_0
    )


@bp.route('/1')
@bp.route('/1.html')
def week1():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_1
    )


@bp.route('/2')
@bp.route('/2.html')
def week2():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_2
    )


@bp.route('/3')
@bp.route('/3.html')
def week3():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_3
    )


@bp.route('/4')
@bp.route('/4.html')
def week4():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_4
    )


@bp.route('/5')
@bp.route('/5.html')
def week5():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_5
    )


@bp.route('/6')
@bp.route('/6.html')
def week6():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_6
    )


@bp.route('/7')
@bp.route('/7.html')
def week7():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_7
    )


@bp.route('/8')
@bp.route('/8.html')
def week8():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_8
    )


@bp.route('/9')
@bp.route('/9.html')
def week9():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=week_9
    )

@bp.route('/10')
@bp.route('/10.html')
def week10():
    return render_template('weeks/10.html', week_page=week_page,
        week=week_10)

@bp.route('/ciberseguranca')
@bp.route('/ciberseguranca.html')
def cybersecurity():
    return render_template(
        'weeks/layout.html',
        week_page=week_page,
        week=cibersecurity
    )