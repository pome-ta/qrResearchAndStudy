# 📝 2023/05/27

久々に開いたら意味わからんだったので、ほぼ記憶リセットやな

[QRコードを生成できるだけでなく「作り方」まで理解できる「Creating a QR Code step by step」 - GIGAZINE](https://gigazine.net/news/20200815-creating-qr-code-step-by-step/)


# 📝 2023/04/04

## `qrcode` -> `pystaQrcode` を読んでいく

無駄にインデントを2 に変えていく

`from hoge import piyo` を`pystaQrcode` で書き替えていく

## `make` と素直に

```python
data = 'https://github.com/pome-ta'
qr = pystaQrcode.make(data)
```

### `maim.py` を読む

[qrResearchAndStudy/main.py at main · pome-ta/qrResearchAndStudy · GitHub](https://github.com/pome-ta/qrResearchAndStudy/blob/main/sandbox/pystaQrcode/main.py)

#### `six` modules

2系 * 3系で、6なんか

`xrange` って書き換えちゃってええんかな？

# 📝 2023/04/03

[/qrcode](https://github.com/pome-ta/qrResearchAndStudy/tree/main/qrcode)

↓

[/sandbox/pystaQrcode](https://github.com/pome-ta/qrResearchAndStudy/tree/main/sandbox/pystaQrcode) rename

Pythonista3 よりコピー

[lincolnloop/python-qrcode: Python QR Code image generator](https://github.com/lincolnloop/python-qrcode)

[qrcode · PyPI](https://pypi.org/project/qrcode/)

これのPythonista3 調整版みたい

# 📝 2023/04/01

## 記載必要内容

> 「QRコード」は㈱デンソーウェーブの登録商標です。

これでええんか？
