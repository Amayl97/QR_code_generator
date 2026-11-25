# import qrcode library and pillow library is imported implicitly
import qrcode 

# link we are storing in the QR_code image
wesbite_link = 'https://amaylportfolio.vercel.app'

# make an instance of qrcode library and use the funcitons
# version is given value from 1 to 40, box_size controls how many pixel each box should have, border controls how many boxes think the border should be.
qr = qrcode.QRCode(version=1, box_size=5, border=5)
# add data in the qr_code
qr.add_data(wesbite_link) 
# create QR code
qr.make()

# create an image and store it in the image
img = qr.make_image(fill_color='black', back_color='white')
# save that image
img.save('my_portfolio_qr.png')