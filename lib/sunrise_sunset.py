#from astral import Astral
import astral, pytz, os, sys, json
import datetime, time
from time import mktime
from datetime import timedelta

def sunset_for_today():
    today = datetime.datetime.now()
    offset = int((mktime(time.localtime())-mktime(time.gmtime()))/60/60)
    long_lat = get_long_lat()

    this_location = astral.Location()
    this_location.longitude = long_lat['longitude']
    this_location.latitude = long_lat['latitude']
    this_location.solar_depression = 'civil'

    return this_location.sunset(date=today) + timedelta(hours=offset)

def sunrise_for_today():
    today = datetime.datetime.now()
    offset = int((mktime(time.localtime())-mktime(time.gmtime()))/60/60)
    long_lat = get_long_lat()

    this_location = astral.Location()
    this_location.longitude = long_lat['longitude']
    this_location.latitude = long_lat['latitude']
    this_location.solar_depression = 'civil'

    return this_location.sunrise(date=today) + timedelta(hours=offset)

def get_long_lat():
    #script_path = os.path.dirname(__file__)
    #os.chdir(script_path)
    settings_file_path = os.path.join(sys.path[0],'..','config/settings.json')

    #settings_json = open('../config/settings.json')
    settings_json = open(settings_file_path)
    settings = json.load(settings_json)
    settings_json.close()

    return {'longitude': settings[0]['longitude'],
            'latitude': settings[0]['latitude']}

def update_timers():
    script_path = os.path.dirname(__file__)
    os.chdir(script_path)
    timers_file_path = '../config/timers.json'

    timers_json = open(timers_file_path)
    timers_list = json.load(timers_json)
    timers_json.close()

    long_lat = get_long_lat()

    for timer in timers_list:
        if timer['sunset']:
            #sunset = sunset_for_today(long_lat['longitude'],long_lat['latitude'])
            sunset = sunset_for_today()
            if timer['sunset'] == 'on':
                timer['on'] = sunset.strftime('%H:%M')
            else:
                timer['off'] = sunset.strftime('%H:%M')
        if timer['sunrise']:
            #sunrise = sunrise_for_today(long_lat['longitude'],long_lat['latitude'])
            sunrise = sunrise_for_today()
            if timer['sunrise'] == 'off':
                timer['off'] = sunrise.strftime('%H:%M')
            else:
                timer['on'] = sunrise.strftime('%H:%M')

    with open(timers_file_path, 'w') as json_file:
        json.dump(timers_list, json_file, indent=4)

if __name__ == '__main__':
    update_timers()
