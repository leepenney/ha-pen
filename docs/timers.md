# Timers

Timers are the programs that set sockets to come on or go off at specific times.

## Reviewing existing timers

You can find a list of existing timers on the home page of the web UI (i.e. http://<your Pi's IP>/ha)

Each existing timer will be list with the appropriate settings.

The details of each timer can also be found in the config file (see below).

## Adding a timer

You can add a timer via the web UI or directly to the timers.json file under the config folder (see below).

### Adding a timer via the web UI

You will find an Add Timer form on the main HA-Pen page. To add a timer:

1. Select the socket from the dropdown
2. Select the time to come on
3. Check the option for Sunrise or Sunset if you wish the system to auto-update the on time with one of those values
4. Select the time for it to go off
5. Check the option for Sunrise or Sunset if you wish the system to auto-update the off time with one of those values
6. Select which days the timer should be invoked:
    * everyday - invoked it every day of the week
    * weekdays - only invoke the timer on weekdays (i.e. Mon-Fri)
    * weekends - only invoke the timer on weekends (i.e. Sat & Sun)
7. Add any rules you wish (see below)
8. Click Add

The new timer should appear below any existing ones.

## Modifying a timer

A timer's settings can be changed via the web UI or via the timers.json config file (see below).

### Modifying a timer via the web UI

To change the details of a timer via the web interface simply change the relevant setting(s) and hit Save. If the action was successfull the button will change to 'Saved.'

## Deleting a timer

A timer can be removed either via the web UI or by editing the timers.json config file (see below).

### Deleting a timer via the web UI

To remove a timer, simply click the Delete button on the relevant entry. The timer should then disappear from the list.

## Timer rules (beta)

Rules is a feature to allow advanced control of when a timer in invoked. It allows you to tell the system to only invoke a timer if a certain scenario is true. For example, if you want a timer to come on only if the on time is less than or equal to sunrise minus twenty minutes you can use the following rule:

    on <= sunrise-20
    
### Supported operators and keywords

The following operators can be used in rules:

```
- **<=**
- **>=**
- **<**
- **>**
- **!=**
```

In addition, the following keywords are supported:

- **sunrise** - converted to the time of today's sunrise
- **sunset** - converted to the time of today's sunset
- **HH:MM** - it should be possible to use an arbitary time (untested)

## Definition of the timers file

An outline of the timers.json config file. An alternative to using the web UI is to edit this file and make changes directly to it.

### Location

The timers are stored in JSON format in a file under the config folder, you can edit it using:

    sudo nano /var/www/ha/config/timers.json

### Format

The file is formatted with each timer having a dictionary entry defined as:

```
{
    "socket_num": 1,
    "on": "09:00",
    "off": "14:00",
    "days": "everyday",
    "sunrise": "on",
    "sunset": false,
    "rules": ""
}
```
