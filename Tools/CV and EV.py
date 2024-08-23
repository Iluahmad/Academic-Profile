# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""



print('Hello World!')
print('it\'s a beautiful world!')
import matplotlib.pyplot as plt
import numpy as np

# Hypothetical values
initial_price = 10
new_price = 15
initial_income = 100

# Utility function: U = sqrt(x)
# Initial consumption: x0 = initial_income / initial_price
initial_consumption = initial_income / initial_price
initial_utility = np.sqrt(initial_consumption)

# New consumption: x1 = initial_income / new_price
new_consumption = initial_income / new_price
new_utility = np.sqrt(new_consumption)

# Compensation Variation (CV)
# Amount needed to achieve initial utility with new prices
CV_income = (initial_utility ** 2) * new_price

# Equivalent Variation (EV)
# Amount the consumer would pay to avoid the price change
EV_income = (initial_utility ** 2) * initial_price - initial_income

# Plotting the graph
fig, ax = plt.subplots()

# Original budget line
x = np.linspace(0, initial_income / initial_price, 100)
y = initial_income - initial_price * x
ax.plot(x, y, label='Initial Budget Line', color='blue')

# New budget line
y_new = initial_income - new_price * x
ax.plot(x, y_new, label='New Budget Line', color='red')

# Utility curves (indifference curves)
x_util = np.linspace(0, initial_consumption, 100)
y_util_initial = (initial_utility ** 2) / x_util
y_util_new = (new_utility ** 2) / x_util
ax.plot(x_util, y_util_initial, '--', label='Initial Utility', color='blue')
ax.plot(x_util, y_util_new, '--', label='New Utility', color='red')

# Marking initial and new consumption points
ax.plot(initial_consumption, 0, 'bo', label='Initial Consumption')
ax.plot(new_consumption, 0, 'ro', label='New Consumption')

# Adding CV and EV lines
ax.plot([0, initial_utility ** 2 / new_price], [CV_income, 0], 'g--', label='Compensation Variation')
ax.plot([0, initial_utility ** 2 / initial_price], [initial_income + EV_income, 0], 'm--', label='Equivalent Variation')

# Labels and legend
ax.set_xlabel('Quantity of Good')
ax.set_ylabel('Income')
ax.legend()
ax.grid(True)
ax.set_title('Compensation Variation and Equivalent Variation')

plt.show()
