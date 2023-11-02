import cv2
import pytesseract as pt

path = 'assets/'

img = cv2.imread(path+'image3.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_value = 170
_, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

print(pt.pytesseract.image_to_string(binary, lang='por'))

# cv2.imshow('binary', binary)
# cv2.waitKey(0)

