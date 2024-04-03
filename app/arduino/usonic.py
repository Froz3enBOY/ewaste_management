import time
from pymata4 import pymata4
import os
trigpin=9
ecopin=10
board=pymata4.Pymata4()
def the_callback(data):
    print("distance: ", data[2])
    if data[2]<100:
        #os.startfile("C:\\Program Files\\Sublime Text 3\\sublime_text.exe")
        print("too close")
board.set_pin_mode_sonar(trigpin, ecopin, the_callback)
#count=0
while True:
    try:
        time.sleep(0.1)
        board.sonar_read(trigpin)
    except Exception:
        board.shutdown()
