#!/usr/bin/env python

from __future__ import print_function

with open('show_ip_bgp_summ.txt') as f:
    show_ip_bgp_summ = f.readlines()

first_line = show_ip_bgp_summ[0]
last_line = show_ip_bgp_summ[-1]

as_number = first_line.split()[-1]
bgp_peer_ip = last_line.split()[0]

print(f'AS number: {as_number}')
print(f'BGP Peer IP address: {bgp_peer_ip}')
