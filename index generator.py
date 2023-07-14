# | ==========================================================================|
# | LEFT-LEANING POPULISM INDEX FOR LATIN AMERICA


# ============================================================================|
# %% LOAD PACKAGES AND SETTINGS

# PACKAGES
import os
import pandas            as pd
import numpy             as np
import matplotlib.pyplot as plt

from pandas_datareader import wb

# | SETTINGS
path = 'C:/Users/ncachanosky/OneDrive/Research/populism-index/'
os.chdir(path)
del path


# ============================================================================|
# %% CREATE COUNTRY LIST: DATASET STRUCTURE

# Create dataset structure with empty rows
index = pd.DataFrame({'ISO'   :[],  
                     'YEAR'   :[],
                     'COUNTRY':[],
                     'REGION' :[],
                     'LDC'    :[],      # Least developed country
                     'LLDC'   :[],      # Land locked developing country
                     'SIDS'   :[]})     # Small island developing state
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
    
   index = pd.concat([index, df_new])
   t = t+1

# CLEAN UP
del start, end, t

# ============================================================================|
# %% LOAD DATASETS

# V-DEM DATA
# Be patient with data import (can take a few minutes)
# Then rename columns used for merging
file = "C:/Users/ncachanosky/OneDrive/Research/Datasets/V-Dem-CY-Core-v13.dta"
vdem = pd.read_stata(file)
vdem = vdem.rename(columns={'country_text_id':'ISO' })
vdem = vdem.rename(columns={'year'           :'YEAR'})

# CLEAN UP
del file


# ============================================================================|
# %% INSTITUTIONAL POPULISM | RULE OF LAW

vdem_new = vdem.loc[:, ['ISO', 'YEAR', 'v2x_rule']]
vdem_new['v2x_rule'] = vdem_new['v2x_rule']*100

index = pd.merge(index, vdem_new, on=['ISO','YEAR'])
del vdem_new


# ============================================================================|
#%% INSTITUTIONAL POPULISM | NEOPATRIMONIALISM

vdem_new = vdem.loc[:, ['ISO', 'YEAR', 'v2x_neopat']]
vdem_new['v2x_neopat'] = vdem_new['v2x_neopat']*100

index = pd.merge(index, vdem_new, on=['ISO', 'YEAR'])
del vdem_new


# ============================================================================|
#%% INSTITUTIONAL POPULISM | CORRUPTION

vdem_new = vdem.loc[:, ['ISO', 'YEAR', 'v2x_execorr']]
vdem_new['v2x_execorr'] = vdem_new['v2x_execorr']*100

index = pd.merge(index, vdem_new, on=['ISO', 'YEAR'])
del vdem_new


# ============================================================================|
#%% INSTITUTIONAL POPULISM | FREEDOM OF EXPRESSION

vdem_new = vdem.loc[:, ['ISO', 'YEAR', 'v2mecenefm_osp']]
vdem_new['v2mecenefm_osp'] = 100 - vdem_new['v2mecenefm_osp']*25

index = pd.merge(index, vdem_new, on=['ISO', 'YEAR'])
del vdem_new