from gpiozero import LED
from time import sleep
sensor = DistanceSensor(17, 3, max_distance=12, threshold_distance=0.1)
led = LED(17)
while True:
    print('Distancia del sensor', sensor.distance, 'm')
    sleep(1)
    sensor.when_in_range = led.on
    sensor.when_out_of_range = led.off
    led.on()
    sleep(1)

