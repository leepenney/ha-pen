#! /usr/bin/env python

# import required modules
import pigpio as pig
import time, sys
gpio_pins = [27,23,22,17] # BCM pins ordered to match the order used in the send codes
transmit_pin = 25
modulator_pin = 24
on_codes = ['1011','1111','1110']
off_codes = ['0011','0111','0110']

def send_code(pi, code_sent):
	# turn on the modulator to send the code set
	time.sleep(0.1) # wait for pins to 'settle'
	pi.write(transmit_pin, 1) # turn modulator on
	time.sleep(0.25) # give time for signal to be transmitted
	pi.write(transmit_pin, 0) # turn modulator off

def prepare_pins(pi):
	# select the GPIO pins used for the encoder inputs and set them to 0000
	output_pins = list(gpio_pins)
	output_pins.extend([modulator_pin,transmit_pin])
	for pin in output_pins:
		pi.set_mode(pin, pig.OUTPUT)

def switch_socket(socket, action):
    # switch a socket on or off
    if (socket and str(socket) in ['0','1','2']) and (action and action in ['on','off']):
        # if arguments look okay, continue
        pi = pig.pi()
        prepare_pins(pi)

        codes = on_codes if action == 'on' else off_codes

        for i,pin_setting in enumerate(codes[int(socket)]):
            pi.write(gpio_pins[i], int(pin_setting))

        send_code(pi, codes[int(socket)])

        # clean up pins for next time
        pi.stop()
        
        return True
    else:
        return False

