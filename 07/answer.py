#!/usr/bin/env python

import re

class Sequencer:
    def __init__(self):
        pass

    def has_abba(self, sequence):
        if len(sequence) >= 4:
            for i in range(0, len(sequence)-3):
                if (sequence[i] != sequence[i+1]) and (sequence[i:i+2] == ''.join(reversed(sequence[i+2:i+4]))):
                    return True
        return False

    def get_abas(self, sequence):
        abas = []
        if len(sequence) >= 3:
            for i in range(0, len(sequence)-2):
                if (sequence[i] != sequence[i+1]) and (sequence[i] == sequence[i+2]):
                    abas.append(sequence[i:i+3])
        return abas

    def has_bab(self, sequence, aba):
        if len(aba) == 3:
            bab = aba[1] + aba[0] + aba[1]
            if bab in sequence:
                return True
        return False

class IpAddress:
    def __init__(self, address):
        self.sequencer = Sequencer()
        self.nets = re.split(r"\[[a-z]+\]", address)
        self.hypernets = re.findall(r"\[([a-z]+)\]", address)

    def supports_tls(self):
        for hypernet in self.hypernets:
            if self.sequencer.has_abba(hypernet):
                return False
        for net in self.nets:
            if self.sequencer.has_abba(net):
                return True
        return False

    def supports_ssl(self):
        aba_list = []
        for net in self.nets:
            aba = self.sequencer.get_abas(net)
            if aba: 
                aba_list.extend(aba)
        for hypernet in self.hypernets:
            for aba in aba_list:
                if self.sequencer.has_bab(hypernet, aba):
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
print 'part1:', tls_count

# part 2

ssl_count = 0
for ip in input_data.split('\n'):
    ipaddress = IpAddress(ip)
    if ipaddress.supports_ssl():
        ssl_count += 1
print 'part2:', ssl_count