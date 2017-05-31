
note = '''
Encryption secures messages so that they can be verified as
accurate and protected from interception. Python's cryptography
support includes hashlib for generating signatures of message
content using standard algorithms, such as MD5 and SHA, and humc
for verifying that a message has not been alerted in transmission.

The hashlib module deprecates the separate md5 and sha module and
makes their API consistent. To work with a specific hash algorithm,
use the appropriate constructor function to create a hash object. From there,
the objects use the same API, no matter what algorithm is being used.

Since hashlib is "backed" by OpenSSL, all algorithms provided by that
library are available, including
'''
