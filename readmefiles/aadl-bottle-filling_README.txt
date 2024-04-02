# Bottle Filling Plant

## Purpose of the system 
The purpose of the modeled system is to represent a simple water bottling station for drinking water. The model must include components that allow handling water from the source to the moment of filling the bottle.
## List of components with a comment 
### Devices 
  - Water Pipe - can be treated as the water source for the entire system. It has a water flow meter. Based on this, the system can determine if a sufficient amount of water is supplied.
  - Filter - This is a filter that has the functionality of informing about the need for replacement. If the filter is used up, the system should block the bottling of water.
  - Water Quality Sensor - Located behind the filter. It informs the system about the quality of the water flowing through the filter.
  - Filling Valve - Determines the flow of water into the bottle. The system should open and close the valve based on information received from other devices.
  - Bottling Sensor - a special sensor that allows detecting whether the bottle is under the nozzle of the filling valve and informs about the filling of the bottle.
  - Production Conveyor Belt - the system has the ability to stop and start the conveyor belt and set its speed. The conveyor belt reports its speed to the system which allows detecting incorrect operation.

### Abstract Elements 
  - Operator Interface - The system assumes the existence of an interface for the operator of the bottling station. The aim of the system is not to create this interface, however, the system assumes that it can accept instructions from the operator.
### Processors and Buses 
  - Main processor - the processor handling the entire system. It is capable of performing 650 mips.
  - Main bus - The bus connecting all devices to the processor. BandWidthCapacity: 200MBps, BandwidthBudget: 950 KBps

### Processes 
  - Main process - the system assumes the existence of only one main process managing the operation of the entire filling station. All the aforementioned devices are connected to this process. Information to them is received and processed through several threads listed below.
### Threads 
  - Water Analysis Thread - A thread processing data from the water pipe, filter, and water quality sensor. Based on these three values, it creates information about the water needed for the filling thread.
  - Filling Thread - A thread processing data from the bottling sensor and receiving data from the water analysis thread, based on which it decides whether the valve should be opened according to the received information. The thread does not make the final decision on opening the valve but passes the expected valve state to the control thread.
  - Operator Thread - Processes input from the operator interface and sends information to the control thread.
  - Conveyor Belt Thread - Processes information received from the conveyor belt. It sends information to the conveyor belt about what its speed should be and sends information to the control thread about whether the conveyor belt should be turned on.
  - Control Thread - Receives information from all other threads - whether the valve should be opened, operator commands, and starting the conveyor belt. It processes the received information and makes the final decision on activating the valves and starting the conveyor belt.
## Model - Drawings 
### Threads 
![water-input-thread](https://github.com/behenate/aadl-bottle-filling/assets/31368152/479930ce-83cc-4dc5-9af1-e677fb8bfc85)
![control-thread](https://github.com/behenate/aadl-bottle-filling/assets/31368152/4a89444e-b0f7-4f06-abde-8cb55a245866)
![conveyor-thread](https://github.com/behenate/aadl-bottle-filling/assets/31368152/5c25c365-91b0-4088-986e-72dce826463d)
![filling-thread](https://github.com/behenate/aadl-bottle-filling/assets/31368152/f2fde94d-7ddd-4c5f-b8f1-9774ce464913)


### Control System - Main Process
![control-system](https://github.com/behenate/aadl-bottle-filling/assets/31368152/29bf5621-55f5-40f2-b75d-91a3456da937)


### Simplified System View 
![Diagram-simple](https://github.com/behenate/aadl-bottle-filling/assets/31368152/78b8196c-5547-4a3e-9130-5ba0278656c1)

### Detailed System View 
![diagram](https://github.com/behenate/aadl-bottle-filling/assets/31368152/93cf97e3-ea57-497b-81c8-a7d02e5b3a2f)
