#!/usr/bin/env python

import re

class AbbaTester:
    def __init__(self):
        pass

    def has_abba(self, sequence):
        if len(sequence) >= 4:
            for i in range(0, len(sequence)-3):
                if (sequence[i] != sequence[i+1]) and (sequence[i:i+2] == ''.join(reversed(sequence[i+2:i+4]))):
                    return True
        return False

class IpAddress:
    def __init__(self, sequence):
        self.abba_tester = AbbaTester()
        self.nets = re.split(r"\[[a-z]+\]", sequence)
        self.hypernets = re.findall(r"\[([a-z]+)\]", sequence)

    def supports_tls(self):
        for hypernet in self.hypernets:
            if self.abba_tester.has_abba(hypernet):
                return False
        for net in self.nets:
            if self.abba_tester.has_abba(net):
                return True
        return False

with open('input') as f:
    input_data = f.read()

# part 1

tls_count = 0
for ip in input_data.split('\n'):
    ipaddress = IpAddress(ip)
    if ipaddress.supports_tls():
        tls_count += 1

print 'part1 :', tls_count
