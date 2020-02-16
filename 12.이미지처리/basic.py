import cv2
import requests
import numpy
from PIL import Image

"""
url = "https://cdn.pixabay.com/photo/2017/03/27/14/49/beach-2179183_1280.jpg"
arr = numpy.asarray(bytearray(requests.get(url).content), dtype=numpy.uint8)

img = cv2.imdecode(arr, cv2.IMREAD_COLOR)

cv2.imshow("A", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

pil_image = Image.open("sample.jpg")
opencv_image = numpy.array(pil_image)
#opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)

cv2.imshow("A", opencv_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
