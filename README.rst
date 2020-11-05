=======================
Agrotech Sensor Kit API
=======================


An API to facilitate interaction with an agriculture tech sensor kit. The sensor kit
contains the following hardware modules in addition to the Raspberry Pi Zero W:
* Quectel L70-M39 GPS
* Adafruit MCP3008 ADC
* Seeed Studio 10102008 Moisture Sensor
* Adafruit TCS34725 Light Sensor


* Free software: GNU General Public License v3

Setup
-------
* Ensure SPI, I2C and UART are enabled on the Raspberry Pi. This can be done using the sudo raspi-config command in the Linux terminal.
* Install required packages. These can be done as follows:
  * pip3 install Adafruit_GPIO  Adafruit_MCP3008 Adafruit-Blinka
  * pip3 install file-read-backwards requests pynmea2 adafruit-circuitpython-tcs34725
  * pip3 install RPi.GPIO

Features
--------

The library includes 4 main classes: MoistureSensor, light_sensor, GPS and AgroKit.
The breakdown of the methods in these are explained below:

MoistureSensor
===============
This class provides methods that relate to reading and using the moisture sensor.


light_sensor
=============



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

The pynmea2 python library was used for GPS parsing of NMEA 0183 messages.
