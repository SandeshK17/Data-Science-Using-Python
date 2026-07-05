import matplotlib.pyplot as plt

# initialize data
x = [1,2,3,4,5,6]
y = [56,78,54,66,56,70]

# Plotting the data
plt.bar(x,y)

# Adding Title
plt.title("Performance Report")

# Adding the labels name
plt.xlabel("Semester")
plt.ylabel("Percentage")
plt.show()
