# OSCORP TEAM
We are the team that proudly represents the San Antonio Institute Educational Unit (U.E.I. San Antonio). We focus on teamwork, hard work, effort, and commitment to every project we undertake to achieve progress and our goals and dreams.

#  Índice
* [Repository Contents](#Repository-Contents)
* [Project Introduction](#Project-Introduction)
* [Photos of our Team](#Photos-of-our-Team)
* [Vehicle Photos](#Vehicle-Photos)
* [List of components used](#List-of-components-used)
* [List of components tested but discarded](#List-of-components-tested-but-discarded)
* [Hardware design](#Hardware-design)
* [electrical components for detection and motion ](#electrical-components-for-detection-and-motion)
* [processing components](#processing-components)
* [power components](#power-components)
* [Electronic connection diagram](#Electronic-connection-diagram)
* [How we put together the robot](#How-we-put-together-the-robot)

# Repository Contents
# Our repository contains the following team data:
|File| description|
|------|------|
| [`t-photos`](https://github.com/nestoxuy/OSCORP/tree/main/t-photos)| Includes 2 team photos (one official and one fun one with all members)|
|[`v-photos`](https://github.com/nestoxuy/OSCORP/tree/main/v-photos) |Contains 9 photos of the vehicle (from all angles, top and bottom)|
|[`video`](https://github.com/nestoxuy/OSCORP/tree/main/video) |A shortcut to our video published on our YouTube account|
|[`schemes`](https://github.com/nestoxuy/OSCORP/tree/main/schemes) |Schematic diagram (PNG) of the electronic connections from the Raspberry to the components|
|[`src`](https://github.com/nestoxuy/OSCORP/tree/main/src)|All the folders with the tests and practices that the team has done throughout the development of the robot along with a brief history of how we evolved and changed the codes along the way|
|[`models`](https://github.com/nestoxuy/OSCORP/tree/main/models)|This folder is empty because our robot does not need 3D printing or virtual modeling|
|[`other`](https://github.com/nestoxuy/OSCORP/tree/main/other)|It contains a list of components we've used, components we've tested and discarded because they didn't work as needed, and components that were implemented in the final version of the robot. It also includes two folders, one containing all the photos and the other containing all the recorded videos|

# Photos of our Team
|OSCORP Team|![OSCORP_Team](https://github.com/nestoxuy/OSCORP/blob/main/t-photos/OSCORP_Team.jpg)|
|-------|-------|

# Vehicle Photos
|Place|Photo|
|:----:|:----:|
|**top level**| ![top_level](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/top_level.jpeg)| 
|**Lower level**|![Lower level"](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Lower_level.jpeg)| 
|**Right side**|![Right side](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Right_side.jpeg )| 
|**Left side**|![Left side](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Left_side.jpeg )|
|**Front Train**|![Front Train](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Front_Train.jpeg )|
|**rear train**|![rear_train](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/rear_train.jpeg ) |
|**Lower left side**|![Lower left side](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Lower_left_side.jpeg ) 
|**Lower right side**|![Lower right side](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Lower_right_side.jpeg )
|**Upper side**|![Upper side](https://github.com/nestoxuy/OSCORP/blob/main/v-photos/Images/Upper_side.jpeg )|




# List of components used

|name|description|image|
|------|-----------|------|
|**engine module**|manages the movement and performance of the motors, as well as managing the flow of energy to prevent the motors or in this case the engine from burning out| ![module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/motor_module.jpg "motor module") |
| **Anti-Slip Wheels** |Designed to increase traction and reduce the risk of losing friction and slipping on the track |![Anti-Slip_Wheels](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/non-slip_wheels.jpg "Anti-slip wheels")|
| **Color Sensor** |Measures light intensity at different wavelengths to determine object colors and sends signals to identify colors|![Color_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/color_sensor.jpg "Color_sensor")|
|**infrared sensor**|Infrared Sensor radiation (IR) through one LED acting as transmitter. The signal bounces back and is detected by another LED acting as receiver. Measures received IR radiation level and return time to calculate object distance|![Infrared_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/infrared_sensor.jpg "Infrared_sensor")|
| **Dupont Wires and Breadboard** | Dupont wires connect to Raspberry Pi5's programmable pins and provide electrical connections for sensors (5V and GND pins). The breadboard serves as intermediary for connections, facilitating pin management and power distribution for sensors|![Dupont_Wires_and_Breadboard](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/ProtoBoard_and_Dupont_cables.jpeg "Dupont_wires_and_breadboard")|
| **Transparent Acrylic Bases** |Primary foundation for the entire assembly. The two-tiered base holds directional components/motors (lower level) and allows mounting/screwing of electronic components (upper level)|![Transparent_Acrylic_Bases](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/base.jpg)
| **Raspberry Pi5**|The motherboard - the robot's brain. Features: 8GB RAM, 4GB ROM, dual 4K GPU support, PCI Express interface. Ports: 2x HDMI, 4x USB (2x USB2.0 + 2x USB3.0), Gigabit Ethernet, 27 programmable pins (2x 3V, 2x 5V, 8x GND), USB-C power, microSD slot. Power: 5V-3A (min) to 5V-5A (max)|![Raspberry_Pi5](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/raspberry-pi-5-03.jpg "Raspberry_Pi5")|
| **Hexagonal Pillar Screw Kit**|Used to create structural pillars enabling two levels: Lower (motors/directional components) and upper (wiring, Raspberry Pi5, battery, breadboard, sensors)|![Hexagonal_Pillar_Screw_Kit](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Hexagonal_screw_kit_for_pillars.jpg "Hexagonal_pillar_screw_kit")|
| **7.4V 6200mAh Rechargeable Lithium Battery**|Primary power source for Raspberry Pi and installed sensors|![7.4V_6200mAh_Rechargeable_Lithium_Battery](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/7.4V_6200mha_Rechargeable_Lithium_Battery.jpg "7.4V_6200mAh_rechargeable_lithium_battery")|
|**Current Regulator Module**|Critical component converting battery's 7.4V to stable 5V (exactly 4.99V), preventing shorts and protecting Raspberry Pi|![Current_Regulator_Module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Current%20_regulator.jpg "Current_regulator")|
|**Cable Ties**|Secure Raspberry Pi, battery, and main wiring to prevent movement and pin disconnection|![Cable_Ties](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Tirrac.jpg "Cable_ties")|
| **Ultrasonic Sensor** |Responsible for sending ultrasonic waves that bounce off sufficiently solid objects and are received by the sensor to obtain environmental measurements. In short, it detects the robot's surroundings and measures distances |![Ultrasonic_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/ultrasound_sensor.jpg "ultrasonic_sensor")|
|**Differential motor mechanics of a toy car**|It allows the wheels to rotate at different speeds, especially during turns, while connected to the same axle. This is crucial for safe and efficient handling, preventing slippage, and with its included motor, it can move the robot both forward and backward|![Differential_motor_mechanics_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Differential_motor_mechanics_of_a_toy_car.jpg)|
|**Mechanical steering of a toy car**|It helps steer the robot by transmitting force from the servomotor to the wheels to change the robot's direction and assist with its turns. The servomotor was adapted so that a plastic lever would fit perfectly into the slot in the turn signal, allowing the servomotor to transmit its force much better|![Mechanical_steering_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Mechanical_steering_of_a_toy_car.jpg)|
|**180 degree servo motor**| The servomotor used was a 180-degree servomotor to control movement|![180_degree_servo_motor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/180_degree_servo_motor.jpg)|

# List of components tested but discarded

|name|description|because it was discarded|image|
|------|-----------|------------------|------|
|**LED Diode, Button and Resistor** |Components indicating program execution: Red LED diode, program activation button, and 200Ω resistor preventing LED burnout|At first we used it as an indicator that the program was running but there came a time when it stopped working, the LED had not burned out so that was not the error we thought it was due to the programming since after a modification it stopped working, it turned out that there was a crash in the program and we preferred to discard the LED and use as an indicator the movement that the servomotor generated when it was activated|![LED_Diode,_Button_and_Resistor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/LED_button_diode_and_resistor.jpg "LED_diode,_button_and_resistor")|

# Hardware design
|name|description|image|
|----|-----------|-----|
| **Transparent Acrylic Bases** |Primary foundation for the entire assembly. The two-tiered base holds directional components/motors (lower level) and allows mounting/screwing of electronic components (upper level)|![Transparent_Acrylic_Bases](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/base.jpg)
|**Differential motor mechanics of a toy car**|It allows the wheels to rotate at different speeds, especially during turns, while connected to the same axle. This is crucial for safe and efficient handling, preventing slippage, and with its included motor, it can move the robot both forward and backward|![Differential_motor_mechanics_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Differential_motor_mechanics_of_a_toy_car.jpg)|
|**Mechanical steering of a toy car**|It helps steer the robot by transmitting force from the servomotor to the wheels to change the robot's direction and facilitate its turns. The servomotor was adapted so that a plastic lever fit perfectly into the servomotor slot, allowing it to transmit its force much better. The servomotor used was a 180-degree servomotor to control movement. The servomotor centers at 90 degrees, turns left at 180 degrees, and turns right at 0 degrees|![Mechanical_steering_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Mechanical_steering_of_a_toy_car.jpg)|

# electrical components for detection and motion 
|name|function|image|
|----|-------|-----|
|**engine module**|This module was purchased with the objective of making the programming compatible with the motor for movement and being able to use it as well as regulate the flow of current that it receives| ![module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/motor_module.jpg "motor module") |
| **Color Sensor** |We use it to help detect colors and know what movements the robot should make when encountering obstacles, which are red and green|![Color_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/color_sensor.jpg "Color_sensor")|
|**infrared sensor**|We installed this sensor to adjust its distance and achieve a slightly easier detection of walls than with ultrasonic sensors|![Infrared_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/infrared_sensor.jpg "Infrared_sensor")|
| **Ultrasonic Sensor** |This sensor was used to detect walls to achieve a more fluid and safe movement, preventing collisions and jamming |![Ultrasonic_Sensor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/ultrasound_sensor.jpg "ultrasonic_sensor")|
|**Differential motor mechanics of a toy car**|The differential was taken from an old car, which aims to facilitate turns and allow tighter, less rigid and forced turns|![Differential_motor_mechanics_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Differential_motor_mechanics_of_a_toy_car.jpg)|
|**Mechanical steering of a toy car**|The directional was also removed from the same place as the differential, this was installed with the objective of helping in turns and the direction that the robot takes|![Mechanical_steering_of_a_toy_car](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Mechanical_steering_of_a_toy_car.jpg)|
|**180 degree servo motor**| The servomotor was used to be adapted to the directional and through programming to have it move and in turn move the direction of the wheels|![180_degree_servo_motor](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/180_degree_servo_motor.jpg)|

# processing components 
|name|function|image|
|----|-------|-----|
| **Raspberry Pi5**|The Raspberry is the brain of the entire robot, allowing the programming to be saved and also executed, which allowed us to implement different commands. Without this control board, nothing would be possible; the robot simply wouldn't know what to do|![Raspberry_Pi5](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/raspberry-pi-5-03.jpg "Raspberry_Pi5")|

# power components 
|name|function|image|
|----|-------|-----|
| **7.4V 6200mAh Rechargeable Lithium Battery**|After doing several experiments with alkaline batteries to be able to provide sufficient power to the Raspberry, we encountered the problem of not sending enough and not lasting long enough, so we decided to buy a lithium battery which not only gives us enough energy but also the necessary performance and durability.|![7.4V_6200mAh_Rechargeable_Lithium_Battery](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/7.4V_6200mha_Rechargeable_Lithium_Battery.jpg "7.4V_6200mAh_rechargeable_lithium_battery")|
|**Current Regulator Module**|Before buying the battery we needed, we looked for different battery models that would fit the bill, but since they didn't provide enough power, we bought a power regulator to use with the current battery and achieve the necessary amount of energy, while also avoiding the risk of damaging the controller|![Current_Regulator_Module](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Current%20_regulator.jpg "Current_regulator")|

# Electronic connection diagram
!["diagram"](https://github.com/nestoxuy/OSCORP/blob/main/schemes/Schemes/Scheme.png )

# How we put together the robot
At the beginning of the entire project, we began testing the Raspberry to ensure its functionality in the competition. We performed basic tests, such as lighting LEDs or programming a simple button, until we moved on to something more complex, such as programming infrared and ultrasonic sensors. We also tested color sensors. However, before all of that, we ran into issues that made testing difficult, such as downloading libraries or problems with the system. Since the Raspberry system is inspired by Linux, all installations were via terminal, which was very time-consuming. 

When we finally finished testing, we began assembling the robot. We used acrylic sheets to adapt the motor and the directional control from an old remote-controlled car (only the directional control and the motor with a mechanical differential were used). From there, we began the first phase of the robot.

|phase|image|
|----|-------|

|first phase | ![First_phase_above_with_the_second_level](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_above_with_the_second_level.jpg)
 |![First_phase_above_with_the_second_level(2)](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_above_with_the_second_level(2).jpg) |
