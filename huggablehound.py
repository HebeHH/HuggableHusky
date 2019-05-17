import facebookhugs
import RPi.GPIO as GPIO
import time
import random

def main():
	GPIO.setmode(GPIO.BOARD)
	print "GPIO setup"

	GPIO.setup(3, GPIO.IN)
	print "current signal: %r" %GPIO.input(3)

	hour_count = 0
	total_count = 0
	last_hug_time = time.time()
	print "hour count set to: %d \ntotal count set to: %d" %(hour_count, total_count)

	while True:
		print "in infinite loop"

		if GPIO.input(3):
			print "teddy hugged!"
			hour_count+=1
			total_count+=1
			last_hug_time=time.time()

			if total_count%3==0:
				facebookhugs.main("I just got hugged!!")
			elif total_count%3==1:
				facebookhugs.main("Thank you for your love :) :)")
			elif total_count%3==2:
				facebookhugs.main("Another hug down!")

			print "facebook message sent!"

			while GPIO.input(3):
				time.sleep(3)
				print "still pressed..."

		if time.time()/(60*60)==0:
			print "it's the hour!"
			msg = "In the past hour, I've been hugged %d times!" %hour_count
			facebookhugs.main(msg)
			print "facebook announcedment sent"
			hour_count = 0

		if total_count == 100:
			facebookhugs.main("I just received my hundredth hug! If this was from you, please visit XXXXXX to collect your prize!")
			print "finally been hugged a hundred times!"

		if time.time()-last_hug_time>60*random.randint(20,50):
			msg = "Aaw, I haven't been hugged in %d minutes and %d seconds. I'm sad. Please come give me love!" %(
				(time.time()-last_hug_time)/60, 
				(time.time()-last_hug_time)%60)


if __name__ == "__main__":
  main()