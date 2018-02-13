import RPi.GPIO as GPIO
import time
from subprocess import call
GPIO.setmode(GPIO.BCM)
TRIG = 23 #trigger pin
ECHO = 24 #echo pin
LED = 2 #pin for led
LED2=17 #pin for led
LED3=27 #pin for led
LED4=3 #pin for led
#print "Distance Measurement In Progress"
GPIO.setup(LED,GPIO.OUT)
GPIO.setup(LED2,GPIO.OUT)
GPIO.setup(LED3,GPIO.OUT)
GPIO.setup(LED4,GPIO.OUT)
GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setwarnings(False)
while True:
        GPIO.output(TRIG, False)
        time.sleep(2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO)==0:
                pulse_start = time.clock()
        while GPIO.input(ECHO)==1:
                pulse_end = time.clock()
	pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        if distance > 50:
                #reset
                call(["echo","reset"])
                GPIO.output(LED,False)
                GPIO.output(LED2,False)
                GPIO.output(LED3,False)
                GPIO.output(LED4,False)
	else:
                #print "The distance is %f"%(distance)
                #glow led1 when distance is between 14 and 18 cm
                if distance<18 and distance>=14:
                        call(["echo","lots to go"])
                        GPIO.output(LED,True)
                        GPIO.output(LED2,False)
                        GPIO.output(LED3,False)
                        GPIO.output(LED4,False)
                #glow led1,led2 when distance is between 14 and 10 cm
                elif distance<14 and distance>=10:
			call(["echo","filling"])
                        GPIO.output(LED,True)
                        GPIO.output(LED2,True)
                        GPIO.output(LED3,False)
                        GPIO.output(LED4,False)
                #glow led1,led2,led3 when distance is between 10 and 5 cm
                elif distance<10 and distance>=5:
                        call(["echo","almost full"])
                        GPIO.output(LED,True)
                        GPIO.output(LED2,True)
                        GPIO.output(LED3,True)
                #glow all leds if distance is less than 5cm
                elif distance<5:
                        #type code to send push notification
                        call(["echo","Dustbin full !! "])
                        call(["echo","notification sent to municipality !!"])
                        GPIO.output(LED,True)
                        GPIO.output(LED2,True)
                        GPIO.output(LED3,True)
                        GPIO.output(LED4,True)


