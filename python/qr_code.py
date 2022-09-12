import io
import qrcode
code = input("Enter text that you want to print as qrcode\n")
qr = qrcode.QRCode()
qr.add_data(code)
f = io.StringIO()
qr.print_ascii(out=f)
f.seek(0)
print(f.read())

