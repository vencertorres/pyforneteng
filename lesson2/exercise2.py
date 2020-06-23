#!/usr/bin/env python

from __future__ import print_function

ip_addr1 = ['10.0.0.0', '172.16.0.0', '192.168.0.0', '224.0.0.6', '224.0.0.10']
ip_addr1.append(['224.0.0.5', '224.0.0.9'])
ip_addr1.extend(['8.8.8.8', '8.8.4.4'])

ip_addr2 = ['1.1.1.1', '1.0.0.1']
ip_addr3 = ip_addr1 + ip_addr2

print(ip_addr3)
print(ip_addr3[0])
print(ip_addr3[-1])

ip_addr3.pop(0)
ip_addr3.pop(-1)
ip_addr3[0] = '2.2.2.2'

print(ip_addr3[0])
