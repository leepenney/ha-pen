from bottle import Bottle, route, run, jinja2_view as view, jinja2_template as template, debug, static_file, request
from lib.sockets import SocketController
from lib import energenie_pig as energenie
from lib import timers
import os, json

app = Bottle()

@route('/')
def index_page():
    socket_info = SocketController('webapp')
    socket_list = socket_info.get_socket_list()
    
    timers_list = timers.get_timers()
    
    return template('index.html',
        { 
            'title': 'HA-Pen',
            'sockets': socket_list,
    	    'path': request.fullpath,
    	    'timers': timers_list
        }
    )

@route('/toggle/<socket_num>')
def toggle_socket(socket_num):
    socket_info = SocketController('webapp')
    socket_list = socket_info.get_socket_list()
    
    for socket in socket_list:
        command = False
        if socket_num == str(socket['num']):
            command = 'off' if socket['state'] else 'on'
        elif socket_num in ['01','00']:
            command = 'off' if socket_num == '00' else 'on'
        
        if command:
            result = energenie.switch_socket(socket_num[:1], command)
            if result:
                set_state = True if command == 'on' else False
                socket_info.update_socket_state(socket_num, set_state)
                prefix = 'all:' if socket_num in ['00','01'] else ''            
                return '{}{}'.format(prefix,command)
            else:
                return 'failed'
            
@route('/del/<timer_num>')
def delete_timers(timer_num):
    timers_list = timers.get_timers()
    for i, timer in enumerate(timers_list):
        if i == int(timer_num):
            del timers_list[i]
    if timers.save_timers(timers_list):
        return 'saved'
    else:
        return 'failed'
        
@route('/mod/<timer_num>', method='POST')
def modify_timer(timer_num):
    import urllib
    timers_list = timers.get_timers()
    for i, timer in enumerate(timers_list):
        if i == int(timer_num):
            timer['on'] = urllib.unquote(request.forms.get('on'))
            timer['off'] = urllib.unquote(request.forms.get('off'))
            timer['days'] = request.forms.get('days')
            timer['rules'] = request.forms.get('rules')
            if request.forms.get('on-rise') == 'true':
                timer['sunrise'] = 'on'
            elif request.forms.get('off-rise') == 'true':
                timer['sunrise'] = 'off'
            else:
                timer['sunrise'] = False
            if request.forms.get('on-set') == 'true':
                timer['sunset'] = 'on'
            elif request.forms.get('off-set') == 'true':
                timer['sunset'] = 'off'
            else:
                timer['sunset'] = False
    if timers.save_timers(timers_list):
        return 'saved'
    else:
        return 'failed'

@route('/add/', method='POST')
def add_new_timer():
    import urllib
    timers_list = timers.get_timers()
    new_timer = {}
    new_timer['socket_num'] = int(request.forms.get('socket'));
    new_timer['on'] = urllib.unquote(request.forms.get('on'))
    new_timer['off'] = urllib.unquote(request.forms.get('off'))
    new_timer['days'] = request.forms.get('days')
    new_timer['rules'] = request.forms.get('rules')
    if request.forms.get('on-rise') == 'true':
        new_timer['sunrise'] = 'on'
    elif request.forms.get('off-rise') == 'true':
        new_timer['sunrise'] = 'off'
    else:
        new_timer['sunrise'] = False
    if request.forms.get('on-set') == 'true':
        new_timer['sunset'] = 'on'
    elif request.forms.get('off-set') == 'true':
        new_timer['sunset'] = 'off'
    else:
        new_timer['sunset'] = False
    timers_list.append(new_timer)
    if timers.save_timers(timers_list):
        socket_info = SocketController('webapp')
        socket_list = socket_info.get_socket_list()
        return template('timer_list.html',
            {
                'sockets': socket_list,
                'timers': timers_list
            }
        )
    else:
        return 'failed'
        
@route('/sockets')
def show_sockets():
    socket_info = SocketController('webapp')
    socket_list = socket_info.get_socket_list()
    return template('sockets.html',
        {
            'title': 'HA-Pen - Sockets',
            'sockets': socket_list,
            'devices': {},
            'path': request.fullpath[:request.fullpath.rfind('/')]
        }
    )

@route('/sockets/add/', method='POST')
def add_socket():
    import urllib
    socket_info = SocketController('webapp')
    socket_list = socket_info.get_socket_list()
    
    skt_name = urllib.unquote(request.forms.get('name'))
    socket_list.append({
            "state": False,
            "num": len(socket_list)+1,
            "name": skt_name
            })
    if socket_info.save_sockets(socket_list):
        return 'success'
    else:
        return 'failed'

@route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root='static')

