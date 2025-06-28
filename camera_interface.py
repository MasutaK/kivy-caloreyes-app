from plyer import camera
from time import time

def take_picture(callback):
    path = f"/sdcard/{int(time())}.jpg"
    camera.take_picture(path, lambda x: callback(x))
