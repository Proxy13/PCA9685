
#!/usr/bin/python
from __builtin__ import input

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

print ('informations::::::')
print ('Angle Between 0-180 Deg')
b = (input('Cycle ? '))
a = (input('channel number ? '))
c = (input('Min Angle ? '))
d = (input('Max Angle ? '))

fmin = (150 + (c * 2.5))
fmax = (600 - (d * 2.5))

print ('Fmin value : ', fmin)
print ('Fmax value : ', fmax)




# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
#pwm = PWM(0x40, debug=True)

servoMin = 150  # Min pulse length out of 4096   150
servoMax = 600 # Max pulse length out of 4096    650

def setServoPulse(channel, pulse):
  pulseLength = 1000000                   # 1,000,000 us per second
  pulseLength /= 60                       # 60 Hz
  print "%d us per period" % pulseLength
  pulseLength /= 4096                     # 12 bits of resolution
  print "%d us per bit" % pulseLength
  pulse *= 1000
  pulse /= pulseLength
  pwm.setPWM(channel, 0, pulse)

pwm.setPWMFreq(60)                        # Set frequency to 60 Hz


while (b >= 1):

  print ('tur', b)
  b = b-1

  pwm.setPWM(a, 0, fmin)
  time.sleep(1)
  pwm.setPWM(a, 0, fmax)
  time.sleep(1)

  if (b == 0):
    break

