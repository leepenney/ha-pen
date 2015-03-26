import json, os, sys, inspect

class SocketController:
    socket_file_path = ''

    def __init__(self, called_from):
        if called_from == 'cron':
            SocketController.socket_file_path = os.path.join(sys.path[0],'..','config/sockets.json')
        else:
            SocketController.socket_file_path = os.path.join(os.getcwd(),'config/sockets.json')

    def get_socket_list(self):
        socket_json = open(SocketController.socket_file_path)
        socket_list = json.load(socket_json)
        socket_json.close()
        return socket_list

    def update_socket_state(self, socket_num, set_state):
        socket_list = self.get_socket_list()
        for socket in socket_list:
            if str(socket['num']) == str(socket_num):
                socket['state'] = set_state
        with open(SocketController.socket_file_path, 'w') as json_file:
            json.dump(socket_list, json_file, indent=4)

    def save_sockets(self, socket_list):
        try:
            with open(SocketController.socket_file_path, 'w')  as socket_file:
                json.dump(socket_list, socket_file, indent=4)
            return True
        except Exception,e:
            print('Error {}'.format(e))
            return False

