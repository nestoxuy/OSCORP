from gpiozero import Servo, Motor, Button, LED, DistanceSensor, DigitalInputDevice
from time import sleep
from signal import pause
       
led=LED(24)
"""

Sensor1 = DistanceSensor(9,22, max_distance = 0.5 , threshold_distance=0.0000001)
"""
"""
Sensor2 = DistanceSensor(14,18,max_distance = 0.2, threshold_distance=0.1 )
"""

button = Button(17)
button2 = Button(15)

servo = Servo(2, min_pulse_width=500/1_000_000, max_pulse_width=2500/1_000_000)
motor = Motor(forward=3, backward=4)

led.on()

robot_enmarcha = False
loops = 3
def robot_status():

    global robot_enmarcha

    if robot_enmarcha:
       
        print("Stop")
        motor.stop()  
        robot_enmarcha = False
   
    else:
       
        print("Avanzando")
        motor.forward()
        sleep(2.35)
           
        servo.value = -0.4
        sleep(0.59)
       
        servo.value = 0
        sleep(1)
       
        motor.forward()
        sleep(1.1)
       
           
           
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
       
       
           
           
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(2)
       
           
           
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
                       
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.7)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.5)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(1.75)
       
        servo.value = -0.4
        sleep(0.59)
        servo.value = 0
        motor.forward()
        sleep(0.7)
       
        motor.stop()
        robot_enmarcha = True

button.when_pressed = robot_status

pause()
