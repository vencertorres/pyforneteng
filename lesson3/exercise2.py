#!/usr/bin/env python

from __future__ import print_function

with open('show_arp.txt') as f:
    show_arp = f.readlines()

found_ip1 = False
found_ip2 = False
for line in show_arp[1:]:
    ip_addr = line.split()[1]
    mac_addr = line.split()[3]

    if ip_addr == '10.220.88.1':
        print('Default gateway IP/MAC: {} {}'.format(ip_addr, mac_addr))
        found_ip1 = True
    elif ip_addr == '10.220.88.30':
        print('Arista3 IP/MAC: {} {}'.format(ip_addr, mac_addr))
        found_ip2 = True

    if found_ip1 and found_ip2:
        break
