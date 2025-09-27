import qrcode
from PIL import Image

def generate_qr_code(url, filename="website_qr.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")

# Replace with your actual GitHub Pages URL
website_url = "https://YOUR_USERNAME.github.io/your-repo-name"  # Update this!
generate_qr_code(website_url, "/Users/qj/Desktop/Admin/Website/qr_code.png")
