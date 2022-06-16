#!/usr/bin/python
# -*- codding: utf-8 -*-

import socket
from time import sleep

HOST = '192.168.1.10'
PORT  = 5038

asterisk_login_command = '''Action: login
Events: off
Username: callbackuser
Secret: 1234\n\n'''

asterisk_call_command = '''Action: Originate
Channel: SIP/some_manager
Context: call_to_client
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

    call_data = f'asterisk_call_command' % number
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

    call_data = asterisk_call_command.format(phone_from, phone_to)
    print(call_data)
    s.send(bytes(call_data, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    s.close()
