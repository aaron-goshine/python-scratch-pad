#! /usr/local/bin/python

import hashlib
import sys

try:
    hash_name = sys.argv[1]
except IndexError:
    print('Specify the hash name as the first argument.')
else:
    try:
        data = sys.argv[2]
    except IndexError:
        from sample_data import note

        h = hashlib.new(hash_name)
        h.update(note)
        print h.hexdigest()


