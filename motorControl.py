import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM

# Coded by Teemu Laurila
# Date: 23.6.2019
#
# This is a control software for the mobile robot
#
# Do NOT use without persmission.

class motorControl:
	#=====================================================
	# Initialize variables for the control software
	#=====================================================
	def __init__(self):
		# Vasen moottorinohjain
		self.l1 = "P9_14"
		self.l2 = "P9_12"
		self.l3 = "P9_16"
		self.l4 = "P9_15"

		# Oikea moottorinohjain
		self.r1 = "P8_13"
		self.r2 = "P8_11"
		self.r3 = "P8_19"
		self.r4 = "P8_17"

	#=====================================================
	# Set digital I/O to be outputs
	#=====================================================
	def begin(self):
		GPIO.setup(self.l2, GPIO.OUT)
		GPIO.setup(self.l4, GPIO.OUT)
		GPIO.setup(self.r2, GPIO.OUT)
		GPIO.setup(self.r4, GPIO.OUT)

	#=====================================================
	# Set speed and direction for the motors
	#=====================================================
	def setSpeed(self, motorID, speed):
		if speed < -100 or speed > 100:
			print('Error: speed greater than 100')
			return

		if motorID == 1 or motorID == 2:
			speed = speed * -1

		dir = -1
		if speed < 0:
			dir = -1
		if speed > 0:
			dir = 1

		if motorID == 0:
			#PWM.start(self.l1, abs(speed), 1000)
			if dir == 1:
				GPIO.output(self.l2, GPIO.HIGH)
				PWM.start(self.l1, 100-abs(speed), 1000)
			else:
				GPIO.output(self.l2, GPIO.LOW)
				PWM.start(self.l1, abs(speed), 1000)

		if motorID == 1:
                        #PWM.start(self.l3, abs(speed), 1000)
			if dir == 1:
				GPIO.output(self.l4, GPIO.HIGH)
				PWM.start(self.l3, 100-abs(speed), 1000)
			else:
				GPIO.output(self.l4, GPIO.LOW)
				PWM.start(self.l3, abs(speed), 1000)

		if motorID == 2:
                        #PWM.start(self.r1, abs(speed), 1000)
			if dir == 1:
				GPIO.output(self.r2, GPIO.HIGH)
				PWM.start(self.r1, 100-abs(speed), 1000)
			else:
				GPIO.output(self.r2, GPIO.LOW)
				PWM.start(self.r1, abs(speed), 1000)

		if motorID == 3:
                        #PWM.start(self.r3, abs(speed), 1000)
			if dir == 1:
				GPIO.output(self.r4, GPIO.HIGH)
				PWM.start(self.r3, 100-abs(speed), 1000)
			else:
				GPIO.output(self.r4, GPIO.LOW)
				PWM.start(self.r3, abs(speed), 1000)

	def close(self):
		PWM.stop(self.l1)
		PWM.stop(self.l3)
		PWM.stop(self.r1)
		PWM.stop(self.r3)
		GPIO.cleanup()
