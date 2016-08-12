import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for x in range(25,29):
	print "setting pin %d" % (x)
	GPIO.setup(x,GPIO.OUT)
for x in range(25,29):
	print "LED %d on" % (x)
	GPIO.output(x,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(x,GPIO.LOW)
	print "LED %d off" % (x)
	time.sleep(1)
print("Done.")
