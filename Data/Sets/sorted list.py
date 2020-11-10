def observed():
    observations = []
    for objects in range(5):
        observation = input("Please enter an observation: ")
        observations.append(observation)
    return observations

def remove_observations(removal):
    remq="yes"
    while remq == "yes":
        remq = input("Do you wish to remove an observation? Yes or no ")
        if remq == "yes":
            remo = input("What observation do you wish to remove?")
            removal.remove (remo)
            print("Done! It has been removed")

        elif remq == "no":
            print("Done! Nothing has been removed")
        
        else:
            print("I do not recognise that option")
    
    return removal

def run():
    print("Counting the observations.....")
    observations=observed()
    removingo=remove_observations(observations)
    seen_set=set()
    for observation in observations:
        seen_set.add((observation,observations.count(observation)))
    print(seen_set)

run()