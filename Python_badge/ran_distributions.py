### 4.use a random number generator to make histograms of popular probability distributions.
###  use the numpy and matplotlib packages. choose THREE from the list below and store your resulting code in your github repo.
import numpy as np
import matplotlib.pyplot as plot
print("yes")

#Binomial distribution
random_bin_nums = np.random.binomial(n=200, p=.5, size=200) 
plot.hist(random_bin_nums, bins=40, density=True, color='r')
plot.show()

#Poisson distribution
random_poisson_nums = np.random.poisson(5, 100)

#Normal distribution
random_norm_nums = np.random.normal(loc=0, scale=1, size=200)
plot.hist(random_norm_nums, bins=40, density=True, color='b')
plot.show()