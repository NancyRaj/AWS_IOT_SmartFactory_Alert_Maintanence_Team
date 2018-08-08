AWS_IOT_SmartFactory_Alert_Maintanence_Team
===========================================

![](media/625bf0a6c2c6385b429ecf2d6646a4bd.png)

In the Smart factory, Machine 1 comprises Arduino Mega and Raspberry Pi.
Temperature sensor is connected with Arduino and from Arduino, data is serially
transmitted to Raspberry Pi. Here making a communication between Arduino and
Raspberry Pi. Raspberry Pi do not have inbuilt ADC, so one way of connecting
analog sensor to it, is through Arduino.

From Raspberry Pi, data is sent to AWS cloud through MQTT protocol. In AWS, Rule
engine is designed in such a way that, as soon as temperature on machine 1 goes
more than 36, it should send an trigger alert to maintanence team via Email and
SMS.

Requirements:

-   Raspberry Pi

-   Arduino Mega

-   Temperature Sensor – LM35

-   PC, USB Cable and Jump Wires

![](media/6ce7e4a422f17eac4cf0cb60d42f3f82.png)

![](media/0ed8bf34cf60c9e5504ca1c35adecdd1.png)
