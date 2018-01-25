from controller import *
from display import *
import time

speed = None
schwellwert = None

"""schliesst die schranke
"""
def schranke_zu():
  global speed, schwellwert
  O7.set_brightness(0)
  O5.set_brightness(254)
  time.sleep(1)
  if not I2.get_state():
    M1.set_speed(1 * speed)
    while not I2.get_state():
      pass
    M1.stop()

"""oeffnet die Schranke
"""
def schranke_auf():
  global speed, schwellwert
  if not I3.get_state():
    M1.set_speed(-1 * speed)
    while not I3.get_state():
      pass
    M1.stop()
  O5.set_brightness(0)
  O7.set_brightness(254)


speed = 500
O5.set_brightness(254)
O7.set_brightness(254)
schwellwert = 0
O3.set_brightness(512)
time.sleep(1)
schwellwert = schwellwert - -1 * I1.get_state()
O3.set_brightness(0)
time.sleep(1)
schwellwert = schwellwert - -1 * I1.get_state()
schwellwert = schwellwert / 2
O3.set_brightness(512)
schranke_zu()
while True:
  if I1.get_state() < schwellwert:
    schranke_auf()
  else:
    if I3.get_state():
      time.sleep(5)
    if I1.get_state() >= schwellwert:
      schranke_zu()
