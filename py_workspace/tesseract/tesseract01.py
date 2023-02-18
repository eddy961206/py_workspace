import pytesseract
from PIL import Image
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

a = Image.open('C:\py_workspace\tesseract\영수증.png')
result = pytesseract.image_to_string(a)
print(result)