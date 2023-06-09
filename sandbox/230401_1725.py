from io import BytesIO
from PIL import Image as ImageP
import qrcode

import ui


def img2ui_img(img_p: ImageP):
  kind = img_p.kind
  with BytesIO() as bIO:
    img_p.save(bIO, kind)
    return ui.Image.from_data(bIO.getvalue())


class View(ui.View):
  def __init__(self, data=None, *args, **kwargs):
    self.bg_color = 1
    self.img = qrcode.make(data)
    self.img_view = ui.ImageView()
    self.img_view.image = img2ui_img(self.img)
    self.img_view.size_to_fit()
    #self.iv.image = ui.Image.from_data(img)
    self.add_subview(self.img_view)


if __name__ == '__main__':
  data = 'https://github.com/pome-ta'
  view = View(data)
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

