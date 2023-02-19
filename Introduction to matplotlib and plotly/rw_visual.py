import matplotlib.pyplot as plt
from random_walks import RandomWalk

#Keep making random walks as long as the program is active
while True:
    #make a random walk
    rw = RandomWalk(50000)
    rw.fill_walks()

    #plotting the points in the walk
    plt.style.use('classic')

    fig, ax = plt.subplots(figsize=(10,6))
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=1)

    #Emphasizing the first as last points
    ax.scatter(0, 0, c='green', edgecolor='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolor='none', s=100)

    #remove the axis
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running = input("Make another random walk? (y/n):")
    if keep_running == 'n':
        break