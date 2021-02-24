import cv2
import os

vidcap =cv2.VideoCapture('video.mp4')
success,image = vidcap.read()

choice = int(input(" 1 for extracting frame every one seond and 2 to extract all frames : "))

if choice == 1 :
    pass
    count = 0
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) # extract frame every one second, remove this line if you want to extract every frame
        cv2.imwrite("frame%d.jpg"% count,image)
        success,image = vidcap.read()
        print("Read a new frame",success)
        count +=1
else:
    print("Extracting each frame")
    count = 0
    while success:
      cv2.imwrite("everyframe%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1
      
print("Cleaning the terminal")

os.system("cls")
