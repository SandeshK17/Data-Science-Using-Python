import matplotlib.pyplot as plt
#data to display on plots
x = [1,2,3,4]
e = (0.1,0,0,0)
# This will plot a simple pie chart
plt.pie(x , explode=e)

# Title to the plot
plt.title("Pie Chart")
plt.show()
