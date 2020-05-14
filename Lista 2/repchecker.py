import os
import sys
import hashlib

PATH = sys.argv[1]


def dir_search(directory):
    hash_list = []
    for root, dirs, files in os.walk("."):
        for file in files:
            with open(root+os.sep+file, "rb") as f:
                data = f.read()
                md5 = hashlib.md5(data).hexdigest()
                size = len(root.encode())
                hash_list.append((md5, size, root+os.sep+file))
    return hash_list


def count_files(item, list_):
    counter = 0
    for i in list_:
        if i[0] == item[0] and i[1] == item[1]:
            counter += 1
    return counter


def remove_non_duplicates(list_):
    new_list = [i for i in list_ if count_files(i, list_) > 1]
    return new_list


def sort_key(item):
    return str(item[0]) + str(item[1])


files = dir_search(PATH)
files = remove_non_duplicates(files)
files = sorted(files, key=sort_key)


current_file = files[0]
for i in files:
    if i[0] != current_file[0] or i[1] != current_file[1]:
        print("--------------------------")
        print(i[2])
    else:
        print(i[2])
    current_file = i
