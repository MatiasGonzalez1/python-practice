#se importa la libreria para creacion de codigo qr
from textwrap import fill
from turtle import back
import qrcode

#se especifica la información que tendrá el codigo
website_link = 'https://galeria-expo-talleres2022-327k5i96k-matiasgonzalez1.vercel.app/'
#se moldea el tamaño, la cantidad de pixeles y que grosor tendrá
qr = qrcode.QRCode(version=1, box_size=5, border=5)
#se agrega el valor al qr
qr.add_data(website_link)
#se finaliza creandolo
qr.make()

img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('galeria_qr.png')

