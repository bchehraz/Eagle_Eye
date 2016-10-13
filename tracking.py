import numpy
import cv2
import datetime
import time
<<<<<<< HEAD
import argparse
=======
>>>>>>> 6af1b033ed3aeb4420bbaf873dd90c8c905cf552

	
bg = cv2.createBackgroundSubtractorMOG2()
sx = 21 #Must be postive and odd
sy = 21 #Must be positive & odd
firstFrame = None
i = 0
res = 60

def getVideo(tf, path):
	if tf == False:
		return cv2.VideoCapture(0)
	else:
		return cv2.VideoCapture(path)

def init(G):
	return G

def play(tf, path):
	bg = cv2.createBackgroundSubtractorMOG2()
	sx = 21 #Must be postive and odd
	sy = 21 #Must be positive & odd
	firstFrame = None
	i = 0
	res = 60

	cap = getVideo(tf, path)
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Create Background Mask
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (sx, sy), 0)
		#initialize firstframe
		if firstFrame is None:
			firstFrame = init(gray)
			continue
		# create threshold
		diff = cv2.absdiff(firstFrame, gray)
		retval, threshold = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
		#Timestamp, copied from 
		cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
			(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
		#cnts = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
		thresh = cv2.dilate(threshold, None, iterations=2)
		cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
		x,y,w,h = cv2.boundingRect(cnts)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		
		# Display the resulting frame
		#(Name, Source)
		cv2.imshow('Video Feed', frame)
		cv2.imshow('Threshold', threshold)
		firstFrame = init(gray)
<<<<<<< HEAD
		continue
	# create threshold
	diff = cv2.absdiff(firstFrame, gray)
	retval, threshold = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
	#Timestamp, this was copy-pasted, NEEDS TO BE EDITED TO AVOID PLAGARISM
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
	thresh = cv2.dilate(threshold, None, iterations=2)
	cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
	x,y,w,h = cv2.boundingRect(cnts)
	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	
	# Display the resulting frame
	#(Name, Source)
	cv2.imshow('Video Feed', frame)
	cv2.imshow('Threshold', threshold)
	firstFrame = init(gray)
	#Exit with the Q key, will figure out how to change to esc
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
# When everything done, release the capture, dont touch this
cap.release()
cv2.destroyAllWindows()
=======
		#Exit with the Q key, will figure out how to change to esc
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
	# When everything done, release the capture, dont touch this
	cap.release()
	cv2.destroyAllWindows()
>>>>>>> 6af1b033ed3aeb4420bbaf873dd90c8c905cf552
