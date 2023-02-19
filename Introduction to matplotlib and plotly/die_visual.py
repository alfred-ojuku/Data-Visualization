from plotly.graph_objs import Bar, Layout
from plotly import offline
from die import Die

#creating a D6
die = Die()

#make some rolls and store the results in list
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
# The next step is to visualize these results

#visualization of the results
x_values = list(range(1, die.num_sides + 1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result'}
y_axis_config = {'title': 'Frequency of result'}
my_layout = Layout(title='Results of rolling D6 die 1000 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')