#!/usr/bin/python
# -*- codding: utf-8 -*-

import socket
from time import sleep

HOST = '192.168.1.9'
PORT = 5038

asterisk_login_command = '''Action: login
Events: off
Username: callbackuser
Secret: 1234\n\n'''

call_to = '''Action: Originate
Channel: SIP/some_manager
Context: call_to_client
Exten: %s
Priority: 1
Callerid: 1112233
Timeout: 30000\n\n'''

call_from_to = '''Action: Originate
Channel: SIP/some_manager
Context: call_from_abonent
Call_from: {}
Call_to: {}
Priority: 1
Callerid: 1112233
Timeout: 30000\n\n'''



def call_from_manager(number=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print(asterisk_login_command)
    s.send(bytes(asterisk_login_command, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    call_data = call_to % number
    print(call_data)
    s.send(bytes(call_data, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    s.close()


def call_from_abonent(phone_from=None, phone_to=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    s.connect((HOST, PORT))
    print(asterisk_login_command)
    s.send(bytes(asterisk_login_command, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    call_data = call_from_to.format(phone_from, phone_to)
    print(call_data)
    s.send(bytes(call_data, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    s.close()
