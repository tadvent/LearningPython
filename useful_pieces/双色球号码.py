#coding=cp936

import random,os

def generate():
    L = random.sample(xrange(1,34),6)
    L.sort()
    print "%-25s + %s" % (L,random.choice(xrange(1,17)))

if __name__ == "__main__":
    s = u'要生成几组数? '
    n = int(raw_input(s.encode("gbk")))
    print
    for i in xrange(0,n):
        generate()
    print
    os.system("pause")
