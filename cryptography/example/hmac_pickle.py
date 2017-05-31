#! /usr/local/bin/python

import hashlib
import hmac
try:
    import cPickle as pickle
except:
    import pickle

from StringIO import StringIO

secret_key = 'secret-shared-key-goes-here'


def make_digest(message):
    "Return a digest for the message."
    hash = hmac.new(secret_key, message, hashlib.sha1)
    return hash.hexdigest()


class SimpleObject (object):
    """A Very simple class to demonstrate
    checking digests before unpickling."""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


# Simulate a writable socket of pipe with StringIO
out__s = StringIO()

# Write a valid object to the stream:
# digest \n length \n pickle
o = SimpleObject('digest matches')
pickled_data = pickle.dumps(o)
digest = make_digest(pickled_data)
header = '%s %s' % (digest, len(pickled_data))
print ('WRITING:', header)
out__s.write(header + '\n')
out__s.write(pickled_data)

# Write a invalid object to the stream:
# digest \n length \n pickle
o = SimpleObject('digest does not matches')
pickled_data = pickle.dumps(o)
digest = make_digest('not the pickled data at all')
header = '%s %s' % (digest, len(pickled_data))
print('\n WRITING:', header)
out__s.write(header + '\n')
out__s.write(pickled_data)

out__s.flush()

# Simulate a readable socket of a pipe with StringIO
in__s = StringIO(out__s.getvalue())

# Read the data
while True:
    first_line = in__s.readline()
    if not first_line:
        break
    incoming_digest, incoming_length = first_line.split(' ')
    incoming_length = int(incoming_length)
    print('\nREAD:', incoming_digest, incoming_length)

    incoming_pickled_data = in__s.readline(incoming_length)

    actual_digest = make_digest(incoming_pickled_data)
    print('ACTUAL:', actual_digest)
    if incoming_digest != actual_digest:
        print('WARNING: Data corruption')
    else:
        obj = pickle.loads(incoming_pickled_data)
        print('OK:', obj)
