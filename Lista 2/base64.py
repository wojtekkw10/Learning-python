# !/usr/bin/python

import sys

CODING_TABLE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
OUTPUT_FILE = sys.argv[2]
INPUT_FILE = sys.argv[3]
CONFIG = sys.argv[1]


def binary_as_ascii(n):
    n = int(n, 2)
    if 0 <= n <= 63:
        return CODING_TABLE[n]
    else:
        return None


def list_to_string(list_):
    result = ""
    for i in list_:
        result+=i
    return result


if CONFIG == "--encode":
    with open(INPUT_FILE) as f:
        data = f.read()
        binary_data = ''.join(format(ord(i), 'b').zfill(8) for i in data)
        data_list = [binary_data[i:i+6] for i in range(0, len(binary_data), 6)]
        with open(OUTPUT_FILE, "w+") as f2:
            f2.write(list_to_string(list(map(binary_as_ascii, data_list))))
else:
    with open(INPUT_FILE) as f:
        data = f.read()
        binary_data = ''.join(format(CODING_TABLE.find(i), 'b').zfill(6) for i in data)
        data_list = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
        result = list_to_string([chr(int(i, 2)) for i in data_list])
        with open(OUTPUT_FILE, "w+") as f2:
            f2.write(result)
