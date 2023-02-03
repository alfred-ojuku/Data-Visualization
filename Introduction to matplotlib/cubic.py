import matplotlib.pyplot as plt

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Purples, s=5)

#set chart title and axis labels
ax.set_title('Cubic Numbers', fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cubic of Value", fontsize=14)

#set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()