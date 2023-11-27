import verificar50
import verificar50.c


@verificar50.verificar()
def existe():
    """helpers.c existe"""
    verificar50.existe("helpers.c")
    verificar50.incluir("Makefile", "bmp.h", "helpers.h", "colorize.c", "smiley.bmp")


@verificar50.verificar(existe)
def compila():
    """colorize compila"""
    verificar50.c.compilar("colorize.c", "helpers.c", lcs50=True)


@verificar50.verificar(compila)
def testar_criacao_imagem():
    """colorize cria uma imagem"""
    verificar50.executar("./colorize smiley.bmp smiley_out.bmp").exit(0)
    verificar50.existe("smiley_out.bmp")


@verificar50.verificar(testar_criacao_imagem)
def cor_diferente():
    """colorize muda as cores da imagem"""
    verificar50.executar("./colorize smiley.bmp smiley_out.bmp")
    if verificar50.hash("smiley_out.bmp") == "1c137ffd2d7adeae0f22e00136d187f6237a4128e2dd8a413c8f9372db673a05":
        raise verificar50.Falha("colorize não mudou a imagem")