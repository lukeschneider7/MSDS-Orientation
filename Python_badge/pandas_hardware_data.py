### 6. load the data from the class hardware survey into memory using pandas
# manipulate that data into a binnable form, and make exploratory histograms
# the features you couldn't address with a histogram provide a qualitative description.
import pandas as pd

# Read the Hardware Data
filepath = "hardware.xlsx"
hardware_data = pd.read_excel(filepath)

#print middle of data
print(hardware_data[20:30])