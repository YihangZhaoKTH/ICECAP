import cv2
import numpy as np

def drawBbox(image,label):
    xcenter=(float(label[0])*512)
    ycenter=(float(label[1])*512) 

    width=float(label[2]*512)
    height=float(label[3]*512)


    start_point=(int( xcenter-0.5*width   ),int(ycenter-0.5*width)   )
    end_point=(int( xcenter+0.5*width   ),int(ycenter+0.5*width)   )

    #print(start_point,end_point)
    color=(0,255,0)
    thick=2
    image = cv2.rectangle(image,start_point,end_point,color=color,thickness=thick)
    return image