#coding=utf-8

import os, sys, random, re
import os.path

def randstr(length):
    str = ""
    for i in range(length):
        str += random.choice("_0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    return str

def newfname(filename):
    npattern = re.compile(r'(?<=_\[)\w{5}(?=\]$)')
    namelist = os.path.splitext(filename)
    mo = npattern.search(namelist[0])
    if mo:
        replacestr = randstr(5)
        while replacestr == mo.group():
            replacestr = randstr(5)
        return npattern.sub(replacestr, namelist[0]) + namelist[1]
    else:
        return namelist[0] + '_[' + randstr(5) + ']' + namelist[1]

def labelnameout(names):
    for i in range(len(names)):
        print(i+1, ':', names[i])

def getnameorder():
    nums = []
    instr = input('please input the order of newfiles: (1 - n):\n')
    p = re.compile(r'\D+')
    for numstr in p.split(instr):
        if numstr:
            nums.append(int(numstr) - 1)
    return nums

if __name__ == "__main__":
    extension = ['.mp3', '.wma', '.ogg', '.mpc', '.wav', '.wmv', '.mpg', '.avi']
    prefix = r'http://dl.getdropbox.com/u/2128104/blogplays/'
    fninm3u = []
    fnindir = []
    newfiles = []
    orders = []
    finalfiles = []

    # fill fnindir and fninm3u
    fnindir = [fn for fn in os.listdir('.') if ((fn != 'playlist.wma') \
        and (os.path.splitext(fn)[1] in extension))]
    try:
        file = open('playlist.wma', 'r')
        for line in file:
            fname = os.path.split(line.strip())[1]
            if fname in fnindir:
                fninm3u.append(fname)
        file.close()
    except IOError:
        pass

    # now we got fnindir and fninm3u
    newfiles = [fname for fname in fnindir if fname not in fninm3u]
    # print the new filenames and their label:
    if newfiles:
        labelnameout(newfiles)
        # get order of them
        orders = getnameorder()

    # fill finalfiles
    for i in orders:
        finalfiles.append(newfiles[i])
    for fname in fninm3u:
        finalfiles.append(fname)

    # rename and write to file
    file = open('playlist.wma', 'w')
    for fname in finalfiles:
        newname = newfname(fname)
        os.rename(fname, newname)
        file.write(prefix + newname + '\n')
    file.close()

