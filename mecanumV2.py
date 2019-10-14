from motorControl import motorControl

import pygame
import os

os.environ["SDL_VIDEODRIVER"] = "dummy"
pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

axisValues = [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]

speed = 100

m = motorControl()
m.begin()

print('Press ESC to exit')

try:
	while True:
		events = pygame.event.get()

		for event in events:
			if event.type == pygame.JOYAXISMOTION:
				axisValues[event.axis] = event.value
				print(axisValues)

		# Stop
		if (axisValues[0] > -0.2 and axisValues[0] < 0.2) and (axisValues[1] > -0.2 and axisValues[1] < 0.2):
			m.setSpeed(0, 0)
			m.setSpeed(1, 0)
			m.setSpeed(2, 0)
			m.setSpeed(3, 0)

		# Move forward
		if axisValues[1] < -0.2 and axisValues[0] > -0.6 and axisValues[0] < 0.6:
			m.setSpeed(0, speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, speed)

		# Move backwards
		if axisValues[1] > 0.2:
			m.setSpeed(0, speed*(-axisValues[1]))
			m.setSpeed(1, speed*(-axisValues[1]))
			m.setSpeed(2, speed*(-axisValues[1]))
			m.setSpeed(3, speed*(-axisValues[1]))

		# Move forward at 45 degree angle to the right
		if axisValues[1] < -0.2 and axisValues[0] > 0.6:
			m.setSpeed(0, speed)
			m.setSpeed(1, 0)
			m.setSpeed(2, speed)
			m.setSpeed(3, 0)

		# Move backwards at 45 degree angle to the left
		if axisValues[1] > 0.2 and axisValues[0] < -0.6:
			m.setSpeed(0, -speed)
			m.setSpeed(1, 0)
			m.setSpeed(2, -speed)
			m.setSpeed(3, 0)

		# Move forward at 45 degree angle to the left
		#if key == 'q':
		#	m.setSpeed(0, 0)
		#	m.setSpeed(1, speed)
		#	m.setSpeed(2, 0)
		#	m.setSpeed(3, speed)

		# Move backwards at 45 degree angle to the right
		#if key == 'c':
		#	m.setSpeed(0, 0)
		#	m.setSpeed(1, -speed)
		#	m.setSpeed(2, 0)
		#	m.setSpeed(3, -speed)

		# Strafe right
		if axisValues[0] > 0.6 and axisValues[1] > -0.2 and axisValues[1] < 0.2:
			m.setSpeed(0, speed)
			m.setSpeed(1, -speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, -speed)

		# Strafe left
		if axisValues[0] < -0.6 and axisValues[1] > -0.2 and axisValues[1] < 0.2:
			m.setSpeed(0,- speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, -speed)
			m.setSpeed(3, speed)

		# Turn left:
		if axisValues[3] > 0.6:
			m.setSpeed(0, speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, -speed)
			m.setSpeed(3, -speed)

		# Turn right
		if axisValues[3] < -0.6:
			m.setSpeed(0, -speed)
			m.setSpeed(1, -speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, speed)

except KeyboardInterrupt:
	print("Exitting...")
	j.quit()

m.setSpeed(0, 0)
m.setSpeed(1, 0)
m.setSpeed(2, 0)
m.setSpeed(3, 0)

m.close()
#termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
