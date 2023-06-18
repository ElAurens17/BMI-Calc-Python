def sheesh():
    # Answer in Kg
    B = float(input("Input your weight: "))
    # Answer in Meters
    A = float(input("Input your height: "))
    # hehe boi
    C = B / (A**2)

    print("Your BMI Index is: " + str(C))

    if C <= 18.5:
        print("get a doctor, bruh")
    elif C >= 25:
        print("get a doctor, nigga!!!!")
    else:
        print("u good nigga")


sheesh()


""" 
BMI INDEX
    <18.5 = Underweight                
    18.5 - 24.9 = Normal
    25 - 29.9 = Overweight
"""

"""
HEIGHT TABLE
    5' 0"	1.52
    5' 1"	1.55
    5' 2"	1.57
    5' 3"	1.60
    5' 4"	1.63
    5' 5"	1.65
    5' 7"	1.70
    5' 8"	1.73
    5' 9"	1.75
    5' 10"	1.78
"""
