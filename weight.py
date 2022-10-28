#!/usr/bin/env python3
unit = input("Are you entering lb or kg?")
weight = int(input("Weight: "))
lb_formula = weight / 2.2
kg_formula = weight * 2.2
if unit == "lb" or unit == "l":
    print("your weight is: " + str(lb_formula) + " in Kg's")
else:
    print("your weight is: " + str(kg_formula) + " in Lb's")
