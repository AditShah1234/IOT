import argparse
import sys
import time

import cv2

print(cv2.__version__)

def extractImages(name="",max_count=10):
    count = 0
    vidcap = cv2.VideoCapture(0)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
        success,image = vidcap.read()
        
        print ('Read a new frame: ', success)
        cv2.imwrite( "asset//"+name+"_frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1
        if cv2.waitKey(1) & 0xFF == ord('q') or count ==max_count:
            break
        time.sleep(1)
    
if __name__=="__main__":
 
  
    extractImages()
    