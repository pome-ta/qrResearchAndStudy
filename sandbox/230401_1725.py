import qrcode
import ui


class View(ui.View):
  def __init__(self, *args, **kwargs):
    self.bg_color = 1


if __name__ == '__main__':
  view = View()
  #view.present()
  #view.present(hide_title_bar=True)
  view.present(style='fullscreen', orientations=['portrait'])

