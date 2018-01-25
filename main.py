from controller import *
from display import *
import time

speed = None

"""oeffnet die Schranke
"""
def schranke_auf():
  global speed
  if not I3.get_state():
    M1.set_speed(-1 * speed)
    while not I3.get_state():
      pass
    M1.stop()
  O5.set_brightness(0)
  O7.set_brightness(254)

"""schliesst die schranke
"""
def schranke_zu():
  global speed
  O7.set_brightness(0)
  O5.set_brightness(254)
  time.sleep(1)
  if not I2.get_state():
    M1.set_speed(1 * speed)
    while not I2.get_state():
      pass
    M1.stop()


speed = 500
O3.set_brightness(512)
O5.set_brightness(254)
O7.set_brightness(254)
time.sleep(3)
schranke_zu()
while True:
  if not I1.get_state():
    schranke_auf()
  else:
    if I3.get_state():
      time.sleep(5)
    if I1.get_state():
      schranke_zu()
