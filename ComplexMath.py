#!/usr/bin/python
# 15foleyj
#Complex Beginnings

def complexAdd(a,b):
    realAnswer = a[0] + b[0]
    imagAnswer = a[1] + b[1]
    return (realAnswer, imagAnswer)
print complexAdd((1,5), (1,1))
print complexAdd((1,2), (3,1))
print complexAdd((0,4), (22, -6))
print complexAdd((0,4), complexAdd((22,-6), (15,-3)))
print complexAdd((1,4), complexAdd((1,1), (1,1)))
