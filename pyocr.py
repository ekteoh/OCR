import pytesseract
from PIL import Image
Image.open("test2.png")
text=pytesseract.image_to_string(Image.open("test2.png"))

print(text)