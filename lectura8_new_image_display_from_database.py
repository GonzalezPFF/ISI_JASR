import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd
#%%
new_table = pd.read_csv('dataset_real.csv')
#%%
#for i in range(len(new_table['FREQUENCY (MHz)'])):
#  new_table['FREQUENCY (MHz)'][i] = float(new_table['FREQUENCY (MHz)'][i].replace('_MHz',''))
#%%
cuales_horas= new_table['TIME (HH:MM)'].unique()
cuales_horas_int= new_table['TIME (INT)'].unique()
cuales_frecuencias= new_table['FREQUENCY (MHz)'].unique()
cuales_delta_ra = new_table['DELTA RA (DEG)'].unique()
cuales_delta_dec = new_table['DELTA DEC (DEG)'].unique()
#%%
sorted_cuales_frecuencias= np.sort(cuales_frecuencias)
#%%
bandwidth= np.round(sorted_cuales_frecuencias[1] - sorted_cuales_frecuencias[0],1)
frequencies_range= np.arange(np.min(cuales_frecuencias),np.max(cuales_frecuencias)+bandwidth,bandwidth)
frequencies_saving= []
for i in frequencies_range:
    frequencies_saving.append(str(i)+'_MHz')
#%%
for i in range(len(cuales_frecuencias)):
  pn_beams={n:[] for n in range(len(cuales_delta_ra)*len(cuales_delta_dec))}
  filtro_frecuencias= new_table['FREQUENCY (MHz)'] == cuales_frecuencias[i]
  tabla_filtrada_frecuencias = new_table[filtro_frecuencias]
  for j in range(len(cuales_horas)):
    filtro_horas = tabla_filtrada_frecuencias['TIME (HH:MM)'] == cuales_horas[j]
    tabla_filtrada_frecuencias_horas = tabla_filtrada_frecuencias[filtro_horas].reset_index()
    for k in range(len(cuales_delta_ra)*len(cuales_delta_dec)):
      pn_beams[k].append(tabla_filtrada_frecuencias_horas['POWER NOISE (dBm)'][k])
  grid2= np.zeros((7,7))
  for j in range(len(pn_beams[0])):
      grid2[0,0]= pn_beams[0][j]
      grid2[0,1]= pn_beams[1][j]
      grid2[0,2]= pn_beams[2][j]
      grid2[0,3]= pn_beams[3][j]
      grid2[0,4]= pn_beams[4][j]
      grid2[0,5]= pn_beams[5][j]
      grid2[0,6]= pn_beams[6][j]
      grid2[1,0]= pn_beams[7][j]
      grid2[1,1]= pn_beams[8][j]
      grid2[1,2]= pn_beams[9][j]
      grid2[1,3]= pn_beams[10][j]
      grid2[1,4]= pn_beams[11][j]
      grid2[1,5]= pn_beams[12][j]
      grid2[1,6]= pn_beams[13][j]
      grid2[2,0]= pn_beams[14][j]
      grid2[2,1]= pn_beams[15][j]
      grid2[2,2]= pn_beams[16][j]
      grid2[2,3]= pn_beams[17][j]
      grid2[2,4]= pn_beams[18][j]
      grid2[2,5]= pn_beams[19][j]
      grid2[2,6]= pn_beams[20][j]
      grid2[3,0]= pn_beams[21][j]
      grid2[3,1]= pn_beams[22][j]
      grid2[3,2]= pn_beams[23][j]
      grid2[3,3]= pn_beams[24][j]
      grid2[3,4]= pn_beams[25][j]
      grid2[3,5]= pn_beams[26][j]
      grid2[3,6]= pn_beams[27][j]
      grid2[4,0]= pn_beams[28][j]
      grid2[4,1]= pn_beams[29][j]
      grid2[4,2]= pn_beams[30][j]
      grid2[4,3]= pn_beams[31][j]
      grid2[4,4]= pn_beams[32][j]
      grid2[4,5]= pn_beams[33][j]
      grid2[4,6]= pn_beams[34][j]
      grid2[5,0]= pn_beams[35][j]
      grid2[5,1]= pn_beams[36][j]
      grid2[5,2]= pn_beams[37][j]
      grid2[5,3]= pn_beams[38][j]
      grid2[5,4]= pn_beams[39][j]
      grid2[5,5]= pn_beams[40][j]
      grid2[5,6]= pn_beams[41][j]
      grid2[6,0]= pn_beams[42][j]
      grid2[6,1]= pn_beams[43][j]
      grid2[6,2]= pn_beams[44][j]
      grid2[6,3]= pn_beams[45][j]
      grid2[6,4]= pn_beams[46][j]
      grid2[6,5]= pn_beams[47][j]
      grid2[6,6]= pn_beams[48][j]

      plt.figure(figsize=(7,5))
      plt.imshow(grid2, cmap='magma', extent=[50.0,-50.0,-50.0,50.0])
      plt.title(str(frequencies_saving[i]) + ' ' + str(cuales_horas[j]))
      plt.xlabel('$\Delta$ RA (deg)')
      plt.ylabel('$\Delta$ Dec (deg)')
      plt.colorbar().set_label('Noise Power [dBm]', rotation= 270, labelpad=15)
      plt.clim(vmin=-145, vmax=-114)
      plt.savefig(str(frequencies_saving[i])+'POWER_AP_SYN_CRN'+str(j)+'_'+str(cuales_horas_int[j])+'.png')    
      plt.cla()
      plt.clf()
      plt.close('all')