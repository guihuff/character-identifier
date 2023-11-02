import cv2
import pytesseract as pt

import sys

if len(sys.argv) > 2:
  print("==============================")
  print("somente um argumento é valido por requisição")
  print("==============================\n\n\ncontinuando...\n")

path = sys.argv[1]

img = cv2.imread(path)

if img is None:
  print("a imagem não foi encontrada! (caminho: " + path + ")")
else:
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  threshold_value = 170
  _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

  print(pt.pytesseract.image_to_string(binary, lang='por'))

  # cv2.imshow('binary', binary)
  # cv2.waitKey(0)

