# pip install qrcode
import qrcode

qr = qrcode.QRCode()
qr.add_data(input("Enter text for QR code: "))

qr.make()

img = qr.make_image()
img.save('qrcode.png')