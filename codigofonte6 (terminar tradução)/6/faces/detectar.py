# Encontre rostos em uma foto
# https://github.com/ageitgey/face_recognition/blob/master/examples/find_faces_in_picture.py


# Biblioteca com ferramentas relacionadas à imagens (Python Imaging Library)
from PIL import Image
# Biblioteca de reconhecimento facial
import face_recognition

# Carregue o arquivo jpg em um array numpy
imagem = face_recognition.load_image_file("yale.jpg")


# Encontre todos os rostos na imagem usando o modelo baseado em HOG padrão
# Este método é relativamente preciso, mas não tão preciso quanto o modelo CNN
# Veja também: find_faces_in_picture_cnn.py

localizacoes_rostos = face_recognition.face_locations(image)

for localizacao_rosto in localizacoes_rostos:

	# Imprima a localização de cada rosto nesta imagem
    cima, direita, baixo, esquerda = localizacaorosto

    # Você pode acessar o rosto assim:
    imagem_rosto = imagem[cima:baixo, esquerda:direita]
    pil_image = Image.fromarray(imagem_rosto)
    pil_image.show()
