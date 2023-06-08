from flask import Blueprint, render_template
from . import psets_bp as bp
import marko
import os
from flask import current_app

@bp.route('/')
@bp.route('/index.html')
def psets():
    return render_template('psets/index.html')

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
    print(current_app.config["URLS"]["hello"])
    
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

@bp.route('/1/mario/mais/')
@bp.route('/1/mario/mais.html')
def mario_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/1/dinheiro/')
@bp.route('/1/dinheiro.html')
def cash():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/1/credito/')
@bp.route('/1/credito.html')
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


@bp.route('/2/legibilidade/')
@bp.route('/2/legibilidade.html')
def readability():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/2/bulbs/')
@bp.route('/2/bulbs.html')
def bulbs():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/bulbs.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )


@bp.route('/2/cesar/')
@bp.route('/2/cesar.html')
def caesar():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/caesar.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )



@bp.route('/2/substituicao/')
@bp.route('/2/substituicao.html')
def substitution():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/substitution.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/2/wordle50/')
@bp.route('/2/wordle50.html')
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

@bp.route('/3/pluralidade/')
@bp.route('/3/pluralidade.html')
def plurality():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/plurality.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/3/preferencia/')
@bp.route('/3/preferencia.html')
def runoff():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/runoff.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/3/pares_ranqueados/')
@bp.route('/3/pares_ranqueados.html')
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

@bp.route('/4/filtro/menos/')
@bp.route('/4/filtro/menos.html')
def filter_less():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/4/filtro/mais/')
@bp.route('/4/filtro/mais.html')
def filter_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/filter_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/4/recuperar/')
@bp.route('/4/recuperar.html')
def recover():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/recover.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/4/reverse/')
@bp.route('/4/reverse.html')
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
    

@bp.route('/5/corretor/')
@bp.route('/5/corretor.html')
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

@bp.route('/6/ola/')
@bp.route('/6/ola.html')
def python_hello():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_hello.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
 
@bp.route('/6/mario/menos/')
@bp.route('/6/mario/menos.html')
def python_mario_less():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_less.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6/mario/mais/')
@bp.route('/6/mario/mais.html')
def python_mario_more():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_mario_more.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6/dinheiro/')
@bp.route('/6/dinheiro.html')
def python_cash():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_cash.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6/credito/')
@bp.route('/6/credito.html')
def python_credit():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_credit.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6/legibilidade/')
@bp.route('/6/legibilidade.html')
def python_readability():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/python_readability.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

@bp.route('/6/dna/')
@bp.route('/6/dna.html')
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

   
@bp.route('/7/filmes/')
@bp.route('/7/filmes.html')
def movies():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/movies.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )

   
@bp.route('/7/vila_cinquenta/')
@bp.route('/7/vila_cinquenta.html')
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
    
   
@bp.route('/8/pagina_inicial/')
@bp.route('/8/pagina_inicial.html')
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

@bp.route('/9/financas/')
@bp.route('/9/financas.html')
def finance():
    with open(f"cs50x/content/{os.environ['COURSE_LANGUAGE']}/specifications/finance.md", "r") as f:
        markdown_text = f.read()

    return render_template(
        'blank.html',
        markdown_text=marko.convert(markdown_text)
    )
   



