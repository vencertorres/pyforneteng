#!/usr/bin/env python

from __future__ import print_function

mac1 = 'Internet  10.220.88.29           94   5254.abbe.5b7b  ARPA   FastEthernet4'
mac2 = 'Internet  10.220.88.30            3   5254.ab71.e119  ARPA   FastEthernet4'
mac3 = 'Internet  10.220.88.32          231   5254.abc7.26aa  ARPA   FastEthernet4'

ip_addr1 = mac1.split()[1]
ip_addr2 = mac2.split()[1]
ip_addr3 = mac3.split()[1]

mac_addr1 = mac1.split()[3]
mac_addr2 = mac2.split()[3]
mac_addr3 = mac3.split()[3]

print('{:>20} {:>20}'.format('IP ADDR', 'MAC ADDRESS'))
print('{:>20} {:>20}'.format('-' * 20, '-' * 20))
print('{:>20} {:>20}'.format(ip_addr1, mac_addr1))
print('{:>20} {:>20}'.format(ip_addr2, mac_addr2))
print('{:>20} {:>20}'.format(ip_addr3, mac_addr3))
