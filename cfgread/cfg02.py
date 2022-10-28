#!/usr/bin/env python3
## create file object in "r"ead mode
configfile = with open("vlanconfig.cfg", "r")

## display file to the screen - .read()
configblog = configfile.readlines()

## break configblog across line boundaries (strips out \n)
configlist = configblog.splitlines()

## display list with no "\n"
print(configlist)

## Always close your file
configfile.close()

