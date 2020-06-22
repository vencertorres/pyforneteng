#!/usr/bin/env python

from __future__ import print_function

ip_addr = input('Please enter an IP address: ')
octets = ip_addr.split('.')

print(f'{"Octet1":^15}{"Octet2":^15}{"Octet3":^15}{"Octet4":^15}')
print('-' * 60)
print(f'{octets[0]:^15}{octets[1]:^15}{octets[2]:^15}{octets[3]:^15}')
print(f'{bin(int(octets[0])):^15}{bin(int(octets[1])):^15}'
      f'{bin(int(octets[2])):^15}{bin(int(octets[3])):^15}')
print(f'{hex(int(octets[0])):^15}{hex(int(octets[1])):^15}'
      f'{hex(int(octets[2])):^15}{hex(int(octets[3])):^15}')
print('-' * 60)
