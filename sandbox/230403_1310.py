# モジュールコピー

from pathlib import Path
import shutil

import qrcode

modules_file_path = qrcode.__file__
modules_name = qrcode.__name__
copy_path = Path(modules_file_path).parent

to_path = Path(f'../{modules_name}').resolve()

shutil.copytree(copy_path, to_path)

