import matplotlib.pyplot as plt
from random_walks import RandomWalk

#Keep making random walks as long as the program is active
while True:
    #make a random walk
    rw = RandomWalk()
    rw.fill_walks()

    #plotting the points in the walk
    plt.style.use('classic')

    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another random walk? (y/n):")
    if keep_running == 'n':
        break