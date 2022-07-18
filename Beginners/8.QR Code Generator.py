
import qrcode
#qr = qrcode.make('helle etete')
#qr.save('myQR.png')
qr = qrcode.QRCode(
   version= 1,
    box_size=15,
    border=5
)
data = 'https://github.com/mdhoussam'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill ='black',black_color='white')
img.save('Github Channel QR Code.png')