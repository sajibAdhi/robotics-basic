import cv2 as cv
img = cv.imread(r'C:\picture\Salman.jpg')
cv.imshow('color', img)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

haar_cascade = cv.CascadeClassifier('C:/picture/haar_face.xml')
#face_rect = haar_cascade.detectMultiplescale
#face_rect = haar_cascade.detectMu
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=3)
print(faces_rect)
print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    #cv.rectangle(img,)

cv.imshow('Detected Faces', img)

cv.waitKey(0)

