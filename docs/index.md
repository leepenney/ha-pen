# HA-Pen Documentation

This documentation will take you through installing and using HA-Pen.

## About HA-Pen

HA-Pen is a webapp built using [Bottle](http://bottlepy.org/) that allows you to create timers and control power sockets using the Pi-mote add-on for Raspberry Pis from Energenie.

Once installed and working you will be able to turn sockets on an off by clicking a button on a web page from any device with a browser, plus you can create timers so the sockets switch on and off at set times.

## Installation

The [installation](install.md) section will take you through installing HA-Pen and the various dependencies.

## Configuration

The [config](config.md) section will take you through the simple config steps.

## Usage

The [usage](usage.md) section will run through how to use the system, both from the web UI and the command line.

## Project structure

The project is laid out as follows:

* app.py - contains the main application logic
* app.wsgi - the settings necessary for the application to run under a WSGI server
* config - contains the various configuration files
    * settings.json - the overall application settings
    * sockets.json - details of the sockets
    * timers.json - all of the timer details for switching sockets on and off
* docs - the various documentation files
* lib - contains the various function files
    * energenie_pig.py - functions for turning on/off the sockets using pigpio
    * scheduler.py - standalone script that turns the sockets on/off based on timers
    * sockets.py - various socket-related functions
    * sunrise_sunset.py - a script that calculates the current day's sunrise/sunset times, based on long and lat and updates the timers
    * timers.py - various timer-related functions
* static - the files pulled in by the views (CSS and JS)
    * js - contains the JS files
        * ha.js - contains the various functions used by the web UI
    * stylesheets - contains the CSS
        * style.css - contains the various styles that control the look and feel of the web UI
* views - the layout files to control the web UI
    * index.html - the main page of the web UI
    * sockets.html - the socket page of the web UI
    * timer_list.html - a sub-page called by index.html returning the timer list

