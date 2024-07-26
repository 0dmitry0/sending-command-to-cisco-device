import json
import telebot
from netmiko import ConnectHandler

def json_reader(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        return data

def json_list_parser(data):
    for switch, hosts in data.items():
        print(switch)

class connection:
    def __init__(self):
        self.ip = ''
        self.username = ''
        self.password = ''

    def device_params(self, data, switch_choose):
        
        for switch, hosts in data.items():
            if switch == switch_choose:
                for host in hosts:
                    self.ip = host['ip']
                    self.username = host['username']
                    self.password = host['password']
                    
    def connection_init(self, command):
        device = ConnectHandler(device_type='cisco_ios', ip=self.ip, username=self.username, password=self.password)
        print(self.ip, self.username, self.password)
        output = device.send_command(command)
        device.disconnect()
        return output

while True:
    data = json_reader('/Users/user/Desktop/bot-project/hosts.json')
    json_list_parser(data)
    switch_choose = input('Введите наименование устройства, с которым хотите работать.')
    device_instance = connection()
    device_instance.device_params(data, switch_choose)
    command = input('Введите команду, которую хотите отправить на устройство.')
    output = device_instance.connection_init(command)
    print(output)
