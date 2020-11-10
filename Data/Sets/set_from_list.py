def observed():
    observations = []

    for count in range(7):
        print("Enter an observation")
        item=input()
        observations.append(item)
    return observations

def run():
    print("Counting observations...")
    observations=observed()
    observation_set=set()

    for observation in observations:
        occurrences = observations.count(observation)
        observations_set.add((observation,occurrences))

    for key in observations_set:
        print(f"{key} observed {occurrences} times")
run()