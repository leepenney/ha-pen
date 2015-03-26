# Installation

To install HA-Pen and get it working, complete the steps outlined below.

All of these steps were completed on a clean install of Raspbian.

## Before you start

If you have a clean install, I'd suggest updating your package list, using:

    sudo apt-get update

## Install PIP

The Pi comes with Python installed but not pip (a package manager), so first up, install it:

    sudo apt-get install python-pip

## Install Bottle

Now install [Bottle](http://bottlepy.org/):

    sudo pip install bottle
