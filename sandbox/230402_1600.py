from io import BytesIO
from PIL import Image as ImageP
import qrcode

import ui


def img2ui_img(img_p: ImageP):
  kind = img_p.kind
  with BytesIO() as bIO:
    img_p.save(bIO, kind)
    return ui.Image.from_data(bIO.getvalue())


def create_btn(icon):
  btn_icon = ui.Image.named(icon)
  btn = ui.Button(image=btn_icon)
  return btn


class InPutViews(ui.View):
  def __init__(self, parent, *args, **kwargs):
    self.parent = parent
    self.bg_color = 'green'

    self.text_field = ui.TextField()
    self.text_field.height = 48
    self.text_field.flex = 'W'

    self.btn = create_btn('iob:ios7_refresh_outline_256')
    self.btn = self.set_btn_size_radius(self.btn)
    self.btn.bg_color = 'red'

    self.add_subview(self.text_field)
    self.add_subview(self.btn)

  def set_btn_size_radius(self, _btn):
    btn_size = min(self.width, self.height) / 2
    _btn.width = _btn.height = btn_size
    _btn.corner_radius = btn_size / 2.0
    return _btn

  def layout(self):
    _, _, w, h = self.parent.frame
    margin = w / 24
    self.x = margin
    self.width = w - (margin * 2.0)

    self.btn = self.set_btn_size_radius(self.btn)
    self.btn.y = margin
    self.btn.x = (self.width / 2.0) - (self.btn.width / 2.0)

    self.text_field.y = self.btn.y + self.btn.height + margin

    self.height = self.text_field.height + self.text_field.y + margin


class View(ui.View):
  def __init__(self, data=None, *args, **kwargs):
    self.bg_color = 1
    self.img = qrcode.make(data)
    self.img_view = ui.ImageView()
    self.img_view.image = img2ui_img(self.img)
    self.img_view.size_to_fit()

    self.input_view = InPutViews(self)
    self.add_subview(self.input_view)
    self.add_subview(self.img_view)

  def layout(self):
    #self.img_view.y = self.input_view.height + self.y
    self.img_view.x = (self.width / 2.0) - (self.img_view.width / 2.0)
    self.input_view.y = self.y + self.img_view.height


if __name__ == '__main__':
  data = 'https://github.com/pome-ta'
  view = View(data)
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

