s1, s2 = '11001101', '10110110'

h = 0
for i in range(len(s1)):
    if s1[i] != s2[i]:
        h += 1

print('The Hamming distance between the strings "{:s}" and "{:s}" is {:d}.'
        .format(s1, s2, h))