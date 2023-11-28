#!/usr/bin/python3
for ascii_letters in range(ord('a'), ord('z')+1):
    print(chr(ascii_letters).format(ascii_letters), end=" ")
