# Identifica e desenha um quadrado no David
# https://github.com/ageitgey/face_recognition/blob/master/examples/identify_and_draw_boxes_on_faces.py

# BIblioteca de reconhecimento facial
import face_recognition
# Biblioteca com ferramentas matemáticas
import numpy as np
# Biblioteca com ferramentas relacionadas a imagens ()
from PIL import Image, ImageDraw

# Carrega uma foto e aprende a como recohecê-la
imagem_conhecida = face_recognition.load_image_file("malan.jpg")
codificacao = face_recognition.face_encodings(imagem_conhecida)[0]

# Carrega uma imagem com rostos desconhecidos
imagem_desconhecida = face_recognition.load_image_file("harvard.jpg")

# Encontra todos os rostos e codificações de rostos na imagem desconhecida
localizacoes_rostos = face_recognition.face_locations(imagem_desconhecida)
codificacoes_rostos = face_recognition.face_encodings(imagem_desconhecida, localizacoes_rostos)

# Converte a imagem para uma imagem em formato PIL para que possamos escrever em cima dela com a biblioteca Pillow
# Saiba mais em http://pillow.readthedocs.io/ for more about PIL/Pillow
imagem_pil = Image.fromarray(imagem_desconhecida)

# Cria uma instância do objeto Draw para desenhar
desenho = ImageDraw.Draw(imagem_pil)

# Percorre o conjunto de rostos encontrados na imagem desconhecida
for (cima, direita, baixo, esquerda), codificacao_rosto in zip(localizacoes_rostos, codificacoes_rostos):

    # Checa se o rosto "combina" com um dos rostos conhecidos
    combinacoes = face_recognition.compare_faces([codificacao], codificacao_rosto)

    # Usa o rosto conhecido com a menor distãncia em relação ao novo rosto
    distancias_rostos = face_recognition.face_distance([codificacao], codificacao_rosto)
    indice_melhor_combinacao = np.argmin(distancias_rostos)
    if combinacoes[indice_melhor_combinacao]:

        # Desenha um quadrado ao redor do rosto usando o módulo Pillow
        desenho.rectangle(((esquerda - 20, cima - 20), (direita + 20, baixo + 20)), outline=(0, 255, 0), width=20)

# Remove a biblioteca de desenho da memória
del desenho

# Exibe a imagem criada
imagem_pil.show()
