from gpiozero import MotionSensor
from signal import pause


#############################
#   Motion Sensor Pins      #
#       (Upside down)       #
#   _____________________   #
#   |                   |   #
#   |                   |   #
#   |                   |   #
#   |_____ 1 2 3 _______|   #
#                           #
#   1: VCC                  #
#   2: OUT                  #
#   3: GND                  #
#                           #
#############################


motion_sensor = MotionSensor(23)


def motion():
    print("Motion detected")


def no_motion():
    print("Motion stopped")


print("Readying sensor...")
motion_sensor.wait_for_no_motion()
print("Sensor ready")

motion_sensor.when_motion = motion
motion_sensor.when_no_motion = no_motion

pause()
