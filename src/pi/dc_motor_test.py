
# import servo_test as servo
# import weight_test as weight
import RPi.GPIO as GPIO
import time
import servo_test as servo

GPIO.setmode(GPIO.BCM)
AIN1 = 26
AIN2 = 19
STBY = 21
PWM_PIN = 12

# Set the GPIO pins as outputs
GPIO.setup(AIN1, GPIO.OUT)
GPIO.setup(AIN2, GPIO.OUT)
GPIO.setup(STBY, GPIO.OUT)
GPIO.setup(PWM_PIN, GPIO.OUT)

GPIO.output(STBY, GPIO.HIGH)

pwm = GPIO.PWM(PWM_PIN, 50)

stuck_speed = 100

def allStop():
    pwm.start(0)
    pwm.stop()
    # Set all pins to LOW
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.LOW)
    #GPIO.setup(AIN1, GPIO.OUT)
    #GPIO.setup(AIN2, GPIO.OUT)
    

def forwardDrive(speed):
    GPIO.output(AIN1, GPIO.HIGH)
    GPIO.output(AIN2, GPIO.LOW)
    pwm.start(speed)

def reverseDrive(speed):
    GPIO.output(AIN1, GPIO.LOW)
    GPIO.output(AIN2, GPIO.HIGH)
    pwm.start(speed)

def unstuck():
    reverseDrive(stuck_speed)
    time.sleep(0.5)
    forwardDrive(stuck_speed)
    time.sleep(0.5)
    reverseDrive(stuck_speed)
    time.sleep(0.5)
    forwardDrive(stuck_speed)
    time.sleep(0.5)
