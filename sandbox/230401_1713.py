import qrcode

data = 'https://github.com/pome-ta'

img = qrcode.make(data)
img.show()
