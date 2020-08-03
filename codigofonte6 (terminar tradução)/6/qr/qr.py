# Programa que gera uma código QR
# https://github.com/lincolnloop/python-qrcode

import qrcode

# Gera o códigon QR
imagem = qrcode.make("https://youtu.be/oHg5SJYRHA0")

# Salva como arquivo
imagem.save("qr.png", "PNG")
