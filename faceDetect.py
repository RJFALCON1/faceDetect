import cv2
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
image = cv2.imread('group-photo-family-group-outdoors-grass-hill-generations.webp')
faces = face_cascade.detectMultiScale(image,1.1,4)
for (x,y,w,h) in faces :
    cv2.rectangle(image,(x,y),(x+w,y+h),(123,0,120),2)
cv2.imshow('facesDetected',image)
cv2.waitKey()