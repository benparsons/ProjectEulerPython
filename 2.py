#! /bin/python
current = 1
cumulative = 0
previous = 1
while current < 4000000:
    if (current % 2 == 0):
        cumulative += current
    temp = current
    current += previous
    previous = temp
    print(previous, current, cumulative)