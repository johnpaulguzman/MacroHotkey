from Actuator import Actuator
# from HotkeyHandler import HotkeyHandler
import keyboard

import os
import sys
from time import sleep

def restart():
    print("Restarting script...\n")
    os.execl(sys.executable, sys.executable, *sys.argv)

def stop():
    print("Sending stop signal to listener...\n")
    return False

def mammonite(actuator):
    print("Mammonite!!")
    actuator.send_clicks(interval=0)


if __name__ == '__main__':
    actuator = Actuator()
    """ combos = {
        ('shift', 'f9'): (restart, ),
        ('shift', 'f12'): (stop, ),
        ('z'): (mammonite, actuator),
    }
    h = HotkeyHandler(combos, debug=True)
    h.start()"""
    (pressed, counter) = (False, 0)
    while True:
        if pressed == False and pressed != keyboard.is_pressed('shift'): counter += 1
        if counter % 2 == 1: mammonite(actuator)
        sleep(0.1)
