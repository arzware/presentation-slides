import qrcode
import qrcode.image.svg

factory = qrcode.image.svg.SvgPathImage
img = qrcode.make('https://arzware.net', image_factory=factory)
img.save('qr.svg')
