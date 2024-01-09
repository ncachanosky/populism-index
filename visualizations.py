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
import numpy             as np
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
region    = INDEX['REGION'].unique()
years     = INDEX['YEAR'].unique()

#### Cleam up
del path, file, style


# ============================================================================|
# %% TIME-SERIES: ALL COUNTRIES

#### Build plots
for country in countries:
    country_data = INDEX[INDEX['COUNTRY'] == country]
    EP = country_data['EP']
    IP = country_data['IP']
    P  = country_data['POPULISM']
    T  = country_data['YEAR']
    #----------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=figsize)
    plt.title(country, size = title_font_size)
    plt.plot(T, P , label='Populism Index')
    plt.plot(T, EP, label='Economic Populism Sub-Index'     , c='tab:blue')
    plt.plot(T, IP, label='Institutional Populism Sub-Index', c='tab:red' )
    plt.xlim(2002, 2020)
    plt.legend(labelcolor='linecolor')
    plt.tight_layout()
    plt.savefig('visualizations/TS_'+country)
    plt.show()

#### Clean up
del country_data, ax, fig, EP, IP, P

# ============================================================================|
# %% TIME-SERIES: LATAM AND SUB-REGIONS

#### Create average series and labels
POP = INDEX.groupby('YEAR')['POPULISM'].mean().reset_index()
EP  = INDEX.groupby('YEAR')['EP'].mean().reset_index()
IP  = INDEX.groupby('YEAR')['IP'].mean().reset_index()

T  = POP['YEAR']
y1 = POP['POPULISM']
y2 = EP['EP']
y3 = IP['IP']

labels = ['Populism index',
          'Economic Populism Sub-Index'    ,
          'Institutional Populism Sub-Index']

#### Average: Latin-America
fig, ax = plt.subplots(figsize=figsize)
plt.title("Populism indices, Latin America averages")
plt.plot(T, y1, label=labels[0], c='black')
plt.plot(T, y2, label=labels[1], c='tab:blue')
plt.plot(T, y3, label=labels[2], c='tab:red')
plt.xlim(2002, 2020)
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/TS_Latam_Average')
plt.show()

#### Average: Regional (Populism)
P = INDEX.pivot_table(index='YEAR',columns='REGION', values='POPULISM', aggfunc='mean')
P['T'] = np.arange(2002, 2020, 1)

T  = P['T']
P1 = P['Caribbean']
P2 = P['Central America']
P3 = P['South America']

fig, ax = plt.subplots(figsize=figsize)
plt.title("Populism, Latin America regional averages")
plt.plot(T, P1, label='Caribbean'      , c='tab:green' )
plt.plot(T, P2, label='Central America', c='tab:purple')
plt.plot(T, P3, label='South America'  , c='tab:olive' )
plt.xlim(2002, 2020)
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/TS_Regional_Populism')
plt.show()

#### Average: Regional (Economic Populism)
EP = INDEX.pivot_table(index='YEAR',columns='REGION', values='EP', aggfunc='mean')
EP['T'] = np.arange(2002, 2020, 1)

T   = EP['T']
EP1 = EP['Caribbean']
EP2 = EP['Central America']
EP3 = EP['South America']

fig, ax = plt.subplots(figsize=figsize)
plt.title("Economic Populism, Latin America regional averages")
plt.plot(T, P1, label='Caribbean'      , c='tab:green' )
plt.plot(T, P2, label='Central America', c='tab:purple')
plt.plot(T, P3, label='South America'  , c='tab:olive' )
plt.xlim(2002, 2020)
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/TS_Regional_EP')
plt.show()


#### Average: Regional (Institutional Populism)
IP = INDEX.pivot_table(index='YEAR',columns='REGION', values='IP', aggfunc='mean')
IP['T'] = np.arange(2002, 2020, 1)

T   = IP['T']
IP1 = IP['Caribbean']
IP2 = IP['Central America']
IP3 = IP['South America']

fig, ax = plt.subplots(figsize=figsize)
plt.title("Institutional Populism, Latin America regional averages")
plt.plot(T, P1, label='Caraibbean'     , c='tab:green' )
plt.plot(T, P2, label='Central America', c='tab:purple')
plt.plot(T, P3, label='South America'  , c='tab:olive' )
plt.xlim(2002, 2020)
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/TS_Regional_IP')
plt.show()


#### Clean up
del POP, EP,EP1, EP2, EP3, IP, IP1, IP2, IP3, T, y1, y2, y3, fig, ax, labels
del P, P1, P2, P3


# ============================================================================|
# %% BARS: TOP & BOTTOM PER YEAR

#### Build plots
axis_range = [0, 100, 0, 100]
#i= years[0]
for year in years:
    i = year.astype(str)
    year_data = INDEX[INDEX['YEAR'] == year]
    EP = year_data['EP']
    IP = year_data['IP']
    #----------------------------------------------------------------------
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



import pandas as pd
import matplotlib.pyplot as plt

# Sample DataFrame (replace this with your actual DataFrame)
data = {
    'County': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] * 5,
    'Year': [2010, 2010, 2010, 2010, 2010, 2010, 2010, 2010, 2010, 2010,
             2011, 2011, 2011, 2011, 2011, 2011, 2011, 2011, 2011, 2011],
    'Rank': [i+1 for i in range(10)] * 2,
    'Value': [100-i for i in range(10)] * 2
}

df = pd.DataFrame(data)

# Filter bottom and top 10 per year
bottom_top_df = pd.concat([
    df[df['Rank'] <= 10].groupby('Year').apply(lambda x: x.nsmallest(10, 'Rank')),
    df[df['Rank'] <= 10].groupby('Year').apply(lambda x: x.nlargest(10, 'Rank'))
])

# Pivot for bar chart
pivot_df = bottom_top_df.pivot(index='Year', columns='County', values='Value')

# Plotting
ax = pivot_df.plot(kind='bar', stacked=True, figsize=(12, 6))
ax.set_ylabel('Value')
ax.set_xlabel('Year')
ax.set_title('Bottom and Top 10 Counties Per Year')

plt.show()
