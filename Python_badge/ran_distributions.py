### 4.use a random number generator to make histograms of popular probability distributions.
###  use the numpy and matplotlib packages. choose THREE from the list below and store your resulting code in your github repo.
import numpy as np
import matplotlib.pyplot as plot
print("yes")

#Binomial distribution
random_bin_nums = np.random.binomial(n=200, p=.5, size=200) 
plot.hist(random_bin_nums, bins=40, color='r')
plot.xlabel('Value')
plot.ylabel('Frequency')
plot.title("Binomial Distribution n=200, p=.5")
plot.show()

#Poisson distribution
random_poisson_nums = np.random.poisson(lam=5, size=200)
plot.hist(random_poisson_nums, bins=40, color='g')
plot.title("Possion Distribution lambda=5")
plot.xlabel('Value')
plot.ylabel('Frequency')
plot.show()

#Normal distribution
random_norm_nums = np.random.normal(loc=0, scale=1, size=200)
plot.hist(random_norm_nums, bins=40, color='b')
plot.xlabel('Value')
plot.ylabel('Frequency')
plot.title("Normal Distribution mean=0, std.dev=1")
plot.show()


