import RPi.GPIO as GPIO
import time


def reset_all():
	GPIO.cleanup()
	GPIO.setmode(GPIO.BOARD)
	return None

def setup_servo(pin_num):
	GPIO.setup(pin_num, GPIO.OUT)
	p1 = GPIO.PWM(pin_num, 50)
	return p1