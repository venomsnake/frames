import cv2
import os

#Takes video
file = input("Enter video name: ")
vidcap =cv2.VideoCapture(file)
success,image = vidcap.read()
print("Current File Name : ",os.path.realpath(file)) #Shows the file path


choice = int(input("Press 1 to extract each frame after one second and 2 All frames : "))

if choice == 1 :
    count = 0
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000)) # extract frame every one second
        cv2.imwrite("frame%d.jpg"% count,image) # Save frame as JPEG file
        success,image = vidcap.read()
        print("Read a new frame: ",success)
        count +=1
        
elif choice == 2:
    print("Extracting each frame")
    count = 0
    while success:
      cv2.imwrite("everyframe%d.jpg" % count, image)     # save frame as JPEG file      
      success,image = vidcap.read()
      print('Read a new frame: ', success)
      count += 1

    print("Cleaning the Terminal")
    os.system("cls")
      
else:
    print("Closing the Terminal")
    for i in range (1,6):
        print("Closing in" , i , "seconds")
        os.system("exit()")
    
