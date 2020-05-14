import os
import sys

PATH = sys.argv[1]

files = os.listdir(path=PATH)
for file in files:
    os.rename(file, file.lower())