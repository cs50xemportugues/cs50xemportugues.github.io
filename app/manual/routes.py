from flask import Blueprint, render_template
from . import manual_bp as bp
import marko
import os
from markdown import markdown

def markdown_convert(content):
    return markdown(content, extensions=['tables'], output_format='html')


@bp.route('/')
@bp.route('/index.html')
def manual():
    return render_template(f'{os.environ["COURSE_LANGUAGE"]}/manual/index.html')

f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html'
# cs50.h
@bp.route('/get_char')
@bp.route('/get_char.html')
def get_char():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_char.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/get_double')
@bp.route('/get_double.html')
def get_double():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_double.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/get_float')
@bp.route('/get_float.html')
def get_float():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_float.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/get_int')
@bp.route('/get_int.html')
def get_int():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_int.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/get_long')
@bp.route('/get_long.html')
def get_long():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_long.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/get_string')
@bp.route('/get_string.html')
def get_string():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/get_string.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# ctype.h

@bp.route('/isalnum')
@bp.route('/isalnum.html')
def isalnum():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isalnum.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/isalpha')
@bp.route('/isalpha.html')
def isalpha():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isalpha.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/isblank')
@bp.route('/isblank.html')
def isblank():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isblank.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/isdigit')
@bp.route('/isdigit.html')
def isdigit():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isdigit.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/islower')
@bp.route('/islower.html')
def islower():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/islower.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/ispunct')
@bp.route('/ispunct.html')
def ispunct():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/ispunct.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/isspace')
@bp.route('/isspace.html')
def isspace():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isspace.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/isupper')
@bp.route('/isupper.html')
def isupper():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/isupper.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/tolower')
@bp.route('/tolower.html')
def tolower():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/tolower.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/toupper')
@bp.route('/toupper.html')
def toupper():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/toupper.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# math.h

@bp.route('/ceil')
@bp.route('/ceil.html')
def ceil():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/ceil.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/floor')
@bp.route('/floor.html')
def floor():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/floor.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/log2')
@bp.route('/log2.html')
def log2():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/log2.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/pow')
@bp.route('/pow.html')
def pow():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/pow.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/round')
@bp.route('/round.html')
def round():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/round.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/sqrt')
@bp.route('/sqrt.html')
def sqrt():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/sqrt.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# stdio.h

@bp.route('/fclose')
@bp.route('/fclose.html')
def fclose():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fclose.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/fopen')
@bp.route('/fopen.html')
def fopen():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fopen.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/fprintf')
@bp.route('/fprintf.html')
def fprintf():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fprintf.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/fread')
@bp.route('/fread.html')
def fread():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fread.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/fscanf')
@bp.route('/fscanf.html')
def fscanf():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fscanf.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/fwrite')
@bp.route('/fwrite.html')
def fwrite():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/fwrite.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/printf')
@bp.route('/printf.html')
def printf():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/printf.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/scanf')
@bp.route('/scanf.html')
def scanf():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/scanf.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/sprintf')
@bp.route('/sprintf.html')
def sprintf():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/sprintf.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# stdlib.h

@bp.route('/atof')
@bp.route('/atof.html')
def atof():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/atof.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/atoi')
@bp.route('/atoi.html')
def atoi():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/atoi.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/atol')
@bp.route('/atol.html')
def atol():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/atol.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/free')
@bp.route('/free.html')
def free():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/free.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/malloc')
@bp.route('/malloc.html')
def malloc():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/malloc.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/random')
@bp.route('/random.html')
def random():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/random.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/realloc')
@bp.route('/realloc.html')
def realloc():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/realloc.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/srandom')
@bp.route('/srandom.html')
def srandom():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/srandom.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# string.h

@bp.route('/strcasestr')
@bp.route('/strcasestr.html')
def strcasestr():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strcasestr.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/strcmp')
@bp.route('/strcmp.html')
def strcmp():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strcmp.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/strcpy')
@bp.route('/strcpy.html')
def strcpy():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strcpy.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/strlen')
@bp.route('/strlen.html')
def strlen():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strlen.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

@bp.route('/strstr')
@bp.route('/strstr.html')
def strstr():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strstr.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# strings.h

@bp.route('/strcasecmp')
@bp.route('/strcasecmp.html')
def strcasecmp():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/strcasecmp.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

# time.h

@bp.route('/time')
@bp.route('/time.html')
def time():
    with open(f"app/content/{os.environ['COURSE_LANGUAGE']}/manual/time.md", "r") as f:
        markdown_text = f.read()
        
    return render_template(
        f'{os.environ["COURSE_LANGUAGE"]}/manual/blank.html',
        markdown_text=markdown_convert(markdown_text)
    )

