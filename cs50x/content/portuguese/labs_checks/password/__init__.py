importa check50
importa check50.c


@check50.check()
def existe():
    """password.c existe"""
    check50.exists("password.c")


@check50.check(existe)
def compila():
    """password.c compila"""
    check50.c.compile("password.c", lcs50=True)


@check50.check(compila)
def valido():
    """Senha 3PQvbQ6_GvneW!3R é aceita."""
    checa_senha(senha="3PQvbQ6_GvneW!3R", valido=True)


@check50.check(compila)
def sem_maiuscula():
    """Senha hqsk3wb. é rejeitada por falta de caracteres maiúsculos."""
    checa_senha(senha="hqsk3wb.", valido=False)


@check50.check(compila)
def sem_minuscula():
    """Senha F-WH8PQP é rejeitada por falta de caracteres minúsculos."""
    checa_senha(senha="F-WH8PQP", valido=False)


@check50.check(compila)
def sem_simbolo():
    """Senha VnrHMtV4 é rejeitada por falta de símbolos."""
    checa_senha(senha="VnrHMtV4", valido=False)


@check50.check(compila)
def sem_numero():
    """Senha iWnktW*q é rejeitada por falta de números."""
    checa_senha(senha="iWnktW*q", valido=False)


# Funções auxiliares
def checa_senha(senha: str, valido: bool):
    programa = check50.run("./password").stdin(senha)
    if valido:
        programa.stdout("Sua senha é válida!")
    else:
        programa.stdout("Sua senha precisa ter pelo menos uma letra maiúscula, uma letra minúscula, um número e um símbolo")