# | ==========================================================================|
'''
LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA
VISUALIZATIONS

Nicolas Cachanosky
Center for Free Enterprise
The University of Texas at El Paso
ncachanosky@utep.edu
www.ncachanosky.com

Version: 1.0
Last update: 08-Jan-2023
'''

# ============================================================================|
# %% LOAD PACKAGES, SETTINGS, AND DATA


#### Packages
import os
import pandas            as pd
import matplotlib.pyplot as plt

#### Settings
path = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/'
os.chdir(path)

#### Load data
file  = "index_2023.xlsx"
file  = pd.ExcelFile(file)

INDEX = pd.read_excel(file)
countries = INDEX['COUNTRY'].unique()

#### Cleam up
del path, file


# ============================================================================|
# %% TIME-SERIES PER COUNTRY


for country in countries:
    country_data = INDEX[INDEX['COUNTRY'] == country]
    EP = country_data['EP']
    IP = country_data['IP']
    P  = country_data['POPULISM']
    T  = country_data['YEAR']
    #------------------------------------------------
    plt.title(country)
    plt.plot(T, EP, label='Economic Populism Sub-Index')
    plt.plot(T, IP, label='Institutional Populism Sub-Index')
    plt.plot(T, P , label='Populism Index')
    plt.legend()
    plt.show()




#### Clean up

# Convert 'Date' column to datetime type
df['Date'] = pd.to_datetime(df['Date'])

# Plot time series line plot for each country
countries = df['Country'].unique()

for country in countries:
    country_data = df[df['Country'] == country]
    plt.plot(country_data['Date'], country_data['Value'], label=country)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Time Series Line Plot for Each Country')
plt.legend()
plt.show()
