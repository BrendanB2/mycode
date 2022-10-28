#!/usr/bin/env python3
'''Dracula docstring'''

i=0
while True:

    with open("dracula.txt","r") as vamp:
        vamplist = vamp.readlines()
    for x in vamplist:
        print([x], end= "")
        if "vampire" in line:
            print(line)
    i +=1
