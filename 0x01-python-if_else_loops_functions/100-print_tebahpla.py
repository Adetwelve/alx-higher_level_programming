#!/usr/bin/python3
for alpha in range(ord('z'), ord('a') - 1, -1):
    if alpha % 2 == 1:
        alpha -= (ord('a') - ord('A'))
    print("{:c}".format(alpha), end='')
