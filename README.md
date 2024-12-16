# Robotics Water System Using Computer Vision
This project aims to create a smart water system. This system works based on which locations are detected by previously designed objects thus producing different outputs.
Dibuat oleh tim Mekatronika dan Kecerdasan Buatan 2021 UPI Purwakarta

## Tools
- Poximity Sensor
- Arduino Uno
- DC Motor
- Relay
- L298N
- Servo Motor
- Adaptor
- Water Pump
- Jumper
- Projecr Board
- Water Hose
- Solders
- Arduino IDE

## Goals
This project is intended to form a smart irrigation system using simple electronic components with Arduino as the main microcontroller. This system also works based on which location is detected by the object that has been designed before so that it will produce different outputs. 

## System
![WhatsApp Image 2024-01-30 at 11 15 13_6bfce799](https://github.com/aisyaaaptr/Water_System/assets/157786477/50e24a4d-a183-4382-9dc4-dfe5247462a2)

A demo video of the tool can be viewed here: https://youtu.be/V1T_ewJL2a0?si=3TsD0SAaZLc5SRSf  

## Step 1: Requirement Analysis
- Identify system goals, including the types of objects to be detected and the specific water outputs required for each location.
- Define hardware requirements and software requirements.
- Understand environmental conditions to optimize system design.

## Step 2: Hardware and Software Design
- Choose a suitable camera module for object detection.
- Select a microcontroller for controlling the system.
- Determine water pump specifications and other hardware components, such as valves and power supply modules, to deliver water to specific locations.
Software Design
- Select or develop a computer vision algorithm to detect predefined objects.
- Train the algorithm to recognize specific objects or patterns associated with different water output locations.
- Write a control program to process camera input and activate the appropriate water pump output.

## Step 3: System Integration
- Connect the camera to the microcontroller or computer for real-time image processing.
- Integrate the water pump control system with the computer vision module to trigger water flow based on detected objects.
- Develop a feedback mechanism to ensure proper execution, such as confirming water output at the correct location.

  Various locations and the resulting output:
  - Position A: Turns on the Water Pump
  - Position B: Turns Off the Water Pump
  - Position C: Starts Motor 1
  - Position D&E: Starts Motor 2
  - Positions F, G, H, and J: Changes the Servo Angle
 
  The system is operated based on which locations are detected by color-coded green objects: 
  - Hmin = 42
  - Hmax = 88
  - Smin = 62
  - Smax = 255
  - Vmin = 45
  - Vmax = 150
