import pyqrcode
text = pyqrcode.create('programmer ako')
text.svg('programerako.svg', scale=8)
print(text.terminal(quiet_zone=1))
