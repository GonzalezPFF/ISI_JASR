#%% PACKAGE LOADING AND FUNCTION DEFINITION
import numpy as np 
import pandas as pd 

#%% BEAM CONSTRUCTION AROUND ZENITH
lat_zl_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
long_zl_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]

# Diccionarios de coordenadas shifteadas de acuerdo al beam requerido 
no_beams= 49

delta1= np.arange(-37.5,50.,12.5)
delta2= np.arange(37.5, -50.,-12.5)

delta_lats=[]
delta_longs=[]
for i in delta1:
    for j in delta2:
        delta_lats.append(i)
        delta_longs.append(j)
    
# Definicion del shifting para cada beam
dict_lats={i:[] for i in range(0,no_beams)}
dict_longs={i:[] for i in range(0,no_beams)}

for i in range(len(lat_zl_M10)):
    for j in range(no_beams):
        dict_lats[j].append(lat_zl_M10[i]+delta_lats[j])
        dict_longs[j].append(long_zl_M10[i]+delta_longs[j])
        
#%%
X1= np.linspace(0, 24, len(lat_zl_M10))
X1_list=[]
for i in X1:
    X1_list.append(i)

time=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45', '24:00']

frequencies_range= np.arange(30,45.5,0.5)

frequencies_saving= []
frequencies_database_beta=[]
for i in frequencies_range:
    frequencies_saving.append(str(i)+'_MHz')
    frequencies_database_beta.append(i)
    
frequencies_database= frequencies_database_beta*no_beams*len(time)
frequencies_database_resh= np.array(frequencies_database).reshape(1,len(frequencies_database))

time_database=[]
X1_database=[]
for i in range(0,len(time)):
    time_database.append([time[i]]*len(frequencies_saving)*no_beams)
    X1_database.append([X1_list[i]]*len(frequencies_saving)*no_beams)
    
time_database_resh= np.array(time_database).reshape(1, len(frequencies_database))
X1_database_resh= np.array(X1_database).reshape(1, len(frequencies_database))

d_lats_database_beta= []
d_longs_database_beta=[]

for i in range(len(delta1)):
    for j in range(len(delta2)):
        for k in range(len(frequencies_saving)):
            d_lats_database_beta.append(delta1[i])
            d_longs_database_beta.append(delta2[j])

d_lats_database= d_lats_database_beta*len(time)
d_lats_database_resh= np.array(d_lats_database).reshape(1,len(frequencies_database))

d_longs_database= d_longs_database_beta*len(time)
d_longs_database_resh= np.array(d_longs_database).reshape(1,len(frequencies_database))

p_n_database= np.random.normal(-107, 15, len(frequencies_database))
p_n_database_resh= np.array(p_n_database).reshape(1,len(frequencies_database))

#%% pandas dataframe creation
headers=['TIME (HH:MM)', 'TIME (INT)', 'FREQUENCY (MHz)', 'DELTA RA (DEG)', 'DELTA DEC (DEG)', 'POWER NOISE (dBm)']

matriz= [np.array(time_database).flatten(),  np.array(X1_database).flatten(), frequencies_database, d_longs_database, d_lats_database, p_n_database]

tabla = pd.DataFrame()
for i in range(len(headers)):
    tabla[headers[i]] = matriz[i]
    
tabla.to_csv('dataset_synth.csv')

#%% txt dataframe creation NOT WORKING YET
array= np.concatenate((time_database_resh, X1_database_resh, frequencies_database_resh, d_longs_database_resh, d_lats_database_resh, p_n_database_resh)).T
np.savetxt('dataset_synth.txt', array, fmt="%s", delimiter=',', header='TIME (HH:MM), TIME (INT), FREQUENCY (MHz), DELTA RA (DEG), DELTA DEC (DEG), POWER NOISE (dBm)')