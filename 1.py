#! /bin/python
l  = []
for x in range(0, 1000):
    if (x % 3 == 0 or x % 5 == 0):    
        l.append(x)
print l
print "\n"
print sum(l)
