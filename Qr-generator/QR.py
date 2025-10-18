# import pyqrcode
# import png
# from pyqrcode import QRCode

import qrcode
import os

# Using PIL to save the image of the QR that is generated
from PIL import Image

"""
    data : URL that is provided
    filename : name of the file that is saved
    box_size : size of the box of the QR
    border : thickness of the border
"""
def generateQR(data: str, filename: str, box_size: int = 10, border: int = 4):
    # Handling case where URL is not provided
    if not data:
        print("URL Not Found ! Please Enter a valid URL!")
        return

# s = input("Enter Url Of Website, To create QR Code")
# url = pyqrcode.create(s)
# url.svg("myqr.svg", scale = 8)
# url.png('myqr.png', scale = 6)
