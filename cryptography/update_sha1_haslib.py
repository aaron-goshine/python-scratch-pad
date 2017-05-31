#! /usr/local/bin/python

import hmac
import hashlib

digest_maker = hmac.new('secret-shared-key-goes-here', '', hashlib.sha1)

with open('update_hashlib.py', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)
digest = digest_maker.hexdigest()

print(digest)
