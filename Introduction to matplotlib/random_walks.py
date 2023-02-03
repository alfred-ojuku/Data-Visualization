from random import choice

class RandomWalk:
    """A class that generates random walks"""

    def __init__(self, num_points=5000):
        """Initializes attributes of the walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    # choosing directions
    def fill_walks(self):
        """Calculate all the points in the walk"""

        # keep taking steps until the walk reaches the desired length
        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)