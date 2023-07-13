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
# %% LOAD DATASETS
# COUNTRY LIST
file = 'populism-index.xlsx'
index   = pd.read_excel(file, sheet_name='INDEX', header=0, usecols="A:G")

# V-DEM DATA
# Be patient with data import (can take a few minutes)
# Then rename columns used for merging
file = "C:/Users/ncachanosky/OneDrive/Research/Datasets/V-Dem-CY-Core-v13.dta"
vdem = pd.read_stata(file)
vdem = vdem.rename(columns={'country_text_id':'ISO'  })
vdem = vdem.rename(columns={'year'           : 'YEAR'})

# CLEAN UP
del file


# ============================================================================|
# %% INSTITUTIONAL POPULISM | RULE OF LAW

vdem1 = vdem.loc[:, ['ISO', 'YEAR', 'v2x_rule']]
vdem1['v2x_rule'] = vdem1['v2x_rule']*100

index = pd.merge(index, vdem1, on=['ISO','YEAR'])


# ============================================================================|
#%% INSTITUTIONAL POPULISM | NEOPATRIMONIALISM

vdem3 = vdem.loc[:, ['ISO', 'YEAR', 'v2x_neopat']]
vdem3['v2x_neopat'] = vdem3['v2x_neopat']*100

index = pd.merge(index, vdem3, on=['ISO', 'YEAR'])


# ============================================================================|
#%% INSTITUTIONAL POPULISM | CORRUPTION

vdem4 = vdem.loc[:, ['ISO', 'YEAR', 'v2x_execorr']]
vdem4['v2x_execorr'] = vdem4['v2x_execorr']*100

index = pd.merge(index, vdem4, on=['ISO', 'YEAR'])


# ============================================================================|
#%% INSTITUTIONAL POPULISM | FREEDOM OF EXPRESSION

vdem5 = vdem.loc[:, ['ISO', 'YEAR', 'v2mecenefm_osp']]
vdem5['v2mecenefm_osp'] = 100 - vdem5['v2mecenefm_osp']*25

index = pd.merge(index, vdem5, on=['ISO', 'YEAR'])