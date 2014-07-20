#-------------------------------------------------------------------------------
# Name:        file name sorted as Windows Explorer
# Purpose:
#
# Author:      tadvent
#
# Created:     23/10/2013
# Copyright:   (c) tadvent 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import re

def subfilename(filename):
    def padnum(matchObj):
        numstr = matchObj.group(0)
        return ' ' * (10 - len(numstr)) + numstr
    return re.sub(r"(\d+)", padnum, filename)


def main():
    print(subfilename('a1b22c3'))
    print(subfilename('a1b2c3'))

if __name__ == '__main__':
    main()
