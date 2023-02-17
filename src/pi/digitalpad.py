import RPi.GPIO as GPIO
import time

L1 = 14
L2 = 2
L3 = 3
L4 = 4

C1 = 23
C2 = 24
C3 = 22
C4 = 27

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

def readLine(line, characters, numpad):
    GPIO.output(line, GPIO.HIGH)
    if(GPIO.input(C1) == 1):
        if characters[0] not in ['A','B','C']:
            numpad.append(characters[0])
    if(GPIO.input(C2) == 1):
        if characters[1] not in ['A','B','C']:
            numpad.append(characters[1])
    if(GPIO.input(C3) == 1):
        if characters[2] not in ['A','B','C']:
            numpad.append(characters[2])
    if(GPIO.input(C4) == 1):
        if characters[3] not in ['A','B','C']:
            numpad.append(characters[3])
    GPIO.output(line, GPIO.LOW)
    return numpad

def get_key(numpad):
    readLine(L1, ["1","2","3","A"], numpad)
    readLine(L2, ["4","5","6","B"], numpad)
    readLine(L3, ["7","8","9","C"], numpad)
    readLine(L4, ["*","0","#","D"], numpad)
    time.sleep(0.2)
    return numpad