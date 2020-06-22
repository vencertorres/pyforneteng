#!/usr/bin/env python

from __future__ import print_function

show_version = "*0        CISCO881-SEC-K9       FTX0000038X    "
show_version = show_version.strip()

model = show_version.split()[1]
serial_number = show_version.split()[2]

print(f"Is 'Cisco' in the model string: {'cisco' in model.lower()}")
print(f"Is '881' in the model string: {'881' in model}")

print(f"Serial Number: {serial_number}")
print(f"Model: {model}")
