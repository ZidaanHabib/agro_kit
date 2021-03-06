=======================
Agrotech Sensor Kit API
=======================


An API to facilitate interaction with an agriculture tech sensor kit. The sensor kit
contains the following hardware modules in addition to the Raspberry Pi Zero W:

* Quectel L70-M39 GPS
* Adafruit MCP3008 ADC
* Seeed Studio 10102008 Moisture Sensor
* Adafruit TCS34725 Light Sensor

Licensing
==========
* Free software: GNU General Public License v3

Features
---------

* Sensor reading

  * GPS
  * Moisture
  * Lux
* Creating sensor profiles
* Logging data to text files
* Sending configuration commands GPS

Setup
-------
* Ensure SPI, I2C and UART are enabled on the Raspberry Pi. This can be done using the sudo raspi-config command in the Linux terminal.
* Install required packages. These can be done as follows:

  * pip3 install Adafruit_GPIO  Adafruit_MCP3008 Adafruit-Blinka
  * pip3 install file-read-backwards requests pynmea2
  * pip3 install RPi.GPIO adafruit-circuitpython-tcs34725
  * pip3 install agro-kit

Note that this API can has to be used on a Raspberry Pi.

Hardware Configuration
=======================

Pin numbers according to datasheets are shown in []

* Adafruit TCS34735 -> Raspberry Pi

  * VDD [1] ->                     GPIO-17 [11]
  * GND [2] ->                     GND
  * SDA [3] ->                     SDA1_I2C [3]
  * SCL [4] ->                     SCL1_I2C [5]

* Seeed Studio -> Raspberry Pi

  * [3] -> GPIO23 [16]
  * [4] -> GND
* MCP3008 -> Seed Studio

  * CHO 0 [1] -> [1]
* MCP3008 -> Raspberry Pi

  * GND [9]  ->                    GND
  * CS [10]  ->                    GPIO_SPI_CE0 [24]
  * D-IN [11]  ->                  GPIO_SPI_MOSI [19]
  * D-OUT [12] ->                 GPIO_SPI_MISO [21]
  * CLK [13]  ->                   GPIO_SPI_CLK [23]
  * GND [14]  ->                  GND
  * VREF [15]  ->                  3.3 V [17]
  * VDD [16]   ->                  3.3 V [17]

* QUECTEL L70-M39

  * TXD [2]  ->                    GPIO_15_UART_RXD [10]
  * RXD [3]    ->                  GPIO_14_UART_TXD [8]
  * VCC [8]    ->                  3.3 V [1]
  * GND [1]      ->                GND



About
--------

* The library includes 4 main classes: MoistureSensor, light_sensor, GPS and AgroKit.
* The AgroKit is an aggregated class built with attributes of the other sensor classes
* The AgroKit class can use any instance method available in the other sensor classes as well as its own aggregated methods

Link to documentation
----------------------



Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

The pynmea2 python library was used for GPS parsing of NMEA 0183 messages.
