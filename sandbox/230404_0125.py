# ローカルモジュールテスト

from io import BytesIO
from PIL import Image as ImageP
#import qrcode

import ui

import pystaQrcode


def img2ui_img(img_p: ImageP):
  kind = img_p.kind
  with BytesIO() as bIO:
    img_p.save(bIO, kind)
    return ui.Image.from_data(bIO.getvalue())


def set_qrdata_img(_data):
  data = pystaQrcode.make(_data)
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
    self.text_field.delegate = self.set_TextFieldDelegate(self.img_view)

    self.text_field.height = 48
    self.text_field.placeholder = 'String to be converted to QRCode'
    self.text_field.text = data

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

  def set_TextFieldDelegate(self, img_view):
    def update_qrcode(_img_view, _text_field):
      data = _text_field.text
      img = set_qrdata_img(data)
      _img_view.image = img

    class _MyTextFieldDelegate(object):
      def textfield_should_begin_editing(self, textfield):
        return True

      def textfield_did_begin_editing(self, textfield):
        update_qrcode(img_view, textfield)

      def textfield_did_end_editing(self, textfield):
        update_qrcode(img_view, textfield)

      def textfield_should_return(self, textfield):
        textfield.end_editing()
        return True

      def textfield_should_change(self, textfield, range, replacement):
        return True

      def textfield_did_change(self, textfield):
        update_qrcode(img_view, textfield)

    return _MyTextFieldDelegate()


if __name__ == '__main__':
  data = 'https://github.com/pome-ta'
  view = View(data)
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

