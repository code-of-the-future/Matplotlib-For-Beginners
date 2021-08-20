# Matplotlib Tutorial Series - Continuing Code

# Import relevant modules
import matplotlib.pyplot as plt
import numpy as np

# Creating simple arrays
x = np.array([0, 100])
y = np.array([0, 4])

# Plotting x and y - a simple line
# The first argument is the x-axis and the second argument
# is the y-axis
# plt.plot(x, y)
# You ALWAYS need to write plt.show() in order to see the graph
# plt.show()  # This shows the plot

# Plotting several points in matplotlib
# Each numpy array has to be the same length!!
x = np.array([0, 30, 12, 56, 19, 100])
y = np.array([40, 72, 80, 13, 17, 39])

# Instead of a line graph, we want a scatter graph
# Method One
# plt.plot(x, y, 'o')
# plt.show()

# Method Two
# plt.scatter(x, y)
# plt.show()

# Matplotlib's default x and y axis
a = np.array([0, 10, 20, 30, 100, 30, 50, 108])

# plt.plot(a)
# plt.show()

# MARKERS IN MATPLOTLIB!!
x = np.array([0, 1, 2, 3, 4])
y = np.array([20, 30, 50, 100, 101])

# plt.plot(x, y, marker='s')
# # plt.plot(x, y)
# plt.show()

# Change the colour and line reference of graphs!
# There are so many different colours and linestyles! Just
# google them to have a play around!
x = np.array([0, 1, 2, 3, 4])
y = np.array([20, 30, 50, 100, 101])

# Markersize - markersize=10 (simplified to ms)
# Marker colour - markerfacecolor="blue" (simplified to mfc)
# Marker edge colour - markeredgecolor="blue" (simplified to mec)
# plt.plot(x, y, c='black', marker='*', linestyle='--',
#          markersize=10, markerfacecolor='blue',
#          markeredgecolor='blue', linewidth=2)
#
# plt.show()

# Line colour - colour='red (simplified to c)
# Line style - linestyle='--' (variety of these!)
# Line width - linewidth=2 (simplified to lw)

# Plotting more than one graph on a plot - 3 plots!
# x = np.array([0, 10, 100])
# y = np.array([0, 1, 2])
# plt.plot(x, y)
#
# r = np.array([0, 50, 10])
# s = np.array([0, 46, 92])
# plt.plot(r, s)
#
# a = np.array([0, 80, 100])
# b = np.array([0, 40, 92])
# plt.plot(a, b)
# plt.show()

# Legends, Labels and Fonts!!

# # These are the measurements from Class 1
# a = np.array([5, 8, 10])
# b = np.array([160, 180, 200])
# # Plot Class 1
# plt.scatter(a, b, label='Class 1')
#
# # These are the measurements from Class 2
# a = np.array([3, 5, 8])
# b = np.array([150, 155, 170])
# # Plot Class 2
# plt.scatter(a, b, label='Class 2')
#
# # Changing the fonts (colour, font, size, etc)
# font1 = {'family': 'serif', 'size': 23, 'color': 'red'}
#
# # Plotting an X and Y label, legend and title!
# plt.title('Shoe Size vs Height for 2 Classes', fontdict=font1)
# plt.xlabel('Shoe Size (UK Size Guide)', fontdict=font1)
# plt.ylabel('Heights (cm)', fontdict=font1)
# # Plot legend
# plt.legend()
# # This has to be done last!
# plt.show()

# Plotting grids in matplotlib!
# a = np.array([5, 8, 10])
# b = np.array([160, 180, 200])
# plt.scatter(a, b)
# plt.grid(axis='x', color='red', linewidth=0.5, linestyle='--')
# plt.show()

# SCATTER PLOTS!!!
# We've already seen how to plot multiple scatter plots on
# the same graph!

# These are the measurements from Class 1
# a = np.array([5, 8, 10])
# b = np.array([160, 180, 200])
#
# # We can assign each scatter point to be a specific colour
# favourite_colours = ['green', 'red', 'blue']
#
# # Plot Class 1
# plt.scatter(a, b, label='Class 1', color=favourite_colours)
#
# # These are the measurements from Class 2
# a = np.array([3, 5, 8])
# b = np.array([150, 155, 170])
# # Plot Class 2
# plt.scatter(a, b, label='Class 2')
#
# # Plotting an X and Y label, legend and title!
# plt.title('Shoe Size vs Height for 2 Classes')
# plt.xlabel('Shoe Size (UK Size Guide)')
# plt.ylabel('Heights (cm)')
# # Plot legend
# plt.legend()
# # This has to be done last!
# plt.show()

# # Colour bar!
# shoe_size = np.array([5, 6, 7])
# heights = np.array([160, 170, 190])
# siblings = np.array([1, 3, 8])
#
# plt.scatter(shoe_size, heights, c=siblings, cmap='rainbow')
# plt.colorbar()
# plt.show()

# # BAR CHARTS IN MATPLOTLIB!!!
# # Let's say we have a toy factory and it sells 4 different
# # types of toys
# toys = ['Teddy', 'Yo-Yo', 'Jack in the Box', 'Electronic Toy']
# in_stock = [200, 150, 100, 300]
# colours = ['red', 'blue', 'green', 'orange']
#
# # Plot a bar chart of this data!
# plt.bar(toys, in_stock, color=colours)
#
# # Plotting labels and title
# plt.title('Number of toys in stock')
# plt.xlabel('Toys')
# plt.ylabel('Number Available')
#
# # We always need this to show the graph
# plt.show()

# PIE CHARTS IN MATPLOTLIB!!!
# We have a vehicle company that sells cars, bicycles, tractors
# and motorbikes
vehicles = ['Cars', 'Bicycles', 'Tractors', 'Motorbikes']
in_stock = [30, 40, 10, 37]
colours = ['red', 'orange', 'green', 'blue']
section_out = [0.1, 0.1, 0.1, 0.1]
plt.pie(in_stock, labels=vehicles, startangle=90, colors=colours,
        shadow=True, explode=section_out)
plt.legend(loc='upper left', bbox_to_anchor=(1.05, 1.15),
           title='Vehicles')
plt.show()



