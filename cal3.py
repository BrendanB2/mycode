#!/usr/bin/env python3
"""TLG Cohort | BBoswell
Celsius / Fahrenheit Conversion Calculator"""

from datetime import datetime
sttime = datetime.now().strftime('%Y%m%d_%H:%M:%S - ')

def main():
    print(f"\nBrendan's Celsius & Fahrenheit Conversion Calculator")
    invalid = (f"\n ****************** That is not a valid entry ****\
************** \n")

    while True:
        print(f"|||||||||||||||||||||||||||||||||||||||||||||||||||||\
||||||||||||||||")
        cORf = input(f"\nEnter 'c' for celsius, 'f' for fahrenheit, 'k'\
for kelvin, 'i' for input,'v' view temp, or 'q' for quit\n ---> : ")

        if cORf.lower() == "q".lower():
            break

# Converting from Celsius to Fahrenheit and Kelvin:
        elif cORf.lower() == "c".lower():
            try:
                celtemp = float(input("Numerical value of celsius\
 temperature?\n ---> : "))
                xceltemp = (celtemp * 9)/5 + 32
                kceltemp = celtemp + 273.15
                print("\n\nConverting ",("%.2f" % celtemp),"°C is ",
                     ("%.2f" % xceltemp), "°F and ",("%.2f" % kceltemp),
                     "°K.\n\n", sep="")
            except ValueError:
                print(f"{invalid}")
                continue

# Converting from Fahrenheit to Celsius and Kelvin:
        elif cORf.lower() == "f".lower():
            try:
                feltemp = float(input("Numerical value of fahrenheit\
 temperature?\n ---> : "))
                xfeltemp = (feltemp - 32) * 5/9
                kfeltemp = xfeltemp + 273.15
                print("\n\nConverting ",("%.2f" % feltemp),"°F is ",
                     ("%.2f" % xfeltemp), "°F and ",("%.2f" % kfeltemp),
                     "°K.\n\n", sep="")
            except ValueError:
                print(f"{invalid}")
                continue

# Converting from Kelvin to Celsius and Fahrenheit:
        elif cORf.lower() == "k".lower():
            try:
                keltemp = float(input("Numerical value of kelvin\
 temperature?\n ---> : "))
                ckeltemp = (keltemp-273.15)
                fkeltemp = (keltemp-273.15)*(5/9)+32
                print("\n\nConverting ",("%.2f" % keltemp),"°K is ",
                     ("%.2f" % ckeltemp), "°C and ",("%.2f" % fkeltemp),
                     "°K.\n\n", sep="")
            except ValueError:
                print(f"{invalid}")
                continue

# Inputing daily temp:
        elif cORf.lower() == "i".lower():
            try:
                hdailytemp = float(input("Numerical value of daily high\
 temp?\n ---> : "))
                ldailytemp = float(input("Numerical value of daily low\
 temp?\n ---> : "))
                cfdailytemp = input("Daily temp °C or °F (c/f)?\n --->\
 : ")
"calc.py" 126L, 4995C                                                            1,1           Top
[ttyd] 0:bash*                                              "student@bchd: ~/mycod" 18:19 27-Oct-22
