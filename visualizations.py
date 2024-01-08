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

#### General settings
path = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/'
os.chdir(path)

#### Plot settings
style = "https://github.com/ncachanosky/populism-index/tree/style_sheet/my-plot_style.mplstyle"
style = "C:/Users/ncachanosky/OneDrive/Research/populism-index/visualizations/style_sheet/my-plot_style.mplstyle"
plt.style.use(style)

figsize = (16,9)
title_font_size = 26

#### Load data
file  = "index_2023.xlsx"
file  = pd.ExcelFile(file)

INDEX = pd.read_excel(file)
INDEX = INDEX[INDEX['YEAR'] != 2000]  # Year 2001 is missing
INDEX = INDEX[INDEX['YEAR'] != 2020]  # Year 2020 is missing

countries = INDEX['COUNTRY'].unique()
years     = INDEX['YEAR'].unique()

#### Cleam up
del path, file, style


# ============================================================================|
# %% TIME-SERIES: ALL COUNTRIES

#### Build plots
axis_range = [2002, 2019]
for country in countries:
    country_data = INDEX[INDEX['COUNTRY'] == country]
    EP = country_data['EP']
    IP = country_data['IP']
    P  = country_data['POPULISM']
    T  = country_data['YEAR']
    #------------------------------------------------
    fig, ax = plt.subplots(figsize=figsize)
    plt.title(country, size = title_font_size)
    plt.plot(T, P , label='Populism Index')
    plt.plot(T, EP, label='Economic Populism Sub-Index'     , c='tab:blue')
    plt.plot(T, IP, label='Institutional Populism Sub-Index', c='tab:red' )
    plt.xlim(2002, 2020)
    plt.axis_range = axis_range
    plt.legend(labelcolor='linecolor')
    plt.tight_layout()
    #plt.savefig('visualizations/TS_'+country)
    plt.show()

#### Clean up
del country_data, ax, fig, EP, IP, P

# ============================================================================|
# %% TIME-SERIES: LATAM


# ============================================================================|
# %% SCATTER PLOT PER YEAR

#### Build plots
axis_range = [0, 100, 0, 100]
#i= years[0]
for year in years:
    i = year.astype(str)
    year_data = INDEX[INDEX['YEAR'] == year]
    EP = year_data['EP']
    IP = year_data['IP']
    #------------------------------------------------
    fig, ax = plt.subplots(figsize=figsize)
    plt.title(year, size=title_font_size)
    plt.scatter(EP,IP, color = 'tab:orange', s=100)
    plt.plot([0,100],[0,100], color='black', ls=':')
    plt.xlabel('Economic populism')
    plt.ylabel('Institutional populism')
    plt.axis_range = axis_range
    plt.tight_layout()
    plt.savefig('visualizations/scatter_'+i)
    plt.show()
    
#### Clean up
del year_data, ax, fig, EP, IP

