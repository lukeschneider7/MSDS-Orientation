### 6. load the data from the class hardware survey into memory using pandas
# manipulate that data into a binnable form, and make exploratory histograms
# the features you couldn't address with a histogram provide a qualitative description.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

# Read the Hardware Data
file_path = 'Python_badge/hardware.xlsx'
data = pd.read_excel(file_path, engine='openpyxl')

# Remove outlier at top of data
clean_data = data.iloc[1:]
hardware_data = clean_data[(clean_data['Hard Drive Size (in GB)']<1000) & (clean_data['CPU Cycle Rate (in GHz)'] < 4) & (clean_data['RAM (in GB)'] < 33)]

#print head of data
pd.set_option('display.max_columns', None)
print(hardware_data.head())

# Cut into quantiles (5 bins)
hardware_data['HD_quantile_bin'] = pd.qcut(hardware_data['Hard Drive Size (in GB)'], q=5, labels=['Q1 HD', 'Q2 HD', 'Q3 HD', 'Q4 HD', 'Q5 HD'])
hardware_data['CPU_rate_quantile_bin'] = pd.qcut(hardware_data['CPU Cycle Rate (in GHz)'], q=5, labels=['Q1 clock', 'Q2 clock', 'Q3 clock', 'Q4 clock', 'Q5 clock'])

# Display the quantile binned DataFrame
print(hardware_data)

# Operating Systems not shown as histograph as they were all either mac or windows
# Github User name and uva id were features included for assignment purposes
# GPU Descriptions did not have many repeats so histogram did not seem like it would be interesting

# Plot different numerical features as histographs
plot.subplot(4, 3, 1)
plot.hist(hardware_data['Hard Drive Size (in GB)'], bins=40, color = "g")
plot.title('Hard Drive Size in GB with outliers')
plot.xlabel('GB')
plot.ylabel('count')

plot.subplot(4, 3, 3)
plot.hist(hardware_data['CPU Cycle Rate (in GHz)'], bins=40, color = "r")
plot.title('CPU Cycle Rate (in GHz)')
plot.xlabel('GHz')
plot.ylabel('count')

plot.subplot(4, 3, 7)
plot.hist(hardware_data['CPU Number of Cores (int)'], bins=40, color = "b")
plot.title('CPU Number of Cores (int)')
plot.xlabel('# Cores')
plot.ylabel('count')

plot.subplot(4, 3, 9)
plot.hist(hardware_data['RAM (in GB)'], bins=40, color = "y")
plot.title('RAM (in GB)')
plot.xlabel('RAM GB')
plot.ylabel('count')
plot.savefig('hardware_plots.png')
plot.show()
