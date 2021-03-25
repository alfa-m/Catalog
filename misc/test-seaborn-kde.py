import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns

plt.figure(figsize=( 15,6  ), facecolor='w')

### RugPlots and Gaussians ###

plt.subplot(1,3,1)
plt.title("RugPlots and Gaussians")

# Dataset
tips = sns.load_dataset('tips')
dataset = np.array(tips['total_bill'])

# RugPlot
sns.rugplot(dataset, c = 'red')

# Cofigure X axis
x_min = dataset.min() - 2
x_max = dataset.max() + 2
x_axis = np.linspace(x_min,x_max,100)

# Configure bandwidth. 
# More info: 
# url = http://en.wikipedia.org/wiki/Kernel_density_estimation#Practical_estimation_of_the_bandwidth
bandwidth = ((4*dataset.std()**5)/(3*len(dataset)))**.2

# Kernel List
kernel_list = []

# Draw Gaussian for Each Point
for point in dataset:
    
    # Creates a Kernel for each point, over the X axis
    kernel = stats.norm(point, bandwidth).pdf(x_axis)
    kernel_list.append(kernel)
    
    # Ploting, Scale Ajusting.
    kernel = kernel / kernel.max()
    kernel = kernel * .4
    plt.plot(x_axis, kernel, 'b', lw=1 ,alpha=0.2)
plt.ylim(0,.6)

### Sum of the Basis Functions ###

plt.subplot(1,3,2)
plt.title('Sum of the Basis Functions')

# Sum the kernel of each point
sum_of_kde = np.sum(kernel_list,axis=0)
plt.plot(x_axis, sum_of_kde, color='b')
plt.ylim(0,15)

sns.rugplot(dataset, c = 'r')

### Using Seaborn ###

plt.subplot(1,3,3)
plt.title('Using Seaborn')

sns.kdeplot(tips['total_bill'])
sns.rugplot(tips['total_bill'])

plt.show()
