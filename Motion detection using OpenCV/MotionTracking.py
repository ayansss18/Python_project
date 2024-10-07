import cv2 as cv

cap=cv.VideoCapture(0)
ret,frame1=cap.read()
ret,frame2=cap.read()

while True:
    diff=cv.absdiff(frame1,frame2)
    gray=cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur=cv.GaussianBlur(gray,(5,5),0)
    _,thresh=cv.threshold(blur,20,255,cv.THRESH_BINARY)
    dilate=cv.dilate(thresh,None,iterations=3)
    contours,hierarchy=cv.findContours(dilate,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    # cv.drawContours(frame1,contour,-1,(0,255,0),3)
    
    for contour in contours:
        (x,y,w,h)=cv.boundingRect(contour)
        
        if cv.contourArea(contour)<800:
            continue
        cv.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    
    cv.imshow('Video',frame1)
    frame1=frame2
    ret,frame2=cap.read()
    
    key=cv.waitKey(1)
    if key==ord('q'):
        break
cap.release()
cv.destroyAllWindows()