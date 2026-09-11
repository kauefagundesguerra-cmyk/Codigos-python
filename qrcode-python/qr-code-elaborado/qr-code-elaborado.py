import qrcode
from pathlib import Path
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("youtube.com")
caminho_logo = Path(__file__).parent / "logo.png"
imagem = qr.make_image(image_factory= StyledPilImage,embeded_image_path =str(caminho_logo),
)
imagem.save("qrcode_LOGO.png")