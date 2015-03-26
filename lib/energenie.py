#! /usr/bin/env python

# import required modules
import RPi.GPIO as gpio
import time, sys
gpio_pins = [13,16,15,11] # ordered to match the order used in the send codes
transmit_pin = 22
modulator_pin = 18
on_codes = ['1011','1111','1110']
off_codes = ['0011','0111','0110']

def send_code(code_sent):
	# turn on the modulator to send the code set
	time.sleep(0.1) # wait for pins to 'settle'
	gpio.output(transmit_pin, True) # turn modulator on
	time.sleep(0.25) # give time for signal to be transmitted
	gpio.output(transmit_pin, False) # turn modulator off

def prepare_pins():
	# select the GPIO pins used for the encoder inputs and set them to 0000
	output_pins = list(gpio_pins)
	output_pins.extend([modulator_pin,transmit_pin])
	for pin in output_pins:
		gpio.setup(pin, gpio.OUT)
		gpio.output(pin, False)

def switch_socket(socket, action):
    # switch a socket on or off
    if (socket and str(socket) in ['0','1','2']) and (action and action in ['on','off']):
        # if arguments look okay, continue
        gpio.setmode(gpio.BOARD)
        prepare_pins()

        codes = on_codes if action == 'on' else off_codes

        for i,pin_setting in enumerate(codes[int(socket)]):
            gpio.output(gpio_pins[i], int(pin_setting))

        send_code(codes[int(socket)])

        # clean up pins for next time
        gpio.cleanup()
        
        return True
    else:
        return False

