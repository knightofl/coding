import numpy as np
import matplotlib.pyplot as plt
import random

plt.rc('font', family='NanumGothicCoding')


w = [0,0]               # Weights (Synapses)
threshold = 0           # Theshold
bias = 1                # Bias
learning_rate = 1       # Learning rate - [0, 1]
max_iterations = 100    # Maximum number allowed of iterations

data = [                # Inputs and Labels
    [0.72,0.82,-1],
    [0.91,-0.69,-1],
    [0.03,0.93,-1],
    [0.12,0.25,-1],
    [0.96,0.47,-1],
    [0.8,-0.75,-1],
    [0.46,0.98,-1],
    [0.66,0.24,-1],
    [0.72,-0.15,-1],
    [0.35,0.01,-1],
    [-0.11,0.1,1],
    [0.31,-0.96,1],
    [0.0,-0.26,1],
    [-0.43,-0.65,1],
    [0.57,-0.97,1],
    [-0.72,-0.64,1],
    [-0.25,-0.43,1],
    [-0.12,-0.9,1],
    [-0.58,0.62,1],
    [-0.77,-0.76,1]
]

y = 0                   # Output
color = ''              # Color - Red or Blue, 1 and -1, respectively
answer = ''             # Answer = Correct or Error


def get_points_of_color(data, label):
    x_coords = [float(point[0]) for point in data if point[2] == label]
    y_coords = [float(point[1]) for point in data if point[2] == label]
    return x_coords, y_coords


plt.ion()               # Turn on the interactive graphics mode

for i in range(1, max_iterations):
    hits = 0
    print(f"\n------------------------- ITERATION {i} ------------------------- ")

    for j in range(0, len(data)):
        sum = 0         # Weighted sum
        
        for k in range(0, len(data[j])-1):
            sum += data[j][k] * w[k]

        # Output = Bias + Weighted sum
        output = bias + sum

        # Output is determined by the Threshold
        if output > threshold:
            y = 1
        else:
            y = -1

        # Update the Weights if the output does not match with the Desired output
        if y == data[j][2]:
            hits += 1
            answer = 'Correct!'
        else:
            for k in range(0, len(w)):
                w[k] += (learning_rate * data[j][2] * data[j][k])
            bias += learning_rate * data[j][2]
            answer = 'Not Correct! to ' + str(w)

        if y == 1:
            print('\n', answer)
        elif y == -1:
            print('\n', answer)

        # Plot the graph
        plt.clf() # Clear figure
        plt.title('Iteration %d\n' % i)
        plt.grid(False) # Plot a grid
        plt.xlim(-1, 1) # Set x-axis limits
        plt.ylim(-1, 1) # Set y-axis limits

        xA = 1
        xB = -1

        if w[1] != 0:
            yA = (- w[0] * xA - bias) / w[1]
            yB = (- w[0] * xB - bias) / w[1]
        else:
            xA = - bias / w[0]
            xB = - bias / w[0]

            yA = 1
            yB = -1

        # Plot the black line, that is, we want to learn the black line as faithfully as possible
        #("Best" Decision Boundary)
        plt.plot([0.77, -0.55], [-1, 1], color='k', linestyle='-', linewidth=1)

        # Generates our green line, that is, our learning line (Decision Boundary)
        plt.plot([xA, xB], [yA, yB], color='g', linestyle='-', linewidth=2)

        # Plot blue points
        x_coords, y_coords = get_points_of_color(data, -1)
        plt.plot(x_coords, y_coords, 'bo')

        # Plot red points
        x_coords, y_coords = get_points_of_color(data, 1)
        plt.plot(x_coords, y_coords, 'ro')

        # Highlights the current point
        if answer == 'Correct!':
            # Correct - with green color
            plt.plot(data[j][0], data[j][1], 'go', markersize=15, alpha=.5)
        else:
            # Incorrect - with magenta color
            plt.plot(data[j][0], data[j][1], 'mo', markersize=30, alpha=.5)

        # Show the plot
        plt.show()

        # We were able to control the loop time, so a figure will be updated and displayed
        plt.pause(0.05)

    if hits == len(data):
        print("\n---------------------------------------------------------------")
        print(f"\nFunctionality learned with {i} iterations!")
        break
    '''else:
        print("\n---------------------------------------------------------------")
        print("\nFunctionality not learned!")
        break'''

print("\nDone!\n")