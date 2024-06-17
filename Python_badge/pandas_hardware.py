### 6. load the data from the class hardware survey into memory using pandas
# manipulate that data into a binnable form, and make exploratory histograms
# the features you couldn't address with a histogram provide a qualitative description.
import pandas as pd
import numpy as np

# Read the Hardware Data
file_path = 'Python_badge/hardware.xlsx'
hardware_data = pd.read_excel(file_path, engine='openpyxl')

#print head of data
pd.set_option('display.max_columns', None)
print(hardware_data.head())

# Cut into quantiles (5 bins)
hardware_data['HD_quantile_bin'] = pd.qcut(hardware_data['Hard Drive Size (in GB)'], q=5, labels=['Q1 HD', 'Q2 HD', 'Q3 HD', 'Q4 HD', 'Q5 HD'])
hardware_data['CPU_rate_quantile_bin'] = pd.qcut(hardware_data['CPU Cycle Rate (in GHz)'], q=5, labels=['Q1 clock', 'Q2 clock', 'Q3 clock', 'Q4 clock', 'Q5 clock'])

# Display the quantile binned DataFrame
print(hardware_data)

