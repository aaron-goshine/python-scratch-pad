#! /usr/local/bin/python

import hashlib
from sample_data import note
hash_name = "md5"
h = hashlib.new(hash_name)
h.update(note)
all_at_once = h.hexdigest()


def chunksize(size, text):
    "Return parts of the text in size-based increments."
    start = 0
    while start < len(text):
        chunk = text[start: start + size]
        yield chunk
        start += size
    return

h = hashlib.new(hash_name)
for chunk in chunksize(64, note):
    h.update(chunk)
    line_by_line = h.hexdigest()
    print('All at once  :', all_at_once)
    print('Line by line :', line_by_line)
    print('Ass at once  :', (all_at_once == line_by_line))
