#!/usr/bin/env python

import hashlib

class Password:
    def __init__(self, cypher_text=''):
        self.cypher_text = cypher_text

    def decrypt(self):
        plain_text = ''
        attempt = 0
        while len(plain_text) < 8:
            md5sum = 'FFFFFF'
            while md5sum[0:5] != '00000':
                m = hashlib.md5(self.cypher_text + str(attempt))
                md5sum = m.hexdigest()
                attempt += 1
            plain_text += md5sum[5]
        return plain_text

with open('input') as f:
    input_data = f.read().replace('\n', '')

# part 1

password = Password(input_data)
print 'part 1:', password.decrypt()