from flask import Blueprint, render_template
from . import psets_bp as bp
import marko
import os
from flask import current_app


@bp.route('/')
@bp.route('/index.html')
def psets():
   return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/index.html',
    )

#############################################################################
#############################################################################
#############################################################################

@bp.route('/0')
@bp.route('/0.html')
def pset0():
   return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/0.html',
    )

@bp.route('/0/scratch/')
@bp.route('/0/scratch.html')
def scratch():

    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/scratch.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################


@bp.route('/1')
@bp.route('/1.html')
def pset1():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/1.html',
    )


@bp.route(f"/1/hello/")
@bp.route(f"/1/hello.html")
def hello():
    
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/hello.md", "r") as f:
        markdown_text = f.read()
    
    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


@bp.route(f"/1/mario/less/")
@bp.route(f"/1/mario/less.html")
def mario_less():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/mario_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/mario/more/")
@bp.route(f"/1/mario/more.html")
def mario_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/cash/")
@bp.route(f"/1/cash.html")
def cash():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/1/credit/")
@bp.route(f"/1/credit.html")
def credit():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/credit.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################



@bp.route('/2')
@bp.route('/2.html')
def pset2():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/2.html',
    )


@bp.route(f"/2/readability/")
@bp.route(f"/2/readability.html")
def readability():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/2/bulbs/")
@bp.route(f"/2/bulbs.html")
def bulbs():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/bulbs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


@bp.route(f"/2/caesar/")
@bp.route(f"/2/caesar.html")
def caesar():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/caesar.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )



@bp.route(f"/2/substitution/")
@bp.route(f"/2/substitution.html")
def substitution():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/substitution.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/2/wordle50/")
@bp.route(f"/2/wordle50.html")
def wordle50():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/wordle50.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################


@bp.route('/3')
@bp.route('/3.html')
def pset3():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/3.html',
    )

@bp.route(f"/3/plurality/")
@bp.route(f"/3/plurality.html")
def plurality():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/plurality.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/3/runoff/")
@bp.route(f"/3/runoff.html")
def runoff():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/runoff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/3/tideman/")
@bp.route(f"/3/tideman.html")
def tideman():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/tideman.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################


@bp.route('/4')
@bp.route('/4.html')
def pset4():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/4.html',
    )

@bp.route(f"/4/filter/less/")
@bp.route(f"/4/filter/less.html")
def filter_less():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/filter/more/")
@bp.route(f"/4/filter/more.html")
def filter_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/recover/")
@bp.route(f"/4/recover.html")
def recover():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/recover.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/4/reverse/")
@bp.route(f"/4/reverse.html")
def reverse():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/reverse.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

#############################################################################
#############################################################################
#############################################################################


@bp.route('/5')
@bp.route('/5.html')
def pset5():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/5.html',
    )
    

@bp.route(f"/5/speller/")
@bp.route(f"/5/speller.html")
def speller():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/speller.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################


@bp.route('/6')
@bp.route('/6.html')
def pset6():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/6.html',
    )

@bp.route(f"/6/hello/")
@bp.route(f"/6/hello.html")
def python_hello():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_hello.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
 
@bp.route(f"/6/mario/less/")
@bp.route(f"/6/mario/less.html")
def python_mario_less():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/mario/more/")
@bp.route(f"/6/mario/more.html")
def python_mario_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/cash/")
@bp.route(f"/6/cash.html")
def python_cash():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/credit/")
@bp.route(f"/6/credit.html")
def python_credit():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_credit.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/readability/")
@bp.route(f"/6/readability.html")
def python_readability():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/6/dna/")
@bp.route(f"/6/dna.html")
def dna():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/dna.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


#############################################################################
#############################################################################
#############################################################################


@bp.route('/7')
@bp.route('/7.html')
def pset7():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/7.html',
    )

@bp.route(f"/7/movies/")
@bp.route(f"/7/movies.html")
def movies():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/movies.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route(f"/7/fiftyville/")
@bp.route(f"/7/fiftyville.html")
def fiftyville():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/fiftyville.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
   

#############################################################################
#############################################################################
#############################################################################


@bp.route('/8/')
@bp.route('/8.html')
def pset8():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/8.html',
    )
    
   
@bp.route(f"/8/homepage/")
@bp.route(f"/8/homepage.html")
def homepage():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/homepage.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
   

#############################################################################
#############################################################################
#############################################################################


@bp.route('/9')
@bp.route('/9.html')
def pset9():
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/psets/9.html',
    )

@bp.route(f"/9/finance/")
@bp.route(f"/9/finance.html")
def finance():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/finance.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
