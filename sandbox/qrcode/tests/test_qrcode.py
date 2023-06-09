#LyX
import six
import qrcode
import qrcode.util
import qrcode.image.svg

try:
    import qrcode.image.pure
    import pymaging_png  # ensure that PNG support is installed
except ImportError:  # pragma: no cover
    pymaging_png = None

import qrcode
from qrcode.exceptions import DataOverflowError
from qrcode.util import (
    QRData, MODE_NUMBER, MODE_ALPHA_NUM, MODE_8BIT_BYTE)
from qrcode.tests.svg import SvgImageWhite

try:
    import unittest2 as unittest
except ImportError:
    import unittest

UNICODE_TEXT = u'\u03b1\u03b2\u03b3'


class QRCodeTests(unittest.TestCase):

    def test_basic(self):
        qr = qrcode.QRCode(version=1)
        qr.add_data('a')
        qr.make(fit=False)

    def test_large(self):
        qr = qrcode.QRCode(version=27)
        qr.add_data('a')
        qr.make(fit=False)

    def test_invalid_version(self):
        qr = qrcode.QRCode(version=41)
        self.assertRaises(ValueError, qr.make, fit=False)

    def test_overflow(self):
        qr = qrcode.QRCode(version=1)
        qr.add_data('abcdefghijklmno')
        self.assertRaises(DataOverflowError, qr.make, fit=False)

    def test_add_qrdata(self):
        qr = qrcode.QRCode(version=1)
        data = QRData('a')
        qr.add_data(data)
        qr.make(fit=False)

    def test_fit(self):
        qr = qrcode.QRCode()
        qr.add_data('a')
        qr.make()
        self.assertEqual(qr.version, 1)
        qr.add_data('bcdefghijklmno')
        qr.make()
        self.assertEqual(qr.version, 2)

    def test_mode_number(self):
        qr = qrcode.QRCode()
        qr.add_data('1234567890123456789012345678901234', optimize=0)
        qr.make()
        self.assertEqual(qr.version, 1)
        self.assertEqual(qr.data_list[0].mode, MODE_NUMBER)

    def test_mode_alpha(self):
        qr = qrcode.QRCode()
        qr.add_data('ABCDEFGHIJ1234567890', optimize=0)
        qr.make()
        self.assertEqual(qr.version, 1)
        self.assertEqual(qr.data_list[0].mode, MODE_ALPHA_NUM)

    def test_regression_mode_comma(self):
        qr = qrcode.QRCode()
        qr.add_data(',', optimize=0)
        qr.make()
        self.assertEqual(qr.data_list[0].mode, MODE_8BIT_BYTE)

    def test_mode_8bit(self):
        qr = qrcode.QRCode()
        qr.add_data(u'abcABC' + UNICODE_TEXT, optimize=0)
        qr.make()
        self.assertEqual(qr.version, 1)
        self.assertEqual(qr.data_list[0].mode, MODE_8BIT_BYTE)

    def test_mode_8bit_newline(self):
        qr = qrcode.QRCode()
        qr.add_data('ABCDEFGHIJ1234567890\n', optimize=0)
        qr.make()
        self.assertEqual(qr.data_list[0].mode, MODE_8BIT_BYTE)

    def test_render_pil(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image()
        img.save(six.BytesIO())

    def test_render_svg(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
        img.save(six.BytesIO())

    def test_render_svg_path(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=qrcode.image.svg.SvgPathImage)
        img.save(six.BytesIO())

    def test_render_svg_fragment(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=qrcode.image.svg.SvgFragmentImage)
        img.save(six.BytesIO())

    def test_render_svg_with_background(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=SvgImageWhite)
        img.save(six.BytesIO())

    @unittest.skipIf(not pymaging_png, "Requires pymaging with PNG support")
    def test_render_pymaging_png(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=qrcode.image.pure.PymagingImage)
        img.save(six.BytesIO())

    @unittest.skipIf(not pymaging_png, "Requires pymaging")
    def test_render_pymaging_png_bad_kind(self):
        qr = qrcode.QRCode()
        qr.add_data(UNICODE_TEXT)
        img = qr.make_image(image_factory=qrcode.image.pure.PymagingImage)
        self.assertRaises(ValueError, img.save, six.BytesIO(), kind='FISH')

    def test_optimize(self):
        qr = qrcode.QRCode()
        text = 'A1abc12345def1HELLOa'
        qr.add_data(text, optimize=4)
        qr.make()
        self.assertEqual(len(qr.data_list), 5)
        self.assertEqual(qr.data_list[0].mode, MODE_8BIT_BYTE)
        self.assertEqual(qr.data_list[1].mode, MODE_NUMBER)
        self.assertEqual(qr.data_list[2].mode, MODE_8BIT_BYTE)
        self.assertEqual(qr.data_list[3].mode, MODE_ALPHA_NUM)
        self.assertEqual(qr.data_list[4].mode, MODE_8BIT_BYTE)
        self.assertEqual(qr.version, 2)

    def test_optimize_size(self):
        text = 'A1abc12345123451234512345def1HELLOHELLOHELLOHELLOa' * 5

        qr = qrcode.QRCode()
        qr.add_data(text)
        qr.make()
        self.assertEqual(qr.version, 10)

        qr = qrcode.QRCode()
        qr.add_data(text, optimize=0)
        qr.make()
        self.assertEqual(qr.version, 11)

    def test_qrdata_repr(self):
        data = b'hello'
        data_obj = qrcode.util.QRData(data)
        self.assertEqual(repr(data_obj), repr(data))

    def test_print_ascii(self):
        qr = qrcode.QRCode(border=0)
        f = six.StringIO()
        qr.print_ascii(out=f)
        printed = f.getvalue()
        f.close()
        expected = u'\u2588\u2580\u2580\u2580\u2580\u2580\u2588'
        self.assertEqual(printed[:len(expected)], expected)

        f = six.StringIO()
        f.isatty = lambda: True
        qr.print_ascii(out=f, tty=True)
        printed = f.getvalue()
        f.close()
        expected = (
            u'\x1b[48;5;232m\x1b[38;5;255m' +
            u'\xa0\u2584\u2584\u2584\u2584\u2584\xa0')
        self.assertEqual(printed[:len(expected)], expected)

    def test_print_tty(self):
        qr = qrcode.QRCode()
        f = six.StringIO()
        f.isatty = lambda: True
        qr.print_tty(out=f)
        printed = f.getvalue()
        f.close()
        BOLD_WHITE_BG = '\x1b[1;47m'
        BLACK_BG = '\x1b[40m'
        WHITE_BLOCK = BOLD_WHITE_BG + '  ' + BLACK_BG
        EOL = '\x1b[0m\n'
        expected = (
            BOLD_WHITE_BG + '  '*23 + EOL +
            WHITE_BLOCK + '  '*7 + WHITE_BLOCK)
        self.assertEqual(printed[:len(expected)], expected)


class ShortcutTest(unittest.TestCase):

    def runTest(self):
        qrcode.make('image')