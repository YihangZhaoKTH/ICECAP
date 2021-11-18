
from posixpath import split
import albumentations as A
import cv2 

import matplotlib.pyplot as plt
from draw import drawBbox
import xml.etree.ElementTree as ET

from os import listdir, getcwd, path
from os.path import join
'''
root_path='/home/zyh/KTH/ICECAP/DataSet/MASATI-v2/'
ca_path='coast_ship'

dir_list=listdir(join(root_path,ca_path))
for str in dir_list:
    if str.strip.split('.')[-1]=='png':
        image_path = join(root_path,ca_path,str)
        label_path = join(root_path,ca_path,str.strip().split('.')[0]+'.txt')
        foo(image_path,label_path)

'''
image_path='/home/zyh/KTH/ICECAP/DataSet/MASATI-v2/coast_ship/x0010.png'
label_path='/home/zyh/KTH/ICECAP/DataSet/MASATI-v2/coast_ship_labels_txt/x0010.txt'




transform = A.Compose([
    #A.RandomCrop(width=450, height=450),
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
], bbox_params=A.BboxParams(format='yolo'))


image = cv2.imread(image_path)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


label_obj=open(label_path,'r')
content=(label_obj.read())
content=content.strip().split()
group=len(content)/5
bboxes=[]
for i in range(int(group)):
    bboxes.append([float(content[1+5*i]), 
    float(content[2+5*i]),
    float(content[3+5*i]), 
    float(content[4+5*i]),
    1,  ]  )




transformed = transform(image=image, bboxes=bboxes)
transformed_image = transformed['image']
transformed_bboxes = transformed['bboxes']

#print(transformed_bboxes[0])
for i in range(len(transformed_bboxes)):
    transformed_image=drawBbox(transformed_image,transformed_bboxes[i])

#transformed_image=drawBbox(transformed_image,transformed_bboxes[1])


plt.imshow(transformed_image)
plt.show()
