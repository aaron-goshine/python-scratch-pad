#! /usr/local/bin/python

import hmac

digest_maker = hmac.new('secret-shared-key-goes-here')

with open('sample_data.py', 'rb') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        digest_maker.update(block)


digest = digest_maker.hexdigest()

print(digest)
