print("Where should I look?")
location=input()
if (location=="in the bedroom"):
    print("Where in the bedroom should I look?")
    bed_location=input()
    if (bed_location=="under the bed"):
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.") 
elif (location=="in the bathroom"):
    print("Where in the bathroom should I look?")
    bath_location=input()
    if (bath_location=="in the bathtub"):
        print("Found a rubber duck but no battery")
    else:
        print("Found a wet surface but no battery.")
elif (location=="in the lab"):
    print("Where in the lab should I look?")
    lab_location=input()
    if (lab_location=="on the table"):
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I am not sure where that place is located.")
