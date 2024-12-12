from deepface import DeepFace
import cv2
img = cv2.imread('d1.png')
cv2.imshow("Myimage",img)
obj = DeepFace.analyze(img_path = "d1.png", actions = ['age', 'gender', 'race', 'emotion'])
#print(obj["age"]," years old ",obj["dominant_race"]," ",obj["dominant_emotion"]," ", obj["gender"])
print(obj)
for x in obj:
    print("Age  ",x["age"])
    print("Gender  ",x["dominant_gender"])
    print("Race  ",x["dominant_race"])
    print("Empotion  ",x["dominant_emotion"])
    