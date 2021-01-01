# import relevant packages
from pdf2image import convert_from_path
import os
import cv2
import pytesseract
import numpy as np
from PIL import ImageGrab
import time

# root dirs
ROOT_SRC_PATH = r"C:\Users\mtiwari33\OneDrive - DXC Production\Uniper\OCR\NativeOCRv0.01\src"
ROOT_DST_PATH = r"C:\Users\mtiwari33\OneDrive - DXC Production\Uniper\OCR\NativeOCRv0.01\dst"
ROOT_TXT_DST_PATH = r"C:\Users\mtiwari33\OneDrive - DXC Production\Uniper\OCR\NativeOCRv0.01\txt_dst"

# settings

# download from the below link (for windows only, for linux and Mac OS need to research)
# https://github.com/oschwartz10612/poppler-windows/releases
# extract the file and paste the file "bin" folder location like below
poppler_path=r"C:\Users\mtiwari33\Downloads\Software\Release-20.12.1\poppler-20.12.1\bin"

# download and install pytesseract
# the paste the ".exe" location like below
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# get the files
files = os.listdir(ROOT_SRC_PATH)

for file in files:
    print(file)
    pages = convert_from_path(os.path.join(ROOT_SRC_PATH,file), poppler_path=poppler_path)
# images = convert_from_bytes(open(file_path,'rb').read(), poppler_path=poppler_path)

    i = 1
    for page in pages:
        image_name = "Page_" + str(i) + ".jpg"  
        page.save(os.path.join(ROOT_DST_PATH,image_name), "JPEG")
        i = i+1

    pages = os.listdir(ROOT_DST_PATH)

    for page in pages:
        print(page)
        img = cv2.imread(os.path.join(ROOT_DST_PATH,page))
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        myData = []
        myData.append(pytesseract.image_to_string(img))

        # write data to file
        filename = file + ".txt" 
        with open(os.path.join(ROOT_TXT_DST_PATH, filename ),'a+') as f:
            for data in myData:
                f.write((str(data)))
            f.write('\n')





