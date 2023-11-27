import check50
import check50.c

HASHES = ["268f2deee976fcc8dcc915be63cd3d4ac003a73a4b8bfd6f7b95c441a42ed1ec", "4481b5a438d359718000dfd58e2a32a7b109eb4a5590e0650c6bd295979c64fc", "3d83603745302935c067379b704573e5addb4356ad407041f0a698070e6e4e7b"]

@check50.check()
def existe():
    """volume.c existe"""
    check50.exists("volume.c")
    check50.incluir("input.wav")

@check50.check(existe)
def compila():
    """volume.c compila"""
    check50.c.compiler("volume.c", lcs50=True)

@check50.check(compila)
def audio_metade():
    """reduz o volume de áudio corretamente com fator de 0.5"""
    check50.run("./volume input.wav output.wav 0.5").exit(0)
    if check50.hash("output.wav") != HASHES[0]:
        raise check50.Failure("o áudio não foi alterado corretamente, fator de 0.5")

@check50.check(compila)
def audio_decimo():
    """reduz o volume de áudio corretamente com fator de 0.1"""
    check50.run("./volume input.wav output.wav 0.1").exit(0)
    if check50.hash("output.wav") != HASHES[1]:
        raise check50.Failure("o áudio não foi alterado corretamente, fator de 0.1")

@check50.check(compila)
def audio_x2():
    """aumenta o volume de áudio corretamente com fator de 2"""
    check50.run("./volume input.wav output.wav 2").exit(0)
    if check50.hash("output.wav") != HASHES[2]:
        raise check50.Failure("o áudio não foi alterado corretamente, fator de 2")