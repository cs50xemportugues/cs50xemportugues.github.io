'from cs50 import SQL

import check50
import re

@check50.check()
def existe():
    """import.py, roster.py existe"""
    check50.exists("import.py", "roster.py")
    check50.include("students.db", "students.csv")

@check50.check(existe)
def importar1():
    """import.py importa corretamente Harry Potter"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Harry'")
    expected = [{"first": "Harry", "middle": "James", "last": "Potter", "house": "Gryffindor", "birth": 1980}]
    if rows != expected:
        raise check50.Mismatch(str(expected), str(rows))

@check50.check(existe)
def importar2():
    """import.py importa corretamente Luna Lovegood"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    rows = db.execute("SELECT first, middle, last, house, birth FROM students WHERE first = 'Luna'")
    expected = [{"first": "Luna", "middle": None, "last": "Lovegood", "house": "Ravenclaw", "birth": 1981}]
    if rows != expected:
        raise check50.Mismatch(str(expected), str(rows))

@check50.check(existe)
def importar_contagem():
    """import.py importa a quantidade correta de linhas"""
    check50.run("python3 import.py students.csv").exit(timeout=10)
    db = SQL("sqlite:///students.db")
    actual = db.execute("SELECT COUNT(*) as count FROM students")[0]["count"]
    expected = 40
    if actual != expected:
        raise check50.Mismatch(str(expected), str(actual))

@check50.check(importar_contagem)
def roster_corvinal():
    """roster.py produz lista correta da casa Corvinal"""
    check50.include("corvinal.txt", "corvinal_re.txt")
    actual = check50.run("python3 roster.py Corvinal").stdout(timeout=10)
    if not re.search(open("corvinal_re.txt").read(), actual):
        raise check50.Mismatch(open("corvinal.txt").read(), actual)

@check50.check(importar_contagem)
def roster_grifinoria():
    """roster.py produz lista correta da casa Grifinória"""
    check50.include("grifinoria.txt", "grifinoria_re.txt")
    actual = check50.run("python3 roster.py Grifinória").stdout(timeout=10)
    if not re.search(open("grifinoria_re.txt").read(), actual):
        raise check50.Mismatch(open("grifinoria.txt").read(), actual)