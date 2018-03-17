from __future__ import print_function
import threading
from flask import Flask
from flask_ask import Ask, statement, convert_errors, convert
import RPi.GPIO as GPIO
import logging
import time as tm
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.OUT)
NUM_OF_TIMERS = 0

app = Flask(__name__)
ask = Ask(app, '/')



#class timer_thread(threading.Thread):
def run(timedelta=0):
	global NUM_OF_TIMERS
	if NUM_OF_TIMERS < 5:
		NUM_OF_TIMERS = NUM_OF_TIMERS + 1
		print ("timer started")
		tm.sleep(timedelta)
		print ("coffee on")
		GPIO.output(4,True)
		tm.sleep(15)
		NUM_OF_TIMERS = NUM_OF_TIMERS - 1
		print ("coffee off")
		GPIO.output(4,False)


'''
so now we do:
  Timer = timer_thread(name="timer {}".format(timer_number))
  Timer.start(desired_time)
  return statement("timer started")
bc setting a timer does work but the skill times out
we can use this for both timer and a desired time we just 
need to calculate the time difference which should be trivial
we should also set a limit on the number of timers bc each timer
is a thread so if people set a lot of timers we will get a 
lot of threads on the pi and slow down or even crash 
'''

#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

'''
@ask.intent('GPIOControlIntent', mapping={'status': 'status', 'pin': 'pin'})
def gpio_control(status, pin):
    try:
        pinNum = int(pin)
    except Exception as e:
        return statement('Pin number not valid.')
    GPIO.setup(pinNum, GPIO.OUT)
    if status in ['on', 'high']:    GPIO.output(pinNum, GPIO.HIGH)
    if status in ['off', 'low']:    GPIO.output(pinNum, GPIO.LOW)
    return statement('Turning pin {} {}'.format(pin, status))
'''
''' mapping={'settime':'time'},'''
@ask.intent('SetTimeIntent', convert={'on_time':'time'})
def set_time(on_time):
	#---NEEDS TESTING -----------------------------------
	time_now = datetime.now()
	#quantity = (on_time - time_now).total_seconds()
	quantity = 6
	TIMER = threading.Thread(target=run,args=(quantity,))
	TIMER.start()
	return statement("coffee will brew at {}".format(on_time))
	# ---------------------------------------------------
	#pass

@ask.intent('SetTimerIntent', mapping={'quantity':'quantity', 'units':'units'})
def set_timer(quantity, units):
	
	Oquantity = quantity
	if units == "seconds" or units=="second":
		quantity = int(quantity)

    	elif units == "minute" or units=="minutes":
		quantity = int(quantity) * 60
		#TIMER.start(secConv)
 	elif units == "hours" or units=="hour":
        	quantity = int(quantity) * 3600
        	#if starting instead of duration:
        	#TIMER.start(secConv)
	else:
		return statement("Please try again")
	#TIMER = timer_thread(name="timer {}".format(NUM_OF_TIMERS),args=(quantity))
	TIMER = threading.Thread(target=run,args=(quantity,))
	TIMER.start()
	return statement("coffee will brew in {} {}".format(Oquantity, units))


@ask.intent('OnIntent')
def turn_on():
	GPIO.output(4,True)

	return statement('Coffee pot is on')

@ask.intent('OffIntent')
def turn_off():
	GPIO.output(4,False)

	return statement('Coffee pot is off')
