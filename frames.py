import cv2
import argparse

vidcap =cv2.VideoCapture('video.mp4')
success,image = vidcap.read()
count = 0
while success:
    vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) # extract frame every one second, remove this line if you want to extract every frame
    cv2.imwrite("frame%d.jpg"% count,image)
    success,image = vidcap.read()
    print("Read a new frame",success)
    count +=1
