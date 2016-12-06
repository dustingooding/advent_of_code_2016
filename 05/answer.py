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

class InterestingPassword:
    def __init__(self, cypher_text=''):
        self.cypher_text = cypher_text

    def decrypt(self):
        plain_text = [None, None, None, None, None, None, None, None]
        attempt = 0
        while None in plain_text:
            md5sum = 'FFFFFF'
            while md5sum[0:5] != '00000':
                m = hashlib.md5(self.cypher_text + str(attempt))
                md5sum = m.hexdigest()
                attempt += 1

            plain_text_index = None
            try:
                plain_text_index = int(md5sum[5])
                if plain_text_index < len(plain_text):
                    if plain_text[plain_text_index] is None:
                        plain_text[plain_text_index] = md5sum[6]
            except ValueError:
                pass

        return ''.join(plain_text)

with open('input') as f:
    input_data = f.read().replace('\n', '')

# part 1

password = Password(input_data)
print 'part 1:', password.decrypt()

# part 2

password = InterestingPassword(input_data)
print 'part 2:', password.decrypt()
