Title: Using libusb to communicate with your Arduino board
Date: 2012-07-06 14:55
Tags: Arduino, libusb, USB, PyUSB
Category: Arduino
Slug: libusb-arduino
Author: Christophe Augier
lang: en

Today, I investigated the USB capabilities of my Arduino Leonardo compatible
boards: the [Adafruit ATmega32U4][1]. I bought them a few months ago when the
official Leonardo wasn’t available yet. Besides these board are less expensive
than the now available [Leonardo][2]. Anyway, I’d like to develop my own USB classes
to exchange data between a computer and the board. Why develop a new class when
by default all the Arduino stack provides the CDC-ACM class emulating a serial
port? Simply because it’s fun ;-)

Therefore I began studying the USB protocol and the [libusb][3] to write a driver for
the CDC-ACM class found on the board. This class is relatively simple yet USB
can get much more complicated. I won’t describe all the details of the USB
protocol neither the CDC-ACM specifications, so whether you want to read them
before or directly dive into the code, I’ll let that to your discretion. Here
are a C program using the [libusb][3] with comments and the equivalent Python program
using [PyUSB][4].

[1]: http://adafruit.com/products/296
[2]: http://adafruit.com/products/849
[3]: http://libusb.org/
[4]: http://sourceforge.net/apps/trac/pyusb/
