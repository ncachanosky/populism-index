# | ==========================================================================|
'''
LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA
VISUALIZATIONS

Nicolas Cachanosky
Center for Free Enterprise
The University of Texas at El Paso
ncachanosky@utep.edu
www.ncachanosky.com

J. P. Bastos
Free Market Institute
Texas Tech University
jpmvbastos@gmail.com
https://www.jpmvbastos.com/

Version: 1.0
Last update: 08-Mar-2025
'''

# ============================================================================|
# %% LOAD PACKAGES, SETTINGS, AND DATA

#### Packages
import os
import numpy             as np
import pandas            as pd
import matplotlib.pyplot as plt

#### General settings
PATH = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/'
os.chdir(PATH)

#### Load data
FILE  = "index_2023.xlsx"
FILE  = pd.ExcelFile(FILE)

INDEX = pd.read_excel(FILE)
INDEX = INDEX[INDEX['YEAR'] != 2000]  # Year 2001 is missing
INDEX = INDEX[INDEX['YEAR'] != 2020]  # Year 2020 is missing

countries = INDEX['COUNTRY'].unique()
region    = INDEX['REGION'].unique()
years     = INDEX['YEAR'].unique()

#### Clean up
del PATH, FILE


# ============================================================================|
# %% PLOT SETTINGS

#### Plot settings
#style = "https://github.com/ncachanosky/populism-index/tree/style_sheet/my-plot_style.mplstyle"
#style = "C:/Users/ncachanosky/OneDrive/Research/populism-index/visualizations/style_sheet/my-plot_style.mplstyle"
#plt.style.use(style)

print(plt.style.available)
plt.style.use('fivethirtyeight')

fig_landscape = (16,9)
fig_square    = (9, 9)
#title_font_size = 26

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
    fig, ax = plt.subplots(figsize=fig_landscape)
    plt.title(country)
    plt.plot(T, P , label='Populism Index'                  , c='black'   )
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
fig, ax = plt.subplots(figsize=fig_landscape)
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

fig, ax = plt.subplots(figsize=fig_landscape)
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

fig, ax = plt.subplots(figsize=fig_landscape)
plt.title("Economic Populism, Latin America regional averages")
plt.plot(T, EP1, label='Caribbean'      , c='tab:green' )
plt.plot(T, EP2, label='Central America', c='tab:purple')
plt.plot(T, EP3, label='South America'  , c='tab:olive' )
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

fig, ax = plt.subplots(figsize=fig_landscape)
plt.title("Institutional Populism, Latin America regional averages")
plt.plot(T, IP1, label='Caribbean'      , c='tab:green' )
plt.plot(T, IP2, label='Central America', c='tab:purple')
plt.plot(T, IP3, label='South America'  , c='tab:olive' )
plt.xlim(2002, 2020)
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/TS_Regional_IP')
plt.show()


#### Clean up
del POP, EP,EP1, EP2, EP3, IP, IP1, IP2, IP3, T, y1, y2, y3, fig, ax, labels
del P, P1, P2, P3


# ============================================================================|
# %% BARS: SCATTER PLOTS

#### By Year
axis_range = [0, 100, 0, 100]
#i= years[0]
for year in years:
    i = year.astype(str)
    year_data = INDEX[INDEX['YEAR'] == year]
    EP = year_data['EP']
    IP = year_data['IP']
    #----------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=fig_square)
    plt.title(year)
    plt.scatter(EP,IP, color = 'tab:orange', s=100)
    plt.plot([0,100],[0,100], color='black', ls=':')
    plt.xlabel('Economic populism')
    plt.ylabel('Institutional populism')
    plt.axis_range = axis_range
    plt.tight_layout()
    plt.savefig('visualizations/scatter_'+i)
    plt.show()


#### Transition
ARG = INDEX[INDEX['ISO3'] == "ARG"]
BOL = INDEX[INDEX['ISO3'] == "BOL"]
ECU = INDEX[INDEX['ISO3'] == "ECU"]
NIC = INDEX[INDEX['ISO3'] == "NIC"]
VEN = INDEX[INDEX['ISO3'] == "VEN"]


axis_range = [0, 100, 0, 100]
LABELS=['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
TITLE = "Populism transition"

fig, ax = plt.subplots(figsize=fig_square)
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.plot(ARG['EP'],ARG['IP'],'o-',markersize=10,color='tab:blue' ,label=LABELS[0])
plt.plot(BOL['EP'],BOL['IP'],'o-',markersize=10,color='tab:green',label=LABELS[1])
plt.plot(ECU['EP'],ECU['IP'],'o-',markersize=10,color='tab:red'  ,label=LABELS[2])
plt.plot(NIC['EP'],NIC['IP'],'o-',markersize=10,color='tab:cyan' ,label=LABELS[3])
plt.plot(VEN['EP'],VEN['IP'],'o-',markersize=10,color='tab:olive',label=LABELS[4])
plt.xlabel("Economic populism")
plt.ylabel("Institutional populism")
plt.axis_range=axis_range
plt.tight_layout()
plt.savefig('visualizations/transition')
plt.show()


#### VPARTY VS EP INDEX
year_data = INDEX[INDEX['YEAR'] == 2015]
EP        = year_data['EP']
IP        = year_data['IP']
VPARTY    = year_data['VPARTY']*100

fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(VPARTY,EP, color = 'tab:orange', s=100)
plt.plot([0,100],[0,100], color='black', ls=':')
plt.xlabel('V-Party')
plt.ylabel('Economic populism')
plt.axis_range = axis_range
plt.tight_layout()
plt.savefig('visualizations/scatter_'+i)
plt.show()


# ============================================================================|
# %% BARS: SCATTER PLOTS
ARG = INDEX[INDEX['YEAR'].between(2007, 2015)]
BOL = INDEX[INDEX['YEAR'].between(2006, 2019)]
ECU = INDEX[INDEX['YEAR'].between(2007, 2017)]
NIC = INDEX[INDEX['YEAR'].between(2007, 2018)]
VEN = INDEX[INDEX['YEAR'].between(1999, 2018)]

ARG = ARG.groupby("ISO3", as_index=False).mean(numeric_only=True)
BOL = BOL.groupby("ISO3", as_index=False).mean(numeric_only=True)
ECU = ECU.groupby("ISO3", as_index=False).mean(numeric_only=True)
NIC = NIC.groupby("ISO3", as_index=False).mean(numeric_only=True)
VEN = VEN.groupby("ISO3", as_index=False).mean(numeric_only=True)


#### ARGENTINA
ARG_A = [ARG['EP'].iloc[ 0], ARG['IP'].iloc[ 0]] 
ARG_B = [ARG['EP'].iloc[ 1], ARG['IP'].iloc[ 1]]
ARG_E = [ARG['EP'].iloc[ 8], ARG['IP'].iloc[ 8]]
ARG_N = [ARG['EP'].iloc[15], ARG['IP'].iloc[15]]
ARG_V = [ARG['EP'].iloc[23], ARG['IP'].iloc[23]]   

LABELS = ['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
axis_range = [0, 100, 0, 100]
fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(ARG['EP'], ARG['IP'], color = 'tab:orange', s=100, alpha=0.5)
plt.scatter(ARG_A[0] , ARG_A[1] , color = 'tab:blue'  , s=200, alpha=1.0, label=LABELS[0])
plt.scatter(ARG_B[0] , ARG_B[1] , color = 'tab:green' , s=100, alpha=0.7, label=LABELS[1])
plt.scatter(ARG_E[0] , ARG_E[1] , color = 'tab:red'   , s=100, alpha=0.7, label=LABELS[2])
plt.scatter(ARG_N[0] , ARG_N[1] , color = 'tab:cyan'  , s=100, alpha=0.7, label=LABELS[3])
plt.scatter(ARG_V[0] , ARG_V[1] , color = 'tab:olive' , s=100, alpha=0.7, label=LABELS[4])
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.xlabel('Economic populism')
plt.ylabel('institutional populism')
plt.axis_range = axis_range
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/Iconic5_Scatter_ARG')
plt.show()


#### BOLIVIA
BOL_A = [BOL['EP'].iloc[ 0], BOL['IP'].iloc[ 0]] 
BOL_B = [BOL['EP'].iloc[ 1], BOL['IP'].iloc[ 1]]
BOL_E = [BOL['EP'].iloc[ 8], BOL['IP'].iloc[ 8]]
BOL_N = [BOL['EP'].iloc[15], BOL['IP'].iloc[15]]
BOL_V = [BOL['EP'].iloc[23], BOL['IP'].iloc[23]]   

LABELS = ['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
axis_range = [0, 100, 0, 100]
fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(BOL['EP'], BOL['IP'], color = 'tab:orange', s=100, alpha=0.5)
plt.scatter(BOL_A[0] , BOL_A[1] , color = 'tab:blue'  , s=100, alpha=0.7, label=LABELS[0])
plt.scatter(BOL_B[0] , BOL_B[1] , color = 'tab:green' , s=200, alpha=1.0, label=LABELS[1])
plt.scatter(BOL_E[0] , BOL_E[1] , color = 'tab:red'   , s=100, alpha=0.7, label=LABELS[2])
plt.scatter(BOL_N[0] , BOL_N[1] , color = 'tab:cyan'  , s=100, alpha=0.7, label=LABELS[3])
plt.scatter(BOL_V[0] , BOL_V[1] , color = 'tab:olive' , s=100, alpha=0.7, label=LABELS[4])
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.xlabel('Economic populism')
plt.ylabel('institutional populism')
plt.axis_range = axis_range
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/Iconic5_Scatter_BOL')
plt.show()


#### ECUADOR
ECU_A = [ECU['EP'].iloc[ 0], ECU['IP'].iloc[ 0]] 
ECU_B = [ECU['EP'].iloc[ 1], ECU['IP'].iloc[ 1]]
ECU_E = [ECU['EP'].iloc[ 8], ECU['IP'].iloc[ 8]]
ECU_N = [ECU['EP'].iloc[15], ECU['IP'].iloc[15]]
ECU_V = [ECU['EP'].iloc[23], ECU['IP'].iloc[23]]   

LABELS = ['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
axis_range = [0, 100, 0, 100]
fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(ECU['EP'], ECU['IP'], color = 'tab:orange', s=100, alpha=0.5)
plt.scatter(ECU_A[0] , ECU_A[1] , color = 'tab:blue'  , s=100, alpha=0.7, label=LABELS[0])
plt.scatter(ECU_B[0] , ECU_B[1] , color = 'tab:green' , s=100, alpha=0.7, label=LABELS[1])
plt.scatter(ECU_E[0] , ECU_E[1] , color = 'tab:red'   , s=200, alpha=1.0, label=LABELS[2])
plt.scatter(ECU_N[0] , ECU_N[1] , color = 'tab:cyan'  , s=100, alpha=0.7, label=LABELS[3])
plt.scatter(ECU_V[0] , ECU_V[1] , color = 'tab:olive' , s=100, alpha=0.7, label=LABELS[4])
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.xlabel('Economic populism')
plt.ylabel('institutional populism')
plt.axis_range = axis_range
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/Iconic5_Scatter_ECU')
plt.show()


#### NICARAGUA
NIC_A = [NIC['EP'].iloc[ 0], NIC['IP'].iloc[ 0]] 
NIC_B = [NIC['EP'].iloc[ 1], NIC['IP'].iloc[ 1]]
NIC_E = [NIC['EP'].iloc[ 8], NIC['IP'].iloc[ 8]]
NIC_N = [NIC['EP'].iloc[15], NIC['IP'].iloc[15]]
NIC_V = [NIC['EP'].iloc[23], NIC['IP'].iloc[23]]   

LABELS = ['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
axis_range = [0, 100, 0, 100]
fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(NIC['EP'], NIC['IP'], color = 'tab:orange', s=100, alpha=0.5)
plt.scatter(NIC_A[0] , NIC_A[1] , color = 'tab:blue'  , s=100, alpha=0.7, label=LABELS[0])
plt.scatter(NIC_B[0] , NIC_B[1] , color = 'tab:green' , s=100, alpha=0.7, label=LABELS[1])
plt.scatter(NIC_E[0] , NIC_E[1] , color = 'tab:red'   , s=100, alpha=0.7, label=LABELS[2])
plt.scatter(NIC_N[0] , NIC_N[1] , color = 'tab:cyan'  , s=200, alpha=1.0, label=LABELS[3])
plt.scatter(NIC_V[0] , NIC_V[1] , color = 'tab:olive' , s=100, alpha=0.7, label=LABELS[4])
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.xlabel('Economic populism')
plt.ylabel('institutional populism')
plt.axis_range = axis_range
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/Iconic5_Scatter_NIC')
plt.show()


#### VENEZUELA
VEN_A = [VEN['EP'].iloc[ 0], VEN['IP'].iloc[ 0]] 
VEN_B = [VEN['EP'].iloc[ 1], VEN['IP'].iloc[ 1]]
VEN_E = [VEN['EP'].iloc[ 8], VEN['IP'].iloc[ 8]]
VEN_N = [VEN['EP'].iloc[15], VEN['IP'].iloc[15]]
VEN_V = [VEN['EP'].iloc[23], VEN['IP'].iloc[23]]   

LABELS = ['Argentina', 'Bolivia', 'Ecuador', 'Nicaragua', 'Venezuela']
axis_range = [0, 100, 0, 100]
fig, ax = plt.subplots(figsize=fig_square)
plt.scatter(VEN['EP'], VEN['IP'], color = 'tab:orange', s=100, alpha=0.5)
plt.scatter(VEN_A[0] , VEN_A[1] , color = 'tab:blue'  , s=100, alpha=0.7, label=LABELS[0])
plt.scatter(VEN_B[0] , VEN_B[1] , color = 'tab:green' , s=100, alpha=0.7, label=LABELS[1])
plt.scatter(VEN_E[0] , VEN_E[1] , color = 'tab:red'   , s=100, alpha=0.7, label=LABELS[2])
plt.scatter(VEN_N[0] , VEN_N[1] , color = 'tab:cyan'  , s=100, alpha=0.7, label=LABELS[3])
plt.scatter(VEN_V[0] , VEN_V[1] , color = 'tab:olive' , s=200, alpha=1.0, label=LABELS[4])
plt.plot([0,100],[0,100], color='gray', ls=':')
plt.xlabel('Economic populism')
plt.ylabel('institutional populism')
plt.axis_range = axis_range
plt.legend(labelcolor='linecolor')
plt.tight_layout()
plt.savefig('visualizations/IcoVEN5_Scatter_VEN')
plt.show()

#### Clean up
del year_data, ax, fig, EP, IP, ARG, BOL, ECU, NIC, VEN, LABELS, i
del ARG_A, ARG_B, ARG_E, ARG_N, ARG_V
del BOL_A, BOL_B, BOL_E, BOL_N, BOL_V
del ECU_A, ECU_B, ECU_E, ECU_N, ECU_V
del NIC_A, NIC_B, NIC_E, NIC_N, NIC_V
del VEN_A, VEN_B, VEN_E, VEN_N, VEN_V
del axis_range, TITLE, fig_landscape, fig_square
