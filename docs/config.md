# Configuring HA-Pen

This section runs through how to config HA-Pen properly. The only necessity is setting your longitude and latitude.

## Setting longitude and latitude

In order to calculate sunrise and sunset you need to enter you longitude and latitidue in the **settings.json** file in the **config** folder

### Working out your longitude and latitude

The easiest way to figure out your location is to do a search for it in [Google Maps](http://maps.google.com).

In the URL you'll find the figures you need. For example, if you [search for Greenwich (UK)](https://www.google.co.uk/maps/place/Greenwich,+London+SE10/@51.482576,-0.0076589,15z/data=!3m1!4b1!4m2!3m1!1s0x47d8a9cea79975f3:0x1470a7a162e4ca6c) you'll find it contains: 51.482576,-0.0076589

51.482576 is the latitude
-0.0076589 is the longitude

### Saving the values

You need to edit the settings.json file:

    sudo nano /var/www/ha/config/settings.json

You'll see a file that looks like this:

```
[
    {
        "longitude": -0.0076589
        "latitude": 51.482576
    }
]
```

Replace the values with the ones for the location you want to use. When done, press CTRL+X, then hit y and Enter to save and exit.

## Timers

See the [timers](timers.md) section for more information on setting up timers.

## Sockets

See the [sockets](sockets.md) section for more information on the sockets.
