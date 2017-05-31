#!/usr/local/bin/python3
from sys import stdin, stdout

while True:
    line = stdin.readline()
    if not line :
        break
    stdout.write("%d \n" % int(line) ** 2)
    stdout.flush()

