import random
import string
from PIL import Image, ImageDraw

# Generate CAPTCHA text
captcha = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Create image
img = Image.new('RGB', (200, 70), 'white')
draw = ImageDraw.Draw(img)
draw.text((40, 20), captcha, fill='black')

# Save and display CAPTCHA
img.save("captcha.png")
img.show()

# Verify CAPTCHA
user = input("Enter CAPTCHA: ")

if user.upper() == captcha:
    print("CAPTCHA Verified Successfully!")
else:
    print("Invalid CAPTCHA!")