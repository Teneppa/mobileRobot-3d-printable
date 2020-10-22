import serial

# Coded by Teemu Laurila
# Date:
#
# This is a control software for the mobile robot
#
# Do NOT use without persmission.


class motorControl:
    # =====================================================
    # Initialize variables for the control software
    # =====================================================
    def __init__(self):
        self.ser = None
        self.motorSpeed = [0, 0, 0, 0]

    # =====================================================
    # Set digital I/O to be outputs
    # =====================================================
    def begin(self):
        self.ser = serial.Serial("/dev/ttyUSB0", 115200)

    # =====================================================
    # Set speed and direction for the motors
    # =====================================================
    def setSpeed(self, motorID, speed):
        if(speed < -255 or speed > 255):
            return
        else:
            self.motorSpeed[motorID] = speed

    # =====================================================
    # This function needs to be run at less that 100 ms
    # intervals to refresh the motor controller.
    # =====================================================
    def run(self):
        self.ser.write(f"{self.motorSpeed[0]},{self.motorSpeed[1]},\
                            {self.motorSpeed[2]},{self.motorSpeed[3]};".encode())

    def close(self):
        self.ser.close()
