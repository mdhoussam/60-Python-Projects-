
import qrcode


#qr = qrcode.make('Welcome to ETETE GITHUB')
#qr.save('myQR.png')
qr = qrcode.QRCode(
   version= 1,
    box_size=15,
    border=5
) 
data = 'https://github.com/mdhoussam'
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill ='green',black_color='white')
img.save('ETETE Github Channel QR Code.png')
