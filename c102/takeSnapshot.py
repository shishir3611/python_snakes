from tkinter import image_names
import cv2
import time
import random
import dropbox

start_time = time.time()
def takeSnapshot():
    number = str(random.randint(1,100))
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        #read the frames while the camera is on
        ret, frame = videoCaptureObject.read()
        #cv2.imwrite() is used to save an image
        image_name = 'img' +number+'.png'
        cv2.imwrite(image_name,frame)
        start_time = time.time()
        result = False
    return image_name
    print('Snapshot taken!')
    
    #close the camera
    videoCaptureObject.release()
    #close all the windows that are open
    cv2.destroyAllWindows()

def upload_file(image_name):
    access_token='sl.BBWvH43QGRg0IstGV2FJ4h5Hc7i2uxraS_1K8eErPyUF1o-Ou_GXPHebl2Ya7R6GiIqkeV4YF6F7QZ1ZPuydlfuD7KCxETD210FMpOPliqdWNiKuVb3L7vzYqEyajxIYy6wduB0'
    file = image_name
    file_from = file
    file_to = "/images/"+(image_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if((time.time()- start_time)>=5):
            name = takeSnapshot()
            upload_file(name)


main()