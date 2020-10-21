from serialMotorControl import motorControl

# Keyboard
import tty
import sys
import termios

orig_settings = termios.tcgetattr(sys.stdin)
tty.setcbreak(sys.stdin)
key = 0
oldKey = 0
speed = 255

m = motorControl()
m.begin()

print('Press ESC to exit')

while key != chr(27): #ESC

    key = sys.stdin.read(1)[0]
    m.run()
        
    if key != oldKey:

        # Stop
        if key == 's':
            m.setSpeed(0, 0)
            m.setSpeed(1, 0)
            m.setSpeed(2, 0)
            m.setSpeed(3, 0)


        # Move forward
        if key == 'w':
            m.setSpeed(0, speed)
            m.setSpeed(1, speed)
            m.setSpeed(2, speed)
            m.setSpeed(3, speed)

        # Move backwards
        if key == 'x':
            m.setSpeed(0, -speed)
            m.setSpeed(1, -speed)
            m.setSpeed(2, -speed)
            m.setSpeed(3, -speed)

        # Move forward at 45 degree angle to the right
        if key == 'e':
            m.setSpeed(0, speed)
            m.setSpeed(1, 0)
            m.setSpeed(2, speed)
            m.setSpeed(3, 0)

        # Move backwards at 45 degree angle to the left
        if key == 'z':
            m.setSpeed(0, -speed)
            m.setSpeed(1, 0)
            m.setSpeed(2, -speed)
            m.setSpeed(3, 0)

        # Move forward at 45 degree angle to the left
        if key == 'q':
            m.setSpeed(0, 0)
            m.setSpeed(1, speed)
            m.setSpeed(2, 0)
            m.setSpeed(3, speed)

        # Move backwards at 45 degree angle to the right
        if key == 'c':
            m.setSpeed(0, 0)
            m.setSpeed(1, -speed)
            m.setSpeed(2, 0)
            m.setSpeed(3, -speed)

        # Strafe right
        if key == 'd':
            m.setSpeed(0, speed)
            m.setSpeed(1, -speed)
            m.setSpeed(2, speed)
            m.setSpeed(3, -speed)

        # Strafe left
        if key == 'a':
            m.setSpeed(0,- speed)
            m.setSpeed(1, speed)
            m.setSpeed(2, -speed)
            m.setSpeed(3, speed)

        # Turn left
        if key == 'h':
            m.setSpeed(0, speed)
            m.setSpeed(1, speed)
            m.setSpeed(2, -speed)
            m.setSpeed(3, -speed)

        # Turn right
        if key == 'g':
            m.setSpeed(0, -speed)
            m.setSpeed(1, -speed)
            m.setSpeed(2, speed)
            m.setSpeed(3, speed)

        oldKey = key

m.setSpeed(0, 0)
m.setSpeed(1, 0)
m.setSpeed(2, 0)
m.setSpeed(3, 0)

m.close()
termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)
