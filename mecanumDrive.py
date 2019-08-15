from motorControl import motorControl

# Coded by Teemu Laurila
# Date: 15.8.2019
#
# This is a test software
# to test out some of the 
# features of the mecanum
# wheels. This code doesn't
# have all of the movements
# yet!
#
# NOTICE!
#
# If you don't restore the buffer settings,
# your terminal session will break. If that
# happens, just close the session and open
# a new one.
#
# Do NOT use without permission.

# Keyboard
import tty
import sys
import termios

# Save original settings and change the
# mode of the input buffer
orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
key = 0
oldKey = 0
speed = 100

# Create an object of the motorControl
# and start the motors up
m = motorControl()
m.begin()

print('Press ESC to exit')

# Run the code
while key != chr(27): #ESC
	key = sys.stdin.read(1)[0]

	if key != oldKey:

		# Stop [S]
		if key == 's':
			m.setSpeed(0, 0)
			m.setSpeed(1, 0)
			m.setSpeed(2, 0)
			m.setSpeed(3, 0)

		# Move forward [W]
		if key == 'w':
			m.setSpeed(0, speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, speed)

		# Move backwards [X]
		if key == 'x':
			m.setSpeed(0, -speed)
			m.setSpeed(1, -speed)
			m.setSpeed(2, -speed)
			m.setSpeed(3, -speed)

		# Strafe right [D]
		if key == 'd':
			m.setSpeed(0, speed)
			m.setSpeed(1, -speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, -speed)

		# Strafe left [A]
		if key == 'a':
			m.setSpeed(0,- speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, -speed)
			m.setSpeed(3, speed)

		# Turn left [H]
		if key == 'h':
			m.setSpeed(0, speed)
			m.setSpeed(1, speed)
			m.setSpeed(2, -speed)
			m.setSpeed(3, -speed)

		# Turn right [G]
		if key == 'g':
			m.setSpeed(0, -speed)
			m.setSpeed(1, -speed)
			m.setSpeed(2, speed)
			m.setSpeed(3, speed)

		oldKey = key

# Set all of the speeds to zero
m.setSpeed(0, 0)
m.setSpeed(1, 0)
m.setSpeed(2, 0)
m.setSpeed(3, 0)

# Shut the motors down and
# restore input buffer settings
m.close()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
