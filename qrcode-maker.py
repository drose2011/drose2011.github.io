import qrcode

website_qr = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_H,
    box_size = 10,
    border = 4
)
website_qr.add_data('https://dylanjrose.com/')

img = website_qr.make_image(fill_color=(5, 99, 187), back_color='white')
img.save('qrcode.png')