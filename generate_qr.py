import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data("https://www.netacad.com/courses/ccna-introduction-networks?courseLang=en-US&instance_id=3af34c77-c488-4a91-8088-ccafdbd8a380")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("ccna_qr.png")