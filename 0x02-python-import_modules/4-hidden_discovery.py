#!/usr/bin/python3
import hidden_4
i = 0
if __name__ == '__main__':
    list = dir(hidden_4)
    newlist = sorted(list)
    while i < len(newlist):
        if newlist[i][0] != '_':
            print(newlist[i])
        i += 1