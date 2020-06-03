#import necessary modules
import RPi.GPIO as GPIO
import picamera
import time
import requests

#Set up GPIO pins for PIR motion sensor
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)
camera = picamera.PiCamera()
#flips camera image as i had the camera upside down
camera.vflip = True

#Sets a variable to be used in the photo file name
var = 0
while True:
	#set variable to represent motion captured 
	motion=GPIO.input(11)
	#if motion = 1, motion was detected
	if motion == 1:
		#printing "working" is not necessary, I have used it to monitor that the motion sensor is working but it would not be needed in a fully developed system
		print("Working")
		camera.capture('motion'+(str)(var)+'.jpg')
		var = var + 1
		#code to post request is modified from "https://thepihut.com/blogs/raspberry-pi-tutorials/using-ifttt-with-the-raspberry-pi" as I could not find appropriate API
		requests.post('https://maker.ifttt.com/trigger/motionPetMaybs/with/key/dYvYNT8VZgRAGgX2LuOa8q', params ={"value1":"none","value2":"none","value3":"none"})
		#Motion detection pauses for 2 minutes to give user the time to take action
		time.sleep(120)

	elif motion == 0:
		print("yep, def working")
		time.sleep(1)



