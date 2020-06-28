#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint

with open('show_vlan.txt') as f:
    show_vlan = f.readlines()

vlan_info = []
for line in show_vlan[2:]:
    if line.split()[0].isdigit():
        vlan_id = line.split()[0]
        vlan_name = line.split()[1]
        vlan_info.append((vlan_id, vlan_name))

pprint(vlan_info)
