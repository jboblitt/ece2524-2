#!/usr/bin/env python

import re

def change_grade(student_string, target_string, replace_num):
    fields = student_string.rstrip().split(',')
    for i in range(0, len(fields)):
        found = re.search(target_string, fields[i])
        if found:
            fields[3] = replace_num
    return ",".join(fields)

if __name__ == '__main__':
    from sys import argv,exit,stdin,stdout,stderr
    
    if len(argv) < 3:
        stderr.write("USAGE: change_grade.py <string> <number>\n")
        exit(1)

    for line in stdin:
        stdout.write(change_grade(line, argv[1], argv[2]) + "\n")
    exit(0)

