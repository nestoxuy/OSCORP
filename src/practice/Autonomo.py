from gpiozero import Button, Servo, Motor, DistanceSensor, DigitalInputDevice, DigitalOutputDevice
from time import sleep, time
from signal import pause

sensor_pin1 = 20
"""

"""


PIN_S0 = 14
PIN_S1 = 27
PIN_S2 = 10
PIN_S3 = 23
PIN_OUT = 22

_s0 = None
_s1 = None
_s2 = None
_s3 = None
_out_pin = None

sensor_1 = DigitalInputDevice(sensor_pin1)
"""
sensor_3 = DigitalInputDevice(sensor_pin3)
"""
button = Button(17)

Sensor1 = DistanceSensor(12,0, max_distance = 1 , threshold_distance=0.1)

Sensor2 = DistanceSensor(24,13, max_distance = 1 , threshold_distance = 0.1)

servo = Servo(2, min_pulse_width=500/1_000_000, max_pulse_width=2500/1_000_000)

motor = Motor(forward=3, backward=4)

robot_enmarcha = False
loop_blue = 0
loop_red = 0

def initialize_tcs230_pins():
    """
    Inicializa los pines GPIO para el sensor TCS230.
    Debe llamarse una vez al inicio del programa principal.
    """
    global _s0, _s1, _s2, _s3
    _s0 = DigitalOutputDevice(PIN_S0)
    _s1 = DigitalOutputDevice(PIN_S1)
    _s2 = DigitalOutputDevice(PIN_S2)
    _s3 = DigitalOutputDevice(PIN_S3)
    # No inicializamos _out_pin aquí porque se crea y cierra en cada llamada a get_color_frequency.
    # Esto es para evitar problemas si otras partes del código necesitan acceder al pin OUT.
    print("Pines del TCS230 inicializados.")

def cleanup_tcs230_pins():
    """
    Libera los pines GPIO utilizados por el sensor TCS230.
    Debe llamarse al finalizar el programa para una limpieza adecuada.
    """
    if _s0: _s0.close()
    if _s1: _s1.close()
    if _s2: _s2.close()
    if _s3: _s3.close()
    # _out_pin se cierra dentro de get_color_frequency
    print("Pines del TCS230 liberados.")

# --- Función para configurar la escala de frecuencia (S0, S1) ---
def set_frequency_scaling(scale):
    """
    Configura la escala de frecuencia de salida del TCS230.
    scale:
        0: Apagado
        1: 2%
        2: 20%
        3: 100%
    """
    if _s0 is None or _s1 is None:
        print("Error: Pines S0/S1 no inicializados. Llame a initialize_tcs230_pins() primero.")
        return

    if scale == 0: # Apagado
        _s0.off()
        _s1.off()
    elif scale == 1: # 2%
        _s0.off()
        _s1.on()
    elif scale == 2: # 20%
        _s0.on()
        _s1.off()
    elif scale == 3: # 100%
        _s0.on()
        _s1.on()
    else:
        print("Escala de frecuencia no válida. Usando 100% por defecto.")
        _s0.on()
        _s1.on()
    sleep(0.01) # Pequeña pausa después de cambiar la configuración

# --- Función para seleccionar el filtro de color (S2, S3) ---
def select_color_filter(color):
    """
    Selecciona el filtro de color para el TCS230.
    color:
        'red': Filtro rojo
        'green': Filtro verde
        'blue': Filtro azul
        'clear': Sin filtro
    """
    if _s2 is None or _s3 is None:
        print("Error: Pines S2/S3 no inicializados. Llame a initialize_tcs230_pins() primero.")
        return

    if color == 'red':
        _s2.off()
        _s3.off()
    elif color == 'blue':
        _s2.off()
        _s3.on()
    elif color == 'green':
        _s2.on()
        _s3.on()
    elif color == 'clear':
        _s2.on()
        _s3.off()
    else:
        print(f"Color '{color}' no válido. Seleccionando 'clear' por defecto.")
        _s2.on()
        _s3.off()
    sleep(0.01) # Pequeña pausa después de cambiar la configuración

# --- Función para leer la frecuencia de un color específico ---
def get_color_frequency(color, num_pulses=100):
    """
    Mide la frecuencia de un color dado por el sensor TCS230.
    color: 'red', 'green', 'blue', 'clear'
    num_pulses: Número de pulsos a contar para la medición de frecuencia.
                Un valor más alto da mayor precisión pero toma más tiempo.
    Retorna la frecuencia en Hz.
    """
    if _s2 is None or _s3 is None:
        print("Error: Pines S2/S3 no inicializados. Llame a initialize_tcs230_pins() primero.")
        return 0

    select_color_filter(color)
    sleep(0.01) # Pequeña pausa para que el sensor se estabilice

    # El pin de salida se abre y cierra en esta función porque es una lectura puntual.
    # Esto evita problemas si otras partes del código quisieran usar el pin_out.
    # Sin embargo, abrir y cerrar DigitalInputDevice repetidamente puede introducir una pequeña latencia.
    # Para mayor rendimiento, se podría hacer que _out_pin sea global y se inicialice una vez.
    # Pero para este nivel de abstracción, es una compensación aceptable.
    out_pin = DigitalInputDevice(PIN_OUT)

    start_time = time()
    pulse_count = 0
    # Esperamos el primer flanco alto para asegurar que empezamos a contar en un punto conocido
    # Agregamos un timeout para evitar bucles infinitos si no hay señal.
    timeout_start = time()
    while not out_pin.is_active: # Espera hasta que el pin esté HIGH
        if time() - timeout_start > 0.1: # Timeout de 100ms
            out_pin.close()
            return 0.0 # No se detectaron pulsos
        pass

    # Contar flancos de bajada (o de subida) para medir los pulsos
    # Hacemos 2*num_pulses porque cada ciclo tiene un flanco de subida y uno de bajada
    for _ in range(num_pulses * 2): # Esperamos num_pulses * 2 transiciones (subida y bajada por pulso)
        if out_pin.is_active: # Si está HIGH, esperamos que baje
            timeout_loop = time()
            while out_pin.is_active:
                if time() - timeout_loop > 0.1: # Timeout para evitar bloqueo
                    break
            pulse_count += 0.5
        else: # Si está LOW, esperamos que suba
            timeout_loop = time()
            while not out_pin.is_active:
                if time() - timeout_loop > 0.1: # Timeout para evitar bloqueo
                    break
            pulse_count += 0.5

    end_time = time()
    elapsed_time = end_time - start_time

    frequency = 0.0
    if elapsed_time > 0:
        frequency = pulse_count / elapsed_time

    out_pin.close()
    return frequency

# --- Función para identificar el color a partir de las frecuencias ---
def identify_color(red_freq, green_freq, blue_freq, clear_freq):
    """
    Identifica el color a partir de las frecuencias RGB.
    ¡Requiere calibración! Los umbrales son ejemplos.
    """
    MIN_LIGHT_THRESHOLD = 500 # Hz

    if red_freq < MIN_LIGHT_THRESHOLD and green_freq < MIN_LIGHT_THRESHOLD and blue_freq < MIN_LIGHT_THRESHOLD:
        return "Negro (o muy oscuro)"
    elif red_freq > 12000 and green_freq > 12000 and blue_freq > 12000 and clear_freq > 35000: # Umbral alto para blanco
        return "Blanco"
    # Lógica para Naranja (requiere calibración fina)
    # Se busca un rojo dominante, un verde significativo, y un azul muy bajo.
    # Estos coeficientes son para ajustar: (red_freq / green_freq) y (red_freq / blue_freq)
    # Por ejemplo, si al calibrar con un naranja obtienes R=5000, G=3000, B=500:
    # 5000/3000 = 1.66 y 5000/500 = 10
    # Entonces podrías usar algo como `red_freq / green_freq > 1.5 and red_freq / blue_freq > 8`
    # O, como en el ejemplo anterior, una comparación directa con multiplicadores:
    
    elif red_freq > green_freq and red_freq > blue_freq:
        return "Rojo"
    elif green_freq > red_freq and green_freq > blue_freq:
        return "Verde"
    elif blue_freq > red_freq and blue_freq > green_freq:
        return "Azul"
    else:
        return "Desconocido (requiere calibración)"

    
   
def robot_status():
    initialize_tcs230_pins()
    set_frequency_scaling(3) # Escala al 100%
    
    global robot_enmarcha
    global loop_blue
    global loop_red
    global Sensor1
    global Sensor2
    
    
    if robot_enmarcha:
           
        print("Stop")
        motor.stop()  
        robot_enmarcha = False
       
    else:
        print("Avanzando")
        
            
        while loop_blue or loop_red != 12:


            red_freq = get_color_frequency('red')
                

            green_freq = get_color_frequency('green')
               

            blue_freq = get_color_frequency('blue')
                

            clear_freq = get_color_frequency('clear')
              

            detected_color = identify_color(red_freq, green_freq, blue_freq, clear_freq)
            
            
            if detected_color == "Azul":
                    
                loop_blue += 1
                
            elif detected_color == "Rojo":
                    
                loop_red += 1
            try:
                print("hola")
                sleep(1)
                if Sensor2.distance >= 0.25 and Sensor1.distance >= 0.25:
                    motor.forward()
                    servo.value = 0
        
                
                elif Sensor2.distance <= 0.24 and Sensor1.distance >= 0.24:
                    servo.value = -1
                
                elif Sensor2.distance >= 0.24 and Sensor1.distance <= 0.24:
                    servo.value = 1
            except Exception as e:
                print("error", e)
            if loop_blue ==  12:
                motor.forward(0.85)
                sleep(0.7)
                motor.stop()
                robot_enmarcha = True
                break
            elif loop_red == 12:
                motor.forward(0.85)
                sleep(0.7)
                motor.stop()
                robot_enmarcha = True
                break
         
    
                

    
            
"""
        motor.stop()
        robot_enmarcha = True
        
"""       
button.when_pressed = robot_status

pause()
            