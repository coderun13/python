import qrcode

def generate_qr(data, filename="my_qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L, 
        box_size=10, 
        border=4,   
    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)
    print(f"Success! QR code saved as {filename}")

if __name__ == "__main__":
    link = "https://github.com/coderun13"
    generate_qr(link)