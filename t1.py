import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
img = cv2.imread("6.jpg")
# Convert to RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Show the Output
cv2.imshow("Output", img)
texts = pytesseract.image_to_string(img)
print("Readt Text is = ",texts)
cv2.waitKey(0)
