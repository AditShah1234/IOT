import argparse
import sys
import time
import face_recognition
import cv2
import pickle
print(cv2.__version__)

def extractImages(name="",max_count=10,save_file_path = "asset"):
    encode_list=[]
    count = 0
    vidcap = cv2.VideoCapture(0)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
        success,image = vidcap.read()
        
        print ('Read a new frame: ', success)
        image = cv2.resize(image,(300,300))
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        boxes = face_recognition.face_locations(rgb,model ="hog")
        encodings = face_recognition.face_encodings(rgb, boxes)
        for encoding in encodings:
            encode_list.append(encoding)
        # cv2.imwrite( "asset//"+name+"_frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1
        if cv2.waitKey(1) & 0xFF == ord('q') or count ==max_count:
            print(save_file_path+"ihuihiuhu")
            f = open(save_file_path+"//"+name, "wb")
            f.write(pickle.dumps(encode_list))
            f.close()
            break
        time.sleep(1)
    return save_file_path+"//"+name
if __name__=="__main__":
 
  
    file = extractImages()
    print(file)
    