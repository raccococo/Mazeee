import RPi.GPIO as GPIO
import time

class LedControl:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.green_pin = 17  # Change this to the GPIO pin connected to the green LED
        self.red_pin = 18    # Change this to the GPIO pin connected to the red LED
        GPIO.setup(self.green_pin, GPIO.OUT)
        GPIO.setup(self.red_pin, GPIO.OUT)

    def turn_on_green(self):
        GPIO.output(self.green_pin, GPIO.HIGH)
        GPIO.output(self.red_pin, GPIO.LOW)

    def turn_on_red(self):
        GPIO.output(self.green_pin, GPIO.LOW)
        GPIO.output(self.red_pin, GPIO.HIGH)

    def turn_off_red(self):
        GPIO.output(self.red_pin, GPIO.LOW)

    def get_result(self):
        # Replace this with the logic to get the result from the fourth program
        return 0

if __name__ == "__main__":
    # You can test the LED control independently if needed
    led_controller = LedControl()
    led_controller.turn_on_green()
    time.sleep(2)
    led_controller.turn_on_red()
    time.sleep(2)
    led_controller.turn_off_red()
    GPIO.cleanup()