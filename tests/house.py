import cv2
from invert import invert

image = cv2.imread('house.tiff')

new = invert(image)
cv2.imwrite('invertedhouse.tiff', new)
