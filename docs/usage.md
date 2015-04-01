# Using HA-Pen

This section briefly runs through how to use the HA-Pen home automation system.

## Via the Web UI

The system is designed to be administered via a web page to make it easy to review and modify the setup.

### Accessing the UI

To bring up the web page showing the user interface, you need to visit http://<your Pi's IP>/ha

It is recommended you set a static IP address or use the network name to make accessing the device easier and more consistent.

### A rundown of the UI

The interface is divided into three sections. On a wide enough display, these will appear as columns. The layout has also been modified to support phone-size screens and will reflow into a vertical layout.

1. Controls for the sockets
2. The currently set timers
3. Adding a timer

#### Controls for the sockets

Each socket the system is aware of (i.e. those in the sockets.json file) will be listed as a toggle button. When the system believes the socket is inactive (based on the true/false flag in the sockets.json file) it will display with a grey background. If the socket is believed to be on, the switch will appear green.

To switch a socket on or off manually, simply click or tap the appropriate button.

There is also the option to switch all sockets on or off, this toggles through the list and changes the state for every socket.

**Note:** A socket doesn't necessarily mean one physical device, multiple devices can be trained to have the same value assigned to them, so you can toggled multiple devices on/off from the same button. 

To change the name of the sockets, see below.

#### Currently set timers

See the Timers section below.

#### Adding a timer

See the Timers section below.

### Timers

The web UI allows you to review, modify and delete existing timers as well add new ones.

#### Existing timers

The central column contains a list of the currently set timers.

##### Modify a timer

To change an existing timer, simply update the details in the relevant entry and click/tap Save. If the action was successful the Save button will change to say Saved.

##### Delete a timer

If you wish to remove a timer, simply click/tap the Delete button in the appropriate section. The timer will vanish from the UI and be removed from the timers.json file.

#### Adding a timer

The third column of the UI contains an Add Timer form.

Simply pick the socket and the relevant settings and click Add to create a new timer entry. The new timer's details will be appended to the list in the central column and will be added to the timers.json file.

### Sockets

You can see a list of the current sockets and add additional ones by visiting the sockets page, which is located in a subfolder called sockets. i.e.

http://<your Pi's IP address>/ha/sockets

Two sockets should have been created by default when you installed the system.

#### Adding additional sockets

On the sockets page is a form to add a socket. You simply need to enter a name and click Add.

It will be assigned the next available number (i.e. if there are two existing sockets, this will be assigned the number three). The Pi-mote supports up to four sockets, although multiple devices can be set to the same ID, so you can control more physical devices in this way (although they will all be switched on/off at the same time).

#### Changing the name of a socket

This isn't currently possibly via the UI, you will need to edit the sockets.json file in the config folder. See below for details.

#### Deleting a socket

This isn't currently possibly via the UI, you will need to edit the sockets.json file in the config folder. See below for details.

## Via the Command Line

The system pulls the information it displays from some JSON formatted configuration files. You can edit/update these files in place of using the web interface.

It's not possible to toggle sockets on and off via the command line, for that ability, check out the [energenie-pimote Python script](https://github.com/leepenney/energenie-pimote).

### Timers

To make add, remove or modify timers via the command line, you will need to edit the timers.json file in the config folder:

    sudo nano /var/www/ha/config/timers.json

See the [timers](timers.md) section for more information about what this file contains.

### Sockets

To make modifications to the sockets via the command line, you will need to edit the sockets.json file in the config folder:

    sudo nano /var/www/ha/config/sockets.json
    
See the [sockets](sockets.md) section for more information about what this file contains.
