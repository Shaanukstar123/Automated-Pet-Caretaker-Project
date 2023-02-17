import weight_test as weight
import servo_test as servo
import dc_motor_test as motor
import time

def stop():
    motor.allStop()

def start_dispense(target):
    print(target)
    servo_pin = 25
    hx = weight.setup_weight()
    pwm_servo = servo.setup_servo()
    count = 0
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
    running = True
    start_time = time.time()
    while running:
        elapsed_time = time.time()
        print("Elapsed TIme: ",elapsed_time)

        if elapsed_time>start_time+120:
            running = False
            print("DISPENSING!")
            motor.allStop()
            servo.dispense(pwm_servo)
            hx.tare()
            break

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
        
        print("Average: ",avg)
        if avg>target:
            running = False
            print("DISPENSING!")
            motor.allStop()
            servo.dispense(pwm_servo)
            hx.tare()
            break
            




