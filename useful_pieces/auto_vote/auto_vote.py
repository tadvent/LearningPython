import os
import sys
import re
import socket
import urllib.request
import shelve

limit = 0

def proxy_vote(ip_port):
    global limit
    proxy = {'http': 'http://%s' % ip_port}
    opener = urllib.request.FancyURLopener(proxy)
    f = opener.open(r'http://www.wwwzqr.cn/public/ajax.aspx?action=addvote&id=73')
    s = f.read().decode('utf-8')
    if s.strip() == '1':
        limit -= 1
        print('ok. limit left: %d' % limit)
        if limit <= 0:
            return False
    else:
        print(s)
    return True

def try_vote(proxy_list):
    socket.setdefaulttimeout(10);

    db = shelve.open('auto_vote_db')
    proxy_used = set([])
    try:
        proxy_used = db['proxy_used']
    except:
        print(r"Can't open proxy_used set...")

    for proxy_str in proxy_list:
        proxy_str = proxy_str.strip()
        print('%-22s' % proxy_str, end='')

        if proxy_str in proxy_used:
            print('used before...')
            continue

        proxy_used.add(proxy_str)
        try:
            if not proxy_vote(proxy_str):
                break
        except:
            print('Error occured...')

    db['proxy_used'] = proxy_used
    db.close()

def parse_file(file):
    with open(file, 'r') as f:
        ip_pat = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?:[:]|(?:\s+))(\d+)')
        tmp_list = ip_pat.findall(f.read())
        proxy_list = []
        for p in tmp_list:
            proxy_list.append(p[0] + ':' + p[1])
        try_vote(proxy_list)

if __name__ == "__main__":
    if(len(sys.argv) < 3):
        print('not enough parameters')
        print('Usage: python %s NUM file1 file2 ...' % sys.argv[0])
    else:
        limit = int(sys.argv[1])
        for i in range(2, len(sys.argv)):
            parse_file(sys.argv[i])
        # parse_file(sys.argv[1])
