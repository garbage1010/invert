# invert
Image inversion in python (OpenCV & numpy)

## Usage
### example
```
import cv2
from invert import invert

image = cv2.imread('house.tiff')

new = invert(image)
cv2.imwrite('invertedhouse.tiff', new)
```
**Original Image**

**Inverted**
