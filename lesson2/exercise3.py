#!/usr/bin/env python

from __future__ import print_function
from pprint import pprint

with open('show_arp.txt') as f:
    show_arp = f.readlines()

# Remove header line
show_arp = show_arp[1:]
pprint(show_arp)

show_arp.sort()

# Get first three entries
arp_entries = show_arp[:3]
arp_entries = '\n'.join(arp_entries)

with open('arp_entries.txt', 'w') as f:
    f.write(arp_entries)
