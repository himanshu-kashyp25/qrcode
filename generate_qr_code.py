import qrcode

# Correct URL of the hosted HTML page
url = "https://github.com/himanshu-kashyp25/qrcode.git" # Replace with your actual URL

# Create a QR code object
qr = qrcode.QRCode(
    version=1,  # QR code size
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box in the QR code grid
    border=4,  # Thickness of the border
)

# Add the URL to the QR code
qr.add_data(url)
qr.make(fit=True)

# Create an image from the QR code
img = qr.make_image(fill="black", back_color="white")

# Save the image as a file
img.save("qr_with_options.png")

# Show the generated QR code image
img.show()
