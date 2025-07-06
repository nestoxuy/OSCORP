from gpiozero import DigitalInputDevice, DistanceSensor,Button, Servo, Motor, DigitalOutputDevice
from time import sleep
button = Button(17)
sensor_pin1 = 20
Sensor1 = DistanceSensor(12,0, max_distance = 1.1 , threshold_distance=1.09)
sensor_1 = DigitalInputDevice(sensor_pin1)
Sensor2 = DistanceSensor(24,13, max_distance = 1.1 , threshold_distance = 1.09)

servo = Servo(2, min_pulse_width=500/1_000_000, max_pulse_width=2500/1_000_000)

motor = Motor(forward=3, backward=4)
contador = 0


while True:
            
            
    if sensor_1.is_active and Sensor2.distance >= 0.45 and Sensor1.distance >= 0.45:
        motor.forward(0.825)
        servo.value = 0      
    elif Sensor2.distance <= 0.55 and Sensor1.distance >= 0.45 and sensor_1.is_active:
        servo.value = -0.57
        motor.forward(0.75)
     
    elif Sensor2.distance >= 0.45 and Sensor1.distance <= 0.55 and sensor_1.is_active:
        servo.value = 1
        motor.forward(0.75)
    elif not sensor_1.is_active and Sensor2.distance >= 0.45 or Sensor2.distance <=0.55 and Sensor1.distance >= 0.45 or Sensor1.distance <= 0.55 :
        motor.backward()
        sleep(1.5)
        
    


            
