import numpy
import cv2
import datetime
import time
import argparse

# Args
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "Video Path")
ap.add_argument("-a", "--min-area", type = int, default = 500, help = "Min motion area")
args = vars(ap.parse_args())

if args.get("video", None) is None:
	cap = cv2.VideoCapture(0)
else:
	cap = cv2.VideoCapture(args["video"])
	
bg = cv2.createBackgroundSubtractorMOG2()
sx = 21 #Must be postive and odd
sy = 21 #Must be positive & odd
firstFrame = None
i = 0
res = 60

def init(G):
	return G

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
