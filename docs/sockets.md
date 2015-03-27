# Sockets

Sockets are the physical plugs that you plug into a power outlet and which you then plug devices into. The default Pi-mote pack comes with two (if you elect to buy it that way), but the device can control up to four.

## Reviewing sockets

You'll see the current sockets available from the dropdown in the Add Timer form on the main page.

Alternatively, head to http://<your Pi's IP>/ha/sockets in a browser to see the existing devices.

If you prefer the command line, you'll find the socket details under /var/www/ha/config/sockets.json

## Adding a socket

The application comes pre-configured for two sockets. If you wish to add additional sockets, you can do this in two ways:

1. via the web UI
2. by editing the sockets.json file

### Via the web UI

To add a socket via the web UI, head to http://<your Pi's IP>/ha/sockets in a web browser.

On the right you'll see an Add Device form.

Fill in the name of the device (e.g. the location) to be able to identify it, then click Add.

**Note:** The system won't prevent you adding more than four sockets, but only four will work.

### Via the command line

To add a socket via the command line, you need to edit config/sockets.json

    sudo nano /var/www/ha/config/sockets.json

It's a JSON formatted file, so add a new dictionary using this format:

```
{
    "state": false,
    "num": 3,
    "name": "Socket 3"
}
```

Where:

* **State** is the current statue (true for on, false for off)
* **num** is the socket number (needs to be an int, not a string, just add one to the previous highest)
* **name** the name used in the web UI, used to identify it

## Removing a socket

Currently, the only way to remove a socket is to edit the sockets.json file. You need to run:

    sudo nano /var/www/ha/config/sockets.json

Then remove the relevant dictionary (the text between the opening { and closing }, and delete the comma the precedes the opening curly bracket.

