import weight_test as weight
import servo_test as servo
import dc_motor_test as motor
import time


def start_dispense():
    servo_pin = 25
    hx = weight.setup_weight()
    pwm_servo = servo.setup_servo()
    count = 0
    target = 10
    avg = 0
    total = 0
    error = 0.5*target
    servo.dispense(pwm_servo)
    hx.tare()
    window = []
    stuck_speed = 100
    speed = 100
    motor.reverseDrive(speed)
    time.sleep(0.5)
    change_in_weight = 0
    elapsed_time = 0
    while True:
        elapsed_time = time.time()
        if int(elapsed_time)%2==0:
            motor.reverseDrive(speed)
        else:
            
            motor.forwardDrive(speed)
        val = weight.measure(hx)
        if len(window)<4:
            change_in_weight = val

        if len(window)>4:
            window.pop(0)
        window.append(val)
        window = sorted(window)
        change_in_weight = avg - window[(len(window)//2)]
        avg = window[(len(window)//2)]
        # if change_in_weight<2.5 and elapsed_time>2:
        #     elapsed_time=  0
        #     start_time = time.time()
        #     unstuck()
        

        if avg>target:
            motor.allStop()
            servo.dispense(pwm_servo)
            hx.tare()
