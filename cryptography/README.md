### cryptography

Encryption secures messages so that they can be verified as accurate and protected from interception.
Python's cryptography support includes `hashlib` for generating signatures of message content using standard algorithms, such as MD5 and SHA, and `humc` for verifying that a message has not been alerted in transmission.

The `hashlib` module deprecates the separate `md5` and `sha` module and makes their API consistent. To work with a specific hash algorithm, use the appropriate constructor function to create a hash object. From there, the objects use the same API, no matter what algorithm is being used.

Since `hashlib` is "backed" by OpenSSL, all algorithms provided by that library are available, including

- md5
- sha1
- sha224
- sha256
- sha384
- sha512

### Reference materials

##### Hmac
[hmac doc](https://docs.python.org/3/library/hmac.html#module-hmac)
The standard library documentation for this module.

##### RFC 2104
[rfc2104](http://tools.ietf.org/html/rfc2104.html)
HMAC: keyed-Hashing for Message Authentication.

#### hashlib
[hashlib](https://docs.python.org/3/library/hashlib.html#module-hashlib)
The hashlib module provides the hash generators listed above.

#### pickle
[pickle](https://docs.python.org/3/library/pickle.html#module-pickle)
Serialization library.

