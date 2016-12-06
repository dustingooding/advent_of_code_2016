#!/usr/bin/env python

import operator


class RepetitionCode:
    def __init__(self, msg_size = 0, use_most = True):
        self.msg_size = msg_size
        self.msg_position_letters = [{} for x in range(self.msg_size)]
        self.use_most = use_most

    def add(self, signal):
        for i in range(self.msg_size):
            if signal[i] in self.msg_position_letters[i]:
                self.msg_position_letters[i][signal[i]] += 1
            else:
                self.msg_position_letters[i][signal[i]] = 1

    def msg(self):
        message = ''
        sorted_msg_position_letters = [{} for x in range(self.msg_size)]
        for i in range(self.msg_size):
            sorted_msg_position_letters[i] = sorted(self.msg_position_letters[i].items(), key=operator.itemgetter(1), reverse=self.use_most)
            message += sorted_msg_position_letters[i][0][0]
        return message

with open('input') as f:
    input_data = f.read()

# part 1

rep_code = RepetitionCode(8)

for msg in input_data.split('\n'):
    rep_code.add(msg.strip())
print 'part 1:', rep_code.msg()

# part 2

rep_code = RepetitionCode(8, False)

for msg in input_data.split('\n'):
    rep_code.add(msg.strip())
print 'part 2:', rep_code.msg()