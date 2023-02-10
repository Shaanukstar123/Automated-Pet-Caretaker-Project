
import servo_test as servo
import weight_test as weight
import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins used by the TB6612FNG controller
AIN1 = 26
AIN2 = 19
STBY = 21
PWM_PIN = 12

# Set the GPIO pins as outputs
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

# Set the STBY pin to active
GPIO.output(STBY, GPIO.HIGH)

# Initialize PWM on the PWM_PIN with a frequency of 50 Hz
pwm = GPIO.PWM(PWM_PIN, 50)

def allStop():
    # Set all pins to LOW
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.stop()

def forwardDrive(speed):
    # Set the AIN1 pin to HIGH and AIN2 to LOW
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    # Start PWM with the specified duty cycle
    pwm.start(speed)

def reverseDrive(speed):
    # Set the AIN1 pin to LOW and AIN2 to HIGH
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    # Start PWM with the specified duty cycle
    pwm.start(speed)

# Example usage
allStop()

servo_pin = 25
hx = weight.setup_weight()
pwm_servo = servo.setup_servo()

while True:
	forwardDrive(20)
	val = weight.measure(hx)
	if val>15:
		allStop()
		servo.dispense(pwm_servo)


sleep(100)
#allStop()
#reverseDrive(50)
#sleep(2)
allStop()

# Clean up the GPIOs
GPIO.cleanup()
