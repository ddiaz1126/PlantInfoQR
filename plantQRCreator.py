# Import libraries
import pandas as pd 
import qrcode
from PIL import Image, ImageDraw, ImageFont

# Input name of CSV containing plants with url's
df = pd.read_csv("PlantDatabase.csv")

# Function to generate QR
def generate_qr(plant_name, url):
    qr = qrcode.QRCode(
        version=1,  # Size of QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Low error correction
        box_size=10,  # Size of each box
        border=4,  # Border thickness
    )
    qr.add_data(url)
    qr.make(fit=True)

    # Create the QR code image
    qr_img = qr.make_image(fill="black", back_color="white")

    # Define padding for text
    padding = 30  # Space for text above QR code
    width, height = qr_img.size
    new_height = height + padding

    # Create a new blank image with extra space on top
    img = Image.new("RGB", (width, new_height), "white")
    draw = ImageDraw.Draw(img)

    # Load a font (use a default one if PIL can't find fonts)
    try:
        font = ImageFont.truetype("arial.ttf", 30)  # Adjust size as needed
    except IOError:
        font = ImageFont.load_default()

    # Get text bounding box to center it
    text_bbox = draw.textbbox((0, 0), plant_name, font=font)
    text_width = text_bbox[2] - text_bbox[0]  # Calculate text width
    text_x = (width - text_width) // 2  # Center the text

    # Draw the text on the new image
    draw.text((text_x, 10), plant_name, fill="black", font=font)

    # Convert QR image to RGB before pasting
    img.paste(qr_img.convert("RGB"), (0, padding))
    filename = plant_name.replace(" ", "").lower() + ".png"
    # Save the final image
    img.save(f"qr_codes/{filename}")
    print(f"QR Code for {plant_name} saved as {filename}")


# Iterate through rows of plants and create QR Code
for index, row in df.iterrows():
    # Pass arguments into the generate_qr function
    generate_qr(row['Plant Name'], row['url'])