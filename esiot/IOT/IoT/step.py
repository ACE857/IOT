import RPi.GPIO as GPIO
import time

TRUE = 1

GPIO.setmode(GPIO.BCM)

control_pins = [22,23,24,25]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin,0)

halfstep_seq = [
  [0,1,1,1],
  [0,0,1,1],
  [1,0,1,1],
  [1,0,0,1],
  [1,1,0,1],
  [1,1,0,0],
  [1,1,1,0],
  [0,1,1,0]
 ]

while TRUE:
  for halfstep in range(8):
	for pin in range(4):
		GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
	time.sleep(0.001)

GPIO.cleanup()