import cv2
from PIL import Image
#read files/ size
import os

#img=Image.open("Images\landscpape.jpg")
#print(img.size)

path="D:/OpenCV/Lesson 6/Images"

#changedirectory--> folder
os.chdir(path)

#. --> go inside path for the listing
print(os.listdir("."))

images=os.listdir(".")
average_w=0
average_h=0

for img in images:
    image=Image.open(os.path.join(path,img))
    w,h=image.size
    average_w+=w
    average_h+=h

num=len(images)
average_width=average_w//num
average_height=average_h//num

for img in images:
    image=Image.open(os.path.join(path,img))
    image_resize=image.resize((average_width,average_height))
    image_resize.save(img, "JPEG", quality=90)

video="MyFirstDiapo.avi"
frame=cv2.imread(os.path.join(path, images[0]))
vid=cv2.VideoWriter(video,0,1,(average_width,average_height))

for img in images:
    if img.endswith('.jpg'):
        vid.write(cv2.imread(os.path.join(path, img)))

vid.release()