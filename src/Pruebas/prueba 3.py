import RPi.GPIO as GPIO
'''import time
TRIG_PIN=3
ECHO_PIN=17
led = 2
led2 = 4
led3 = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
def measure_distance():
    GPIO.output(TRIG_PIN, True)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, False)
    pulse_start = time.time()
    while GPIO.input(ECHO_PIN) == 0:
        pulse_start = time.time()
    pulse_end =time.time()
    while GPIO.input(ECHO_PIN) ==1:
        pulse_end = time.time()
    pulse_durat = pulse_end - pulse_start
   
    dist = (pulse_durat * 34300) / 2
    return dist
try:
    while True:
        dist = measure_distance()
        print("distance: {:.2f} cm".format(dist))
        time.sleep(0.5)  
       
        if dist >= 30.0 and dist <=40.0:
            GPIO.output(led, True)
            GPIO.output(led2, True)
            GPIO.output(led3, True)
        else:
            GPIO.output(led, False)
            GPIO.output(led2, False)
            GPIO.output(led3, False)
           
           
except KeyboardInterrupt:
    print("stop")
finally:
    GPIO.cleanup()

'''
import time
boton = 3
LED = 4
LED2 = 27
LED3 = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(boton, GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)

# GPIO.output(LED, False)
# try:
#     while True:
#         if GPIO.input(boton) == GPIO.LOW:
#             GPIO.output(LED, True)
#         else:
#             GPIO.output(LED, False)
#         time.sleep(0.1)
# except KeyboardInterrupt:
#     print("stop")
try:
    while True:
        if GPIO.input(boton) == GPIO.LOW:
            GPIO.output(LED, True)
            print("encendido")
            time.sleep(1)
            GPIO.output(LED2, True)
            time.sleep(2)
            GPIO.output(LED3, True)
            time.sleep(3)
        else:
            GPIO.output(LED, False)
            GPIO.output(LED2, False)
            GPIO.output(LED3, False)
            print("en")
except KeyboardInterrupt:
    print("error")
