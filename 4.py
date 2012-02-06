def isPalandrome(toTest):
    length = len(str(toTest))
    if length % 2 != 0:
        return False
    l0 = list(str(toTest))
    l1 = []
    l2 = []
    for i in range(0,length):
        if i > (length / 2) - 1:
            l1.append(l0[i])
        else:
            l2.append(l0[i])
    l2.reverse()
    if l1 != l2:
        return False
    return True

results = []
for x in range(1, 999):
    for y in range(x, 999):
        product = x*y
        if (isPalandrome(product)):
            results.append(product)
            #print(x, y, product)

results.sort()
print(results)