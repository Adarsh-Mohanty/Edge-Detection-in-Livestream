#Import modules
import picamera
import picamera.array
import time
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera



import numpy as np
#Initialize camera
camera = picamera.PiCamera()
camera.resolution = (640,480)
rawCapture = picamera.array.PiRGBArray(camera)
#Let camera warm up
time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	#Capture image
	#camera.capture(rawCapture, format="bgr")
	img = frame.array

	#Convert to Grayscale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Perform canny edge-detection
	edged = cv2.Canny(gray, 50, 150,5)
	
	# show the frame
	
	cv2.imshow("Frame",edged)
	key = cv2.waitKey(1) & 0xFF

	# clear the stream in preparation for the next frame
	rawCapture.truncate(0)
 
	#cv2.waitKey(0)
