### 5. Show with histograms that Binomial and Normal Distributions converge in the large N limit
import matplotlib.pyplot as plot
import numpy as np

# Generate binomial and Random Distributions with large N (2000)
N_value = 2000
probability = .5
avg=probability*N_value
std_dev=np.sqrt(N_value * probability*(1-probability))
binomial_dist = np.random.binomial(n=N_value, p=probability, size=2000) 
random_dist = np.random.normal(loc=avg, scale=std_dev, size=2000) 

# Plot the Binomial and Normal Distributions with large N
plot.subplot(1,2,1)
plot.hist(binomial_dist, bins=30, color = "b")
plot.title(f'Binomial Distribution (N={N_value}, p={probability})')
plot.xlabel("value")
plot.ylabel("probability")

plot.subplot(1, 2, 2)
plot.hist(binomial_dist, bins=30, color = "g")
plot.title(f'Normal Distribution (mean={avg}, std={std_dev})')
plot.xlabel("value")
plot.ylabel("probability")
plot.savefig('Converging_histograms.png')
plot.show()


