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

## Install Astral

The Astral package is used to calculate sunrise and sunset, install using:

    sudo pip install astral
    
## Install Jinja2

Bottle has it's own templating language built in, but I've used Jinja more, so opted to use that. Install using:

    sudo pip install Jinja2

## Install pigpio

In order to access the GPIO pins on the Pi, we need a library to do so, pigpio can do this without requiring root privileges. Install using:

```
wget abyz.co.uk/rpi/pigpio/pigpio.zip
unzip pigpio.zip
cd PIGPIO
make
make install
```

These instructions were taken from [this page](http://abyz.co.uk/rpi/pigpio/download.html)

Start the pigpio daemon using:

    sudo pigpiod

Finally, add the daemon to your rc.local file to run it at boot (so it's available should the machine restart):

    sudo nano /etc/rc.local

Just before the line

    exit 0

Add:

    sudo pigpio

Hit CTRL+X to exit and type y and Enter when prompted to save it.

## Install Apache

To view the pages in a browser we need a web server, so install Apache using:

    sudo apt-get install apache2 libapache2-mod-wsgi

Note: If you have Apache installed already, you will need the wsgi extension

## Create a directory for the HA-Pen files

This is used for all of the application's files.

```
cd /var/www
sudo mkdir ha
```

## Install HA-Pen

Copy the HA-Pen files into the newly created directory:

```
cd /var/www/ha
git clone https://github.com/leepenney/ha-pen .
```

Now we need to sort out the permissions so the web server can control the files:

```
cd ..
sudo chown -R www-data:www-data ha
```

Next, we need to replace the Virtual Hosts file with the one supplied in the HA-pen download, first backing up the original (should you hit problems, you can restore it by reversing the parameters):

```
sudo cp /etc/apache2/sites-available/default /etc/apache2/sites-available/default.old
sudo cp /var/www/ha/default /etc/apache2/sites-available/default
```

Finally, make Apache aware of the changes by restarting the service:

    sudo service apache2 restart

## Setting up the Cron jobs

To run the script that check the timers and switch sockets on and off, as well as upating the sunrise and sunset times, we need to add some Cron jobs that run at scheduled intervals.

To this, first open Crontab in edit mode:

    sudo crontab -e
    
Now add the following at the end of the file:

```
* * * * * /usr/bin/python /var/www/ha/lib/scheduler.py >/dev/null 2>&1
3 0 * * * /usr/bin/python /var/www/ha/lib/sunrise_sunset.py >/dev/null 2>$1
```

## Congratulations

You should now be able to see the web UI if you visit http://<your Pi's IP>/ha in a browser.

Next up is the [config](config.md]

