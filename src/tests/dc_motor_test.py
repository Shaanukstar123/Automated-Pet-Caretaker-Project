# from gpiozero import PWMOutputDevice
# from gpiozero import DigitalOutputDevice
# from time import sleep
# # import RPi.GPIO as GPIO
# from gpiozero import OutputDevice



# # GPIO.setmode(GPIO.BCM)
# # GPIO.setup(18,GPIO.OUT)

# # print((GPIO.input(18)))
 
# #///////////////// Define Motor Driver GPIO Pins /////////////////
# # Motor A, Left Side GPIO CONSTANTS
# PWM_DRIVE_LEFT = 26		# ENA - H-Bridge enable pin
# FORWARD_LEFT_PIN = 23	# IN1 - Forward Drive
# REVERSE_LEFT_PIN = 24	# IN2 - Reverse Drive
 
# # Initialise objects for H-Bridge GPIO PWM pins
# # Set initial duty cycle to 0 and frequency to 1000
# driveLeft = PWMOutputDevice(PWM_DRIVE_LEFT)#, True, 0, 1000)
 
# # Initialise objects for H-Bridge digital GPIO pins
# forwardLeft = DigitalOutputDevice(FORWARD_LEFT_PIN)
# reverseLeft = DigitalOutputDevice(REVERSE_LEFT_PIN)
 
# # output_pin = OutputDevice(18)
# # print((output_pin in output_pin.input_devices))

# def allStop():
# 	forwardLeft.value = False
# 	reverseLeft.value = False
# 	driveLeft.value = 0
 
# def forwardDrive():
# 	forwardLeft.value = True
# 	reverseLeft.value = True
# 	driveLeft.value = 1.0
 
# def reverseDrive():
# 	forwardLeft.value = False
# 	reverseLeft.value = True
# 	driveLeft.value = 1.0
	
# allStop()
# forwardDrive()
# #reverseDrive()
# sleep(2)
# allStop()

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
forwardDrive(50)
sleep(100)
#allStop()
#reverseDrive(50)
#sleep(2)
allStop()

# Clean up the GPIOs
GPIO.cleanup()
