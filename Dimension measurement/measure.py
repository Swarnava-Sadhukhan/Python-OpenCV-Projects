	
import cv2
import utlis
 
###################################
webcam = False
path = '1.jpg'
#cap = cv2.VideoCapture(0)
#cap.set(10,160)
#cap.set(3,1920)
#cap.set(4,1080)
scale = 2
wP = 210 *scale
hP= 297 *scale
###################################
 
#while True:
#if webcam:
#    success,img = cap.read()
#else: 
img = cv2.imread('3.jpg')
img = cv2.resize(img, (620, 800))  # RESIZE IMAGE
cv2.imshow('Original',img)

#displays until key is pressed
cv2.waitKey(0)
#stores image with contours
imgContours , conts = utlis.getContours(img,filter=4)
if len(conts) != 0:
# selects contour of A4 paper
    biggest = conts[0][2]
#crops image
    imgWarp = utlis.warpImg(img, biggest, wP,hP)
    cv2.imshow('A4',imgWarp)

#to get contours of the object
    imgContours2, conts2 = utlis.getContours(imgWarp,minArea=2000, filter=4,cThr=[50,50],draw = False)
    if len(conts2) != 0:
        for obj in conts2:
		#draw green contour lines on the image 
            cv2.polylines(imgContours2,[obj[2]],True,(0,255,0),2)
		#rearranges points
            nPoints = utlis.reorder(obj[2])
		#calculates width & height
            nW = round((utlis.findDis(nPoints[0][0]//scale,nPoints[1][0]//scale)/10),1)
            nH = round((utlis.findDis(nPoints[0][0]//scale,nPoints[2][0]//scale)/10),1)
		#Draws arrow along width and height
            cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[1][0][0], nPoints[1][0][1]),(255, 0, 255), 3, 8, 0, 0.05)
            cv2.arrowedLine(imgContours2, (nPoints[0][0][0], nPoints[0][0][1]), (nPoints[2][0][0], nPoints[2][0][1]),(255, 0, 255), 3, 8, 0, 0.05)
            x, y, w, h = obj[3]
		#Displays measurement of dimension
            cv2.putText(imgContours2, '{}cm'.format(nW), (x + w//2, y + 50), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,(255, 0, 255), 2)
            cv2.putText(imgContours2, '{}cm'.format(nH), (x + 50, y + h // 2), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1.5,(255, 0, 255), 2)
    cv2.imshow('Final', imgContours2)

cv2.waitKey(0)
