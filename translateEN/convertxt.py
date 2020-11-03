# -*- coding: UTF-8 -*-
#翻译时有换行，google翻译不连续
#resolve google translate txt turn row issue

import sys
#use ru style
def filterStr():
    f = open("a.txt","rU")
    lines = f.readlines()
    a = ''
    i = 0
    for line in lines:
        a += line.strip()
        i += 1
    print(a)
    print("\n")
    print(i)
    f.close()
    return

filterStr()
