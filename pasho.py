import threading
import os
from time import sleep
import subprocess

period = 60 * 20
duration = 60 * 2

def func():
    while True:
        sleep(period)
        b = subprocess.check_output('sudo cat /sys/class/backlight/intel_backlight/brightness', shell=True).decode('utf-8').strip()
        os.system('echo 0 | sudo tee /sys/class/backlight/intel_backlight/brightness')
        sleep(duration)
        os.system('echo {} | sudo tee /sys/class/backlight/intel_backlight/brightness'.format(b))

threading.Thread(target=func).start()

