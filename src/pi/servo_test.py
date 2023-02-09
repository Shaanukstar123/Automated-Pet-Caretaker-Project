import RPi.GPIO as GPIO
import time

# Initialize the GPIO pin as an output
servo_pin = 25
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo_pin, GPIO.OUT)

# Create a PWM instance with a 50Hz frequency
pwm = GPIO.PWM(servo_pin, 50)
pwm.start(0)

# Define the duty cycle required to rotate the servo to a specific angle
def set_angle(angle):
    duty = (angle / 18) + 2
    GPIO.output(servo_pin, True)
    pwm.ChangeDutyCycle(duty)
    time.sleep(0.3)
    GPIO.output(servo_pin, False)
    #pwm.ChangeDutyCycle(0)

# Example: rotate the servo to 90 degrees
set_angle(50)
time.sleep(1)
set_angle(0)


# Clean up the GPIO when done
GPIO.cleanup()