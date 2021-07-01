# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

name = 'sifiso'
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.start_preview()
time.sleep(11)
for i in range(10):
    camera.capture("/home/pi/Face Recognition/dataset/sifiso/"+name+str(i)+'.jpg')
camera.stop_preview()    