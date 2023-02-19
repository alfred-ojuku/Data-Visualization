from random import choice

class RandomWalk:
    """A class that generates random walks"""

    def __init__(self, num_points=5000):
        """Initializes attributes of the walk"""
        self.num_points = num_points

        # All walks start at (0,0)
        self.x_values = [0]
        self.y_values = [0]

    # determining direction
    def get_step(self):
        """Determines the direction and distance of each step"""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4, ])
        step = direction * distance
        return step

    def fill_walk(self):
        """calculates all the points in the walk"""
        while len(self.x_values) < self.num_points:
            x_step = self.get_step()
            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # calculate the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)