#!/usr/bin/env python

import re
from sys import argv,exit,stdin,stdout,stderr

if len(argv) < 3:
    stderr.write("USAGE: change_grade.py <string> <number>\n")
    exit(1)

target_string = argv[1]
replace_num = argv[2]

for line in stdin:
    fields = line.rstrip().split(',')
    for i in range(0,len(fields)):
        found = re.search(target_string, fields[i])
        if found:
            fields[3] = replace_num
                
    stdout.write(",".join(fields) + "\n")
exit(0)

