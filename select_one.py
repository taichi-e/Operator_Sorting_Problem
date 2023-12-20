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
    ite = 0
    while 1:
        try:
            line = input()
            line_splited = list(line.split())
            if ite < int(line_splited[0]):
                print(line)
                ite = int(line_splited[0])

        except EOFError:
            break

            




if __name__ == "__main__":
    main()