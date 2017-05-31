#! /usr/local/bin/python

import base64
import hmac
import hashlib

with open('update_hashlib.py', 'rb') as f:
        body = f.read()

hash = hmac.new('secret-shared-key-goes-here', body, hashlib.sha1)
digest = hash.digest()
print(base64.encodestring(digest))
