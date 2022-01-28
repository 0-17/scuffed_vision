#!/usr/bin/env python3

import cv2 
import numpy as np
from math import degrees, atan

positivesavepath = "haarcascades/collectedimages/pos"
negativesavepath = "haarcasdaes/collectedimages/neg"
path = "/cancascade.xml"
objectname = "can"
savedata = False
frameparams = [640, 480]
samplepath = "/collected/pos"
br = 190
fcap = 10
minblur = 500
gray = True
savedata = False

global countfolder 
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, br)

count = 0
countsv = 0

def empty(a):
	pass

cv2.namedWindow("romania")
cv2.resizeWindow("romania", frameparams[0], frameparams[1])

cascade = cv2.CascadeClassifier(path)

# def drawAngle(x1, y1, x2, y2):
# 	#im gonna be real, i dont know how this works, but it works and thats what matters
# 	#nvm it doesnt work FUCK
# 	something = np.linalg.inv(randomshit)
# 	somethingagain = something.dot([x1, y1, 1.0])
# 	somethingagain2 = something.dot([x2,y2,1.0])
# 	cos_angle = somethingagain.dot(somethingagain2) / (np.linalg.norm(somethingagain) * np.linalg.norm(somethingagain2))
# 	print(degrees(np.arccos(cos_angle)))

#!!!!!!!!!!!!!!!ANGLES ARE SCUFFED, I DO NOT HAVE THE TIME OR RESOURCES TO CALIBRATE MY CAMERA SO THERE WILL BE ERROR, WILL CALIBRATE WHEN I HAVE TIME!!!!!!!!!!!!!
#this is assuming there is no camera distortion and that the middle of the screen is the centre.
def drawAngleWorking(x):
	xc = 320
	focallength = 1200 #this is literally just a guess at the focal length
	print(degrees(atan((x-xc)/focallength)))


# def saveimgs():
# 	global countfolder
# 	countfolder = 0
# 	while os.path.exists(path + str(countfolder)):
# 		countfolder += 1
# 	os.makedirs(samplepath + str(countfolder))

# if savedata:saveimgs()

while True:
	cap.set(10, 180)
	success, img = cap.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	sval = 1 + (17 / 1000)
	print("asd")
	cans = cascade.detectMultiScale(gray, sval, 1, 3)

	for (x, y, w, h) in cans:
		area = w*h
		if area > 8:
			cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 0, 255), 3)
			cv2.putText(gray, "romanian can", (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 255), 2)
			rcol = gray[y:y+h, x:x+w]
			drawAngleWorking(x)
		if savedata:
			blur = cv2.Laplacian(gray, cv2.CV_64F).var()
			if count % fcap == 0 and blur > minblur:
				ctime = time.time()
				cv2.imwrite(path + str(countfolder) + "/" + str(countsv) + " " + str(int(blur)) + " " + str(ctime) + ".png", gray)
				countsv += 1
			count += 1

	cv2.imshow("romania", gray)

	if cv2.waitKey(1) == 27:
		break

cam.release()
cv2.destroyAllWindows()
