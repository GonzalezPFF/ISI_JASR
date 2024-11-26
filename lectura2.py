#%%
import numpy as np 
#import matplotlib.pyplot as plt
#import healpy as hp
#from scipy.stats import scoreatpercentile as percentile

#%%
data_30 = np.genfromtxt('output-30.dat')
data_30_5= np.genfromtxt('output-30_5.dat')
data_31 = np.genfromtxt('output-31.dat')
data_31_5= np.genfromtxt('output-31_5.dat')
data_32 = np.genfromtxt('output-32.dat')
data_32_5= np.genfromtxt('output-32_5.dat')
data_33 = np.genfromtxt('output-33.dat')
data_33_5= np.genfromtxt('output-33_5.dat')
data_34 = np.genfromtxt('output-34.dat')
data_34_5= np.genfromtxt('output-34_5.dat')
data_35 = np.genfromtxt('output-35.dat')
data_35_5= np.genfromtxt('output-35_5.dat')
data_36 = np.genfromtxt('output-36.dat')
data_36_5= np.genfromtxt('output-36_5.dat')
data_37 = np.genfromtxt('output-37.dat')
data_37_5= np.genfromtxt('output-37_5.dat')
data_38 = np.genfromtxt('output-38.dat')
data_38_5= np.genfromtxt('output-38_5.dat')
data_39 = np.genfromtxt('output-39.dat')
data_39_5= np.genfromtxt('output-39_5.dat')
data_40 = np.genfromtxt('output-40.dat')
data_40_5= np.genfromtxt('output-40_5.dat')
data_41 = np.genfromtxt('output-41.dat')
data_41_5= np.genfromtxt('output-41_5.dat')
data_42 = np.genfromtxt('output-42.dat')
data_42_5= np.genfromtxt('output-42_5.dat')
data_43 = np.genfromtxt('output-43.dat')
data_43_5= np.genfromtxt('output-43_5.dat')
data_44 = np.genfromtxt('output-44.dat')
data_44_5= np.genfromtxt('output-44_5.dat')
data_45 = np.genfromtxt('output-45.dat')

data_38_2= np.genfromtxt('output-38_2.dat')

T_30= data_30[0:]
T_30_5= data_30_5[0:]
T_31= data_31[0:]
T_31_5= data_31_5[0:]
T_32= data_32[0:]
T_32_5= data_32_5[0:]
T_33= data_33[0:]
T_33_5= data_33_5[0:]
T_34= data_34[0:]
T_34_5= data_34_5[0:]
T_35= data_35[0:]
T_35_5= data_35_5[0:]
T_36= data_36[0:]
T_36_5= data_36_5[0:]
T_37= data_37[0:]
T_37_5= data_37_5[0:]
T_38= data_38[0:]
T_38_5= data_38_5[0:]
T_39= data_39[0:]
T_39_5= data_39_5[0:]
T_40= data_40[0:]
T_40_5= data_40_5[0:]
T_41= data_41[0:]
T_41_5= data_41_5[0:]
T_42= data_42[0:]
T_42_5= data_42_5[0:]
T_43= data_43[0:]
T_43_5= data_43_5[0:]
T_44= data_44[0:]
T_44_5= data_44_5[0:]
T_45= data_45[0:]

T_38_2= data_38_2[0:]


prom_30= np.mean(T_30)
max_30= np.max(T_30)
min_30= np.min(T_30)
std_30= np.std(T_30)

prom_30_5= np.mean(T_30_5)
max_30_5= np.max(T_30_5)
min_30_5= np.min(T_30_5)
std_30_5= np.std(T_30_5)

prom_31= np.mean(T_31)
max_31= np.max(T_31)
min_31= np.min(T_31)
std_31= np.std(T_31)

prom_31_5= np.mean(T_31_5)
max_31_5= np.max(T_31_5)
min_31_5= np.min(T_31_5)
std_31_5= np.std(T_31_5)

prom_32= np.mean(T_32)
max_32= np.max(T_32)
min_32= np.min(T_32)
std_32= np.std(T_32)

prom_32_5= np.mean(T_32_5)
max_32_5= np.max(T_32_5)
min_32_5= np.min(T_32_5)
std_32_5= np.std(T_32_5)

prom_33= np.mean(T_33)
max_33= np.max(T_33)
min_33= np.min(T_33)
std_33= np.std(T_33)

prom_33_5= np.mean(T_33_5)
max_33_5= np.max(T_33_5)
min_33_5= np.min(T_33_5)
std_33_5= np.std(T_33_5)

prom_34= np.mean(T_34)
max_34= np.max(T_34)
min_34= np.min(T_34)
std_34= np.std(T_34)

prom_34_5= np.mean(T_34_5)
max_34_5= np.max(T_34_5)
min_34_5= np.min(T_34_5)
std_34_5= np.std(T_34_5)

prom_35= np.mean(T_35)
max_35= np.max(T_35)
min_35= np.min(T_35)
std_35= np.std(T_35)

prom_35_5= np.mean(T_35_5)
max_35_5= np.max(T_35_5)
min_35_5= np.min(T_35_5)
std_35_5= np.std(T_35_5)

prom_36= np.mean(T_36)
max_36= np.max(T_36)
min_36= np.min(T_36)
std_36= np.std(T_36)

prom_36_5= np.mean(T_36_5)
max_36_5= np.max(T_36_5)
min_36_5= np.min(T_36_5)
std_36_5= np.std(T_36_5)

prom_37= np.mean(T_37)
max_37= np.max(T_37)
min_37= np.min(T_37)
std_37= np.std(T_37)

prom_37_5= np.mean(T_37_5)
max_37_5= np.max(T_37_5)
min_37_5= np.min(T_37_5)
std_37_5= np.std(T_37_5)

prom_38= np.mean(T_38)
max_38= np.max(T_38)
min_38= np.min(T_38)
std_38= np.std(T_38)

prom_38_5= np.mean(T_38_5)
max_38_5= np.max(T_38_5)
min_38_5= np.min(T_38_5)
std_38_5= np.std(T_38_5)

prom_39= np.mean(T_39)
max_39= np.max(T_39)
min_39= np.min(T_39)
std_39= np.std(T_39)

prom_39_5= np.mean(T_39_5)
max_39_5= np.max(T_39_5)
min_39_5= np.min(T_39_5)
std_39_5= np.std(T_39_5)

prom_40= np.mean(T_40)
max_40= np.max(T_40)
min_40= np.min(T_40)
std_40= np.std(T_40)

prom_40_5= np.mean(T_40_5)
max_40_5= np.max(T_40_5)
min_40_5= np.min(T_40_5)
std_40_5= np.std(T_40_5)

prom_41= np.mean(T_41)
max_41= np.max(T_41)
min_41= np.min(T_41)
std_41= np.std(T_41)

prom_41_5= np.mean(T_41_5)
max_41_5= np.max(T_41_5)
min_41_5= np.min(T_41_5)
std_41_5= np.std(T_41_5)

prom_42= np.mean(T_42)
max_42= np.max(T_42)
min_42= np.min(T_42)
std_42= np.std(T_42)

prom_42_5= np.mean(T_42_5)
max_42_5= np.max(T_42_5)
min_42_5= np.min(T_42_5)
std_42_5= np.std(T_42_5)

prom_43= np.mean(T_43)
max_43= np.max(T_43)
min_43= np.min(T_43)
std_43= np.std(T_43)

prom_43_5= np.mean(T_43_5)
max_43_5= np.max(T_43_5)
min_43_5= np.min(T_43_5)
std_43_5= np.std(T_43_5)

prom_44= np.mean(T_44)
max_44= np.max(T_44)
min_44= np.min(T_44)
std_44= np.std(T_44)

prom_44_5= np.mean(T_44_5)
max_44_5= np.max(T_44_5)
min_44_5= np.min(T_44_5)
std_44_5= np.std(T_44_5)

prom_45= np.mean(T_45)
max_45= np.max(T_45)
min_45= np.min(T_45)
std_45= np.std(T_45)


prom_38_2= np.mean(T_38_2)
max_38_2= np.max(T_38_2)
min_38_2= np.max(T_38_2)
std_38_2= np.std(T_38_2)


IDs=np.arange(0,len(data_30),1)

#%% Array construction
col_0= [] #ID
col_1= [] #T30
col_2= [] #T30.5
col_3= [] #T31
col_4= [] #T31.5
col_5= [] #T32
col_6= [] #T32.5
col_7= [] #T33
col_8= [] #T33.5
col_9= [] #T34
col_10= [] #T34.5
col_11= [] #T35
col_12= [] #T35.5
col_13= [] #T36
col_14= [] #T36.5
col_15= [] #T37
col_16= [] #T37.5
col_17= [] #T38
col_18= [] #T38.5
col_19= [] #T39
col_20= [] #T39.5
col_21= [] #T40
col_22= [] #T40.5
col_23= [] #T41
col_24= [] #T41.5
col_25= [] #T42
col_26= [] #T42.5
col_27= [] #T43
col_28= [] #T43.5
col_29= [] #T44
col_30= [] #T44.5
col_31= [] #T45

col_add= [] #T38.2

for i in range(len(IDs)):
    col_0.append(IDs[i])
    col_1.append(T_30[i])
    col_2.append(T_30_5[i])
    col_3.append(T_31[i])
    col_4.append(T_31_5[i])
    col_5.append(T_32[i])
    col_6.append(T_32_5[i])
    col_7.append(T_33[i])
    col_8.append(T_33_5[i])
    col_9.append(T_34[i])
    col_10.append(T_34_5[i])
    col_11.append(T_35[i])
    col_12.append(T_35_5[i])
    col_13.append(T_36[i])
    col_14.append(T_36_5[i])
    col_15.append(T_37[i])
    col_16.append(T_37_5[i])
    col_17.append(T_38[i])
    col_18.append(T_38_5[i])
    col_19.append(T_39[i])
    col_20.append(T_39_5[i])
    col_21.append(T_40[i])
    col_22.append(T_40_5[i])
    col_23.append(T_41[i])
    col_24.append(T_41_5[i])
    col_25.append(T_42[i])
    col_26.append(T_42_5[i])
    col_27.append(T_43[i])
    col_28.append(T_43_5[i])
    col_29.append(T_44[i])
    col_30.append(T_44_5[i])
    col_31.append(T_45[i])
    
    col_add.append(T_38_2[i])

col_0_resh= np.array(col_0).reshape(1, len(IDs))
col_1_resh= np.array(col_1).reshape(1, len(IDs))
col_2_resh= np.array(col_2).reshape(1, len(IDs))
col_3_resh= np.array(col_3).reshape(1, len(IDs))
col_4_resh= np.array(col_4).reshape(1, len(IDs))
col_5_resh= np.array(col_5).reshape(1, len(IDs))
col_6_resh= np.array(col_6).reshape(1, len(IDs))
col_7_resh= np.array(col_7).reshape(1, len(IDs))
col_8_resh= np.array(col_8).reshape(1, len(IDs))
col_9_resh= np.array(col_9).reshape(1, len(IDs))
col_10_resh= np.array(col_10).reshape(1, len(IDs))
col_11_resh= np.array(col_11).reshape(1, len(IDs))
col_12_resh= np.array(col_12).reshape(1, len(IDs))
col_13_resh= np.array(col_13).reshape(1, len(IDs))
col_14_resh= np.array(col_14).reshape(1, len(IDs))
col_15_resh= np.array(col_15).reshape(1, len(IDs))
col_16_resh= np.array(col_16).reshape(1, len(IDs))
col_17_resh= np.array(col_17).reshape(1, len(IDs))
col_18_resh= np.array(col_18).reshape(1, len(IDs))
col_19_resh= np.array(col_19).reshape(1, len(IDs))
col_20_resh= np.array(col_20).reshape(1, len(IDs))
col_21_resh= np.array(col_21).reshape(1, len(IDs))
col_22_resh= np.array(col_22).reshape(1, len(IDs))
col_23_resh= np.array(col_23).reshape(1, len(IDs))
col_24_resh= np.array(col_24).reshape(1, len(IDs))
col_25_resh= np.array(col_25).reshape(1, len(IDs))
col_26_resh= np.array(col_26).reshape(1, len(IDs))
col_27_resh= np.array(col_27).reshape(1, len(IDs))
col_28_resh= np.array(col_28).reshape(1, len(IDs))
col_29_resh= np.array(col_29).reshape(1, len(IDs))
col_30_resh= np.array(col_30).reshape(1, len(IDs))
col_31_resh= np.array(col_31).reshape(1, len(IDs))


col_add_resh= np.array(col_add).reshape(1, len(IDs))


array= np.concatenate((col_0_resh, col_1_resh, col_2_resh, col_3_resh, col_4_resh, col_5_resh, col_6_resh, col_7_resh, col_8_resh, col_9_resh, col_10_resh, col_11_resh, col_12_resh, col_13_resh, col_14_resh, col_15_resh, col_16_resh, col_17_resh, col_18_resh, col_19_resh, col_20_resh, col_21_resh, col_22_resh, col_23_resh, col_24_resh, col_25_resh, col_26_resh, col_27_resh, col_28_resh, col_29_resh, col_30_resh, col_31_resh)).T 
array2= np.concatenate((col_0_resh, col_add_resh)).T
#%% Saving database
np.savetxt('latlong_temps_NOLATLONG_V2_FREQUENCIES.txt', array, delimiter=',')
np.savetxt('latlong_temps_NOLATLONG_V2.txt', array2, delimiter=',')
#%%
#%% Plots
#plt.figure(figsize=(10,10))
#plt.plot(IDs,T_30, '.', c='r', label='30 MHz')
#plt.plot(IDs,T_38, '.', c='y', label='38 MHz')
#plt.plot(IDs, T_38_2, '.', C='g', label='38.2 MHz')
#plt.plot(IDs,T_45, '.', c='b', label='45 MHz')
#plt.xlabel('ID')
#plt.ylabel('T[K]')
#plt.legend(loc='best')

#%%
#plt.figure(figsize=(7,5))
#plt.hist(T_30, bins=100, alpha=0.5, color='r', label='30 MHz')
#plt.hist(T_38, bins=100, alpha=0.5, color='y', label='38 MHz')
#plt.hist(T_38_2, bins=100, color='g', label='38.2 MHz')
#plt.hist(T_45, bins=100, alpha=0.5, color='b', label='45 MHz')
#plt.xlabel('T[K]')
#plt.ylabel('#')
#plt.legend(loc='best')

#%% MOLLWEIDE PROJECTION 38.2 MHz
#vmin = percentile(T_38_2, 0)
#vmax = percentile(T_38_2, 100)
#hp.visufunc.mollview(T_38_2, title='LFSM @ 38.2 MHz', notext=True, min=vmin, max=vmax, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

#%% DATA FINDING AROUND A LAT/LONG POSITION
# QDC-Temperatures MARCH 10-29, 2004; 
# Selected plots March 17, 19, 23,25 and 26 

#nside=hp.npix2nside(len(T_38_2))
#T_zenith= T_38_2
# March 10; data've been taken during 21:00:00 MARCH 9 to 20:00:00 (1 hour intervale,
#Santiago -3h; equivalent in UTC: 00:00 to 23:00)
#QDC_Ts_M10= []
#lat_zenith_list_M10= [(180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317)]
#long_zenith_list_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383]

#lat_zenith_list_M10= [(180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333)]
#long_zenith_list_M10= [95.9439, 110.9852, 126.0263, 141.0673, 156.1083, 171.1494, -173.8098, -158.7685, -143.7273, -128.6863, -113.6454, -98.6042, -83.5633, -68.5225, -53.4810, -38.4398, -23.3990, -8.3577, 6.6833, 21.7258, 36.7652, 51.8065, 66.8475, 81.8883 ]
#110.0017, 125.0429, 140.08, 155.1260, 170.1633, -174.8017, -159.7521, -144.7108, -129.6704, -114.6342, -99.5883, -84.5483, -69.5058, -54.4750, -39.4242, -24.3833, -9.3350, 5.6742, 20.7246, 35.7746, 50.8250, 65.8608, 80.9016

#for i in range(len(lat_zenith_list_M10)):
#    lat_zenith_M10= lat_zenith_list_M10[i]
#    long_zenith_M10= long_zenith_list_M10[i]
#    vec_zenith_M10=hp.ang2vec(np.radians(lat_zenith_M10), np.radians(long_zenith_M10))
#    ipix_disc_zenith_M10= hp.query_disc(nside=nside, vec=vec_zenith_M10, radius=np.radians(25))
#    mean_zenith_M10= np.mean(T_zenith[ipix_disc_zenith_M10])
#    QDC_Ts_M10.append(mean_zenith_M10)

# March 11; 20:56:04 MARCH 10 to 19:56:04 SANTIAGO TIME (-3h); 1h intervale
#QDC_Ts_M11=[]
#lat_zenith_list_M11= [(180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333), (180-36.8333)]
#long_zenith_list_M11= [95.9583, 109.9992, 125.04, 140.0813, 155.1242, 170.16333, -174.7954, -159.75, -144.7133, -129.6725, -114.6312, -99.5904, -84.5496, -69.5083, -54.4667, -39.4258, -24.3850, -9.3438, 5.6971, 20.7383, 35.7796, 50.8333, 65.8613, 80.9025]

#for i in range(len(lat_zenith_list_M11)):
#    lat_zenith_M11= lat_zenith_list_M11[i]
#    long_zenith_M11= long_zenith_list_M11[i]
#    vec_zenith_M11=hp.ang2vec(np.radians(lat_zenith_M11), np.radians(long_zenith_M11))
#    ipix_disc_zenith_M11= hp.query_disc(nside=nside, vec=vec_zenith_M11, radius=np.radians(25))
#    mean_zenith_M11= np.mean(T_zenith[ipix_disc_zenith_M11])
#    QDC_Ts_M11.append(mean_zenith_M11)

#X= np.linspace(0, 23, len(QDC_Ts_M10))

#plt.figure(figsize=(7,5))
#plt.plot(X, QDC_Ts_M10, label='March 10')
#plt.plot(X, QDC_Ts_M11, label='March 11 (-3m 56s)')
#plt.xlabel('Universal Time [h] (UTC)')
#plt.ylabel('Temperature [K] (Zenith 25$^o$ integrated)')
#plt.title('Brightness Temperature Day Curves (38.2 MHz) on March, 2004')
#plt.legend(loc='best')
#plt.show()

#MARCH 10 LIST ERASER: (180-36.8372) 21:00 santiago -3; (180-36.8323) 22:00 santiago -3; (180-36.8329) 23:00 santiago -3
#                      95.9371 21:00 santiago -3; 110.9875 22:00 santiago -3; 126.0246 23:00 santiago -3
#%% TRIAL



