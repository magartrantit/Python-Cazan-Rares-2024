l1 = [80, 84, 79, 32, 117, 101]
l2 = [121, 104, 110, 82, 76, 83]
result = ''.join(chr(l1[i]) + chr(l2[i]) for i in range(len(l1)))
print(result)