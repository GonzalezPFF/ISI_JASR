import pandas as pd 
import numpy as np 
#%%
new_table = pd.read_csv('dataset_real.csv')

#%%
#for i in range(len(new_table['FREQUENCY (MHz)'])):
#  new_table['FREQUENCY (MHz)'][i] = float(new_table['FREQUENCY (MHz)'][i].replace('_MHz',''))

#%%
mu=-1
sigma=1
pn_random=[]
for i in range(len(new_table['POWER NOISE (dBm)'])):
  pn_random.append(new_table['POWER NOISE (dBm)'][i] + np.random.normal(mu, sigma))

new_table.insert(6, 'RAND POWER NOISE (dBm)', pn_random, True)

#%%
relative_abs_coef= []
for i in range(len(new_table['POWER NOISE (dBm)'])):
  relative_abs_coef.append(10*np.log10(new_table['RAND POWER NOISE (dBm)'][i]/new_table['POWER NOISE (dBm)'][i]))

new_table.insert(7, 'RELATIVE ABSORPTION COEF (dB)', relative_abs_coef, True)
#%%
new_table.to_csv('dataset_sim_abs.csv')