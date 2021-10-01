import os
import numpy as np
import cv2


def blur_face(image, factor=3.0):
	(h, w) = image.shape[:2]
	kernelW = int(w / factor)
	kernelH = int(h / factor)
	# ensure the width of the kernel is odd
	if kernelW % 2 == 0:
		kernelW -= 1
	# ensure the height of the kernel is odd
	if kernelH % 2 == 0:
		kernelH -= 1
	# apply a Gaussian blur to the input image using our computed
	# kernel size
	return cv2.GaussianBlur(image, (kernelW, kernelH), 0)
# Load the cascade

# Read the input image
cd = os.getcwd()
image_path = os.path.join(cd,"opencv","image.jpg")
cascade_path = os.path.join(cd,"opencv",'haarcascade_frontalface.xml')
face_cascade = cv2.CascadeClassifier(cascade_path)
img = cv2.imread(image_path)
# Convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Detect faces
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces
for (x, y, w, h) in faces:
    #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    crop_img = img[y:y+h, x:x+w]
    crop_img = blur_face(crop_img, 3)
    img[y:y+h, x:x+w] = crop_img
# Display the output
cv2.imshow('img', img)
cv2.waitKey()

