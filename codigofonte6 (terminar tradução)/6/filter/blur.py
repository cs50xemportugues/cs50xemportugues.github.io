# Aplica efeito de desfoque em uma imagem

# Biblioteca com ferramentas relacionadas à imagens
from PIL import Image, ImageFilter

# Desfoca a imagem
antes = Image.open("ponte.bmp")
depois = antes.filter(ImageFilter.BLUR)
depois.save("desfocado.bmp")
