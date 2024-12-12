import cv2
import mysql.connector
con=mysql.connector.connect(host='localhost',user='root',password='',database='aadhar')
cur=con.cursor()

faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
image = cv2.imread("14.jpg")



gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow("Tital",gray)
# cv2.waitKey(0)  

faces = faceCascade.detectMultiScale(gray,1.1,minNeighbors=5)

for (x, y, w, h) in faces:
    a1=cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
x1=image.shape[:2]

 
s="select * from aadhar"
cur.execute(s)
x=0
for row in cur:
    x=x+1
    img=row[13]
    img2=cv2.imread("test\\"+img)
    x2=image.shape[:2]
    cv2.imshow("Tital",img2)

    cv2.waitKey(0)
    gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,minNeighbors=5)
    for (x, y, w, h) in faces:
        a2=cv2.rectangle(img2, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    if(x1==x2):
        print("Both Size Image are same")
        difference=cv2.subtract(image,img2)
        b,g,r=cv2.split(difference)
        if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0:
            print(row)
            break
        else:
            print("Image are not same")
    else:
        print("Image have differnt size")