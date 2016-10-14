#Quentin Minor, Babak Chehraz, 
import numpy
import cv2
import datetime
import time

def getVideo(tf, path):#Get video from path or from webcam
	if tf == False:
		return cv2.VideoCapture(0)
	else:
		return cv2.VideoCapture(path)

def init(G):#initialzie first frame
	return G

def play(tf, path, pause):
	#varriable declaration
	bg = cv2.createBackgroundSubtractorMOG2()
	sx = 21 #Must be postive and odd
	sxMod = 2
	firstFrame = None
	i = 0
	res = 60
	#Video Object
	cap = getVideo(tf, path)
	while(True):
		# Capture frame-by-frame
		ret, frame = cap.read()
		# Create Background Mask
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (sx, sx), 0)
		#initialize firstframe
		if firstFrame is None:
			firstFrame = init(gray)
			continue
		# create threshold
		diff = cv2.absdiff(firstFrame, gray)
		retval, threshold = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
		thresh = cv2.dilate(threshold, None, iterations=2)
		#Find contours
		cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]
		#Draw rectangle around object
		x,y,w,h = cv2.boundingRect(cnts)
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
		
		# Display the resulting frame
		#(Name, Source)
		cv2.imshow('Video Feed', frame)
		#cv2.imshow('Threshold', threshold)
		#Reinitialize first frame
		firstFrame = init(gray)
		#Exit with the Q key
		if cv2.waitKey(1) & 0xFF == ord('q'):
			break
		if cv2.waitKey(1) & 0xFF == ord('.'):
			sx+= sxMod
			print(sx)
		if cv2.waitKey(1) & 0xFF == ord(','):
			sx -= sxMod
			print(sx)
	# Cleanup
	cap.release()
	cv2.destroyAllWindows()
