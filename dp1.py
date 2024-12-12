from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
img1= cv2.imread("d1.png")
img2= cv2.imread("d2.png")
    
plt.imshow(img1[:,:,::-1])
plt.show()
plt.imshow(img2[:,:,::-1])
plt.show()
output = DeepFace.verify("d1.png","d2.png")
print(output)
verification = output['verified']
if verification:
      print('They are same')
else:
       print('The are not same')