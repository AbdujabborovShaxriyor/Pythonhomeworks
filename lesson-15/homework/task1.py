import matplotlib.pyplot as plt
import numpy as np
import math
from mpl_toolkits.mplot3d import Axes3D

#task1

x=np.linspace(-10,10,5)
y=x**2-4*x+4
plt.plot(x,y,label=r'$y = x^2 - 4x + 4$',marker='o')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Plot of y = x² - 4x + 4')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#task 2

x = np.linspace(0,math.pi)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x,y1,c='b',ls='--',marker='X')
plt.plot(x,y1,c='g',ls='solid',marker='o')
plt.legend()
plt.show()

#task 3
fig, axes = plt.subplots(2, 2, figsize=(8, 6)) 
x = np.linspace(1,5,5)

axes[0,0].plot(x,x**3,'r')
axes[0,0].set_title('polynomial')
axes[0,0].set_xlabel('x')
axes[0,0].set_ylabel('x cube')

axes[0,1].plot(x,np.sin(x),'b')
axes[0,1].set_title('trigonometric')
axes[0,1].set_xlabel('x')
axes[0,1].set_ylabel('sin(x)')

axes[1,0].plot(x,np.e**x,'g')
axes[1,0].set_title('exponential')
axes[1,0].set_xlabel('x')
axes[1,0].set_ylabel('e to x')

axes[1,1].plot(x,np.log(x+1),'k')
axes[1,1].set_title('logarithmic')
axes[1,1].set_xlabel('x')
axes[1,1].set_ylabel('log(x+1)')

plt.tight_layout()
plt.show()

#task 4

x = np.random.uniform(0,10,100)
y = np.random.uniform(0,10,100)

plt.xlabel("x values")
plt.ylabel("y values")
plt.title('Random 100 points')
colors = np.random.rand(100)
plt.scatter(x, y, c=colors, cmap='viridis', s=100, edgecolors='black',marker='o')
plt.colorbar(label="Color Intensity")
plt.grid()
plt.show()

#task 5

data = np.random.normal(loc=0,scale=1, size=1000)
plt.hist(data, bins=30, alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Histogram of Normally Distributed Data (mean=0, std=1)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#task 6

x = np.linspace(-5,5,10)
y = np.linspace(-5,5,10)
X, Y = np.meshgrid(x, y)
z = np.cos(X**2+Y**2)
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')
figure = ax.plot_surface(X,Y,z,cmap='viridis')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('3D Plot')
fig.colorbar(figure)
plt.show()

#task 7

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [200, 150, 250, 175, 225]
colors = ['r','b','g','k','hotpink']

plt.bar(products,values,color=colors)
plt.title('Store products')
plt.xlabel('Products')
plt.ylabel('Prices')
plt.show()

#task 8

categories = ['Category A', 'Category B', 'Category C']
time_periods = ['T1', 'T2', 'T3', 'T4']
data = np.array([[5, 7, 6, 8],  
                 [3, 4, 5, 6],  
                 [2, 3, 4, 5]]) 
fig, ax = plt.subplots(figsize=(8, 6))
bottom = np.zeros(len(time_periods))

for i, category in enumerate(categories):
    ax.bar(time_periods, data[i], label=category, bottom=bottom)
    bottom += data[i]
ax.set_title('Stacked Bar Chart of Category Contributions')
ax.set_xlabel('Time Periods')
ax.set_ylabel('Contribution')
ax.legend(title="Categories")
plt.show()