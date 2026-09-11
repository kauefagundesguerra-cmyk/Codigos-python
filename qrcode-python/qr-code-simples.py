import qrcode
imagem = qrcode.make("https://youtube.com")
imagem.save("qrcode.png")