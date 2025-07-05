# Lista de componenes usados

|nombre|descripción|imágen|
|------|-----------|------|
| **Motor Module** | This module manages the movement and performance of the motors, in addition to managing the energy flow| ![module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/modulo_de_motores.jpg "motor module") |
| **Anti-Slip Wheels** |Designed to increase traction and reduce the risk of losing friction and slipping on the track |![Anti-Slip_Wheels](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/ruedas_antiresbalantes.jpg "Anti-slip wheels")|
| **Color Sensor** |Measures light intensity at different wavelengths to determine object colors and sends signals to identify colors|![Color_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/sensor_de_color.jpg "Color_sensor")|
# Lista de componenes usados

|nombre|descripción|imágen|
|-frared radiation (IR) through one LED acting as transmitter. The signal bounces back and is detected by another LED acting as receiver. Measures received IR radiation level and return time to calculate object distance|![Infrared_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/sensor_infrarrojos.jpg "Infrared_sensor")|
# Lista de componenes usados
| **Dupont Wires and Breadboard** | Dupont wires connect to Raspberry Pi5's programmable pins and provide electrical connections for sensors (5V and GND pins). The breadboard serves as intermediary for connections, facilitating pin management and power distribution for sensors|![Dupont_Wires_and_Breadboard](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Proto_Board_y_cables_Dupont.jpeg "Dupont_wires_and_breadboard")|
| **Transparent Acrylic Bases** |Primary foundation for the entire assembly. The two-tiered base holds directional components/motors (lower level) and allows mounting/screwing of electronic components (upper level)|![Transparent_Acrylic_Bases](https://github.com# Lista de componenes usados

|nombre|descripción|imágen|
|-frared radiation (IR) throher/Fotos/base.jpg "Transparent_acrylic_bases")|
| **Raspberry Pi5**|The motherboard - the robot's brain. Features: 8GB RAM, 4GB ROM, dual 4K GPU support, PCI Express interface. Ports: 2x HDMI, 4x USB (2x USB2.0 + 2x USB3.0), Gigabit Ethernet, 27 programmable pins (2x 3V, 2x 5V, 8x GND), USB-C power, microSD slot. Power: 5V-3A (min) to 5V-5A (max)|![Raspberry_Pi5](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/raspberry-pi-5-03.jpg "Raspberry_Pi5")|
| **Hexagonal Pillar Screw Kit**|Used to create structural pillars enabling two levels: Lower (motors/directional components) and upper (wiring, Raspberry Pi5, battery, breadboard, sensors)|![Hexagonal_Pillar_Screw_Kit](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Kit_de_tornillos_hexagonales_para_pilares.jpg "Hexagonal_pillar_screw_kit")|
| **7.4V 6200mAh Rechargeable Lithium Battery**|Primary power source for Raspberry Pi and installed sensors|![7.4V_6200mAh_Rechargeable_Lithium_Battery](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Bateria_de_Litio_recargable_de_7.4V_y_6200mha.jpg "7.4V_6200mAh_rechargeable_lithium_battery")|
|**Current Regulator Module**|Critical component converting battery's 7.4V to stable 5V (exactly 4.99V), preventing shorts and protecting Raspberry Pi|![Current_Regulator_Module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Modulo_regulador_de_corriente.jpg "Current_regulator_module")|
|**Cable Ties**|Secure Raspberry Pi, battery, and main wiring to prevent movement and pin disconnection|![Cable_Ties](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Tirrac.jpg "Cable_ties")|


# Lista de componentes probados pero descartados

|nombre|descripción|porque se descartó|imágen|
|------|-----------|------------------|------|
|**LED Diode, Button and Resistor** |Components indicating program execution: Red LED diode, program activation button, and 200Ω resistor preventing LED burnout|At first we used it as an indicator that the program was running but there came a time when it stopped working, the LED had not burned out so that was not the error we thought it was due to the programming since after a modification it stopped working, it turned out that there was a crash in the program and we preferred to discard the LED and use as an indicator the movement that the servomotor generated when it was activated|![LED_Diode,_Button_and_Resistor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Diodo_LED%2C_boton_y_resistencia.jpg "LED_diode,_button_and_resistor")|
| **Ultrasonic Sensor** |Responsible for sending ultrasonic waves that bounce off sufficiently solid objects and are received by the sensor to obtain environmental measurements. In short, it detects the robot's surroundings and measures distances |Due to the complication of adapting the sensor programming to the movement of the motor since the detection threshold was very low, we preferred to discard it and use only the infrared sensors.|![Ultrasonic_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/sensor_ultrasonido.jpg "ultrasonic_sensor")|
