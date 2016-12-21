import time
from __init__ import *

b = WifiLedBulb("192.168.1.61")
time.sleep(2)
# b.turnOff()
# time.sleep(2)
# b.turnOn()
# time.sleep(2)
# b.setRgbw(255,0,0,100, True, 50)
# b.setRgbw(255,0,0,0, True, 255)
# b.setRgb(255,0,0)
# b.setNiceColor(217,50,206, 60)
# time.sleep(2)
# print(b.brightness)
# time.sleep(2)
# b.setNiceColor(217,50,206,2)
# b.setNiceColor(255,0,0,100)
# time.sleep(2)
# b.setNiceColor(255,0,0,20)
print(b.getNiceColor())
# print(utils.color_rgb_to_rgbw(181,219,232))

