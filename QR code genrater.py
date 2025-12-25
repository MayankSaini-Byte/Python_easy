import qrcode
data=input('Enetr the text or URL: ').strip()
filename=input("enter the name of the file: ").strip()
code=qrcode.QRCode(box_size=10,border=4)
code.add_data(data)
code.make(fit=True) 
image = code.make_image(fill_color="Black",back_color="White")
image.save(filename)
print(f"QR code save as {filename}")