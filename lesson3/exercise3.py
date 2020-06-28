#!/usr/bin/env python

from __future__ import print_function

with open('show_lldp_neighbors_detail.txt') as f:
    show_lldp = f.readlines()

found_port_id = False
found_system_name = False
for line in show_lldp:
    if 'Port id: ' in line:
        port_id = line.split()[2]
        found_port_id = True
    elif 'System Name: ' in line:
        system_name = line.split()[2]
        found_system_name = True

    if found_port_id and found_system_name:
        break

print('Port id: {}'.format(port_id))
print('System Name: {}'.format(system_name))
