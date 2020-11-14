import cv2
import numpy as np
import glob

img_array = []
g = sorted(glob.glob('final_img/*.jpg'))
print(g)
for filename in g:
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width, height)
    img_array.append(img)

out = cv2.VideoWriter('object_tracking.avi', cv2.VideoWriter_fourcc(*'DIVX'), 10, size)

for i in range(len(img_array)):
    out.write(img_array[i])
out.release()