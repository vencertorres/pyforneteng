#!/usr/bin/env python

from __future__ import print_function

show_version = '*0        CISCO881-SEC-K9       FTX0000038X    '
show_version = show_version.strip()

model = show_version.split()[1]
serial_number = show_version.split()[2]

print('Is "Cisco" in the model string: {}'.format('cisco' in model.lower()))
print('Is "881" in the model string: {}'.format('881' in model))

print('Serial Number: {}'.format(serial_number))
print('Model: {}'.format(model))
