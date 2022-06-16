#!/usr/bin/python
# -*- codding: utf-8 -*-

import socket
from time import sleep

asterisk_login_command = '''Action: login
Events: off
Username: callbackuser
Secret: 1234\n\n'''

asterisk_call_command = '''Action: Originate
Channel: SIP/some_manager
Context: call_to_client
Exten: %s
Priority: 1
Callerid: 1112233
Timeout: 30000\n\n'''


def connect_to_asterisk(number=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '192.168.1.10'
    port = 5038

    s.connect((host, port))
    print(asterisk_login_command)
    s.send(bytes(asterisk_login_command, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    call_data = asterisk_call_command % number
    print(call_data)
    s.send(bytes(call_data, 'utf-8'))
    sleep(0.1)
    data = s.recv(1024)
    print(data)

    s.close()
