import os
import sys

path = sys.argv[1]

for root, dirs, files in os.walk(path):
    for f in files:
        if f[-4:] == '.png':
            print(f)