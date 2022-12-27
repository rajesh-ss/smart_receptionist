
import cv2
import RPi.GPIO as GPIO
from time import sleep
from gpiozero import Servo
import time
import os
import demo
import subprocess

GPIO.setmode(GPIO.BCM)
 
 #set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27


base_servo = Servo(2)
upper_servo = Servo(3)


#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)



val = -1
base_servo.value = val
upper_servo.value = 0


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# capture frames from a camera
cap = cv2.VideoCapture(0)

forExit = True




def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
 

# loop runs if capturing has been initialized.
while forExit:
    
    
    #base_servo.value = val
    #upper_servo.value = val
    #sleep(0.1)
    #val = val + 0.05
    #if val > 1:
        #val = -1
        
    # reads frames from a camera
    ret, img = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_SIMPLEX

    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)




    for (x,y,w,h) in faces:
        # To draw a rectangle in a face
        cv2.putText(img,'face detected',(x+30,y-20),font, 1,(0, 255, 255),2,cv2.LINE_4)
        print("x: ",x)
        print("y: ",y)
        print(distance())
        if(distance()<60):
            #cmd = os.path.join(os.getcwd(), "demo.py")
            #os.system('{} {}'.format('python', cmd))
            #os.system("~/speakRecognitionDemo/demo.py")
            #execfile('demo.py')
            #os.system('python demo.py')
            forExit = False
            break
            #subprocess.call("demo.py", shell=True)
        if(x<=180):
            base_servo.value = val
            sleep(0.1)
            val = val + 0.05
            if val>1:
                val = val-0.05
#        if (x>181 and x<229):
#            print("in center")
        if(x>230):
            base_servo.value = val
            sleep(0.1)
            val = val - 0.05
            if val<1:
                val = val+0.05
            
        
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        # Detects eyes of different sizes in the input image
        eyes = eye_cascade.detectMultiScale(roi_gray)

        #To draw a rectangle in eyes
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)

    # Display an image in a window
    cv2.imshow('img',img)

    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()

