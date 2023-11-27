import check50
import check50.c


@check50.check()
def existe():
    """reverse.c existe"""
    check50.include("input.wav")
    check50.include("wav.h")
    check50.exists("reverse.c")


@check50.check(existe)
def compila():
    """reverse.c compila"""
    check50.c.compile("reverse.c", lcs50=True)


@check50.check(compila)
def testar_sem_arquivo():
    """reverse.c lida com falta de arquivo de entrada"""
    check50.run("./reverse").exit(1)


@check50.check(compila)
def testar_arquivo_saida():
    """reverse.c cria um arquivo de saída"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    check50.exists("output.wav")


@check50.check(testar_arquivo_saida)
def testar_cabecalho():
    """reverse.c escreve cabeçalho WAV no arquivo de saída"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    with open("output.wav", "rb") as f:
        f.seek(8)
        for b in [b'W', b'A', b'V', b'E']:
            if f.read(1) != b:
                raise check50.Failure("o arquivo de saída não possui assinatura de arquivo WAV")


@check50.check(testar_cabecalho)
def testar_inverte_audio():
    """reverse.c inverte a escala ascendente"""
    check50.run("./reverse input.wav output.wav").exit(0, timeout=10)
    file_hash = check50.hash("output.wav")
    if file_hash != "bb4a927734bee48387e820ebf0ad3cf67fa5db88bf8c11eea6b61162174ec02f":
        
        # Correto, exceto pelo último bloco
        if file_hash == "d7beb50a997b78e257cf77e1c6fa0bf835e8e59f86aa082a7a35f7ccc8d307b4":
            raise check50.Failure("o arquivo não está invertido conforme especificado", help="você esqueceu de incluir o último bloco do arquivo de entrada?")
            
        # Inclui cabeçalho invertido (seja faltando o último bloco ou não)
        elif file_hash == "f206747786873dd0c565b048a2da1eb23d925cb862dd6c4d151a2978f6090c13" or file_hash == "e1e69515128debe5575995e89f4003bc44e2d5a362afa7314e81b621e9620934":
            raise check50.Failure("o arquivo não está invertido conforme especificado", help="parece que você incluiu um cabeçalho invertido no final do arquivo!")
        
        # Todos os outros casos
        raise check50.Failure("o arquivo não está invertido conforme especificado")