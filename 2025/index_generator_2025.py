# | ==========================================================================|
'''
LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA
INDEX GENERATOR

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
# %% LOAD PACKAGES AND SETTINGS

#### Packages
import os
import pandas     as pd

#### Settings
PATH = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/2025/'
os.chdir(PATH)
del PATH

# ============================================================================|
# %% INDEX SKELETON

#### Create dataset structure with empty rows
START = 1990
END   = 2020

INDEX = pd.DataFrame({'ISO2'   : [],
                      'ISO3'   : [],  
                      'YEAR'   : [],
                      'COUNTRY': [],
                      'REGION' : [],
                      'LDC'    : [],      # Least developed country
                      'LLDC'   : [],      # Land locked developing country
                      'SIDS'   : []})     # Small island developing state


t = START
while t <= END:
    df_new = pd.DataFrame(
        [['NA', 'AIA', t, 'Anguila'                       , 'Caribbean'      , 0, 0, 1],
         ['NA', 'ATG', t, 'Antigua and Barbuda'           , 'Caribbean'      , 0, 0, 1],
         ['AR', 'ARG', t, 'Argentina'                     , 'South America'  , 0, 0, 0],
         ['NA', 'SBW', t, 'Aruba'                         , 'Caribbean'      , 0, 0, 1],
         ['BS', 'BHS', t, 'Bahamas'                       , 'Caribbean'      , 0, 0, 1],
         ['BB', 'BRB', t, 'Barbados'                      , 'Caribbean'      , 0, 0, 1],
         ['BZ', 'BLZ', t, 'Belize'                        , 'Central America', 0, 0, 1],
         ['BO', 'BOL', t, 'Bolivia'                       , 'South America'  , 0, 1, 0],
         ['NA', 'BES', t, 'Bonaire'                       , 'Caribbean'      , 0, 0, 0],
         ['NA', 'BVT', t, 'Bouvet Island'                 , 'South America'  , 0, 0, 0],
         ['BR', 'BRA', t, 'Brazil'                        , 'South America'  , 0, 0, 0],
         ['NA', 'VGB', t, 'British Virgin Islands'        , 'Caribbean'      , 0, 0, 1],
         ['NA', 'CYM', t, 'Cayman Islands'                , 'Caribbean'      , 0, 0, 0],
         ['CL', 'CHL', t, 'Chile'                         , 'South America'  , 0, 0, 0],
         ['CO', 'COL', t, 'Colombia'                      , 'South America'  , 0, 0, 0],
         ['CR', 'CRI', t, 'Costa Rica'                    , 'Central America', 0, 0, 0],
         ['NA', 'CUB', t, 'Cuba'                          , 'Caribbean'      , 0, 0, 1],
         ['NA', 'CUW', t, 'Curaçao'                       , 'Caribbean'      , 0, 0, 1],
         ['DM', 'DMA', t, 'Dominica'                      , 'Caribbean'      , 0, 0, 1],
         ['DO', 'DOM', t, 'Dominican Republic'            , 'Caribbean'      , 0, 0, 1],
         ['EC', 'ECU', t, 'Ecuador'                       , 'South America'  , 0, 0, 0],
         ['SV', 'SLV', t, 'El Salvador'                   , 'Central America', 0, 0, 0],
         ['NA', 'FLK', t, 'Falkland Islands'              , 'South America'  , 0, 0, 0],
         ['NA', 'GUF', t, 'French Guiana'                 , 'South America'  , 0, 0, 0],
         ['NA', 'GRD', t, 'Grenada'                       , 'Caribbean'      , 0, 0, 1],
         ['NA', 'GLP', t, 'Guadeloupe'                    , 'Caribbean'      , 0, 0, 0],
         ['GT', 'GTM', t, 'Guatemala'                     , 'Central America', 0, 0, 0],
         ['GY', 'GUY', t, 'Guyana'                        , 'South America'  , 0, 0, 1],
         ['HT', 'HTI', t, 'Haiti'                         , 'Haiti'          , 1, 0, 1],
         ['HN', 'HND', t, 'Honduras'                      , 'Central America', 0, 0, 0],
         ['JM', 'JAM', t, 'Jamaica'                       , 'Caribbean'      , 0, 0, 1],
         ['NA', 'MTQ', t, 'Martinique'                    , 'Caribbean'      , 0, 0, 0],
         ['MX', 'MEX', t, 'Mexico'                        , 'Central America', 0, 0, 0],
         ['NA', 'MSR', t, 'Montserrat'                    , 'Caribbean'      , 0, 0, 1],
         ['NI', 'NIC', t, 'Nicaragua'                     , 'Central America', 0, 0, 0],
         ['PA', 'PAN', t, 'Panama'                        , 'Central America', 0, 0, 0],
         ['PY', 'PRY', t, 'Paraguay'                      , 'South America'  , 0, 1, 0],
         ['PE', 'PER', t, 'Peru'                          , 'South America'  , 0, 0, 0],
         ['NA', 'PRI', t, 'Puerto Rico'                   , 'Caribbean'      , 0, 0, 1],
         ['NA', 'BLM', t, 'Saint Barthélemy'              , 'Caribbean'      , 0, 0, 0],
         ['NA', 'KNA', t, 'Saint Kitts and Nevis'         , 'Caribbean'      , 0, 0, 1],
         ['LC', 'LCA', t, 'Saint Lucia'                   , 'Caribbean'      , 0, 0, 1],
         ['NA', 'MAF', t, 'St. Martin (French Part)'      , 'Caribbean'      , 0, 0, 0],
         ['VC', 'VCT', t, 'St. Vincent and the Grenadines', 'Caribbean'      , 0, 0, 1],
         ['NA', 'SXM', t, 'Sint Marteen (Dutch Part)'     , 'Caribbean'      , 0, 0, 1],
         ['NA', 'SGS', t, 'South Georgia and the South Sandwich Islands', 'South America', 0, 0, 0],
         ['SR', 'SUR', t, 'Suriname'                      , 'South America'  , 0, 0, 1],
         ['TT', 'TTO', t, 'Trinidad y Tobago'             , 'Caribbean'      , 0, 0, 1],
         ['NA', 'TCA', t, 'Turks and Caicos Island'       , 'Caribbean'      , 0, 0, 0],
         ['NA', 'VIR', t, 'United States Virgin Islands'  , 'Caribbean'      , 0, 0, 1],
         ['UY', 'URY', t, 'Uruguay'                       , 'South America'  , 0, 0, 0],
         ['VE', 'VEN', t, 'Venezuela'                     , 'South America'  , 0, 0, 0]],
         columns=['ISO2', 'ISO3', 'YEAR', 'COUNTRY', 'REGION', 'LDC', 'LLDC', 'SIDS'],)
    
    INDEX = pd.concat([INDEX, df_new])
    t = t+1

#### Clean up
del START, END, t, df_new

# ============================================================================|
# %% DATA | V-PARTY INDEX

#### Data
FILE = "V-Party-2.dta."
VPARTY = pd.read_stata(FILE)
del FILE

# Rename columns for future merge (when building the index)
VPARTY = VPARTY.rename(columns={'country_text_id':'ISO3' })
VPARTY = VPARTY.rename(columns={'year'           :'YEAR'})

# Drop unnecesary columns and rows
KEEP = ['ISO3'      ,
        'YEAR'      ,
        'v2paid'    ,
        'v2paenname',
        'v2pashname',
        'v2xpa_popul']

VPARTY = VPARTY[KEEP]
VPARTY = VPARTY[VPARTY['YEAR'] >= 1990]

# Drop non-Latam countries and Suriname (no data)
KEEP = 'AIA|ATG|ARG|ABW|BHS|BRB|BLZ|BOL|BES|BVT|BRA|VGB|CYM|\
CHL|COL|CRI|CUB|CUW|DMA|DOM|ECU|SLV|FLK|GUF|GRD|GLP|\
GTM|GUY|HTI|HND|JAM|MTQ|MEX|MSR|NIC|PAN|PRY|PER|PRI|\
BLM|KNA|LCA|MAF|VCT|SXM|SGS|SUR|TTO|TCA|VIR|URY|VEN'

VPARTY = VPARTY[VPARTY['ISO3'].str.contains(KEEP)]

del KEEP

#### Interpolate missing observations
VPARTY = VPARTY.sort_values(by=['ISO3', 'v2paenname', 'YEAR'])
VPARTY = VPARTY.pivot(index='YEAR', values='v2xpa_popul', columns=['ISO3', 'v2paid', 'v2paenname','v2pashname'])
VPARTY = VPARTY.interpolate()
VPARTY = VPARTY.sort_index(axis=1)

#### Export to excel for *manual* completion
FILE = 'Data/VParty.xlsx'

with pd.ExcelWriter(FILE,
                    engine='openpyxl',
                    mode='a',
                    if_sheet_exists='replace') as writer:
    VPARTY.to_excel(writer, sheet_name="V-Party")

del writer, FILE


# ============================================================================|
# %% DATA | V-PARTY MERGE

#### Data
FILE = 'Data/VParty.xlsx'

### After manual update, re-import data from Excel
FILE   = pd.ExcelFile(FILE)
VPARTY = pd.read_excel(FILE, sheet_name='INDEX', usecols="A,B,E,F,G")

#### Merge
INDEX = pd.merge(INDEX, VPARTY, on=['ISO3','YEAR'])
del VPARTY, FILE


# ============================================================================|
# %% DATA | V-DEM

#### Data
# Be patient with data import (can take a few minutes)
# Then rename columns used for merging

FILE = "Data/V-Dem-13.dta"
VDEM = pd.read_stata(FILE)
VDEM = VDEM.rename(columns={'country_text_id':'ISO3' })
VDEM = VDEM.rename(columns={'year'           :'YEAR'})

#### Select institutional variables
code1 = "v2x_rule"         # Rule of Law
code2 = "v2x_jucon"        # Judiciary Constraints on the Executive
code3 = "v2xlg_legcon"     # Legislative Constraints on the Executive
code4 = "v2x_execorr"      # Corruption
code5 = "v2x_neopat"       # Neopatrimonialism
code6 = "v2mecenefm_osp"   # Freedom of Expression

#### Merge
VDEM_1 = VDEM.loc[:, ['ISO3','YEAR',code1,code2,code3,code4,code5,code6]]

VDEM_1[code1] = 100 - VDEM_1[code1]*100
VDEM_1[code2] = 100 - VDEM_1[code2]*100
VDEM_1[code3] = 100 - VDEM_1[code3]*100
VDEM_1[code4] = VDEM_1[code4]*100
VDEM_1[code5] = VDEM_1[code5]*100
VDEM_1[code6] = 100 - VDEM_1[code6]*25

INDEX = pd.merge(INDEX, VDEM_1, on=['ISO3','YEAR'])

INDEX = INDEX.rename(columns={code1:'VDEM_1'})
INDEX = INDEX.rename(columns={code2:'VDEM_2'})
INDEX = INDEX.rename(columns={code3:'VDEM_3'})
INDEX = INDEX.rename(columns={code4:'VDEM_4'})
INDEX = INDEX.rename(columns={code5:'VDEM_5'})
INDEX = INDEX.rename(columns={code6:'VDEM_6'})

#### Clean up
del VDEM, VDEM_1, code1, code2, code3, code4, code5, code6, FILE


# ============================================================================|
# %% DATA | WGI

#### Data
FILE = "Data/wgidataset.dta"
WGI = pd.read_stata(FILE)
WGI = WGI.rename(columns={'year':'YEAR'})
WGI = WGI.rename(columns={'code':'ISO3' })
WGI = WGI.rename(columns={'rle':'WGI_1' ,   # Rule of Law
                          'cce':'WGI_2'})   # Control of Corruption

#### Drop unnecessary columns
KEEP = ['ISO3', 'YEAR', 'WGI_1', 'WGI_2']
WGI = WGI[KEEP]

#### Rescale data
WGI['WGI_1'] = 100 - (WGI['WGI_1'] + 2.5)*20
WGI['WGI_2'] = 100 - (WGI['WGI_2'] + 2.5)*20

#### Drop non-Latam countries
KEEP = 'AIA|ATG|ARG|ABW|BHS|BRB|BLZ|BOL|BES|BVT|BRA|VGB|CYM|\
CHL|COL|CRI|CUB|CUW|DMA|DOM|ECU|SLV|FLK|GUF|GRD|GLP|\
GTM|GUY|HTI|HND|JAM|MTQ|MEX|MSR|NIC|PAN|PRY|PER|PRI|\
BLM|KNA|LCA|MAF|VCT|SXM|SGS|SUR|TTO|TCA|VIR|URY|VEN'

WGI = WGI[WGI['ISO3'].str.contains(KEEP)]

INDEX = pd.merge(INDEX, WGI, on=['ISO3','YEAR'])


#### Clean up
del FILE, KEEP, WGI


# ============================================================================|
# %% DATA | HERITAGE

#### Data
FILE  = "Data/heritage.xlsx"
FILE  = pd.ExcelFile(FILE)

HERITAGE = pd.read_excel(FILE)

#### Drop unnecessary columns
KEEP = ['ISO Code'         ,
        'Index Year'       ,
        'Property Rights'  ,    
        'Business Freedom' ,    
        'Monetary Freedom' ,    
        'Trade Freedom'    ,    
        'Financial Freedom',]


HERITAGE = HERITAGE[KEEP].rename(columns={'ISO Code'         :'ISO2',
                                          'Index Year'       :'YEAR',
                                          'Property Rights'  :'HERITAGE_1',
                                          'Business Freedom' :'HERITAGE_2',
                                          'Monetary Freedom' :'HERITAGE_3',
                                          'Trade Freedom'    :'HERITAGE_4',
                                          'Financial Freedom':'HERITAGE_5'})


INDEX = pd.merge(INDEX, HERITAGE, on=['ISO2', 'YEAR'])

INDEX['HERITAGE_1'] = 100 - INDEX['HERITAGE_1']
INDEX['HERITAGE_2'] = 100 - INDEX['HERITAGE_2']
INDEX['HERITAGE_3'] = 100 - INDEX['HERITAGE_3']
INDEX['HERITAGE_4'] = 100 - INDEX['HERITAGE_4']
INDEX['HERITAGE_5'] = 100 - INDEX['HERITAGE_5']

#### Clean up
del FILE, KEEP, HERITAGE


# ============================================================================|
# %% DATA | FRASER

#### Data
FILE  = "Data/efw.xlsx"
FILE  = pd.ExcelFile(FILE)
SHEET = "EFW Ratings 1970-2021"
COLS  = "B, D, K, T, AO, BH, BU, BZ"

EFW = pd.read_excel(FILE, sheet_name=SHEET, skiprows=4, usecols=COLS)
 
EFW = EFW.rename(columns={'ISO Code 3'                         :'ISO3' ,
                          'Year'                               :'YEAR' ,
                          '1B  Transfers and subsidies'        :'EFW_1',
                          'IE State ownership'                 :'EFW_2',
                          '3D  Foreign currency bank accounts' :'EFW_3',
                          '4  Freedom to trade internationally':'EFW_4',
                          '5B  Labor market regulations'       :'EFW_5',
                          '5C  Business regulations'           :'EFW_6'})


INDEX = pd.merge(INDEX, EFW, on=['ISO3', 'YEAR'])

INDEX['EFW_1'] = 100 - INDEX['EFW_1']*10    # Transfers and subsidies
INDEX['EFW_2'] = 100 - INDEX['EFW_2']*10    # State ownership
INDEX['EFW_3'] = 100 - INDEX['EFW_3']*10    # Foreign currency bank accounts
INDEX['EFW_4'] = 100 - INDEX['EFW_4']*10    # Freedom to Trade Internationally
INDEX['EFW_5'] = 100 - INDEX['EFW_5']*10    # Labor market regulations
INDEX['EFW_6'] = 100 - INDEX['EFW_6']*10    # Business regulations


#### Clean up
del FILE, SHEET, COLS, EFW


# # ============================================================================|
# %% INDEX | INSTITUTIONAL POPULISM

#### Define sub-indices
IP11 = INDEX['VDEM_1']     # Rule of Law
IP12 = INDEX['VDEM_2']     # Judiciary Constraints on the Executive
IP13 = INDEX['VDEM_3']     # Legislative Constraints on the Executive
IP14 = INDEX['WGI_1']      # Rule of Law

IP21 = INDEX['VDEM_4']     # Corruption
IP22 = INDEX['WGI_2']      # Control of Corruption


INDEX['IP_1'] = (IP11 + IP12 + IP13 + IP14)/4         # IP1: Rule of Law
INDEX['IP_2'] = (IP21 + IP22)/2                       # IP2: Corruption
INDEX = INDEX.rename(columns={'VDEM_3'    : 'IP_3'})  # IP3: Neopatrimonialism
INDEX = INDEX.rename(columns={'VDEM_4'    : 'IP_4'})  # IP4: Freedom of the Press
INDEX = INDEX.rename(columns={'VDEM_5'    : 'IP_5'})  # IP5: Neopatrimonialism
INDEX = INDEX.rename(columns={'HERITAGE_1': 'IP_6'})  # IP6: Property Rights

#### Build index
IP1 = INDEX['IP_1']     # Rule of Law
IP2 = INDEX['IP_2']     # Corruption
IP3 = INDEX['IP_3']     # Neopatrimonialism
IP4 = INDEX['IP_4']     # Freedom of the Press
IP5 = INDEX['IP_5']     # Clean Election Index
IP6 = INDEX['IP_6']     # Property Rights
INDEX['IP'] = INDEX['VPARTY'] * (IP1 + IP2 + IP3 + IP4 + IP5 + IP6)/6


INDEX['IP_RANK']       = INDEX.groupby('YEAR')['IP'].rank(ascending=False)
INDEX['IP_PERCENTILE'] = INDEX.groupby('YEAR')['IP'].rank(pct=True)

#### Clean up
del IP11, IP12, IP13, IP14, IP21, IP22, IP1, IP2, IP3, IP4, IP5, IP6


# ============================================================================|
# %% INDEX | ECONOMIC POPULISM

#### Define sub-indices
# Business and labor regulations
EP1 = (INDEX['HERITAGE_2'] + INDEX['EFW_5'] + INDEX['EFW_6'])/3
# Government interventions
EP2 = (INDEX['EFW_1']      + INDEX['EFW_2'])/2
# Money and financial regulations
EP3 = (INDEX['HERITAGE_3'] + INDEX['HERITAGE_5'] + INDEX['EFW_3'])/3
# International trade
EP4 = (INDEX['HERITAGE_4'] + INDEX['EFW_4'])/2

#### Build index
INDEX['EP_1'] = EP1
INDEX['EP_2'] = EP2
INDEX['EP_3'] = EP3
INDEX['EP_4'] = EP4
INDEX['EP']   = INDEX['VPARTY'] * (EP1 + EP2 + EP3 + EP4)/4

INDEX['EP_RANK']       = INDEX.groupby('YEAR')['EP'].rank(ascending=False)
INDEX['EP_PERCENTILE'] = INDEX.groupby('YEAR')['EP'].rank(pct=True)

#### Clean up
del EP1, EP2, EP3, EP4


# ============================================================================|
# %% INDEX | POPULISM OVERAL INDEX

INDEX['POPULISM'] = (INDEX['IP'] + INDEX['EP'])/2

INDEX['POPULISM_RANK']       = INDEX.groupby('YEAR')['POPULISM'].rank(ascending=False)
INDEX['POPULISM_PERCENTILE'] = INDEX.groupby('YEAR')['POPULISM'].rank(pct=True)

# ============================================================================|
# %% CLEAN UP DATASET

KEEP = ['ISO2'               ,
        'ISO3'               ,
        'COUNTRY'            ,
        'REGION'             ,
        'LDC'                ,
        'LLDC'               ,
        'SIDS'               ,
        'YEAR'               ,
        'POPULISM'           ,
        'POPULISM_RANK'      ,
        'POPULISM_PERCENTILE',
        'IP'                 ,
        'IP_RANK'            ,
        'IP_PERCENTILE'      ,
        'IP_1','IP_2','IP_3' ,'IP_4','IP_5','IP_6',
        'EP'                 ,
        'EP_RANK'            ,
        'EP_PERCENTILE'      ,
        'EP_1','EP_2','EP_3' ,'EP_4',
        'VPARTY'             ,
        'PARTY_CODE'         ,
        'PARTY_NAME']

INDEX = INDEX[KEEP]

# Drop Latin American countries with empty observations
INDEX = INDEX[INDEX['ISO3'] != "SUR"]

del KEEP


# ============================================================================|
# %% EXPORT DATA

#### Replace character not accepted by STATA
replacements = {'\u2013':'-',
                '\u2019':'-'}

INDEX['PARTY_CODE'] = INDEX['PARTY_CODE'].replace(replacements, regex=True)
INDEX['PARTY_NAME'] = INDEX['PARTY_NAME'].replace(replacements, regex=True)

#### Export
file_name   = 'index_2025'
extension_1 = '.csv'
extension_2 = '.xlsx'
extension_3 = '.html' 
extension_4 = '.dta'

INDEX.to_csv(file_name + extension_1  , encoding='utf-8')
INDEX.to_excel(file_name + extension_2, index=False)
INDEX.to_html(file_name + extension_3)
INDEX.to_stata(file_name + extension_4)

#### Clean up
del file_name, extension_1, extension_2, extension_3, extension_4
del replacements


# ============================================================================|
# %% THE END

"""
#### Sample Code: Rearrange pandas' columns
import pandas as pd

# Sample DataFrame
data = {'A': [1, 2, 3],
        'B': [4, 5, 6],
        'C': [7, 8, 9]}

df = pd.DataFrame(data)

# Current column order
print("Original DataFrame:")
print(df)

# Specify the desired column order
desired_order = ['B', 'C', 'A']

# Rearrange columns based on the desired order
df = df[desired_order]

# Updated column order
print("\nDataFrame with Rearranged Columns:")
print(df)

#### Sample Code: Ranking
# Rank data within each year group in ascending order with the
# 'min' tie-breaking method
df['Rank'] = df.groupby('Year')['Value'].rank(ascending=True, method='min')
"""
# ===========================================================================
# End-of-File