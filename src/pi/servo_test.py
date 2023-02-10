import RPi.GPIO as GPIO
from gpiozero import Servo
import time


# Initialize the GPIO pin as an output
def setup_servo():
    servo_pin = 25
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servo_pin, GPIO.OUT)

    # Create a PWM instance with a 50Hz frequency
    pwm_servo = GPIO.PWM(servo_pin, 50)
    pwm_servo.start(0)
    return pwm_servo

# Define the duty cycle required to rotate the servo to a specific angle
def set_angle(angle,pwm_servo):
    servo_pin = 25
    duty = (angle / 18) + 2
    GPIO.output(servo_pin, True)
    pwm_servo.ChangeDutyCycle(duty)
    time.sleep(0.3)
    GPIO.output(servo_pin, False)
    pwm_servo.ChangeDutyCycle(0)

def dispense(pwm_servo):
    target = 50
    for i in range(0,target,10):
        set_angle(i,pwm_servo)

    time.sleep(1)
    set_angle(0,pwm_servo)


# Servo(50)
# servo_pin = 25
# pwm_servo = setup_servo()
# dispense(pwm_servo)

# # Clean up the GPIO when done
# GPIO.cleanup()
