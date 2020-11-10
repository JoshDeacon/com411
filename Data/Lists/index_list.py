def movements():
    path=["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path
def run():
    print("Moving...")
    movements()
    dir_path=movements()
    print("{} for {} steps".format(dir_path[0],dir_path[1]))
    print("{} for {} steps".format(dir_path[2],dir_path[3]))
    print("{} for {} steps".format(dir_path[4],dir_path[5]))
    print("{} for {} steps".format(dir_path[6],dir_path[7]))
run()

def gang():
    print("Loading gang....")
    friends["Scooby Doo","Shaggy Rogers","Fred Jones","Daphne Blake","Velma Dinkley"]
    return gang
    
def run():
    print(friends)
    print("....Done!")
run()
