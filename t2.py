import cv2
import os
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
images=os.listdir("photos")
for image in images:
    
    img = cv2.imread("photos\\"+image)
# Convert to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Show the Output
    #cv2.imshow("Output", img)
    texts = pytesseract.image_to_string(img)
    print("Readt Text is = ",texts)
