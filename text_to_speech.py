from PIL import Image
from pytesseract import image_to_string
text=image_to_string(Image.open("download.jpg"),lang="eng")