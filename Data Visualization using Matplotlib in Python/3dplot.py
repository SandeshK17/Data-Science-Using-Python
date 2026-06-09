import matplotlib.pyplot as plt

fig = plt.figure()
x = [1,2,3,4,5]
y = [1,4,9,16,25]
z = [1,8,27,64,125]

ax = plt.axes(projection = '3d')
ax.plot3D(x,y,z)
plt.show()
