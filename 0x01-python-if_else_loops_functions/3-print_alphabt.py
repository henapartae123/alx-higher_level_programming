#!/usr/bin/python3
for i in range(ord('a'), ord('z')):
    if chr(i) == "e" or chr(i) == "q":
        continue
    print ("{}".format(chr(i)), end ="")