import numpy
import cv2
import datetime
import time
import argparse

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(0)
bg = cv2.createBackgroundSubtractorMOG2()
sx = 21 #Must be postive and odd
sy = 21 #Must be positive & odd
firstFrame = None

while(True):
	# Capture frame-by-frame
	ret, frame = cap.read()
	# Create Background Mask
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray,(sx,sy), 0) #Blurs the image to deal with sensitivity.  Tweak sx and sy for more sensitivity (lower) or less (higher)
	mask = bg.apply(gray)
	#initialize firstframe
	if firstFrame is None:
		firstFrame = gray
	# create threshold
	retval, threshold = cv2.threshold(mask, 12, 255, cv2.THRESH_BINARY)
	#Timestamp, this was copy-pasted, NEEDS TO BE EDITED TO AVOID PLAGARISM
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	# Display the resulting frame
	#(Name, Source)
	cv2.imshow('FF', firstFrame)
	cv2.imshow('Video Feed', frame)
	cv2.imshow('Threshold', threshold)
	cv2.imshow('Mask', mask)
	#Exit with the Q key, will figure out how to change to esc
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture, dont touch this
cap.release()
cv2.destroyAllWindows()