import cv2
import pytesseract as pt

path = 'assets/'

img = cv2.imread(path+'image2.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
threshold_value = 170
_, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

boxes = pt.pytesseract.image_to_boxes(binary, lang='por')

imH, imW, _ = img.shape

print(boxes)

for b in boxes.splitlines():
  b = b.split(' ')
  letra, x, y, w, h = b[0],int(b[1]),int(b[2]),int(b[3]),int(b[4])
  if letra != '~' :
    cv2.rectangle(img,(x,imH-y),(w,imH-h),(0,0,255),1)
  # cv2.putText(img, letra, (x, imH-y+25),cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)


cv2.imshow('img', img)
cv2.waitKey(0)