def directions():
    directions=["Move Forward", "Move Backward", "Turn Left", "Turn Right"]
    return directions
def menu():
    print("Please select a direction:")
    dir_menu=directions()
    for index in range(len(dir_menu)):
        print("{}: {}.".format(index,dir_menu[index]))
def run():
    menu()
run()