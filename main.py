from PIL import Image
import numpy as np
from math import radians, tan,sqrt

def openimg(Imgname):
    with Image.open(f"./images/{Imgname}") as img:
        img_matrix = np.array(img)


    
    y,x = np.where(np.all(img_matrix == [200,10,30,255], axis =-1))

    return x,y,len(img_matrix[1])


img1 = input("\nEnter image 1 name:\n> ")
img2 = input("\nEnter image 2 name:\n> ")

x1, y1, w1 = openimg(img1)
x2, y2, w2 = openimg(img2)

print(x1)
print(y1)
print(w1)
W_i = w1
O_i = sqrt((x2[0]-x1[0])**2)
print(O_i)


O_r = float(input("\nInput camera Offset (meters):\n> "))
W_r = (O_r * W_i)/O_i
FOV = float(input("\nInput camera FOV(in degrees):\n> "))


print(f'\nDistance: {W_r/(2*tan(radians(FOV/2)))} meters')

