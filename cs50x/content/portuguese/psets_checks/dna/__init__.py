import check50

@check50.check()
def existe():
    """dna.py existe"""
    check50.exists("dna.py")
    check50.include("sequences", "databases")

@check50.check(existe)
def teste1():
    """identifica corretamente sequences/1.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/1.txt").stdout("^Bob", "Bob\n", timeout=5).exit()

@check50.check(existe)
def teste2():
    """identifica corretamente sequences/2.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/2.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(existe)
def teste3():
    """identifica corretamente sequences/3.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/3.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(existe)
def teste4():
    """identifica corretamente sequences/4.txt"""
    check50.run("python3 dna.py databases/small.csv sequences/4.txt").stdout("^Alice", "Alice\n", timeout=5).exit()

@check50.check(existe)
def teste5():
    """identifica corretamente sequences/5.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/5.txt").stdout("^Lavender", "Lavender\n", timeout=5).exit()

@check50.check(existe)
def teste6():
    """identifica corretamente sequences/6.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/6.txt").stdout("^Luna", "Luna\n", timeout=5).exit()

@check50.check(existe)
def teste7():
    """identifica corretamente sequences/7.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/7.txt").stdout("^Ron", "Ron\n", timeout=5).exit()

@check50.check(existe)
def teste8():
    """identifica corretamente sequences/8.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/8.txt").stdout("^Ginny", "Ginny\n", timeout=5).exit()

@check50.check(existe)
def teste9():
    """identifica corretamente sequences/9.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/9.txt").stdout("^Draco", "Draco\n", timeout=5).exit()

@check50.check(existe)
def teste10():
    """identifica corretamente sequences/10.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/10.txt").stdout("^Albus", "Albus\n", timeout=5).exit()

@check50.check(existe)
def teste11():
    """identifica corretamente sequences/11.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/11.txt").stdout("^Hermione", "Hermione\n", timeout=5).exit()

@check50.check(existe)
def teste12():
    """identifica corretamente sequences/12.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/12.txt").stdout("^Lily", "Lily\n", timeout=5).exit()

@check50.check(existe)
def teste13():
    """identifica corretamente sequences/13.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/13.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(existe)
def teste14():
    """identifica corretamente sequences/14.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/14.txt").stdout("^Severus", "Severus\n", timeout=5).exit()

@check50.check(existe)
def teste15():
    """identifica corretamente sequences/15.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/15.txt").stdout("^Sirius", "Sirius\n", timeout=5).exit()

@check50.check(existe)
def teste16():
    """identifica corretamente sequences/16.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/16.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(existe)
def teste17():
    """identifica corretamente sequences/17.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/17.txt").stdout("^Harry", "Harry\n", timeout=5).exit()

@check50.check(existe)
def teste18():
    """identifica corretamente sequences/18.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/18.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()

@check50.check(existe)
def teste19():
    """identifica corretamente sequences/19.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/19.txt").stdout("^Fred", "Fred\n", timeout=5).exit()

@check50.check(existe)
def teste20():
    """identifica corretamente sequences/20.txt"""
    check50.run("python3 dna.py databases/large.csv sequences/20.txt").stdout("^[Nn]o [Mm]atch\.?\n", "No match\n", timeout=5).exit()