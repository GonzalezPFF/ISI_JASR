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
data_all= np.loadtxt('latlong_temps_NOLATLONG_V2.txt',delimiter=',')

#%% BEAM CONSTRUCTION AROUND ZENITH
#lat_zl_M10= [(180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317)]
lat_zl_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
long_zl_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]

no_beams= 49
dict_lats={i:[] for i in range(0,no_beams)}
dict_longs={i:[] for i in range(0,no_beams)}

for i in range(len(lat_zl_M10)):
    dict_lats[0].append(lat_zl_M10[i]+0)
    dict_lats[1].append(lat_zl_M10[i]+0)
    dict_lats[2].append(lat_zl_M10[i]-12.5)
    dict_lats[3].append(lat_zl_M10[i]-12.5)
    dict_lats[4].append(lat_zl_M10[i]-12.5)
    dict_lats[5].append(lat_zl_M10[i]+0)
    dict_lats[6].append(lat_zl_M10[i]+12.5)
    dict_lats[7].append(lat_zl_M10[i]+12.5)
    dict_lats[8].append(lat_zl_M10[i]+12.5)
    dict_lats[9].append(lat_zl_M10[i]+0)
    dict_lats[10].append(lat_zl_M10[i]-12.5)
    dict_lats[11].append(lat_zl_M10[i]-25.0)
    dict_lats[12].append(lat_zl_M10[i]-25.0)
    dict_lats[13].append(lat_zl_M10[i]-25.0)
    dict_lats[14].append(lat_zl_M10[i]-25.0)
    dict_lats[15].append(lat_zl_M10[i]-25.0)
    dict_lats[16].append(lat_zl_M10[i]-12.5)
    dict_lats[17].append(lat_zl_M10[i]+0)
    dict_lats[18].append(lat_zl_M10[i]+12.5)
    dict_lats[19].append(lat_zl_M10[i]+25.0)
    dict_lats[20].append(lat_zl_M10[i]+25.0)
    dict_lats[21].append(lat_zl_M10[i]+25.0)
    dict_lats[22].append(lat_zl_M10[i]+25.0)
    dict_lats[23].append(lat_zl_M10[i]+25.0)
    dict_lats[24].append(lat_zl_M10[i]+12.5)
    dict_lats[25].append(lat_zl_M10[i]+0)
    dict_lats[26].append(lat_zl_M10[i]-12.5)
    dict_lats[27].append(lat_zl_M10[i]-25.0)
    dict_lats[28].append(lat_zl_M10[i]-37.5)
    dict_lats[29].append(lat_zl_M10[i]-37.5)
    dict_lats[30].append(lat_zl_M10[i]-37.5)
    dict_lats[31].append(lat_zl_M10[i]-37.5)
    dict_lats[32].append(lat_zl_M10[i]-37.5)
    dict_lats[33].append(lat_zl_M10[i]-37.5)
    dict_lats[34].append(lat_zl_M10[i]-37.5)
    dict_lats[35].append(lat_zl_M10[i]-25.0)
    dict_lats[36].append(lat_zl_M10[i]-12.5)
    dict_lats[37].append(lat_zl_M10[i]+0)
    dict_lats[38].append(lat_zl_M10[i]+12.5)
    dict_lats[39].append(lat_zl_M10[i]+25.0)
    dict_lats[40].append(lat_zl_M10[i]+37.5)
    dict_lats[41].append(lat_zl_M10[i]+37.5) 
    dict_lats[42].append(lat_zl_M10[i]+37.5) 
    dict_lats[43].append(lat_zl_M10[i]+37.5) 
    dict_lats[44].append(lat_zl_M10[i]+37.5) 
    dict_lats[45].append(lat_zl_M10[i]+37.5) 
    dict_lats[46].append(lat_zl_M10[i]+37.5) 
    dict_lats[47].append(lat_zl_M10[i]+25.0)
    dict_lats[48].append(lat_zl_M10[i]+12.5)
    
    dict_longs[0].append(long_zl_M10[i]+0)
    dict_longs[1].append(long_zl_M10[i]-12.5)
    dict_longs[2].append(long_zl_M10[i]-12.5)
    dict_longs[3].append(long_zl_M10[i]+0)
    dict_longs[4].append(long_zl_M10[i]+12.5)
    dict_longs[5].append(long_zl_M10[i]+12.5)
    dict_longs[6].append(long_zl_M10[i]+12.5)
    dict_longs[7].append(long_zl_M10[i]+0)
    dict_longs[8].append(long_zl_M10[i]-12.5)
    dict_longs[9].append(long_zl_M10[i]-25.0)
    dict_longs[10].append(long_zl_M10[i]-25.0)
    dict_longs[11].append(long_zl_M10[i]-25.0)
    dict_longs[12].append(long_zl_M10[i]-12.5)
    dict_longs[13].append(long_zl_M10[i]+0)
    dict_longs[14].append(long_zl_M10[i]+12.5)
    dict_longs[15].append(long_zl_M10[i]+25.0)
    dict_longs[16].append(long_zl_M10[i]+25.0)
    dict_longs[17].append(long_zl_M10[i]+25.0)
    dict_longs[18].append(long_zl_M10[i]+25.0)
    dict_longs[19].append(long_zl_M10[i]+25.0)
    dict_longs[20].append(long_zl_M10[i]+12.5)
    dict_longs[21].append(long_zl_M10[i]+0)
    dict_longs[22].append(long_zl_M10[i]-12.5)
    dict_longs[23].append(long_zl_M10[i]-25.0)
    dict_longs[24].append(long_zl_M10[i]-25.0)
    dict_longs[25].append(long_zl_M10[i]-37.5)
    dict_longs[26].append(long_zl_M10[i]-37.5)
    dict_longs[27].append(long_zl_M10[i]-37.5)
    dict_longs[28].append(long_zl_M10[i]-37.5)
    dict_longs[29].append(long_zl_M10[i]-25.0)
    dict_longs[30].append(long_zl_M10[i]-12.5)
    dict_longs[31].append(long_zl_M10[i]+0)
    dict_longs[32].append(long_zl_M10[i]+12.5)
    dict_longs[33].append(long_zl_M10[i]+25.0)
    dict_longs[34].append(long_zl_M10[i]+37.5)
    dict_longs[35].append(long_zl_M10[i]+37.5)
    dict_longs[36].append(long_zl_M10[i]+37.5)
    dict_longs[37].append(long_zl_M10[i]+37.5)
    dict_longs[38].append(long_zl_M10[i]+37.5)
    dict_longs[39].append(long_zl_M10[i]+37.5)
    dict_longs[40].append(long_zl_M10[i]+37.5) 
    dict_longs[41].append(long_zl_M10[i]+25.0) 
    dict_longs[42].append(long_zl_M10[i]+12.5) 
    dict_longs[43].append(long_zl_M10[i]+0)    
    dict_longs[44].append(long_zl_M10[i]-12.5) 
    dict_longs[45].append(long_zl_M10[i]-25.0) 
    dict_longs[46].append(long_zl_M10[i]-37.5) 
    dict_longs[47].append(long_zl_M10[i]-37.5) 
    dict_longs[48].append(long_zl_M10[i]-37.5)

#%% TEMPERATURA SEQUENCE BUILDING
T_map= data_all[:, 1]
nside=hp.npix2nside(len(T_map))
vmin = percentile(T_map, 0)
vmax = percentile(T_map, 100)
    
qdc_beams={i:[] for i in range(0,no_beams)}
pn_beams={i:[] for i in range(0,no_beams)}
    
for i in range(len(dict_lats[0])):
    for j in range(0,no_beams):
        lat_bj_M10 = dict_lats[j][i]
        long_bj_M10 = dict_longs[j][i]
        vec_bj_M10=hp.ang2vec(np.radians(lat_bj_M10), np.radians(long_bj_M10))
        ipix_disc_bj_M10= hp.query_disc(nside=nside, vec=vec_bj_M10, radius=np.radians(25.), inclusive=False)
        mean_bj_M10= np.mean(T_map[ipix_disc_bj_M10])
        qdc_beams[j].append(mean_bj_M10)
        pn_beams[j].append(power_dbm(power_noise(mean_bj_M10)))
            
X1= np.linspace(0, 24, len(qdc_beams[0])) #UTC
X1_resh= np.array(X1).reshape(1, len(X1))

fig, axs = plt.subplots(7, 7, sharex=True, sharey=True)
fig.suptitle('Brightness Temperature Day Curve (FWHM 25$^o$ at 38.2 MHz) on March 10, 2004')
    
axs[0, 0].plot(X1, qdc_beams[34], c='r')
#axs[0, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +37.5^o)$')
axs[0, 0].set_xlim([0,24])
axs[0, 0].set_ylim([0,37000])

axs[0, 1].plot(X1, qdc_beams[33], c='r')
#axs[0, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +37.5^o)$')
axs[0, 1].set_xlim([0,24])
axs[0, 1].set_ylim([0,37000])
 
axs[0, 2].plot(X1, qdc_beams[32] , c='r')
#axs[0, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +37.5^o)$')
axs[0, 2].set_xlim([0,24])
axs[0, 2].set_ylim([0,37000])
  
axs[0, 3].plot(X1, qdc_beams[31] , c='r')
#axs[0, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +37.5^o)$')
axs[0, 3].set_xlim([0,24])
axs[0, 3].set_ylim([0,37000])
 
axs[0, 4].plot(X1, qdc_beams[30] , c='r')
#axs[0, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +37.5^o)$')
axs[0, 4].set_xlim([0,24])
axs[0, 4].set_ylim([0,37000])
  
axs[0, 5].plot(X1, qdc_beams[29] , c='r')
#axs[0, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +37.5^o)$')
axs[0, 5].set_xlim([0,24])
axs[0, 5].set_ylim([0,37000])

axs[0, 6].plot(X1, qdc_beams[28] , c='r')
#axs[0, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +37.5^o)$')
axs[0, 6].set_xlim([0,24])
axs[0, 6].set_ylim([0,37000])

axs[1, 0].plot(X1, qdc_beams[35] , c='r')
#axs[1, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +25.0^o)$')
axs[1, 0].set_xlim([0,24])
axs[1, 0].set_ylim([0,37000])

axs[1, 1].plot(X1, qdc_beams[15] , c='r')
#axs[1, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +25.0^o)$')
axs[1, 1].set_xlim([0,24])
axs[1, 1].set_ylim([0,37000])

axs[1, 2].plot(X1, qdc_beams[14] , c='r')
#axs[1, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +25.0^o)$')
axs[1, 2].set_xlim([0,24])
axs[1, 2].set_ylim([0,37000])
    
axs[1, 3].plot(X1, qdc_beams[13] , c='r')
#axs[1, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +25.0^o)$')
axs[1, 3].set_xlim([0,24])
axs[1, 3].set_ylim([0,37000])

axs[1, 4].plot(X1, qdc_beams[12] , c='r')
#axs[1, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +25.0^o)$')
axs[1, 4].set_xlim([0,24])
axs[1, 4].set_ylim([0,37000])
 
axs[1, 5].plot(X1, qdc_beams[11] , c='r')
#axs[1, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +25.0^o)$')
axs[1, 5].set_xlim([0,24])
axs[1, 5].set_ylim([0,37000])

axs[1, 6].plot(X1, qdc_beams[27] , c='r')
#axs[1, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +25.0^o)$')
axs[1, 6].set_xlim([0,24])
axs[1, 6].set_ylim([0,37000])
    
axs[2, 0].plot(X1, qdc_beams[36] , c='r')
#axs[2, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +12.5^o)$')
axs[2, 0].set_xlim([0,24])
axs[2, 0].set_ylim([0,37000])
   
axs[2, 1].plot(X1, qdc_beams[16] , c='r')
#axs[2, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +12.5^o)$')
axs[2, 1].set_xlim([0,24])
axs[2, 1].set_ylim([0,37000])
  
axs[2, 2].plot(X1, qdc_beams[4] , c='r')
#axs[2, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +12.5^o)$')
axs[2, 2].set_xlim([0,24])
axs[2, 2].set_ylim([0,37000])
 
axs[2, 3].plot(X1, qdc_beams[3] , c='r')
#axs[2, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +12.5^o)$')
axs[2, 3].set_xlim([0,24])
axs[2, 3].set_ylim([0,37000])
  
axs[2, 4].plot(X1, qdc_beams[2] , c='r')
#axs[2, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +12.5^o)$')
axs[2, 4].set_xlim([0,24])
axs[2, 4].set_ylim([0,37000])
 
axs[2, 5].plot(X1, qdc_beams[10] , c='r')
#axs[2, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +12.5^o)$')
axs[2, 5].set_xlim([0,24])
axs[2, 5].set_ylim([0,37000])

axs[2, 6].plot(X1, qdc_beams[26] , c='r')
#axs[2, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +12.5^o)$')
axs[2, 6].set_xlim([0,24])
axs[2, 6].set_ylim([0,37000])
    
axs[3, 0].plot(X1, qdc_beams[37] , c='r')
#axs[3, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +0.0^o)$')
axs[3, 0].set_xlim([0,24])
axs[3, 0].set_ylim([0,37000])

axs[3, 1].plot(X1, qdc_beams[17] , c='r')
#axs[3, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +0.0^o)$')
axs[3, 1].set_xlim([0,24])
axs[3, 1].set_ylim([0,37000])
    
axs[3, 2].plot(X1, qdc_beams[5] , c='r')
#axs[3, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +0.0^o)$')
axs[3, 2].set_xlim([0,24])
axs[3, 2].set_ylim([0,37000])
    
axs[3, 3].plot(X1, qdc_beams[0] , c='r')
#axs[3, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +0.0^o)$')
axs[3, 3].set_xlim([0,24])
axs[3, 3].set_ylim([0,37000])
    
axs[3, 4].plot(X1, qdc_beams[1] , c='r')
#axs[3, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +0.0^o)$')
axs[3, 4].set_xlim([0,24])
axs[3, 4].set_ylim([0,37000])

axs[3, 5].plot(X1, qdc_beams[9] , c='r')
#axs[3, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +0.0^o)$')
axs[3, 5].set_xlim([0,24])
axs[3, 5].set_ylim([0,37000])
    
axs[3, 6].plot(X1, qdc_beams[25] , c='r')
#axs[3, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +0.0^o)$')
axs[3, 6].set_xlim([0,24])
axs[3, 6].set_ylim([0,37000])
    
axs[4, 0].plot(X1, qdc_beams[38] , c='r')
#axs[4, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -12.5^o)$')
axs[4, 0].set_xlim([0,24])
axs[4, 0].set_ylim([0,37000])
    
axs[4, 1].plot(X1, qdc_beams[18] , c='r')
#axs[4, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -12.5^o)$')
axs[4, 1].set_xlim([0,24])
axs[4, 1].set_ylim([0,37000])
    
axs[4, 2].plot(X1, qdc_beams[6] , c='r')
#axs[4, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -12.5^o)$')
axs[4, 2].set_xlim([0,24])
axs[4, 2].set_ylim([0,37000])
   
axs[4, 3].plot(X1, qdc_beams[7] , c='r')
#axs[4, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -12.5^o)$')
axs[4, 3].set_xlim([0,24])
axs[4, 3].set_ylim([0,37000])
    
axs[4, 4].plot(X1, qdc_beams[8] , c='r')
#axs[4, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -12.5^o)$')
axs[4, 4].set_xlim([0,24])
axs[4, 4].set_ylim([0,37000])
    
axs[4, 5].plot(X1, qdc_beams[24] , c='r')
#axs[4, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -12.5^o)$')
axs[4, 5].set_xlim([0,24])
axs[4, 5].set_ylim([0,37000])
    
axs[4, 6].plot(X1, qdc_beams[48] , c='r')
#axs[4, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -12.5^o)$')
axs[4, 6].set_xlim([0,24])
axs[4, 6].set_ylim([0,37000])
  
axs[5, 0].plot(X1, qdc_beams[39] , c='r')
#axs[5, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -25.0^o)$')
axs[5, 0].set_xlim([0,24])
axs[5, 0].set_ylim([0,37000])
  
axs[5, 1].plot(X1, qdc_beams[19] , c='r')
#axs[5, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -25.0^o)$')
axs[5, 1].set_xlim([0,24])
axs[5, 1].set_ylim([0,37000])

axs[5, 2].plot(X1, qdc_beams[20] , c='r')
#axs[5, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -25.0^o)$')
axs[5, 2].set_xlim([0,24])
axs[5, 2].set_ylim([0,37000])

axs[5, 3].plot(X1, qdc_beams[21] , c='r')
#axs[5, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -25.0^o)$')
axs[5, 3].set_xlim([0,24])
axs[5, 3].set_ylim([0,37000])
  
axs[5, 4].plot(X1, qdc_beams[22] , c='r')
#axs[5, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -25.0^o)$')
axs[5, 4].set_xlim([0,24])
axs[5, 4].set_ylim([0,37000])
   
axs[5, 5].plot(X1, qdc_beams[23] , c='r')
#axs[5, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -25.0^o)$')
axs[5, 5].set_xlim([0,24])
axs[5, 5].set_ylim([0,37000])
   
axs[5, 6].plot(X1, qdc_beams[47] , c='r')
#axs[5, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -25.0^o)$')
axs[5, 6].set_xlim([0,24])
axs[5, 6].set_ylim([0,37000])
    
axs[6, 0].plot(X1, qdc_beams[40] , c='r')
#axs[6, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -37.5^o)$')
axs[6, 0].set_xlim([0,24])
axs[6, 0].set_ylim([0,37000])
    
axs[6, 1].plot(X1, qdc_beams[41] , c='r')
#axs[6, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -37.5^o)$')
axs[6, 1].set_xlim([0,24])
axs[6, 1].set_ylim([0,37000])
    
axs[6, 2].plot(X1, qdc_beams[42] , c='r')
#axs[6, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -37.5^o)$')
axs[6, 2].set_xlim([0,24])
axs[6, 2].set_ylim([0,37000])
   
axs[6, 3].plot(X1, qdc_beams[43] , c='r')
#axs[6, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -37.5^o)$')
axs[6, 3].set_xlim([0,24])
axs[6, 3].set_ylim([0,37000])
   
axs[6, 4].plot(X1, qdc_beams[44] , c='r')
#axs[6, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -37.5^o)$')
axs[6, 4].set_xlim([0,24])
axs[6, 4].set_ylim([0,37000])
    
axs[6, 5].plot(X1, qdc_beams[45] , c='r')
#axs[6, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -37.5^o)$')
axs[6, 5].set_xlim([0,24])
axs[6, 5].set_ylim([0,37000])
    
axs[6, 6].plot(X1, qdc_beams[46] , c='r')
#axs[6, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -37.5^o)$')
axs[6, 6].set_xlim([0,24])
axs[6, 6].set_ylim([0,37000])

#for ax in axs.flat:
#    ax.set(xlabel='Universal Time [h] (UTC)', ylabel='B. Temperature [K]')
#    ax.label_outer()

fig.text(0.5, 0.04, 'UTC from 00:00 to 23:59', ha='center')
fig.text(0.04, 0.5, 'Brightness temperature [K]', va='center', rotation='vertical')

savename= 'drift_curve_IRIS_38.2.png'
plt.savefig(savename)
plt.show()
plt.cla()
plt.clf()
plt.close('all')
plt.close(fig)
    
fig, axs = plt.subplots(7, 7, sharex=True, sharey=True)
fig.suptitle('Noise Power Quiet Day Curve (FWHM 25$^o$ at 38.2 MHz) on March 10, 2004')

axs[0, 0].plot(X1, pn_beams[34], c='r')
#axs[0, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +37.5^o)$')
axs[0, 0].set_xlim([0,24])
axs[0, 0].set_ylim([-140,-114])
    
axs[0, 1].plot(X1, pn_beams[33], c='r')
#axs[0, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +37.5^o)$')
axs[0, 1].set_xlim([0,24])
axs[0, 1].set_ylim([-140,-114])
    
axs[0, 2].plot(X1, pn_beams[32] , c='r')
#axs[0, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +37.5^o)$')
axs[0, 2].set_xlim([0,24])
axs[0, 2].set_ylim([-140,-114])
    
axs[0, 3].plot(X1, pn_beams[31] , c='r')
#axs[0, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +37.5^o)$')
axs[0, 3].set_xlim([0,24])
axs[0, 3].set_ylim([-140,-114])
    
axs[0, 4].plot(X1, pn_beams[30] , c='r')
#axs[0, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +37.5^o)$')
axs[0, 4].set_xlim([0,24])
axs[0, 4].set_ylim([-140,-114])
 
axs[0, 5].plot(X1, pn_beams[29] , c='r')
#axs[0, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +37.5^o)$')
axs[0, 5].set_xlim([0,24])
axs[0, 5].set_ylim([-140,-114])

axs[0, 6].plot(X1, pn_beams[28] , c='r')
#axs[0, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +37.5^o)$')
axs[0, 6].set_xlim([0,24])
axs[0, 6].set_ylim([-140,-114])

axs[1, 0].plot(X1, pn_beams[35] , c='r')
#axs[1, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +25.0^o)$')
axs[1, 0].set_xlim([0,24])
axs[1, 0].set_ylim([-140,-114])

axs[1, 1].plot(X1, pn_beams[15] , c='r')
#axs[1, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +25.0^o)$')
axs[1, 1].set_xlim([0,24])
axs[1, 1].set_ylim([-140,-114])

axs[1, 2].plot(X1, pn_beams[14] , c='r')
#axs[1, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +25.0^o)$')
axs[1, 2].set_xlim([0,24])
axs[1, 2].set_ylim([-140,-114])
    
axs[1, 3].plot(X1, pn_beams[13] , c='r')
#axs[1, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +25.0^o)$')
axs[1, 3].set_xlim([0,24])
axs[1, 3].set_ylim([-140,-114])
   
axs[1, 4].plot(X1, pn_beams[12] , c='r')
#axs[1, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +25.0^o)$')
axs[1, 4].set_xlim([0,24])
axs[1, 4].set_ylim([-140,-114])
    
axs[1, 5].plot(X1, pn_beams[11] , c='r')
#axs[1, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +25.0^o)$')
axs[1, 5].set_xlim([0,24])
axs[1, 5].set_ylim([-140,-114])

axs[1, 6].plot(X1, pn_beams[27] , c='r')
#axs[1, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +25.0^o)$')
axs[1, 6].set_xlim([0,24])
axs[1, 6].set_ylim([-140,-114])
    
axs[2, 0].plot(X1, pn_beams[36] , c='r')
#axs[2, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +12.5^o)$')
axs[2, 0].set_xlim([0,24])
axs[2, 0].set_ylim([-140,-114])
    
axs[2, 1].plot(X1, pn_beams[16] , c='r')
#axs[2, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +12.5^o)$')
axs[2, 1].set_xlim([0,24])
axs[2, 1].set_ylim([-140,-114])
    
axs[2, 2].plot(X1, pn_beams[4] , c='r')
#axs[2, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +12.5^o)$')
axs[2, 2].set_xlim([0,24])
axs[2, 2].set_ylim([-140,-114])
    
axs[2, 3].plot(X1, pn_beams[3] , c='r')
#axs[2, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +12.5^o)$')
axs[2, 3].set_xlim([0,24])
axs[2, 3].set_ylim([-140,-114])
    
axs[2, 4].plot(X1, pn_beams[2] , c='r')
#axs[2, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +12.5^o)$')
axs[2, 4].set_xlim([0,24])
axs[2, 4].set_ylim([-140,-114])
    
axs[2, 5].plot(X1, pn_beams[10] , c='r')
#axs[2, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +12.5^o)$')
axs[2, 5].set_xlim([0,24])
axs[2, 5].set_ylim([-140,-114])

axs[2, 6].plot(X1, pn_beams[26] , c='r')
#axs[2, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +12.5^o)$')
axs[2, 6].set_xlim([0,24])
axs[2, 6].set_ylim([-140,-114])
    
axs[3, 0].plot(X1, pn_beams[37] , c='r')
#axs[3, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, +0.0^o)$')
axs[3, 0].set_xlim([0,24])
axs[3, 0].set_ylim([-140,-114])

axs[3, 1].plot(X1, pn_beams[17] , c='r')
#axs[3, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, +0.0^o)$')
axs[3, 1].set_xlim([0,24])
axs[3, 1].set_ylim([-140,-114])
    
axs[3, 2].plot(X1, pn_beams[5] , c='r')
#axs[3, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +0.0^o)$')
axs[3, 2].set_xlim([0,24])
axs[3, 2].set_ylim([-140,-114])
    
axs[3, 3].plot(X1, pn_beams[0] , c='r')
#axs[3, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, +0.0^o)$')
axs[3, 3].set_xlim([0,24])
axs[3, 3].set_ylim([-140,-114])
    
axs[3, 4].plot(X1, pn_beams[1] , c='r')
#axs[3, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +0.0^o)$')
axs[3, 4].set_xlim([0,24])
axs[3, 4].set_ylim([-140,-114])

axs[3, 5].plot(X1, pn_beams[9] , c='r')
#axs[3, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, +0.0^o)$')
axs[3, 5].set_xlim([0,24])
axs[3, 5].set_ylim([-140,-114])
  
axs[3, 6].plot(X1, pn_beams[25] , c='r')
#axs[3, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, +0.0^o)$')
axs[3, 6].set_xlim([0,24])
axs[3, 6].set_ylim([-140,-114])
    
axs[4, 0].plot(X1, pn_beams[38] , c='r')
#axs[4, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -12.5^o)$')
axs[4, 0].set_xlim([0,24])
axs[4, 0].set_ylim([-140,-114])
    
axs[4, 1].plot(X1, pn_beams[18] , c='r')
#axs[4, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -12.5^o)$')
axs[4, 1].set_xlim([0,24])
axs[4, 1].set_ylim([-140,-114])
    
axs[4, 2].plot(X1, pn_beams[6] , c='r')
#axs[4, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -12.5^o)$')
axs[4, 2].set_xlim([0,24])
axs[4, 2].set_ylim([-140,-114])
    
axs[4, 3].plot(X1, pn_beams[7] , c='r')
#axs[4, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -12.5^o)$')
axs[4, 3].set_xlim([0,24])
axs[4, 3].set_ylim([-140,-114])
  
axs[4, 4].plot(X1, pn_beams[8] , c='r')
#axs[4, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -12.5^o)$')
axs[4, 4].set_xlim([0,24])
axs[4, 4].set_ylim([-140,-114])
    
axs[4, 5].plot(X1, pn_beams[24] , c='r')
#axs[4, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -12.5^o)$')
axs[4, 5].set_xlim([0,24])
axs[4, 5].set_ylim([-140,-114])
   
axs[4, 6].plot(X1, pn_beams[48] , c='r')
#axs[4, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -12.5^o)$')
axs[4, 6].set_xlim([0,24])
axs[4, 6].set_ylim([-140,-114])
    
axs[5, 0].plot(X1, pn_beams[39] , c='r')
#axs[5, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -25.0^o)$')
axs[5, 0].set_xlim([0,24])
axs[5, 0].set_ylim([-140,-114])
    
axs[5, 1].plot(X1, pn_beams[19] , c='r')
#axs[5, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -25.0^o)$')
axs[5, 1].set_xlim([0,24])
axs[5, 1].set_ylim([-140,-114])

axs[5, 2].plot(X1, pn_beams[20] , c='r')
#axs[5, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -25.0^o)$')
axs[5, 2].set_xlim([0,24])
axs[5, 2].set_ylim([-140,-114])

axs[5, 3].plot(X1, pn_beams[21] , c='r')
#axs[5, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -25.0^o)$')
axs[5, 3].set_xlim([0,24])
axs[5, 3].set_ylim([-140,-114])

axs[5, 4].plot(X1, pn_beams[22] , c='r')
#axs[5, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -25.0^o)$')
axs[5, 4].set_xlim([0,24])
axs[5, 4].set_ylim([-140,-114])
    
axs[5, 5].plot(X1, pn_beams[23] , c='r')
#axs[5, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -25.0^o)$')
axs[5, 5].set_xlim([0,24])
axs[5, 5].set_ylim([-140,-114])
    
axs[5, 6].plot(X1, pn_beams[47] , c='r')
#axs[5, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -25.0^o)$')
axs[5, 6].set_xlim([0,24])
axs[5, 6].set_ylim([-140,-114])
    
axs[6, 0].plot(X1, pn_beams[40] , c='r')
#axs[6, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+37.5^o, -37.5^o)$')
axs[6, 0].set_xlim([0,24])
axs[6, 0].set_ylim([-140,-114])
    
axs[6, 1].plot(X1, pn_beams[41] , c='r')
#axs[6, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+25.0^o, -37.5^o)$')
axs[6, 1].set_xlim([0,24])
axs[6, 1].set_ylim([-140,-114])
    
axs[6, 2].plot(X1, pn_beams[42] , c='r')
#axs[6, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -37.5^o)$')
axs[6, 2].set_xlim([0,24])
axs[6, 2].set_ylim([-140,-114])
    
axs[6, 3].plot(X1, pn_beams[43] , c='r')
#axs[6, 3].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+0.0^o, -37.5^o)$')
axs[6, 3].set_xlim([0,24])
axs[6, 3].set_ylim([-140,-114])
    
axs[6, 4].plot(X1, pn_beams[44] , c='r')
#axs[6, 4].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -37.5^o)$')
axs[6, 4].set_xlim([0,24])
axs[6, 4].set_ylim([-140,-114])
    
axs[6, 5].plot(X1, pn_beams[45] , c='r')
#axs[6, 5].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-25.0^o, -37.5^o)$')
axs[6, 5].set_xlim([0,24])
axs[6, 5].set_ylim([-140,-114])
    
axs[6, 6].plot(X1, pn_beams[46] , c='r')
#axs[6, 6].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-37.5^o, -37.5^o)$')
axs[6, 6].set_xlim([0,24])
axs[6, 6].set_ylim([-140,-114])
    
#for ax in axs.flat:
#    ax.set(xlabel='Universal Time [h] (UTC)', ylabel='Noise P. [W]')
#    ax.label_outer()
fig.text(0.5, 0.04, 'UTC from 00:00 to 23:59', ha='center')
fig.text(0.04, 0.5, 'Noise power [dBm]', va='center', rotation='vertical')

savename2= 'noise_power_curve_IRIS_38.2MHz.png'
plt.savefig(savename2)
plt.show()
plt.cla()
plt.clf()
plt.close('all')
plt.close(fig)
    
grid= np.zeros((7,7))
time=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45', '24:00']
for i in range(len(qdc_beams[0])):
    grid[0,0]=qdc_beams[34][i]
    grid[0,1]=qdc_beams[33][i]
    grid[0,2]=qdc_beams[32][i]
    grid[0,3]=qdc_beams[31][i]
    grid[0,4]=qdc_beams[30][i]
    grid[0,5]=qdc_beams[29][i]
    grid[0,6]=qdc_beams[28][i]
    grid[1,0]=qdc_beams[35][i]
    grid[1,1]=qdc_beams[15][i]
    grid[1,2]=qdc_beams[14][i]
    grid[1,3]=qdc_beams[13][i]
    grid[1,4]=qdc_beams[12][i]
    grid[1,5]=qdc_beams[11][i]
    grid[1,6]=qdc_beams[27][i]
    grid[2,0]=qdc_beams[36][i]
    grid[2,1]=qdc_beams[16][i]
    grid[2,2]=qdc_beams[4][i]
    grid[2,3]=qdc_beams[3][i]
    grid[2,4]=qdc_beams[2][i]
    grid[2,5]=qdc_beams[10][i]
    grid[2,6]=qdc_beams[26][i]
    grid[3,0]=qdc_beams[37][i]
    grid[3,1]=qdc_beams[17][i]
    grid[3,2]=qdc_beams[5][i]
    grid[3,3]=qdc_beams[0][i]
    grid[3,4]=qdc_beams[1][i]
    grid[3,5]=qdc_beams[9][i]
    grid[3,6]=qdc_beams[25][i]
    grid[4,0]=qdc_beams[38][i]
    grid[4,1]=qdc_beams[18][i]
    grid[4,2]=qdc_beams[6][i]
    grid[4,3]=qdc_beams[7][i]
    grid[4,4]=qdc_beams[8][i]
    grid[4,5]=qdc_beams[24][i]
    grid[4,6]=qdc_beams[48][i]
    grid[5,0]=qdc_beams[39][i]
    grid[5,1]=qdc_beams[19][i]
    grid[5,2]=qdc_beams[20][i]
    grid[5,3]=qdc_beams[21][i]
    grid[5,4]=qdc_beams[22][i]
    grid[5,5]=qdc_beams[23][i]
    grid[5,6]=qdc_beams[47][i]
    grid[6,0]=qdc_beams[40][i]
    grid[6,1]=qdc_beams[41][i]
    grid[6,2]=qdc_beams[42][i]
    grid[6,3]=qdc_beams[43][i]
    grid[6,4]=qdc_beams[44][i]
    grid[6,5]=qdc_beams[45][i]
    grid[6,6]=qdc_beams[46][i]
     
    plt.figure(figsize=(7,5))
    plt.imshow(grid, cmap='viridis', extent=[50.0,-50.0,-50.0,50.0])
    plt.title(str(time[i]))
    plt.xlabel('$\Delta$ RA (deg)')
    plt.ylabel('$\Delta$ Dec (deg)')
    plt.colorbar().set_label('Brightness temperature [K]', rotation= 270, labelpad=15)
    plt.clim(vmin=7800, vmax=30800)
    plt.savefig('38.2MHz_AP_SYN_CRN'+str(i)+'_'+str(X1[i])+'.png')
    plt.cla()
    plt.clf()
    plt.close('all')
    plt.close(fig)
        
grid2= np.zeros((7,7))
for i in range(len(qdc_beams[0])):
    grid2[0,0]= pn_beams[34][i]
    grid2[0,1]= pn_beams[33][i]
    grid2[0,2]= pn_beams[32][i]
    grid2[0,3]= pn_beams[31][i]
    grid2[0,4]= pn_beams[30][i]
    grid2[0,5]= pn_beams[29][i]
    grid2[0,6]= pn_beams[28][i]
    grid2[1,0]= pn_beams[35][i]
    grid2[1,1]= pn_beams[15][i]
    grid2[1,2]= pn_beams[14][i]
    grid2[1,3]= pn_beams[13][i]
    grid2[1,4]= pn_beams[12][i]
    grid2[1,5]= pn_beams[11][i]
    grid2[1,6]= pn_beams[27][i]
    grid2[2,0]= pn_beams[36][i]
    grid2[2,1]= pn_beams[16][i]
    grid2[2,2]= pn_beams[4][i]
    grid2[2,3]= pn_beams[3][i]
    grid2[2,4]= pn_beams[2][i]
    grid2[2,5]= pn_beams[10][i]
    grid2[2,6]= pn_beams[26][i]
    grid2[3,0]= pn_beams[37][i]
    grid2[3,1]= pn_beams[17][i]
    grid2[3,2]= pn_beams[5][i]
    grid2[3,3]= pn_beams[0][i]
    grid2[3,4]= pn_beams[1][i]
    grid2[3,5]= pn_beams[9][i]
    grid2[3,6]= pn_beams[25][i]
    grid2[4,0]= pn_beams[38][i]
    grid2[4,1]= pn_beams[18][i]
    grid2[4,2]= pn_beams[6][i]
    grid2[4,3]= pn_beams[7][i]
    grid2[4,4]= pn_beams[8][i]
    grid2[4,5]= pn_beams[24][i]
    grid2[4,6]= pn_beams[48][i]
    grid2[5,0]= pn_beams[39][i]
    grid2[5,1]= pn_beams[19][i]
    grid2[5,2]= pn_beams[20][i]
    grid2[5,3]= pn_beams[21][i]
    grid2[5,4]= pn_beams[22][i]
    grid2[5,5]= pn_beams[23][i]
    grid2[5,6]= pn_beams[47][i]
    grid2[6,0]= pn_beams[40][i]
    grid2[6,1]= pn_beams[41][i]
    grid2[6,2]= pn_beams[42][i]
    grid2[6,3]= pn_beams[43][i]
    grid2[6,4]= pn_beams[44][i]
    grid2[6,5]= pn_beams[45][i]
    grid2[6,6]= pn_beams[46][i]
    plt.figure(figsize=(7,5))
    plt.imshow(grid2, cmap='magma', extent=[50.0,-50.0,-50.0,50.0])
    plt.title(str(time[i]))
    plt.xlabel('$\Delta$ RA (deg)')
    plt.ylabel('$\Delta$ Dec (deg)')
    plt.colorbar().set_label('Noise Power [dBm]', rotation= 270, labelpad=15)
    plt.clim(vmin=-140, vmax=-114)
    plt.savefig('38.2MHz_POWER_AP_SYN_CRN'+str(i)+'_'+str(X1[i])+'.png')    
    plt.cla()
    plt.clf()
    plt.close('all')
    plt.close(fig)
