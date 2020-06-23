#!/usr/bin/env python

from __future__ import print_function

with open('show_ip_int_brief.txt') as f:
    show_ip_int_brief = f.readlines()

# Get FastEthernet4 interface details
fast_eth4 = show_ip_int_brief[5]

intf_name = fast_eth4.split()[0]
ip_address = fast_eth4.split()[1]

intf_information = (intf_name, ip_address)

print(intf_information)
