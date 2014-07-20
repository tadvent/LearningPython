import os
import os.path
import random

def randstr(length):
    str = ""
    for i in xrange(length):
        str = str + random.choice("abcedfghijklmnopqrstuvwxyz")
    return str

def randfile(file, length):
    fnlist = os.path.splitext(file)
    if len(os.path.basename(fnlist[0])) > 4:
        return None
    newname = fnlist[0] + randstr(length) + fnlist[1]
    os.rename(file, newname)

if __name__ == "__main__":
    random.seed()
    for file in os.listdir('.'):
        if os.path.isfile(file):
            randfile(file, 10)

            