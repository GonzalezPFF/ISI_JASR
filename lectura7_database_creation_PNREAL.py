import pandas as pd
import numpy as np 
#import matplotlib.pyplot as plt
import healpy as hp
from scipy.stats import scoreatpercentile as percentile
import scipy.constants as sc

def power_noise(T_A):
    G_sys= 10**5.83
    Delta_nu= 7.8125*(10**5)
    P_n = sc.k*(300+T_A)*G_sys*Delta_nu
    return P_n

def power_dbm(power_watts):
    power_dbm= 10*np.log(power_watts)+30
    return power_dbm

#%%
data_all= np.loadtxt('SMOOTHED_latlong_temps_NOLATLONG_V2_FREQUENCIES.txt',delimiter=',')

#%%
lat_zl_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
#long_zl_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]
long_zl_M10= [94.955, 98.705, 102.455, 106.205, 109.9950, 113.705, 117.455, 121.205, 124.955, 128.705, 132.455, 136.205, 139.955, 143.705, 147.455, 151.205, 154.955, 158.705, 162.455, 166.205, 169.955, 173.705, 177.455, -178.795, -175.045, -171.295, -167.545, -163.795, -160.045, -156.295, -152.545, -148.795, -145.045, -141.295, -137.545, -133.795, -130.045, -126.295, -122.545, -118.795, -115.045, -111.295, -107.545, -103.795, -100.045, -96.295, -92.545, -88.795, -85.045, -81.295, -77.545, -73.795, -70.045, -66.295, -62.545, -58.795, -55.045, -51.295, -47.545, -43.795, -40.045, -36.295, -32.545, -28.795, -25.045, -21.295, -17.545, -13.795, -10.045, -6.295, -2.545, 1.205, 4.955, 8.705, 12.455, 16.205, 19.955, 23.705, 27.455, 31.205, 34.955, 38.705, 42.455, 46.205, 49.955, 53.705, 57.455, 61.205, 64.955, 68.705, 72.455, 76.205, 79.955, 83.705, 87.455, 91.205, 94.955]
#%%
no_beams= 49
delta1= np.arange(-37.5,50.,12.5)
delta2= np.arange(37.5, -50.,-12.5)

delta_lats=[]
delta_longs=[]
for i in delta1:
    for j in delta2:
        delta_lats.append(i)
        delta_longs.append(j)
        
#%%
dict_lats={i:[] for i in range(0,no_beams)}
dict_longs={i:[] for i in range(0,no_beams)}

for i in range(len(lat_zl_M10)):
    for n in range(no_beams):
        dict_lats[n].append(lat_zl_M10[i]+delta_lats[n])
        dict_longs[n].append(long_zl_M10[i]+delta_longs[n])
        
X1= np.linspace(0, 24, len(lat_zl_M10))
X1_list=[]
for n in X1:
    X1_list.append(n)
    
time=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45', '24:00']
frequencies_range= np.arange(30,45.5,0.5)

frequencies_saving= []
for i in frequencies_range:
    frequencies_saving.append(str(i)+'_MHz')
    
#%%
headers= ['TIME (HH:MM)', 'TIME (INT)', 'FREQUENCY (MHz)', 'DELTA RA (DEG)', 'DELTA DEC (DEG)', 'POWER NOISE (dBm)']

time_hhmm=[]
time_int=[]
frequency_mhz=[]
delta_ra_deg_beta=[]
delta_dec_deg_beta=[]
power_noise_dbm=[]

for i in range(1,32):
    T_map= data_all[:, i]
    nside=hp.npix2nside(len(T_map))
    vmin = percentile(T_map, 0)
    vmax = percentile(T_map, 100)
    
    # Diccionarios de temperaturas de brillo y potencia de ruido por beam en funcion
    #de UTC.
    qdc_beams={j:[] for j in range(0,no_beams)}
    pn_beams={j:[] for j in range(0,no_beams)}
    
    # Busqueda en el mapa y adicion a las listas de beams de la temperatura de brillo
    #y potencia de ruido capturada por beam.
    for j in range(len(dict_lats[0])):
        for k in range(0,no_beams):
            lat_bk_M10 = dict_lats[k][j]
            long_bk_M10 = dict_longs[k][j]
            vec_bk_M10=hp.ang2vec(np.radians(lat_bk_M10), np.radians(long_bk_M10))
            ipix_disc_bk_M10= hp.query_disc(nside=nside, vec=vec_bk_M10, radius=np.radians(25.))
            mean_bk_M10= np.mean(T_map[ipix_disc_bk_M10])
            qdc_beams[k].append(mean_bk_M10)
            pn_beams[k].append(power_dbm(power_noise(mean_bk_M10)))
            
            time_hhmm.append(time[j])
            time_int.append(X1[j])
            frequency_mhz.append(frequencies_range[i-1])
#            frequency_mhz.append(frequencies_saving[i-1])
 #           delta_dec_deg.append(dict_lats[k][j]-lat_zl_M10[i])
 #           delta_ra_deg.append(dict_longs[k][j]-long_zl_M10[i])
            power_noise_dbm.append(power_dbm(power_noise(mean_bk_M10)))

#%%
for i in range(len(delta2)):
    for j in range(len(delta2)):
#        for k in range(len(frequencies_saving)):
        delta_ra_deg_beta.append(delta2[j])
        delta_dec_deg_beta.append(delta2[i])

delta_dec_deg= delta_dec_deg_beta*len(time)*len(frequencies_saving)
delta_ra_deg= delta_ra_deg_beta*len(time)*len(frequencies_saving)
#%%      
matrix= [time_hhmm, time_int, frequency_mhz, delta_ra_deg, delta_dec_deg, power_noise_dbm]
tabla = pd.DataFrame()
for i in range(len(headers)):
    tabla[headers[i]] = matrix[i]
    
tabla.to_csv('dataset_real.csv')