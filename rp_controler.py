import RPi.GPIO as GPIO
from time import sleep


def start_pump():

    GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD
    GPIO.setup(18, GPIO.OUT)  # set GPIO24 as an output

    i=0
    while i < 20:
            GPIO.output(24, 1)  # set GPIO24 to 1/GPIO.HIGH/True
            sleep(0.5)  # wait half a second
            GPIO.output(24, 0)  # set GPIO24 to 0/GPIO.LOW/False
            sleep(0.5)  # wait half a second
            i = i+1


    GPIO.cleanup()