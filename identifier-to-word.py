import cv2
import pytesseract as pt

path = 'assets/'

img = cv2.imread(path+'image.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_value = 170
_, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

data = pt.pytesseract.image_to_data(binary, lang='por')

for x, line in enumerate(data.splitlines()):
  if x!= 0:
    line = line.split()
    if len(line) == 12: 
      x, y, w, h = int(line[6]), int(line[7]), int(line[8]), int(line[9])
      word = line[11]
      cv2.rectangle(img,(x, y),(w+x,h+y),(0,0,255),1)


cv2.imshow('img', img)
cv2.waitKey(0)