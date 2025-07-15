# OSCORP TEAM
We are the team that proudly represents the San Antonio Institute Educational Unit (U.E.I. San Antonio). We focus on teamwork, hard work, effort, and commitment to every project we undertake to achieve progress and our goals and dreams.

#  Índice
* [Repository Contents](#Repository-Contents)
* [Project Introduction](#Project-Introduction)
* [Photos of our Team](#Photos-of-our-Team)
* [First model](#First-model)
* [Vehicle Photos](#Vehicle-Photos)
* [List of components used](#List-of-components-used)
* [List of components tested but discarded](#List-of-components-tested-but-discarded)
* [Hardware design](#Hardware-design)
* [Software design](#Software-design)
	* [Brief summary of our evolution](#Brief-summary-of-our-evolution)
* [GPIOZERO schematic](#GPIOZERO-schematic)
* [electrical components for detection and motion ](#electrical-components-for-detection-and-motion)
* [processing components](#processing-components)
* [power components](#power-components)
* [refrigeration system](#refrigeration-system)
* [Electronic connection diagram](#Electronic-connection-diagram)
* [How we put together the robot](#How-we-put-together-the-robot)
	* [first phase](#first-phase)
	* [second phase](#second-phase)
 	* [third and final phase](#third-and-final-phase)
* [creation of the tracks](#creation-of-the-tracks)
* [Techbot robot video ](#Techbot-robot-video)

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

# Project Introduction
At the beginning, our project encountered some complications, but despite the adversities and lack of time, we managed to create a functional and mostly autonomous robot. The members of the Oscorp team are proud to present our obstacle- and color-detecting robot to Techbot.

This robot's design was made with recycled materials from old competitions, such as acrylic bases, which were essential for assembling the robot. A directional control and a motor with a differential were salvaged from an old remote-controlled car, from which only the differential, motor, and the directional control were salvaged.

Despite having encountered so many obstacles in creating the robot, we managed to make it, and it is the result of the fact that with effort and motivation, everything is possible.

# First model
# Photos of our Team
| **OSCORP Team**| ![OSCORP_Team](https://github.com/nestoxuy/OSCORP/blob/main/t-photos/OSCORP_Team.jpg )|
|-----------|--------|
| |![OSCORP_Team (2)](https://github.com/nestoxuy/OSCORP/blob/main/t-photos/OSCORP_Team(2).jpg)|


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
> [!NOTE]
> The images shown are not of the final model; they are almost at the end. These are just a sample of what the robot looks like from all angles.


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

# Software design

## Brief summary of our evolution 
Throughout our time assembling the robot, there were various changes in its programming, in which we can see an evolution of the code, a use and disuse of some components, such as the color sensor, which we discarded due to a bug that occurred when using the color sensor and the ultrasound sensors, when there was an error in these we decided to leave the ultrasound sensor and the infrared sensors, the ultrasound sensors are responsible for detecting walls, and depending on which wall is closer, they will turn in reverse, sensor 1, located on the right side of the robot, when it detects that it has a wall nearby, it will indicate to the servomotor that it should turn left, in turn, sensor 2, which is on the left side of the robot, when it detects a wall it will go to the right side, and the infrared sensor when it detects that it has a wall in front of it, it will indicate to the motors that they should go back for a certain time in order to continue executing their actions

## GPIOZERO library
For our project programming, we used libraries such as the **GPIOZERO library**, which allows us to use a wide variety of commands for programming, from a simple button to programming ultrasonic and infrared sensors

## GPIOZERO schematic
|Bookshop|specific section of the library|Funtion|
|--------|-------------------------------|-------|
|**GPIOZERO**|**DigitalInpuDevice**|It allows the detection and representation of a device, such as a button or a switch, allowing to determine if the device is active or inactive and to detect changes in its state **In summary** this section of the library allows you to: detect the device state, handle events and configure the behavior|
|**GPIOZERO**|**DigitalOutpuDevice**|This section is used to control digital output devices, such as LEDs, relays, etc. These are connected to the Raspberry Pi's GPIO pins. **In summary** it allows devices to be turned on and off more easily|
|**GPIOZERO**|**Button**|It allows reading the state of a physical button connected to a GPIOZERO pin, allowing detection when a button is pressed or released and executing specific actions|
|**GPIOZERO**|**Servo**|It allows generating pulse width modulation (PWM) signals to control the angular position of the servo|
|**GPIOZERO**|**Motor**|It simplifies hardware programming by offering an abstract interface that facilitates the control of devices such as motors|
|**GPIOZERO**|**DistanceSensor**|This class allows interaction with the ultrasonic sensor allowing the sensor to emit an ultrasonic pulse and detect an echo helping to measure the distance of an object to the sensor based on the time it takes for the ultrasonic signal to travel and return|

## Time library
Like the **time library**, this allows us to use **Time** in programming to determine how much time we need to generate a certain robot action

# detection system
Each of our sensors performs specific functions to guide the robot and ensure it doesn't crash or get stuck on any obstacles or walls:

* The infrared sensors are located on the front of the robot, providing quick and safe detection to avoid unexpected collisions with walls or obstacles.
* The ultrasonic sensors are located at the front, specifically on the robot's diagonals, measuring long distances to maintain our movement margins with respect to the side and front walls.
* Finally, our color sensor identifies the lines on the map, allowing us to navigate the track and count how many times it passes over any of the lines on the same track, thus keeping track of laps more efficiently.
![Detection_system](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Detection_system%20.jpg)

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
# refrigeration system
|function|image|
|--------|-----|
|This system allows for faster and safer cooling of the power regulator and the Raspberry, avoiding possible damage to the system or simply overheating.|![Refrigeration_system](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Refrigeration_system%20.jpg)|

# Electronic connection diagram
!["diagram"](https://github.com/nestoxuy/OSCORP/blob/main/schemes/Schemes/Scheme.png )

# How we put together the robot
At the beginning of the entire project, we began testing the Raspberry to ensure its functionality in the competition. We performed basic tests, such as lighting LEDs or programming a simple button, until we moved on to something more complex, such as programming infrared and ultrasonic sensors. We also tested color sensors. However, before all of that, we ran into issues that made testing difficult, such as downloading libraries or problems with the system. Since the Raspberry system is inspired by Linux, all installations were via terminal, which was very time-consuming. 

## first phase 
When we finally finished testing, we began assembling the robot. We used acrylic sheets to adapt the motor and the directional control from an old remote-controlled car (only the directional control and the motor with a mechanical differential were used). From there, we began the first phase of the robot.

|phase| | | | | | |
|-----|-----|-----|-----|-----|-----|-----|
|**first phase**| ![First_phase_above_with_the_second_level](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_above_with_the_second_level.jpg)| ![First_phase_above_with_the_second_level(2)](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_above_with_the_second_level(2).jpg)| ![First_phase_from_above](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_from_above%20.jpg)| ![First_phase_from_above(2)](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_from_above(2).jpg)| ![First_phase_on_one_side](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_on_one_side%20.jpg)| ![First_phase_on_the_front](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/First%20phase/First_phase_on_the_front.jpg)|

## second phase 
after mounting the two levels we began to mount the sensors, the raspberry and the ProtoBoard along with the installation of the pins with the Dupont cables, we put two infrared sensors to detect the walls on the side along with two ultrasonic sensors, one in front and one behind, this to detect the walls in front and behind also as a possible solution for parking, on the front side we put a color sensor to help us with the detection of the color of the obstacles and at the top the raspberry and a 4-battery module were tied with some tyracs which were initially the power source for the motor module and finally we put a powerband with an adapter for the power of the raspberry (this does not appear in the photo because we were still looking for a way to mount it without it falling)

|phase| | | | | | 
|-----|-----|-----|-----|-----|-----|
|**Second phase**|![Second_phase_top_part](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Second%20phase/Second_phase_top_part.jpg)|![Second_phase_left_side](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Second%20phase/Second_phase_left_side.jpg)|![Second_phase_Right_side](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Second%20phase/Second_phase_Right_side.jpg)|![Second_phase_from_the_front](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Second%20phase/Second_phase_from_the_front.jpg)|![Second_phase_rear_part](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Second%20phase/Second_phase_rear_part%20.jpg)|

## third and final phase
By this point we had quite a few things to fix. Problems arose with the color sensors and the ultrasonic sensors, so we decided to take it step by step. We already had an idea of ​​what we wanted: for the robot to complete 3 laps and not crash. By this point, we discarded the front color sensor and, to ensure that the robot managed to finish exactly where it started, a new color sensor was installed. This would go on the bottom wall, prepared to read the lines on the track floor. Depending on the color it read first, it would start counting. If it passed over the first color detected 4 times, this would mean that it had already completed a lap. It would have to pass a total of 12 times for it to count as 3 laps. This would not only give it endless progress, but would also give the robot greater autonomy, allowing it to complete the laps without any possible programming errors.

To avoid collisions with walls and make it easier to avoid obstacles, we removed the infrared sensors that were on the sides and left only one in the front, right in the center. Next to this sensor, almost at the corners, we added two ultrasonic sensors, one on each side to obtain a greater detection range and avoid collisions, in addition to helping avoid obstacles and providing a little help in the parking lot.

Finally, we added the new rechargeable lithium battery that was purchased. In addition, a fan cooler was installed on the current regulator due to overheating. With the fan cooler, it would cool as much as possible and prevent the regulator from burning out.

|phase|part |image | 
|-----|-----|-----|
|**third phase**|**Third phase top part**|![Third_phase_top_part](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Third%20phase%20/Third_phase_top_part%20.jpg)|
| |**Third phase front part**|![Third_phase_front_part](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Third%20phase%20/Third_phase_front_part%20.jpg)|
| |**Third phase back part**|![Third_phase_back_part](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Third%20phase%20/Third_phase_back_part%20.jpg)|
| |**Third phase right side**|![Third_phase_right_side](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Third%20phase%20/Third_phase_right_side%20.jpg)|
| |**Third phase left side**|![Third_phase_left_side](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/Third%20phase%20/Third_phase_left_side%20.jpg)|

# creation of the tracks
Our team had two practical tracks. The first was custom-made to the measurements of the WROC, made of matte banner. Then we switched to another, more improvised track to test the sensors and test the robot's autonomy and performance.This other track was created by recycling materials from past competitions, such as old tracks or pieces of wood
|image|image|image| 
|-----|-----|-----|
|![](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/training%20tracks/%20IMG-20250706-WA0001.jpg)|![](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/training%20tracks/IMG-20250706-WA0003.jpg)|![](https://github.com/nestoxuy/OSCORP/blob/main/other/Fotos/training%20tracks/IMG-20250706-WA0017.jpg)|

# Techbot robot video

## video of the first oscorp test 
[![video of the first oscorp test](https://img.youtube.com/vi/hP1flFgDdLQ/0.jpg)](https://www.youtube.com/watch?v=hP1flFgDdLQ "VIDEO DEL ROBOT OSCORP "
)
## video of the second oscorp test 
[![video of the second oscorp test ](https://img.youtube.com/vi/hP1flFgDdLQ/0.jpg)](https://youtu.be/AnX9UVvoi4Q?si=hP1flFgDdLQ.jpg)
