import qrcode
from PIL import Image

# Data to be encoded in the QR code
data = "https://iniyavandesign.github.io/ar/index.html"

# Create QR code instance with specific settings
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
    box_size=10,  # size of each box in the QR code
    border=4,  # size of border around the QR code
)

# Add data to the instance
qr.add_data(data)
qr.make(fit=True)

# Create and save the QR code pattern
qr_image = qr.make_image(fill_color="black", back_color="white")
qr_image.save("qr_code.png")

# Display the QR code (optional)
qr_image.show()
