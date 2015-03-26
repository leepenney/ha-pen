import os, sys, json, time, datetime
import energenie_pig as energenie
from sockets import SocketController
from datetime import timedelta


def check_timers():
    timers_file_path = os.path.join(sys.path[0],'..','config/timers.json')
    weekday = [0,1,2,3,4]
    weekend = [5,6]

    timers_json = open(timers_file_path)
    timers_list = json.load(timers_json)
    timers_json.close()

    current_datetime = datetime.datetime.now()

    for timer in timers_list:
        if (timer['days'] == 'everyday' or 
                (timer['days'] == 'weekdays' and current_datetime.weekday() < 5) or
                (timer['days'] == 'weekends' and current_datetime.weekday() > 4)):

            # TODO - add handling for blank times (due to sunrise/sunset)
            on_datetime = modify_dt(current_datetime, timer['on'])
            on_diff = (current_datetime - on_datetime).seconds
            
            off_datetime = modify_dt(current_datetime, timer['off'])
            off_diff = (current_datetime - off_datetime).seconds

            update_socket = SocketController('cron')
            if len(timer['rules']) > 0:
                rule_result = process_rules(timer['rules'], on_datetime, off_datetime)
            else:
                rule_result = True
            
            if (on_diff > 0) and (on_diff < 180) and rule_result:
                result = energenie.switch_socket(timer['socket_num'], 'on')
                if result:
                    update_socket.update_socket_state(timer['socket_num'], True)

            if (off_diff > 0) and (off_diff < 180) and rule_result:
               result = energenie.switch_socket(timer['socket_num'], 'off')
               if result:
                   update_socket.update_socket_state(timer['socket_num'], False)

def process_rules(timer_rules, on_dt, off_dt):
    import sunrise_sunset
    from datetime import timedelta
    
    current_dt = datetime.datetime.now()
    sunrise = sunrise_sunset.sunrise_for_today()
    sunset = sunrise_sunset.sunset_for_today()

    rule_list = timer_rules.split(',')
    for rule in rule_list:
        rule = rule.replace('sunrise',sunrise.strftime('%H:%M'))
        rule = rule.replace('sunset',sunset.strftime('%H:%M'))
        rule_breakdown = rule.split(' ')
        timer_dt = on_dt if rule_breakdown[0] == 'on' else off_dt

        modifier = '+' if '+' in rule_breakdown[2] else '-'

        calc_parts = rule_breakdown[2].split(modifier)
        rule_dt = create_rule_dt(current_dt, calc_parts[0], modifier, calc_parts[1])
        if not test_values(timer_dt, rule_breakdown[1], rule_dt):
            return False
    return True

def create_rule_dt(starting_dt, time_str, modify_op, modify_val):
    import operator
    ops = { '+':operator.add, '-':operator.sub }
    rule_dt = modify_dt(starting_dt, time_str)
    return ops[modify_op](rule_dt,timedelta(minutes=int(modify_val)))

def modify_dt(starting_dt, time_str):
    # modifies given datetime by settings hours from supplied time string
    # time_str format = %H:%M
    return starting_dt.replace(
                hour=int(time_str[:time_str.find(':')]),
                minute=int(time_str[time_str.find(':')+1:])
            )

def test_values(timer_dt, op, rule_dt):
    import operator
    timer_dt = (timer_dt - datetime.datetime(1970,1,1)).total_seconds()
    rule_dt = (rule_dt - datetime.datetime(1970,1,1)).total_seconds()
    
    ops = {
            '<=': operator.le,
            '>=': operator.ge,
            '<': operator.lt,
            '>': operator.gt,
            '!=': operator.ne
        }
    return ops[op](timer_dt, rule_dt)

if __name__ == '__main__':
    check_timers()
