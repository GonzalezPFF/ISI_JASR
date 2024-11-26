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

#%% DATA LOADING
data_all= np.loadtxt('latlong_temps_NOLATLONG_V2_FREQUENCIES.txt',delimiter=',')
data_38_2MHz= np.loadtxt('latlong_temps_NOLATLONG_V2.txt',delimiter=',')

IDs= data_all[:, 0]
IDs_resh= np.array(IDs).reshape(1, len(IDs))

T_30= data_all[:, 1]
T_30_5= data_all[:, 2]
T_31= data_all[:, 3]
T_31_5= data_all[:, 4]
T_32= data_all[:, 5]
T_32_5= data_all[:, 6]
T_33= data_all[:, 7]
T_33_5= data_all[:, 8]
T_34= data_all[:, 9]
T_34_5= data_all[:, 10]
T_35= data_all[:, 11]
T_35_5= data_all[:, 12]
T_36= data_all[:, 13]
T_36_5= data_all[:, 14]
T_37= data_all[:, 15]
T_37_5= data_all[:, 16]
T_38= data_all[:, 17]
T_38_5= data_all[:, 18]
T_39= data_all[:, 19]
T_39_5= data_all[:, 20]
T_40= data_all[:, 21]
T_40_5= data_all[:, 22]
T_41= data_all[:, 23]
T_41_5= data_all[:, 24]
T_42= data_all[:, 25]
T_42_5= data_all[:, 26]
T_43= data_all[:, 27]
T_43_5= data_all[:, 28]
T_44= data_all[:, 29]
T_44_5= data_all[:, 30]
T_45= data_all[:, 31]

T_38_2= data_38_2MHz[:, 1]

#%% MOLLWEIDE PROJECTION 38.2 MHz
vmin = percentile(T_38_2, 0)
vmax = percentile(T_38_2, 100)
hp.visufunc.mollview(T_38_2, title='LFSM @ 38.2 MHz', notext=True, min=vmin, max=vmax, unit='K', xsize=1000, format='%.3f')

T_38_2_smoothed = hp.smoothing(T_38_2, fwhm=np.radians(25.)) # ME SMOOTHEA EL MAPA COMPLETO DE ACUERDO AL FWHM DEL BEAM
vmin_smoothed = percentile(T_38_2_smoothed, 0)
vmax_smoothed= percentile(T_38_2_smoothed, 100)
hp.visufunc.mollview(T_38_2_smoothed,  title='LFSM @ 38.2 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
hp.graticule(color='k')
plt.show()

#%% DATA FINDING AROUND A LAT/LONG POSITION
nside=hp.npix2nside(len(T_38_2))
T_zenith= T_38_2_smoothed
# March 10; data've been taken during 21:00:00 MARCH 9 to 21:00:00 MARCH 10 (15 min intervale,
#Santiago -3h; equivalent in UTC: 00:00 to 24:00)
QDC_Ts_38_2_M10= []
#lat_zenith_list_M10= [(180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317)]
lat_zenith_list_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
long_zenith_list_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]

for i in range(len(lat_zenith_list_M10)):
    lat_zenith_M10= lat_zenith_list_M10[i]
    long_zenith_M10= long_zenith_list_M10[i]
    vec_zenith_M10=hp.ang2vec(np.radians(lat_zenith_M10), np.radians(long_zenith_M10)) #ME GENERA EL VECTOR QUE APUNTA HACIA UNA DETERMINADA POSICION DEL MAPA
    ipix_disc_zenith_M10= hp.query_disc(nside=nside, vec=vec_zenith_M10, radius=np.radians(25.)) #ME GENERA UN DISCO SOLIDO ALREDEDOR DEL PUNTO SENALADO POR EL VECTOR DEL TAMANO SOLICITADO, EN ESTE CASO FWHM=25.
    mean_zenith_M10= np.mean(T_zenith[ipix_disc_zenith_M10])
    QDC_Ts_38_2_M10.append(mean_zenith_M10)
    
#%% PLOT BTC
X1= np.linspace(0, 24, len(QDC_Ts_38_2_M10)) #UTC
X1_resh= np.array(X1).reshape(1, len(X1))

plt.figure(figsize=(7,5))
plt.plot(X1, QDC_Ts_38_2_M10, c='g')
plt.xlim(0,24)
plt.ylim(0,57000)
plt.xlabel('Universal Time [h] (UTC)')
plt.ylabel('Brightness Temperature [K] (FWHM 25$^o$)')
plt.title('Brightness Temperature Day Curve (38.2 MHz) on March 10, 2004')
plt.show()

#%% STATS
max_MZ_M10_38_2_MHz= np.max(QDC_Ts_38_2_M10)
place_max_38_2= np.where(QDC_Ts_38_2_M10==max_MZ_M10_38_2_MHz)
peak_h_MZ_M10_38_2_MHz= X1[place_max_38_2]
print('Valor maximo QDCT 38_2: ', peak_h_MZ_M10_38_2_MHz, 'h', ' con Tb = ', max_MZ_M10_38_2_MHz)

#%% MOLLWEIDE PROJ 30-45 MHz
T_30_smoothed = hp.smoothing(T_30, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_30_smoothed, 0)
#vmax_smoothed= percentile(T_30_smoothed, 100)
#hp.visufunc.mollview(T_30_smoothed,  title='LFSM @ 30 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_30_5_smoothed = hp.smoothing(T_30_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_30_5_smoothed, 0)
#vmax_smoothed= percentile(T_30_5_smoothed, 100)
#hp.visufunc.mollview(T_30_5_smoothed,  title='LFSM @ 30.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_31_smoothed = hp.smoothing(T_31, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_31_smoothed, 0)
#vmax_smoothed= percentile(T_31_smoothed, 100)
#hp.visufunc.mollview(T_31_smoothed,  title='LFSM @ 31 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_31_5_smoothed = hp.smoothing(T_31_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_31_5_smoothed, 0)
#vmax_smoothed= percentile(T_31_5_smoothed, 100)
#hp.visufunc.mollview(T_31_5_smoothed,  title='LFSM @ 31.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_32_smoothed = hp.smoothing(T_32, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_32_smoothed, 0)
#vmax_smoothed= percentile(T_32_smoothed, 100)
#hp.visufunc.mollview(T_32_smoothed,  title='LFSM @ 32 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_32_5_smoothed = hp.smoothing(T_32_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_32_5_smoothed, 0)
#vmax_smoothed= percentile(T_32_5_smoothed, 100)
#hp.visufunc.mollview(T_32_5_smoothed,  title='LFSM @ 32.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_33_smoothed = hp.smoothing(T_33, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_33_smoothed, 0)
#vmax_smoothed= percentile(T_33_smoothed, 100)
#hp.visufunc.mollview(T_33_smoothed,  title='LFSM @ 33 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_33_5_smoothed = hp.smoothing(T_33_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_33_5_smoothed, 0)
#vmax_smoothed= percentile(T_33_5_smoothed, 100)
#hp.visufunc.mollview(T_33_5_smoothed,  title='LFSM @ 33.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_34_smoothed = hp.smoothing(T_34, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_34_smoothed, 0)
#vmax_smoothed= percentile(T_34_smoothed, 100)
#hp.visufunc.mollview(T_34_smoothed,  title='LFSM @ 34 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_34_5_smoothed = hp.smoothing(T_34_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_34_5_smoothed, 0)
#vmax_smoothed= percentile(T_34_5_smoothed, 100)
#hp.visufunc.mollview(T_34_5_smoothed,  title='LFSM @ 34.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_35_smoothed = hp.smoothing(T_35, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_35_smoothed, 0)
#vmax_smoothed= percentile(T_35_smoothed, 100)
#hp.visufunc.mollview(T_35_smoothed,  title='LFSM @ 35 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_35_5_smoothed = hp.smoothing(T_35_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_35_5_smoothed, 0)
#vmax_smoothed= percentile(T_35_5_smoothed, 100)
#hp.visufunc.mollview(T_35_5_smoothed,  title='LFSM @ 35.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_36_smoothed = hp.smoothing(T_36, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_36_smoothed, 0)
#vmax_smoothed= percentile(T_36_smoothed, 100)
#hp.visufunc.mollview(T_36_smoothed,  title='LFSM @ 36 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_36_5_smoothed = hp.smoothing(T_36_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_36_5_smoothed, 0)
#vmax_smoothed= percentile(T_36_5_smoothed, 100)
#hp.visufunc.mollview(T_36_5_smoothed,  title='LFSM @ 36.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_37_smoothed = hp.smoothing(T_37, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_37_smoothed, 0)
#vmax_smoothed= percentile(T_37_smoothed, 100)
#hp.visufunc.mollview(T_37_smoothed,  title='LFSM @ 37 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_37_5_smoothed = hp.smoothing(T_37_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_37_5_smoothed, 0)
#vmax_smoothed= percentile(T_37_5_smoothed, 100)
#hp.visufunc.mollview(T_37_5_smoothed,  title='LFSM @ 37.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_38_smoothed = hp.smoothing(T_38, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_38_smoothed, 0)
#vmax_smoothed= percentile(T_38_smoothed, 100)
#hp.visufunc.mollview(T_38_smoothed,  title='LFSM @ 38 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_38_5_smoothed = hp.smoothing(T_38_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_38_5_smoothed, 0)
#vmax_smoothed= percentile(T_38_5_smoothed, 100)
#hp.visufunc.mollview(T_38_5_smoothed,  title='LFSM @ 38.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_39_smoothed = hp.smoothing(T_39, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_39_smoothed, 0)
#vmax_smoothed= percentile(T_39_smoothed, 100)
#hp.visufunc.mollview(T_39_smoothed,  title='LFSM @ 39 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_39_5_smoothed = hp.smoothing(T_39_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_39_5_smoothed, 0)
#vmax_smoothed= percentile(T_39_5_smoothed, 100)
#hp.visufunc.mollview(T_39_5_smoothed,  title='LFSM @ 39.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_40_smoothed = hp.smoothing(T_40, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_40_smoothed, 0)
#vmax_smoothed= percentile(T_40_smoothed, 100)
#hp.visufunc.mollview(T_40_smoothed,  title='LFSM @ 40 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_40_5_smoothed = hp.smoothing(T_40_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_40_5_smoothed, 0)
#vmax_smoothed= percentile(T_40_5_smoothed, 100)
#hp.visufunc.mollview(T_40_5_smoothed,  title='LFSM @ 40.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_41_smoothed = hp.smoothing(T_41, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_41_smoothed, 0)
#vmax_smoothed= percentile(T_41_smoothed, 100)
#hp.visufunc.mollview(T_41_smoothed,  title='LFSM @ 41 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_41_5_smoothed = hp.smoothing(T_41_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_41_5_smoothed, 0)
#vmax_smoothed= percentile(T_41_5_smoothed, 100)
#hp.visufunc.mollview(T_41_5_smoothed,  title='LFSM @ 41.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_42_smoothed = hp.smoothing(T_42, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_42_smoothed, 0)
#vmax_smoothed= percentile(T_42_smoothed, 100)
#hp.visufunc.mollview(T_42_smoothed,  title='LFSM @ 42 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_42_5_smoothed = hp.smoothing(T_42_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_42_5_smoothed, 0)
#vmax_smoothed= percentile(T_42_5_smoothed, 100)
#hp.visufunc.mollview(T_42_5_smoothed,  title='LFSM @ 42.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_43_smoothed = hp.smoothing(T_43, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_43_smoothed, 0)
#vmax_smoothed= percentile(T_43_smoothed, 100)
#hp.visufunc.mollview(T_43_smoothed,  title='LFSM @ 43 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_43_5_smoothed = hp.smoothing(T_43_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_43_5_smoothed, 0)
#vmax_smoothed= percentile(T_43_5_smoothed, 100)
#hp.visufunc.mollview(T_43_5_smoothed,  title='LFSM @ 43.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_44_smoothed = hp.smoothing(T_44, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_44_smoothed, 0)
#vmax_smoothed= percentile(T_44_smoothed, 100)
#hp.visufunc.mollview(T_44_smoothed,  title='LFSM @ 44 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_44_5_smoothed = hp.smoothing(T_44_5, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_44_5_smoothed, 0)
#vmax_smoothed= percentile(T_44_5_smoothed, 100)
#hp.visufunc.mollview(T_44_5_smoothed,  title='LFSM @ 44.5 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

T_45_smoothed = hp.smoothing(T_45, fwhm=np.radians(25.))
#vmin_smoothed = percentile(T_45_smoothed, 0)
#vmax_smoothed= percentile(T_45_smoothed, 100)
#hp.visufunc.mollview(T_45_smoothed,  title='LFSM @ 45 MHz (smoothed)', notext=True, min=vmin_smoothed, max=vmax_smoothed, unit='K', xsize=1000, format='%.3f')
#hp.graticule(color='k')
#plt.show()

#%%
QDC_T30_M10= []
QDC_T30_5_M10= []
QDC_T31_M10= []
QDC_T31_5_M10= []
QDC_T32_M10= []
QDC_T32_5_M10= []
QDC_T33_M10= []
QDC_T33_5_M10= []
QDC_T34_M10= []
QDC_T34_5_M10= []
QDC_T35_M10= []
QDC_T35_5_M10= []
QDC_T36_M10= []
QDC_T36_5_M10= []
QDC_T37_M10= []
QDC_T37_5_M10= []
QDC_T38_M10= []
QDC_T38_5_M10= []
QDC_T39_M10= []
QDC_T39_5_M10= []
QDC_T40_M10= []
QDC_T40_5_M10= []
QDC_T41_M10= []
QDC_T41_5_M10= []
QDC_T42_M10= []
QDC_T42_5_M10= []
QDC_T43_M10= []
QDC_T43_5_M10= []
QDC_T44_M10= []
QDC_T44_5_M10= []
QDC_T45_M10= []

for i in range(len(lat_zenith_list_M10)):
    lat_zenith_M10= lat_zenith_list_M10[i]
    long_zenith_M10= long_zenith_list_M10[i]
    vec_zenith_M10=hp.ang2vec(np.radians(lat_zenith_M10), np.radians(long_zenith_M10))
    ipix_disc_zenith_M10= hp.query_disc(nside=nside, vec=vec_zenith_M10, radius=np.radians(25.))
    MZ_M10_30MHz= np.mean(T_30_smoothed[ipix_disc_zenith_M10])
    MZ_M10_30_5_MHz= np.mean(T_30_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_31MHz= np.mean(T_31_smoothed[ipix_disc_zenith_M10])
    MZ_M10_31_5_MHz= np.mean(T_31_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_32MHz= np.mean(T_32_smoothed[ipix_disc_zenith_M10])
    MZ_M10_32_5_MHz= np.mean(T_32_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_33MHz= np.mean(T_33_smoothed[ipix_disc_zenith_M10])
    MZ_M10_33_5_MHz= np.mean(T_33_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_34MHz= np.mean(T_34_smoothed[ipix_disc_zenith_M10])
    MZ_M10_34_5_MHz= np.mean(T_34_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_35MHz= np.mean(T_35_smoothed[ipix_disc_zenith_M10])
    MZ_M10_35_5_MHz= np.mean(T_35_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_36MHz= np.mean(T_36_smoothed[ipix_disc_zenith_M10])
    MZ_M10_36_5_MHz= np.mean(T_36_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_37MHz= np.mean(T_37_smoothed[ipix_disc_zenith_M10])
    MZ_M10_37_5_MHz= np.mean(T_37_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_38MHz= np.mean(T_38_smoothed[ipix_disc_zenith_M10])
    MZ_M10_38_5_MHz= np.mean(T_38_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_39MHz= np.mean(T_39_smoothed[ipix_disc_zenith_M10])
    MZ_M10_39_5_MHz= np.mean(T_39_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_40MHz= np.mean(T_40_smoothed[ipix_disc_zenith_M10])
    MZ_M10_40_5_MHz= np.mean(T_40_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_41MHz= np.mean(T_41_smoothed[ipix_disc_zenith_M10])
    MZ_M10_41_5_MHz= np.mean(T_41_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_42MHz= np.mean(T_42_smoothed[ipix_disc_zenith_M10])
    MZ_M10_42_5_MHz= np.mean(T_42_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_43MHz= np.mean(T_43_smoothed[ipix_disc_zenith_M10])
    MZ_M10_43_5_MHz= np.mean(T_43_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_44MHz= np.mean(T_44_smoothed[ipix_disc_zenith_M10])
    MZ_M10_44_5_MHz= np.mean(T_44_5_smoothed[ipix_disc_zenith_M10])
    MZ_M10_45MHz= np.mean(T_45_smoothed[ipix_disc_zenith_M10])

    QDC_T30_M10.append(MZ_M10_30MHz)
    QDC_T30_5_M10.append(MZ_M10_30_5_MHz)
    QDC_T31_M10.append(MZ_M10_31MHz)
    QDC_T31_5_M10.append(MZ_M10_31_5_MHz)
    QDC_T32_M10.append(MZ_M10_32MHz)
    QDC_T32_5_M10.append(MZ_M10_32_5_MHz)
    QDC_T33_M10.append(MZ_M10_33MHz)
    QDC_T33_5_M10.append(MZ_M10_33_5_MHz)
    QDC_T34_M10.append(MZ_M10_34MHz)
    QDC_T34_5_M10.append(MZ_M10_34_5_MHz)
    QDC_T35_M10.append(MZ_M10_35MHz)
    QDC_T35_5_M10.append(MZ_M10_35_5_MHz)
    QDC_T36_M10.append(MZ_M10_36MHz)
    QDC_T36_5_M10.append(MZ_M10_36_5_MHz)
    QDC_T37_M10.append(MZ_M10_37MHz)
    QDC_T37_5_M10.append(MZ_M10_37_5_MHz)
    QDC_T38_M10.append(MZ_M10_38MHz)
    QDC_T38_5_M10.append(MZ_M10_38_5_MHz)
    QDC_T39_M10.append(MZ_M10_39MHz)
    QDC_T39_5_M10.append(MZ_M10_39_5_MHz)
    QDC_T40_M10.append(MZ_M10_40MHz)
    QDC_T40_5_M10.append(MZ_M10_40_5_MHz)
    QDC_T41_M10.append(MZ_M10_41MHz)
    QDC_T41_5_M10.append(MZ_M10_41_5_MHz)
    QDC_T42_M10.append(MZ_M10_42MHz)
    QDC_T42_5_M10.append(MZ_M10_42_5_MHz)
    QDC_T43_M10.append(MZ_M10_43MHz)
    QDC_T43_5_M10.append(MZ_M10_43_5_MHz)
    QDC_T44_M10.append(MZ_M10_44MHz)
    QDC_T44_5_M10.append(MZ_M10_44_5_MHz)
    QDC_T45_M10.append(MZ_M10_45MHz)

fig= plt.figure(figsize=(7,5))
ax= fig.add_subplot(111)
number_of_plots= 31
colormap= plt.cm.nipy_spectral_r
colormaplist= [colormap(i) for i in np.linspace(0, 1, number_of_plots+1)]
ax.set_color_cycle(colormaplist)
ax.plot(X1, QDC_T30_M10, label='30')
ax.plot(X1, QDC_T30_5_M10, label='30.5')
ax.plot(X1, QDC_T31_M10, label='31')
ax.plot(X1, QDC_T31_5_M10, label='31.5')
ax.plot(X1, QDC_T32_M10, label='32')
ax.plot(X1, QDC_T32_5_M10, label='32.5')
ax.plot(X1, QDC_T33_M10, label='33')
ax.plot(X1, QDC_T33_5_M10, label='33.5')
ax.plot(X1, QDC_T34_M10, label='34')
ax.plot(X1, QDC_T34_5_M10, label='34.5')
ax.plot(X1, QDC_T35_M10, label='35')
ax.plot(X1, QDC_T35_5_M10, label='35.5')
ax.plot(X1, QDC_T36_M10, label='36')
ax.plot(X1, QDC_T36_5_M10, label='36.5')
ax.plot(X1, QDC_T37_M10, label='37')
ax.plot(X1, QDC_T37_5_M10, label='37.5')
ax.plot(X1, QDC_T38_M10, label='38')
ax.plot(X1, QDC_T38_5_M10, label='38.5')
ax.plot(X1, QDC_T39_M10, label='39')
ax.plot(X1, QDC_T39_5_M10, label='39.5')
ax.plot(X1, QDC_T40_M10, label='40')
ax.plot(X1, QDC_T40_5_M10, label='40.5')
ax.plot(X1, QDC_T41_M10, label='41')
ax.plot(X1, QDC_T41_5_M10, label='41.5')
ax.plot(X1, QDC_T42_M10, label='42')
ax.plot(X1, QDC_T42_5_M10, label='42.5')
ax.plot(X1, QDC_T43_M10, label='43')
ax.plot(X1, QDC_T43_5_M10, label='43.5')
ax.plot(X1, QDC_T44_M10, label='44')
ax.plot(X1, QDC_T44_5_M10, label='44.5')
ax.plot(X1, QDC_T45_M10, label='45')
plt.xlabel('Universal Time [h] (UTC)')
plt.ylabel('Brightness Temperature [K] (FWHM 25$^o$)')
plt.xlim(0,24)
plt.ylim(0,57000)
plt.title('Brightness Temperature Day Curves on March 10, 2004')
#plt.legend(loc='best', fontsize='small', title='Frequencies [MHz]')
sm=plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=30,vmax=45))
Z=np.arange(30,45.5,0.5)
sm.set_array(Z)
plt.colorbar(sm, label='Frequency [MHz]', spacing='uniform')
plt.show()

#%% POWER CONTRIBUTION OF CRN TO QDC 38.2 MHz
P_n_38_2=[]
for i in range(len(QDC_Ts_38_2_M10)):
    P_n_38_2.append(power_dbm(power_noise(QDC_Ts_38_2_M10[i])))

plt.figure(figsize=(7,5))  
plt.plot(X1, P_n_38_2, c='y')
plt.xlim(0,24)
plt.ylim(-145,-114)
plt.xlabel('Universal Time [h] (UTC)')
plt.ylabel('Noise power [W] (FWHM 25$^o$)')
plt.title('Noise Power Day Curve (38.2 MHz) on March 10, 2004')
plt.show()

#%% POWER CONTRIBUTION OF CRN TO QDC 30-45 MHz
P_n_30=[]
P_n_30_5=[]
P_n_31=[]
P_n_31_5=[]
P_n_32=[]
P_n_32_5=[]
P_n_33=[]
P_n_33_5=[]
P_n_34=[]
P_n_34_5=[]
P_n_35=[]
P_n_35_5=[]
P_n_36=[]
P_n_36_5=[]
P_n_37=[]
P_n_37_5=[]
P_n_38=[]
P_n_38_5=[]
P_n_39=[]
P_n_39_5=[]
P_n_40=[]
P_n_40_5=[]
P_n_41=[]
P_n_41_5=[]
P_n_42=[]
P_n_42_5=[]
P_n_43=[]
P_n_43_5=[]
P_n_44=[]
P_n_44_5=[]
P_n_45=[]
for i in range(len(QDC_Ts_38_2_M10)):
    P_n_30.append(power_dbm(power_noise(QDC_T30_M10[i])))
    P_n_30_5.append(power_dbm(power_noise(QDC_T30_5_M10[i])))
    P_n_31.append(power_dbm(power_noise(QDC_T31_M10[i])))
    P_n_31_5.append(power_dbm(power_noise(QDC_T31_5_M10[i])))
    P_n_32.append(power_dbm(power_noise(QDC_T32_M10[i])))
    P_n_32_5.append(power_dbm(power_noise(QDC_T32_5_M10[i])))
    P_n_33.append(power_dbm(power_noise(QDC_T33_M10[i])))
    P_n_33_5.append(power_dbm(power_noise(QDC_T33_5_M10[i])))
    P_n_34.append(power_dbm(power_noise(QDC_T34_M10[i])))
    P_n_34_5.append(power_dbm(power_noise(QDC_T34_5_M10[i])))
    P_n_35.append(power_dbm(power_noise(QDC_T35_M10[i])))
    P_n_35_5.append(power_dbm(power_noise(QDC_T35_5_M10[i])))
    P_n_36.append(power_dbm(power_noise(QDC_T36_M10[i])))
    P_n_36_5.append(power_dbm(power_noise(QDC_T36_5_M10[i])))
    P_n_37.append(power_dbm(power_noise(QDC_T37_M10[i])))
    P_n_37_5.append(power_dbm(power_noise(QDC_T37_5_M10[i])))
    P_n_38.append(power_dbm(power_noise(QDC_T38_M10[i])))
    P_n_38_5.append(power_dbm(power_noise(QDC_T38_5_M10[i])))
    P_n_39.append(power_dbm(power_noise(QDC_T39_M10[i])))
    P_n_39_5.append(power_dbm(power_noise(QDC_T39_5_M10[i])))
    P_n_40.append(power_dbm(power_noise(QDC_T40_M10[i])))
    P_n_40_5.append(power_dbm(power_noise(QDC_T40_5_M10[i])))
    P_n_41.append(power_dbm(power_noise(QDC_T41_M10[i])))
    P_n_41_5.append(power_dbm(power_noise(QDC_T41_5_M10[i])))
    P_n_42.append(power_dbm(power_noise(QDC_T42_M10[i])))
    P_n_42_5.append(power_dbm(power_noise(QDC_T42_5_M10[i])))
    P_n_43.append(power_dbm(power_noise(QDC_T43_M10[i])))
    P_n_43_5.append(power_dbm(power_noise(QDC_T43_5_M10[i])))
    P_n_44.append(power_dbm(power_noise(QDC_T44_M10[i])))
    P_n_44_5.append(power_dbm(power_noise(QDC_T44_5_M10[i])))
    P_n_45.append(power_dbm(power_noise(QDC_T45_M10[i])))
    
fig= plt.figure(figsize=(7,5))
ax= fig.add_subplot(111)
number_of_plots= 31
colormap= plt.cm.gist_stern_r
colormaplist= [colormap(i) for i in np.linspace(0, 1, number_of_plots+1)] 
ax.set_color_cycle(colormaplist)
ax.plot(X1, P_n_30, label='30 MHz')
ax.plot(X1, P_n_30_5, label='30.5 MHz')
ax.plot(X1, P_n_31, label='31 MHz')
ax.plot(X1, P_n_31_5, label='31.5 MHz')
ax.plot(X1, P_n_32, label='32 MHz')
ax.plot(X1, P_n_32_5, label='32.5 MHz')
ax.plot(X1, P_n_33, label='33 MHz')
ax.plot(X1, P_n_33_5, label='33.5 MHz')
ax.plot(X1, P_n_34, label='34 MHz')
ax.plot(X1, P_n_34_5, label='34.5 MHz')
ax.plot(X1, P_n_35, label='35 MHz')
ax.plot(X1, P_n_35_5, label='35.5 MHz')
ax.plot(X1, P_n_36, label='36 MHz')
ax.plot(X1, P_n_36_5, label='36.5 MHz')
ax.plot(X1, P_n_37, label='37 MHz')
ax.plot(X1, P_n_37_5, label='37.6 MHz')
ax.plot(X1, P_n_38, label='38 MHz')
ax.plot(X1, P_n_38_5, label='38.5 MHz')
ax.plot(X1, P_n_39, label='39 MHz')
ax.plot(X1, P_n_39_5, label='39.5 MHz')
ax.plot(X1, P_n_40, label='40 MHz')
ax.plot(X1, P_n_40_5, label='40.5 MHz')
ax.plot(X1, P_n_41, label='41 MHz')
ax.plot(X1, P_n_41_5, label='41.5 MHz')
ax.plot(X1, P_n_42, label='42 MHz')
ax.plot(X1, P_n_42_5, label='42.5 MHz')
ax.plot(X1, P_n_43, label='43 MHz')
ax.plot(X1, P_n_43_5, label='43.5 MHz')
ax.plot(X1, P_n_44, label='44 MHz')
ax.plot(X1, P_n_44_5, label='44.5 MHz')
ax.plot(X1, P_n_45, label='45 MHz')
plt.xlim(0,24)
plt.ylim(-145,-114)
plt.xlabel('Universal Time [h] (UTC)')
plt.ylabel('Noise power [dBm] (FWHM 25$^o$)')
plt.title('Noise Power Day Curves on March 10, 2004')
#plt.legend(loc='best')
sm=plt.cm.ScalarMappable(cmap=colormap, norm=plt.Normalize(vmin=30,vmax=45))
Z=np.arange(30,45.5,0.5)
sm.set_array(Z)
plt.colorbar(sm, label='Frequency [MHz]', spacing='uniform')
plt.show()

#%% SMOOTHED TEMPERATURES ARRAY CONSTRUCTION (FOR MAPPING LFSM SMOOTHED)
T_30_smoothed_resh = np.array(T_30_smoothed).reshape(1, len(IDs))
T_30_5_smoothed_resh = np.array(T_30_5_smoothed).reshape(1, len(IDs))
T_31_smoothed_resh = np.array(T_31_smoothed).reshape(1, len(IDs))
T_31_5_smoothed_resh = np.array(T_31_5_smoothed).reshape(1, len(IDs))
T_32_smoothed_resh = np.array(T_32_smoothed).reshape(1, len(IDs))
T_32_5_smoothed_resh = np.array(T_32_5_smoothed).reshape(1, len(IDs))
T_33_smoothed_resh = np.array(T_33_smoothed).reshape(1, len(IDs))
T_33_5_smoothed_resh = np.array(T_33_5_smoothed).reshape(1, len(IDs))
T_34_smoothed_resh = np.array(T_34_smoothed).reshape(1, len(IDs))
T_34_5_smoothed_resh = np.array(T_34_5_smoothed).reshape(1, len(IDs))
T_35_smoothed_resh = np.array(T_35_smoothed).reshape(1, len(IDs))
T_35_5_smoothed_resh = np.array(T_35_5_smoothed).reshape(1, len(IDs))
T_36_smoothed_resh = np.array(T_36_smoothed).reshape(1, len(IDs))
T_36_5_smoothed_resh = np.array(T_36_5_smoothed).reshape(1, len(IDs))
T_37_smoothed_resh = np.array(T_37_smoothed).reshape(1, len(IDs))
T_37_5_smoothed_resh = np.array(T_37_5_smoothed).reshape(1, len(IDs))
T_38_smoothed_resh = np.array(T_38_smoothed).reshape(1, len(IDs))
T_38_5_smoothed_resh = np.array(T_38_5_smoothed).reshape(1, len(IDs))
T_39_smoothed_resh = np.array(T_39_smoothed).reshape(1, len(IDs))
T_39_5_smoothed_resh = np.array(T_39_5_smoothed).reshape(1, len(IDs))
T_40_smoothed_resh = np.array(T_40_smoothed).reshape(1, len(IDs))
T_40_5_smoothed_resh = np.array(T_40_5_smoothed).reshape(1, len(IDs))
T_41_smoothed_resh = np.array(T_41_smoothed).reshape(1, len(IDs))
T_41_5_smoothed_resh = np.array(T_41_5_smoothed).reshape(1, len(IDs))
T_42_smoothed_resh = np.array(T_42_smoothed).reshape(1, len(IDs))
T_42_5_smoothed_resh = np.array(T_42_5_smoothed).reshape(1, len(IDs))
T_43_smoothed_resh = np.array(T_43_smoothed).reshape(1, len(IDs))
T_43_5_smoothed_resh = np.array(T_43_5_smoothed).reshape(1, len(IDs))
T_44_smoothed_resh = np.array(T_44_smoothed).reshape(1, len(IDs))
T_44_5_smoothed_resh = np.array(T_44_5_smoothed).reshape(1, len(IDs))
T_45_smoothed_resh = np.array(T_45_smoothed).reshape(1, len(IDs))

T_38_2_smoothed_resh = np.array(T_38_2_smoothed).reshape(1, len(IDs))

array= np.concatenate((IDs_resh, T_30_smoothed_resh, T_30_5_smoothed_resh, T_31_smoothed_resh, T_31_5_smoothed_resh, T_32_smoothed_resh, T_32_5_smoothed_resh, T_33_smoothed_resh, T_33_5_smoothed_resh, T_34_smoothed_resh, T_34_5_smoothed_resh, T_35_smoothed_resh, T_35_5_smoothed_resh, T_36_smoothed_resh, T_36_5_smoothed_resh, T_37_smoothed_resh, T_37_5_smoothed_resh, T_38_smoothed_resh, T_38_5_smoothed_resh, T_39_smoothed_resh, T_39_5_smoothed_resh, T_40_smoothed_resh, T_40_5_smoothed_resh, T_41_smoothed_resh, T_41_5_smoothed_resh, T_42_smoothed_resh, T_42_5_smoothed_resh, T_43_smoothed_resh, T_43_5_smoothed_resh, T_44_smoothed_resh, T_44_5_smoothed_resh, T_45_smoothed_resh)).T
array2= np.concatenate((IDs_resh, T_38_2_smoothed_resh)).T

#%% SMOOTHED TEMPERATURE ARRAY CONSTRUCTION OF QDC (TIME, ZENITH TEMPERATURE AT THE TIME)
QDC_T30_M10_resh = np.array(QDC_T30_M10).reshape(1, len(X1))
QDC_T30_5_M10_resh = np.array(QDC_T30_5_M10).reshape(1, len(X1))
QDC_T31_M10_resh = np.array(QDC_T31_M10).reshape(1, len(X1))
QDC_T31_5_M10_resh = np.array(QDC_T31_5_M10).reshape(1, len(X1))
QDC_T32_M10_resh = np.array(QDC_T32_M10).reshape(1, len(X1))
QDC_T32_5_M10_resh = np.array(QDC_T32_5_M10).reshape(1, len(X1))
QDC_T33_M10_resh = np.array(QDC_T33_M10).reshape(1, len(X1))
QDC_T33_5_M10_resh = np.array(QDC_T33_5_M10).reshape(1, len(X1))
QDC_T34_M10_resh = np.array(QDC_T34_M10).reshape(1, len(X1))
QDC_T34_5_M10_resh = np.array(QDC_T34_5_M10).reshape(1, len(X1))
QDC_T35_M10_resh = np.array(QDC_T35_M10).reshape(1, len(X1))
QDC_T35_5_M10_resh = np.array(QDC_T35_5_M10).reshape(1, len(X1))
QDC_T36_M10_resh = np.array(QDC_T36_M10).reshape(1, len(X1))
QDC_T36_5_M10_resh = np.array(QDC_T36_5_M10).reshape(1, len(X1))
QDC_T37_M10_resh = np.array(QDC_T37_M10).reshape(1, len(X1))
QDC_T37_5_M10_resh = np.array(QDC_T37_5_M10).reshape(1, len(X1))
QDC_T38_M10_resh = np.array(QDC_T38_M10).reshape(1, len(X1))
QDC_T38_5_M10_resh = np.array(QDC_T38_5_M10).reshape(1, len(X1))
QDC_T39_M10_resh = np.array(QDC_T39_M10).reshape(1, len(X1))
QDC_T39_5_M10_resh = np.array(QDC_T39_5_M10).reshape(1, len(X1))
QDC_T40_M10_resh = np.array(QDC_T40_M10).reshape(1, len(X1))
QDC_T40_5_M10_resh = np.array(QDC_T40_5_M10).reshape(1, len(X1))
QDC_T41_M10_resh = np.array(QDC_T41_M10).reshape(1, len(X1))
QDC_T41_5_M10_resh = np.array(QDC_T41_5_M10).reshape(1, len(X1))
QDC_T42_M10_resh = np.array(QDC_T42_M10).reshape(1, len(X1))
QDC_T42_5_M10_resh = np.array(QDC_T42_5_M10).reshape(1, len(X1))
QDC_T43_M10_resh = np.array(QDC_T43_M10).reshape(1, len(X1))
QDC_T43_5_M10_resh = np.array(QDC_T43_5_M10).reshape(1, len(X1))
QDC_T44_M10_resh = np.array(QDC_T44_M10).reshape(1, len(X1))
QDC_T44_5_M10_resh = np.array(QDC_T44_5_M10).reshape(1, len(X1))
QDC_T45_M10_resh = np.array(QDC_T45_M10).reshape(1, len(X1))

QDC_T38_2_M10_resh = np.array(QDC_Ts_38_2_M10).reshape(1, len(X1))

#print(len(X1), len(QDC_T30_M10_resh), len(QDC_T30_5_M10_resh), len(QDC_T31_M10_resh), len(QDC_T31_5_M10_resh), len(QDC_T32_M10_resh), len(QDC_T32_5_M10_resh), len(QDC_T33_M10_resh), len(QDC_T33_5_M10_resh), len(QDC_T34_M10_resh), len(QDC_T34_5_M10_resh), len(QDC_T35_M10_resh), len(QDC_T35_5_M10_resh), len(QDC_T36_M10_resh), len(QDC_T36_5_M10_resh), len(QDC_T37_M10_resh), len(QDC_T37_5_M10_resh), len(QDC_T38_M10_resh), len(QDC_T38_5_M10_resh), len(QDC_T39_M10_resh), len(QDC_T39_5_M10_resh), len(QDC_T40_M10_resh), len(QDC_T40_5_M10_resh), len(QDC_T41_M10_resh), len(QDC_T41_5_M10_resh), len(QDC_T42_M10_resh), len(QDC_T42_5_M10_resh), len(QDC_T43_M10_resh), QDC_T43_5_M10_resh, QDC_T44_M10_resh, QDC_T44_5_M10_resh, QDC_T45_M10_resh
array3= np.concatenate((X1_resh, QDC_T30_M10_resh, QDC_T30_5_M10_resh, QDC_T31_M10_resh, QDC_T31_5_M10_resh, QDC_T32_M10_resh, QDC_T32_5_M10_resh, QDC_T33_M10_resh, QDC_T33_5_M10_resh, QDC_T34_M10_resh, QDC_T34_5_M10_resh, QDC_T35_M10_resh, QDC_T35_5_M10_resh, QDC_T36_M10_resh, QDC_T36_5_M10_resh, QDC_T37_M10_resh, QDC_T37_5_M10_resh, QDC_T38_M10_resh, QDC_T38_5_M10_resh, QDC_T39_M10_resh, QDC_T39_5_M10_resh, QDC_T40_M10_resh, QDC_T40_5_M10_resh, QDC_T41_M10_resh, QDC_T41_5_M10_resh, QDC_T42_M10_resh, QDC_T42_5_M10_resh, QDC_T43_M10_resh, QDC_T43_5_M10_resh, QDC_T44_M10_resh, QDC_T44_5_M10_resh, QDC_T45_M10_resh)).T
array4= np.concatenate((X1_resh, QDC_T38_2_M10_resh)).T

#%% SMOOTHED POWER ARRAY CONSTRUCTION OF QDC (TIME, ZENITH POWER AT THE TIME)
P_n_30_resh= np.array(P_n_30).reshape(1, len(X1))
P_n_30_5_resh= np.array(P_n_30_5).reshape(1, len(X1))
P_n_31_resh= np.array(P_n_31).reshape(1, len(X1))
P_n_31_5_resh= np.array(P_n_31_5).reshape(1, len(X1))
P_n_32_resh= np.array(P_n_32).reshape(1, len(X1))
P_n_32_5_resh= np.array(P_n_32_5).reshape(1, len(X1))
P_n_33_resh= np.array(P_n_33).reshape(1, len(X1))
P_n_33_5_resh= np.array(P_n_33_5).reshape(1, len(X1))
P_n_34_resh= np.array(P_n_34).reshape(1, len(X1))
P_n_34_5_resh= np.array(P_n_34_5).reshape(1, len(X1))
P_n_35_resh= np.array(P_n_35).reshape(1, len(X1))
P_n_35_5_resh= np.array(P_n_35_5).reshape(1, len(X1))
P_n_36_resh= np.array(P_n_36).reshape(1, len(X1))
P_n_36_5_resh= np.array(P_n_36_5).reshape(1, len(X1))
P_n_37_resh= np.array(P_n_37).reshape(1, len(X1))
P_n_37_5_resh= np.array(P_n_37_5).reshape(1, len(X1))
P_n_38_resh= np.array(P_n_38).reshape(1, len(X1))
P_n_38_5_resh= np.array(P_n_38_5).reshape(1, len(X1))
P_n_39_resh= np.array(P_n_39).reshape(1, len(X1))
P_n_39_5_resh= np.array(P_n_39_5).reshape(1, len(X1))
P_n_40_resh= np.array(P_n_40).reshape(1, len(X1))
P_n_40_5_resh= np.array(P_n_40_5).reshape(1, len(X1))
P_n_41_resh= np.array(P_n_41).reshape(1, len(X1))
P_n_41_5_resh= np.array(P_n_41_5).reshape(1, len(X1))
P_n_42_resh= np.array(P_n_42).reshape(1, len(X1))
P_n_42_5_resh= np.array(P_n_42_5).reshape(1, len(X1))
P_n_43_resh= np.array(P_n_43).reshape(1, len(X1))
P_n_43_5_resh= np.array(P_n_43_5).reshape(1, len(X1))
P_n_44_resh= np.array(P_n_44).reshape(1, len(X1))
P_n_44_5_resh= np.array(P_n_44_5).reshape(1, len(X1))
P_n_45_resh= np.array(P_n_45).reshape(1, len(X1))

P_n_38_2_resh = np.array(P_n_38_2).reshape(1, len(X1))

array5= np.concatenate((X1_resh, P_n_30_resh, P_n_30_5_resh, P_n_31_resh, P_n_31_5_resh, P_n_32_resh, P_n_32_5_resh, P_n_33_resh, P_n_33_5_resh, P_n_34_resh, P_n_34_5_resh, P_n_35_resh, P_n_35_5_resh, P_n_36_resh, P_n_36_5_resh, P_n_37_resh, P_n_37_5_resh, P_n_38_resh, P_n_38_5_resh, P_n_39_resh, P_n_39_5_resh, P_n_40_resh, P_n_40_5_resh, P_n_41_resh, P_n_41_5_resh, P_n_42_resh, P_n_42_5_resh, P_n_43_resh, P_n_43_5_resh, P_n_44_resh, P_n_44_5_resh, P_n_45_resh)).T
array6= np.concatenate((X1_resh, P_n_38_2_resh)).T
#%%
np.savetxt('SMOOTHED_latlong_temps_NOLATLONG_V2_FREQUENCIES.txt', array, delimiter=',')
np.savetxt('SMOOTHED_latlong_temps_NOLATLONG_V2.txt', array2, delimiter=',')
np.savetxt('SMOOTHED_TEMPERATURE_QDC_2004_experiment_FREQUENCIES.txt', array3, delimiter=',')
np.savetxt('SMOOTHED_TEMPERATURE_QDC_2004_experiment.txt', array4, delimiter=',')
np.savetxt('SMOOTHED_POWER_QDC_2004_experiment_FREQUENCIES.txt', array5, delimiter=',')
np.savetxt('SMOOTHED_POWER_QDC_2004_experiment.txt', array6, delimiter=',')
