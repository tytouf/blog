Title: Flashing Adafruit 32u4 Boards
Date: 2012-08-12 18:23
Tags: Arduino, ISP, Flashing
Slug: flashing-adafruit-32u4-boards
Author: Christophe Augier
Category: Arduino
lang: en

I updated my [atmega32u4 based boards][1] with the Arduino Leonardo bootloader but
unfortunately the Lufa projects I tried are not so happy with it. I have no clue
why but I know it works fine with the original Bootloader so I reflased my
boards with the previous CDC Bootloader. Having no AVR programmer in hand, I
used one board that I fortunately did not update and flashed it with the Lufa
AVRISP-MKII programmer. Here are some notes with steps and the needed files.
[1]: http://adafruit.com/products/296

AVRISP-MKII
-----------

To build the AVRISP-MKII project, modify the following lines in the makefile:

    :::makefile
    MCU=atmega32u4
    ARCH=AVR8
    BOARD=ADAFRUITU4
    F_CPU=16000000

Flash AVRISP-MKII on the survivor board

    :::sh
    $ avrdude -p m32u4 -P /dev/ttyACM0 \
    -c avr109 -U flash:w:AVRISP-MKII.hex

Bootloader CDC
--------------

Plug both boards together:

![Wiring schema]({filename}/images/AVRISP-MKII_programming_bb.png)

Flash the other boards with the Bootloader:

    :::sh
    $ avrdude -p m32u4 -P usb -c avrispmkII \
      -U flash:w:BootloaderCDC.hex

BootloaderCDC.hex can be found
[here](http://blog.tytouf.fr/wp-content/uploads/2012/08/BootloaderCDC.hex_.txt)

Make sure the fuses are correctly set up:

    :::sh
    $ avrdude -p m32u4 -P usb -c avrispmkII \
      -U lfuse:w:0xFC:m -U hfuse:w:0xD0:m \
      -U efuse:w:0xC3:m
