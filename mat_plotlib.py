# importing matplotlib module
import matplotlib.pyplot as plt
# x-axis values
day = [1, 2, 3, 4, 5,6,7]
# Y-axis values
temp = [45,49,43,42,47,48,43]

# Function to plot graph
# plt.plot(day, temp,color='red',linestyle='dotted', marker='o', markerfacecolor="blue" )

#fuction to plot scatter graph
plt.scatter(day, temp,color='red' )
# plt.title("Weather Temperature graph")
plt.ylabel("Temperature")
plt.xlabel("Days")
 # plt.bar(x,y)
# function to show the plot
plt.show()
