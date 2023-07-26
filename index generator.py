# | ==========================================================================|
# | LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA


# ============================================================================|
# %% LOAD PACKAGES AND SETTINGS

# PACKAGES
import os
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt

# | SETTINGS
path = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/'
os.chdir(path)
del path


# ============================================================================|
# %% CREATE COUNTRY LIST: DATASET STRUCTURE

# Create dataset structure with empty rows
INDEX = pd.DataFrame({'ISO'   : [],  
                     'YEAR'   : [],
                     'COUNTRY': [],
                     'REGION' : [],
                     'LDC'    : [],      # Least developed country
                     'LLDC'   : [],      # Land locked developing country
                     'SIDS'   : []})     # Small island developing state
start = 1990
end   = 2020

t = start
while t <= end:
    df_new = pd.DataFrame(
        [['AIA', t, 'Anguila'                       , 'Caribbean'      , 0, 0, 1],
         ['ATG', t, 'Antigua and Barbuda'           , 'Caribbean'      , 0, 0, 1],
         ['ARG', t, 'Argentina'                     , 'South America'  , 0, 0, 0],
         ['SBW', t, 'Aruba'                         , 'Caribbean'      , 0, 0, 1],
         ['BHS', t, 'Bahamas'                       , 'Caribbean'      , 0, 0, 1],
         ['BRB', t, 'Barbados'                      , 'Caribbean'      , 0, 0, 1],
         ['BLZ', t, 'Belize'                        , 'Central America', 0, 0, 1],
         ['BOL', t, 'Bolivia'                       , 'South America'  , 0, 1, 0],
         ['BES', t, 'Bonaire'                       , 'Caribbean'      , 0, 0, 0],
         ['BVT', t, 'Bouvet Island'                 , 'South America'  , 0, 0, 0],
         ['BRA', t, 'Brazil'                        , 'South America'  , 0, 0, 0],
         ['VGB', t, 'British Virgin Islands'        , 'Caribbean'      , 0, 0, 1],
         ['CYM', t, 'Cayman Islands'                , 'Caribbean'      , 0, 0, 0],
         ['CHL', t, 'Chile'                         , 'South America'  , 0, 0, 0],
         ['COL', t, 'Colombia'                      , 'South America'  , 0, 0, 0],
         ['CRI', t, 'Costa Rica'                    , 'Central America', 0, 0, 0],
         ['CUB', t, 'Cuba'                          , 'Caribbean'      , 0, 0, 1],
         ['CUW', t, 'Curaçao'                       , 'Caribbean'      , 0, 0, 1],
         ['DMA', t, 'Dominica'                      , 'Caribbean'      , 0, 0, 1],
         ['DOM', t, 'Dominican Republic'            , 'Caribbean'      , 0, 0, 1],
         ['ECU', t, 'Ecuador'                       , 'South America'  , 0, 0, 0],
         ['SLV', t, 'El Salvador'                   , 'Central America', 0, 0, 0],
         ['FLK', t, 'Falkland Islands'              , 'South America'  , 0, 0, 0],
         ['GUF', t, 'French Guiana'                 , 'South America'  , 0, 0, 0],
         ['GRD', t, 'Grenada'                       , 'Caribbean'      , 0, 0, 1],
         ['GLP', t, 'Guadeloupe'                    , 'Caribbean'      , 0, 0, 0],
         ['GTM', t, 'Guatemala'                     , 'Central America', 0, 0, 0],
         ['GUY', t, 'Guyana'                        , 'South America'  , 0, 0, 1],
         ['HTI', t, 'Haiti'                         , 'Haiti'          , 1, 0, 1],
         ['HND', t, 'Honduras'                      , 'Central America', 0, 0, 0],
         ['JAM', t, 'Jamaica'                       , 'Caribbean'      , 0, 0, 1],
         ['MTQ', t, 'Martinique'                    , 'Caribbean'      , 0, 0, 0],
         ['MEX', t, 'Mexico'                        , 'Central America', 0, 0, 0],
         ['MSR', t, 'Montserrat'                    , 'Caribbean'      , 0, 0, 1],
         ['NIC', t, 'Nicaragua'                     , 'Central America', 0, 0, 0],
         ['PAN', t, 'Panama'                        , 'Central America', 0, 0, 0],
         ['PRY', t, 'Paraguay'                      , 'South America'  , 0, 1, 0],
         ['PER', t, 'Peru'                          , 'South America'  , 0, 0, 0],
         ['PRI', t, 'Puerto Rico'                   , 'Caribbean'      , 0, 0, 1],
         ['BLM', t, 'Saint Barthélemy'              , 'Caribbean'      , 0, 0, 0],
         ['KNA', t, 'Saint Kitts and Nevis'         , 'Caribbean'      , 0, 0, 1],
         ['LCA', t, 'Saint Lucia'                   , 'Caribbean'      , 0, 0, 1],
         ['MAF', t, 'St. Martin (French Part)'      , 'Caribbean'      , 0, 0, 0],
         ['VCT', t, 'St. Vincent and the Grenadines', 'Caribbean'      , 0, 0, 1],
         ['SXM', t, 'Sint Marteen (Dutch Part)'     , 'Caribbean'      , 0, 0, 1],
         ['SGS', t, 'South Georgia and the South Sandwich Islands', 'South America', 0, 0, 0],
         ['SUR', t, 'Suriname'                      , 'South America'  , 0, 0, 1],
         ['TTO', t, 'Trinidad y Tobago'             , 'Caribbean'      , 0, 0, 1],
         ['TCA', t, 'Turks and Caicos Island'       , 'Caribbean'      , 0, 0, 0],
         ['VIR', t, 'United States Virgin Islands'  , 'Caribbean'      , 0, 0, 1],
         ['URY', t, 'Uruguay'                       , 'South America'  , 0, 0, 0],
         ['VEN', t, 'Venezuela'                     , 'South America'  , 0, 0, 0]],
         columns=['ISO', 'YEAR', 'COUNTRY', 'REGION', 'LDC', 'LLDC', 'SIDS'])
    
    INDEX = pd.concat([INDEX, df_new])
    t = t+1


# CLEAN UP
del start, end, t, df_new

# ============================================================================|
# %% DATA: V-PARTY POPULISM INDEX

file = "C:/Users/ncachanosky/OneDrive/Research/Datasets/V-Dem-CPD-Party-V2.dta"
VPARTY = pd.read_stata(file)
del file

# Rename columns for future merge (when building the index)
VPARTY = VPARTY.rename(columns={'country_text_id':'ISO' })
VPARTY = VPARTY.rename(columns={'year'           :'YEAR'})

# Drop unnecesary columns and rows
keep = ['ISO'       ,
        'YEAR'      ,
        'v2paenname',
        'v2pashname' ,
        'v2paid'    ,
        'v2xpa_popul']

VPARTY = VPARTY[keep]
VPARTY = VPARTY[VPARTY['YEAR'] >= 1990]

# Drop non-Latam countries
keep = 'AIA|ATG|ARG|ABW|BHS|BRB|BLZ|BOL|BES|BVT|BRA|VGB|CYM|\
CHL|COL|CRI|CUB|CUW|DMA|DOM|ECU|SLV|FLK|GUF|GRD|GLP|\
GTM|GUY|HTI|HND|JAM|MTQ|MEX|MSR|NIC|PAN|PRY|PER|PRI|\
BLM|KNA|LCA|MAF|VCT|SXM|SGS|SUR|TTO|TCA|VIR|URY|VEN'

VPARTY = VPARTY[VPARTY['ISO'].str.contains(keep)]
del keep

# Interpolate missing observations
VPARTY = VPARTY.sort_values(by=['ISO', 'v2paenname', 'YEAR'])
VPARTY = VPARTY.pivot(index='YEAR', values='v2xpa_popul', columns=['ISO', 'v2paenname','v2pashname', 'v2paid'])
VPARTY = VPARTY.interpolate()
VPARTY = VPARTY.sort_index(axis=1)

# Export to excel for *manual* completion
file = 'Data/VParty.xlsx'

with pd.ExcelWriter(file,
                    engine='openpyxl',
                    mode='a',
                    if_sheet_exists='replace') as writer:
    VPARTY.to_excel(writer, sheet_name="V-Party")

del writer, file


# ============================================================================|
# %% DATA: V-DEM V-PARTY MERGE
file = 'Data/VParty.xlsx'
# After manual update, re-import data from Excel
file   = pd.ExcelFile(file)
VPARTY = pd.read_excel(file, sheet_name='INDEX', usecols="A,B,E")

# Merge with INDEX
INDEX = pd.merge(INDEX, VPARTY, on=['ISO','YEAR'])
del VPARTY, file


# ============================================================================|
# %% DATA: V-DEM INDICES

# Be patient with data import (can take a few minutes)
# Then rename columns used for merging

file = "C:/Users/ncachanosky/OneDrive/Research/Datasets/V-Dem-CY-Core-v13.dta"
VDEM = pd.read_stata(file)
VDEM = VDEM.rename(columns={'country_text_id':'ISO' })
VDEM = VDEM.rename(columns={'year'           :'YEAR'})


# CLEAN UP
del file


# ============================================================================|
# %% DATA: WGI

file = "Data/wgidataset.dta"
WGI = pd.read_stata(file)
WGI = WGI.rename(columns={'year':'YEAR'})
WGI = WGI.rename(columns={'code':'ISO' })
WGI = WGI.rename(columns={'rle':'WGI_1' ,
                          'cce':'WGI_3'})

# Drop unnecessary columns
keep = ['ISO'  ,
        'YEAR' ,
        'WGI_1',
        'WGI_3']

WGI = WGI[keep]


# Drop non-Latam countries
keep = 'AIA|ATG|ARG|ABW|BHS|BRB|BLZ|BOL|BES|BVT|BRA|VGB|CYM|\
CHL|COL|CRI|CUB|CUW|DMA|DOM|ECU|SLV|FLK|GUF|GRD|GLP|\
GTM|GUY|HTI|HND|JAM|MTQ|MEX|MSR|NIC|PAN|PRY|PER|PRI|\
BLM|KNA|LCA|MAF|VCT|SXM|SGS|SUR|TTO|TCA|VIR|URY|VEN'

WGI = WGI[WGI['ISO'].str.contains(keep)]

# CLEAN UP
del file, keep


# ============================================================================|
# %% INSTITUTIONAL POPULISM | V-DEM: RULE OF LAW

VDEM_NEW = VDEM.loc[:, ['ISO', 'YEAR', 'v2x_rule']]
VDEM_NEW['v2x_rule'] = VDEM_NEW['v2x_rule']*100

INDEX = pd.merge(INDEX, VDEM_NEW, on=['ISO','YEAR'])
INDEX = INDEX.rename(columns={'v2x_rule':'VDEM_1'})
del VDEM_NEW


# ============================================================================|
# %% INSTITUTIONAL POPULISM | V_DEM: NEOPATRIMONIALISM

VDEM_NEW = VDEM.loc[:, ['ISO', 'YEAR', 'v2x_neopat']]
VDEM_NEW['v2x_neopat'] = VDEM_NEW['v2x_neopat']*100

INDEX = pd.merge(INDEX, VDEM_NEW, on=['ISO', 'YEAR'])
INDEX = INDEX.rename(columns={'v2x_neopat':'VDEM_2'})
del VDEM_NEW


# ============================================================================|
# %% INSTITUTIONAL POPULISM | V_DEM: CORRUPTION

VDEM_NEW = VDEM.loc[:, ['ISO', 'YEAR', 'v2x_execorr']]
VDEM_NEW['v2x_execorr'] = VDEM_NEW['v2x_execorr']*100

INDEX = pd.merge(INDEX, VDEM_NEW, on=['ISO', 'YEAR'])
INDEX = INDEX.rename(columns={'v2x_execorr':'VDEM_3'})
del VDEM_NEW


# ============================================================================|
# %% INSTITUTIONAL POPULISM | V-DEM: FREEDOM OF EXPRESSION

VDEM_NEW = VDEM.loc[:, ['ISO', 'YEAR', 'v2mecenefm_osp']]
VDEM_NEW['v2mecenefm_osp'] = 100 - VDEM_NEW['v2mecenefm_osp']*25

INDEX = pd.merge(INDEX, VDEM_NEW, on=['ISO', 'YEAR'])
INDEX = INDEX.rename(columns={'v2mecenefm_osp':'VDEM_4'})
del VDEM_NEW


# ============================================================================|
# %% INSTITUTIONAL POPULISM | WGI: RULE OF LAW

WGI_NEW = WGI.loc[:, ['ISO', 'YEAR', 'WGI_1']]
WGI_NEW['WGI_1'] = (WGI_NEW['WGI_1'] + 2.5)*20

INDEX = pd.merge(INDEX, WGI_NEW, on=['ISO', 'YEAR'])
del WGI_NEW


# ============================================================================|
# %% INSTITUTIONAL POPULISM | WGI: CORRUPTION

WGI_NEW = WGI.loc[:, ['ISO', 'YEAR', 'WGI_3']]
WGI_NEW['WGI_3'] = (WGI_NEW['WGI_3'] + 2.5)*20

INDEX = pd.merge(INDEX, WGI_NEW, on=['ISO', 'YEAR'])
del WGI_NEW


# ============================================================================|
# %% INDEX | INSTITUTIONAL POPULISM

INDEX['IP_1'] = (INDEX['VDEM_1'] + INDEX['WGI_1'])/2
INDEX = INDEX.rename(columns={'VDEM_2': 'IP_2'})
INDEX['IP_3'] = (INDEX['VDEM_3'] + INDEX['WGI_3'])/2
INDEX = INDEX.rename(columns={'VDEM_4': 'IP_4'})

INDEX['IP'] = (INDEX['IP_1']+INDEX['IP_2']+INDEX['IP_3']+INDEX['IP_4'])/4

# Drop unnecessary columns
keep = ['ISO'    , 
        'YEAR'   ,
        'COUNTRY',
        'REGION' ,
        'LDC'    ,
        'LLDC'   ,
        'SIDS'   ,
        'VPARTY' ,
        'IP', 'IP_1', 'IP_2', 'IP_3', 'IP_4']

INDEX = INDEX[keep]
del keep