#!/usr/bin/python

import sys

FILENAME = sys.argv[1]

with open(FILENAME) as f:
    data = f.read()

print("Liczba bajtów: ", len(data.encode()))
print("Liczba słów: ", len(data.split()))
print("Liczba linii: ", len(data.splitlines()))
print("Maksymalna długość linii: ", max([len(i) for i in data.splitlines()]))
