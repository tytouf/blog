Title: Flashage des cartes Adafruit 32u4
Date: 2012-08-12 18:23
Tags: Arduino, ISP, Flashing
Slug: flashing-adafruit-32u4-boards
Author: Christophe Augier
Category: Arduino
lang: fr


J’avais flashé mes [cartes Adafruit][1] à base d’atmega32u4 avec le bootloader de la
Leonardo mais voilà il semblerait que le bootloader ne cohabite pas très bien
avec les programmes LUFA. J’ai donc dû repasser au Bootloader CDC de base.
N’ayant pas de programmeur AVR à portée de main j’ai utilisé une carte pour
programmer une autre en y chargeant auparavant le programme AVRISP-MKII du
projet Lufa. Pour mémoire voici les opérations à effectuer ainsi que les
fichiers nécessaires.
[1]: http://adafruit.com/products/296

AVRISP-MKII
-----------

Pour compiler AVRISP-MKII, modifiez le fichier makefile comme suit :

    :::makefile
    MCU=atmega32u4
    ARCH=AVR8
    BOARD=ADAFRUITU4
    F_CPU=16000000

Flasher une carte rescapée avec AVRISP-MKII :

    :::sh
    $ avrdude -p m32u4 -P /dev/ttyACM0 \
    -c avr109 -U flash:w:AVRISP-MKII.hex

Bootloader CDC
--------------

Brancher les deux cartes ensembles :

![Wiring schema]({filename}/images/AVRISP-MKII_programming_bb.png)

sher les autres cartes avec le Bootloader:

    :::sh
    $ avrdude -p m32u4 -P usb -c avrispmkII \
      -U flash:w:BootloaderCDC.hex

BootloaderCDC.hex peut être téléchargé
[ici](http://blog.tytouf.fr/wp-content/uploads/2012/08/BootloaderCDC.hex_.txt).

On s’assure que les fusibles sont correctement configurés :

    :::sh
    $ avrdude -p m32u4 -P usb -c avrispmkII \
      -U lfuse:w:0xFC:m -U hfuse:w:0xD0:m \
      -U efuse:w:0xC3:m
