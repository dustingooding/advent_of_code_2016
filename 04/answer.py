#!/usr/bin/env python

import operator
import re


class Room:
    def __init__(self, description=''):
        m = re.match(r"([a-z\-]+)-([0-9]+)\[([a-z]+)\]", description)
        self.cypher_text = m.group(1)
        self.sector_id = int(m.group(2))
        self.checksum = m.group(3)

    def real(self):
        letters = {}
        for letter in self.cypher_text.replace('-',''):
            if letter in letters:
                letters[letter] = letters[letter] + 1
            else:
                letters[letter] = 1
        sorted_letters = sorted(letters.items(), key=operator.itemgetter(1), reverse=True)

        counts = {}
        for letter, count in sorted_letters:
            if count in counts:
                counts[count] += letter
            else:
                counts[count] = letter
        sorted_counts = sorted(counts.items(), reverse=True)

        calculated_checksum = ''
        for count, substring in sorted_counts:
            if len(calculated_checksum) < len(self.checksum):
                if len(calculated_checksum) + len(substring) <= len(self.checksum):
                    calculated_checksum += ''.join(sorted(substring))
                else:
                    letters_to_add = len(self.checksum) - len(calculated_checksum)
                    calculated_checksum += ''.join(sorted(substring))[:letters_to_add]
            else:
                break

        if calculated_checksum == self.checksum:
            return True
        else:
            return False

    def decrypt(self):
        plain_text = ''
        for letter in self.cypher_text:
            if letter == '-':
                plain_text += ' '
            else:
                letter_index = ord(letter) - 97
                shifted_letter_index = (letter_index + self.sector_id) % 26
                shifted_letter = chr(shifted_letter_index + 97)
                plain_text += shifted_letter
        return plain_text

with open('input') as f:
    input_data = f.readlines()
input_data_stripped = [x.strip() for x in input_data]

# part 1

sector_id_sum = 0
all_rooms = [Room(entry) for entry in input_data_stripped]
for room in all_rooms:
    if room.real():
        sector_id_sum += room.sector_id

print 'part 1:', sector_id_sum

# part 2

all_rooms = [Room(entry) for entry in input_data_stripped]
for room in all_rooms:
    if room.real():
        if 'north' in room.decrypt():
            print 'part 2:', room.sector_id
            break