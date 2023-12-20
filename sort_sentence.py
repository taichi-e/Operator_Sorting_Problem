#!/usr/bin/env python3
#
#
# Copyright (c) 2023, Taichi Emi.
# All rights reserved.
#
# $Id: $
#

import collections
import fileinput
import os
import os.path
import re
import subprocess
import sys

def main():
    lst=[]
    while 1:
        try:
            line = list(input().split())
            line[0] = int(line[0])
            lst.append(line)
        except EOFError:
            break
    lst.sort(reverse=False, key=lambda x:x[0])
    for i in range(len(lst)):
        lst[i][0] = str(lst[i][0])
        print(f'{" ".join(lst[i])}')

            




if __name__ == "__main__":
    main()