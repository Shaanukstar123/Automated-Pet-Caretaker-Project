import weight_test as weight
import servo_test as servo
import dc_motor_test as motor
import time

def stop():
    motor.allStop()

def start_dispense(target):
    print(target)
    hx = weight.setup_weight()
    pwm_servo = servo.setup_servo()
    avg = 0
    servo.dispense(pwm_servo)
    hx.tare()
    window = []
    speed = 100
    motor.reverseDrive(speed)
    time.sleep(0.5)
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
        
        print("Average: ",avg)
        if avg>target:
            running = False
            print("DISPENSING!")
            motor.allStop()
            servo.dispense(pwm_servo)
            hx.tare()
            break
            




