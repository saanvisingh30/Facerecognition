import cv2
vid=cv2.VideoCapture("12.mp4")
ret,img=vid.read()
x=0
a=0
while ret:
    if a%30==0:
     cv2.imwrite("allfiles//"+str(x)+".jpg",img)
     x=x+1
     print(" Image Created ",x)
    ret,img=vid.read() 
    a=a+1  
                  

cv2.waitKey(0)