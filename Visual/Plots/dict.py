import matplotlib.pyplot as plt
import random as random

def data():
    paths = {}
    print("What type of line (:, -- or -)?")
    line_style = input()
    
    print("What colour would you like (r, g or b)?")
    colour = input()

    print("What type of marker (o, s or ^)?")
    marker_style = input()

    paths['line_style'] = line_style
    paths['colour'] = colour
    paths['marker_style'] = marker_style

    return paths

def generate():
    print("How many lines would you like to display?")
    num_lines = int(input())

    for num_line in range(num_lines):
        values = data()
        x = [0, random.randrange(1, 10, 2)]
        y = [0, random.randrange(1, 10, 2)]

        
        plt.plot(x, y, f"{values['colour']}{values['line_style']}{values['marker_style']}")
    
    plt.show()

def run():
    print("Running....")
    generate()
    print("Done!")
run()