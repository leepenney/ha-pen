import os, sys, json

def get_timers():
    timers_file_path = os.path.join(sys.path[0],'config/timers.json')
    
    timers_json = open(timers_file_path)
    timers_list = json.load(timers_json)
    timers_json.close()
    
    return timers_list
    
def save_timers(timers_list):
    timers_file_path = os.path.join(sys.path[0],'config/timers.json')
    
    try:
        with open(timers_file_path,'w') as timers_file:
            json.dump(timers_list, timers_file, indent=4)
        return True
    except Exception,e:
        print('Error {}',format(e))
        return False

