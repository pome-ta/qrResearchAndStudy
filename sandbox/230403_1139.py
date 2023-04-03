from io import BytesIO
from PIL import Image as ImageP
import qrcode

import ui


def img2ui_img(img_p: ImageP):
  kind = img_p.kind
  with BytesIO() as bIO:
    img_p.save(bIO, kind)
    return ui.Image.from_data(bIO.getvalue())


def set_qrdata_img(_data):
  data = qrcode.make(_data)
  img = img2ui_img(data)
  return img


def create_btn(icon):
  btn_icon = ui.Image.named(icon)
  btn = ui.Button(image=btn_icon)
  return btn


class View(ui.View):
  def __init__(self, data=None, *args, **kwargs):
    self.bg_color = 1

    self.img_view = ui.ImageView()
    self.img_view.image = set_qrdata_img(data)

    self.img_view.size_to_fit()

    self.text_field = ui.TextField()
    self.text_field.height = 48
    self.text_field.placeholder = 'String to be converted to QRCode'

    self.add_subview(self.text_field)
    self.add_subview(self.img_view)

  def layout(self):
    _, _, w, h = self.frame
    self.img_view.x = self.to_center(self.img_view)

    margin = w / 24
    self.text_field.width = w - (margin * 2.0)
    self.text_field.x = self.to_center(self.text_field)
    self.text_field.y = self.img_view.height + (margin / 2.0)

  def to_center(self, this):
    return (self.width / 2.0) - (this.width / 2.0)


if __name__ == '__main__':
  data = 'https://github.com/pome-ta'
  view = View(data)
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

