# Simple script to make an LED blink

from gpiozero import LED
from signal import pause

led = LED(17)
led.blink()

pause()
