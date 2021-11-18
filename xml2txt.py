
'''
transfrom the xml pascal voc to txt yolo

pascal voc:   x_min  y_min  x_max  y_max

yolo  :  x_center y_center  width height

'''
import xml.etree.ElementTree as ET
import pickle
import os
import cv2
from os import listdir, getcwd, path
from os.path import join
import numpy as np

position=['xmin','ymin','xmax','ymax']
width='width'
height='height'

root_path='/home/zyh/KTH/ICECAP/DataSet/MASATI-v2/'
multi_labels_path='ship_labels'
multi_image_path='ship'

def convert(p,w,h):
    
    xmin=float(p[0])
    ymin=float(p[1])
    xmax=float(p[2])
    ymax=float(p[3])
    #print(xmin,ymin,xmax,ymax)
    xcenter=(xmin+xmax)/2.0
    ycenter=(ymin+ymax)/2.0

    xcenter/=w
    ycenter/=h
    
    width=(xmax-xmin)/(w)
    height=(ymax-ymin)/(h)
    
    return (xcenter,ycenter,width,height)


def convert_xml_to_txt(xml_absolute_path,xml_id,txt_save_dir,w,h):
    print(w,h)
    '''
    path: the absolute path of the xml file
    '''
    #the save
    #create the txt file
    txt_file_path=join(txt_save_dir,xml_id+'.txt')
    txt_obj=open(txt_file_path,'w')

    tree = ET.parse(xml_absolute_path)
    root = tree.getroot()

    #element.find('name'): find the child 'name', not recursive 
    #print(root.find('size').find(width).text)
    
    



    for obj in root.iter('object'):
        #print("=============")
        bndbox=obj.find('bndbox')
        p=[]
        for pos in position:
            p.append(bndbox.find(pos).text)

        (xcenter,ycenter,width,height)=convert(p,w,h)
        txt_obj.write(str(1)+' ')
        txt_obj.write(str(xcenter)+' ')
        txt_obj.write(str(ycenter)+' ')
        txt_obj.write(str(width)+' ')
        txt_obj.write(str(height)+'\n')

    txt_obj.close()

        

    
#wd = getcwd() #get current path
#print(wd)



dir_path=join(root_path,multi_labels_path)
txt_save_dir=join(root_path,multi_labels_path+'_txt')

if not os.path.exists(txt_save_dir):
    os.mkdir(txt_save_dir)

dir_list=listdir(dir_path)



xml_absolute_list=[]
xml_id_list=[]
for xml_name in dir_list:
    new=(join(dir_path,xml_name))
    #print(xml_name,new)
    xml_absolute_list.append(new)
    tmp=xml_name.split('.')
    
    xml_id_list.append(tmp[0])
    #pass



for i in range(len(xml_absolute_list)):
    
   
    image=cv2.imread(join(root_path,multi_image_path,xml_id_list[i]+'.png'))
    image =cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    w=image.shape[0]
    h=image.shape[1]

    convert_xml_to_txt(xml_absolute_list[i],xml_id_list[i],txt_save_dir,w,h)

