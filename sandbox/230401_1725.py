import qrcode
import ui


class View(ui.View):
  def __init__(self, data=None, *args, **kwargs):
    self.bg_color = 1
    img = qrcode.make(data)
    self.iv = ui.ImageView()
    self.iv.image = ui.Image.from_data(img)
    self.add_subview(self.iv)
    


if __name__ == '__main__':
  data = 'https://github.com/pome-ta'
  view = View(data)
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

