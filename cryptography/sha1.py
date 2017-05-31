import hashlib
from sample_data import note

h = hashlib.sha1()
h.update(note)
print h.hexdigest()


