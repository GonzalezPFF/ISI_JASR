#%% PACKAGE LOADING AND FUNCTION DEFINITION
import numpy as np 
import matplotlib.pyplot as plt
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

#%% DATABASE LOADING
data_all= np.loadtxt('SMOOTHED_latlong_temps_NOLATLONG_V2_FREQUENCIES.txt',delimiter=',')

#%% BEAM CONSTRUCTION AROUND ZENITH
lat_zl_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
long_zl_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]

# Diccionarios de coordenadas shifteadas de acuerdo al beam requerido 
no_beams= 49

delta1= np.arange(-37.5,50.,12.5)
delta2= np.arange(37.5, -50.,-12.5)

# Shifting para cada beam
delta_lats=[]
delta_longs=[]
for i in delta1:
    for j in delta2:
        delta_lats.append(i)
        delta_longs.append(j)
        
# Realizacion del shifting desde el zenit
dict_lats={i:[] for i in range(0,no_beams)}
dict_longs={i:[] for i in range(0,no_beams)}

for i in range(len(lat_zl_M10)):
    for n in range(no_beams):
        dict_lats[n].append(lat_zl_M10[i]+delta_lats[n])
        dict_longs[n].append(long_zl_M10[i]+delta_longs[n])
        
# Definicion del tiempo / hora UTC y frecuencias
X1= np.linspace(0, 24, len(lat_zl_M10))
X1_list=[]
for n in X1:
    X1_list.append(n)
    
time=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45', '24:00']
frequencies_range= np.arange(30,45.5,0.5)

frequencies_saving= []
for i in frequencies_range:
    frequencies_saving.append(str(i)+'_MHz')

# Desde la database generadora de los mapas LFSM Mollweide, se cargan las temperaturas
#de brillo de interes guardadas previamente en columnas cada 0.5 MHz. 
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

    # Plots grid
    # Brightness temperature
    grid= np.zeros((7,7))
    for j in range(len(qdc_beams[0])):
        grid[0,0]=qdc_beams[0][j]
        grid[0,1]=qdc_beams[1][j]
        grid[0,2]=qdc_beams[2][j]
        grid[0,3]=qdc_beams[3][j]
        grid[0,4]=qdc_beams[4][j]
        grid[0,5]=qdc_beams[5][j]
        grid[0,6]=qdc_beams[6][j]
        grid[1,0]=qdc_beams[7][j]
        grid[1,1]=qdc_beams[8][j]
        grid[1,2]=qdc_beams[9][j]
        grid[1,3]=qdc_beams[10][j]
        grid[1,4]=qdc_beams[11][j]
        grid[1,5]=qdc_beams[12][j]
        grid[1,6]=qdc_beams[13][j]
        grid[2,0]=qdc_beams[14][j]
        grid[2,1]=qdc_beams[15][j]
        grid[2,2]=qdc_beams[16][j]
        grid[2,3]=qdc_beams[17][j]
        grid[2,4]=qdc_beams[18][j]
        grid[2,5]=qdc_beams[19][j]
        grid[2,6]=qdc_beams[20][j]
        grid[3,0]=qdc_beams[21][j]
        grid[3,1]=qdc_beams[22][j]
        grid[3,2]=qdc_beams[23][j]
        grid[3,3]=qdc_beams[24][j]
        grid[3,4]=qdc_beams[25][j]
        grid[3,5]=qdc_beams[26][j]
        grid[3,6]=qdc_beams[27][j]
        grid[4,0]=qdc_beams[28][j]
        grid[4,1]=qdc_beams[29][j]
        grid[4,2]=qdc_beams[30][j]
        grid[4,3]=qdc_beams[31][j]
        grid[4,4]=qdc_beams[32][j]
        grid[4,5]=qdc_beams[33][j]
        grid[4,6]=qdc_beams[34][j]
        grid[5,0]=qdc_beams[35][j]
        grid[5,1]=qdc_beams[36][j]
        grid[5,2]=qdc_beams[37][j]
        grid[5,3]=qdc_beams[38][j]
        grid[5,4]=qdc_beams[39][j]
        grid[5,5]=qdc_beams[40][j]
        grid[5,6]=qdc_beams[41][j]
        grid[6,0]=qdc_beams[42][j]
        grid[6,1]=qdc_beams[43][j]
        grid[6,2]=qdc_beams[44][j]
        grid[6,3]=qdc_beams[45][j]
        grid[6,4]=qdc_beams[46][j]
        grid[6,5]=qdc_beams[47][j]
        grid[6,6]=qdc_beams[46][j]

        plt.figure(figsize=(7,5))
        plt.imshow(grid, cmap='viridis', extent=[50.0,-50.0,-50.0,+50.0])
        plt.title(str(time[j]))
        plt.xlabel('$\Delta$ RA (deg)')
        plt.ylabel('$\Delta$ Dec (deg)')
        plt.colorbar().set_label('Brightness temperature [K]', rotation= 270, labelpad=15)
        plt.clim(vmin=5000, vmax=55000)
        plt.savefig(str(frequencies_saving[i-1])+'_AP_SYN_CRN'+str(j)+'_'+str(X1[j])+'.png')
        plt.cla()
        plt.clf()
        plt.close('all')
    
    # Power noise
    grid2= np.zeros((7,7))
    for j in range(len(qdc_beams[0])):
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
        plt.title(str(time[j]))
        plt.xlabel('$\Delta$ RA (deg)')
        plt.ylabel('$\Delta$ Dec (deg)')
        plt.colorbar().set_label('Noise Power [dBm]', rotation= 270, labelpad=15)
        plt.clim(vmin=-140, vmax=-114)
        plt.savefig(str(frequencies_saving[i-1])+'POWER_AP_SYN_CRN'+str(j)+'_'+str(X1[j])+'.png')    
        plt.cla()
        plt.clf()
        plt.close('all')
            
    