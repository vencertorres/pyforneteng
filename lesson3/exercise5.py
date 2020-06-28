#!/usr/bin/env python

from __future__ import print_function
import os

WINDOWS = False

base_ip = '10.10.100.'
base_cmd_linux = 'ping -c 2'
base_cmd_windows = 'ping -n 2'

WINDOWS = True if os.name == 'nt' else False
base_cmd = base_cmd_windows if WINDOWS else base_cmd_linux

ip_addr_list = []
for i in range(1, 255):
    ip_addr_list.append(base_ip + str(i))

for index, ip_addr in enumerate(ip_addr_list):
    print('{} ---> {}'.format(index, ip_addr))

ip_addr_list = ip_addr_list[2:6]

for ip_addr in ip_addr_list:
    os.system('{} {}'.format(base_cmd, ip_addr))
