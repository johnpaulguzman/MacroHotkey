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
    pass
    """
    actuator = Actuator()
    combos = {
        ('shift', 'f9'): (restart, ),
        ('shift', 'f12'): (stop, ),
        ('z'): (mammonite, actuator),
    }
    h = HotkeyHandler(combos, debug=True)
    h.start()
    execute = False
    while True:
        if keyboard.is_pressed('['): execute = True
        elif keyboard.is_pressed(']'): execute = False
        if execute: mammonite(actuator)
        sleep(0.05)
    """

from pywinauto.application import Application
from time import sleep

(w, h) = (1920, 1080)
var = 0.15
cooldown = 10
process_id = int(input("Enter PID: "))
def clicks():
    wrapper.click_input(coords=(int(0.50 * w), int(0.50 * h)))
    wrapper.click_input(coords=(int((0.50 - var) * w), int(0.50 * h)))
    wrapper.click_input(coords=(int(0.50 * w), int((0.50 + var) * h)))
    wrapper.click_input(coords=(int((0.50 + var) * w), int(0.50 * h)))
    wrapper.click_input(coords=(int(0.50 * w), int((0.50 - var) * h)))
    wrapper.minimize()

app = Application().connect(process=process_id)
wrapper = app.window().wrapper_object()
while(True):
    clicks()
    sleep(cooldown)