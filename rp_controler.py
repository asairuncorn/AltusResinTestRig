import time

def start_pump(button_id, proces_time):
    print("message recived to controler", button_id, proces_time)
    print("---------------------------------------")


    def countdown_timer(duration):
        seconds = 0
        while seconds < duration:
            print(f"Elapsed time: {seconds} seconds", end='\r')  # Display time in-place
            time.sleep(1)  # Wait for 1 second
            seconds += 1
        print(f"Elapsed time: {seconds} seconds")  # Display final time when done

    # Run the timer for a specified number of seconds (e.g., 10)
    countdown_timer(10)


def stop_pomp(button_id):
    print("message recived to controler", button_id)
    print("---------------------------------------")

# import RPi.GPIO as GPIO
# from time import sleep
#
#
# def start_pump():
#
#     GPIO.setmode(GPIO.BOARD)  # choose BCM or BOARD
#     GPIO.setup(18, GPIO.OUT)  # set GPIO24 as an output
#
#     i=0
#     while i < 20:
#             GPIO.output(18, 1)  # set GPIO24 to 1/GPIO.HIGH/True
#             sleep(0.5)  # wait half a second
#             GPIO.output(18, 0)  # set GPIO24 to 0/GPIO.LOW/False
#             sleep(0.5)  # wait half a second
#             i = i+1
#
#
#     GPIO.cleanup()