import cv2

img = cv2.imread('bts.webp', cv2.IMREAD_GRAYSCALE)

cv2.imshow('inspiration', img)

cv2.waitKey(3000)
