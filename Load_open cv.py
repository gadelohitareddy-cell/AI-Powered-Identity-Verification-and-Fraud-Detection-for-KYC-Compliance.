#Write a Python script to load and display an image
#using OpenCV (cv2.imread, cv2.imshow).

import cv2

image = cv2.imread("photo.png")

if image is None:
    print("Cannot open image")
else:
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
