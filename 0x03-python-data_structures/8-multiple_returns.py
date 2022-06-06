#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        mytuple = (0, None)
    else:
        mytuple = (len(sentence), sentence[:1])
    return(mytuple)