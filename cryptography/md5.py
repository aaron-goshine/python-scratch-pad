import hashlib
from sample_data import note

h = hashlib.md5()
h.update(note)
print h.hexdigest()


