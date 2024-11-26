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
#lat_zenith_list_M10= [(180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317), (180-36.8317)]
lat_zenith_list_M10= [(180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687), (180-53.1687)]
long_zenith_list_M10= [94.995, 98.7558, 102.5158, 106.276, 110.0365, 113.7967, 117.5567, 121.3175, 125.0775, 128.8375, 132.5979, 136.3583, 140.1183, 143.8788, 147.6392, 151.3992, 155.1596, 158.9192, 162.68, 166.44, 170.2004, 173.9608, 177.7208, -178.5192, -174.7583, -170.9983, -167.2379, -163.8317, -159.7179, -155.9577, -152.1969, -148.4371, -144.6767, -140.9163, -137.1563, -133.3958, -129.6354, -125.8754, -122.1150, -118.3508, -114.5941, -110.8342, -107.0740, -103.3137, -99.5533, -95.7933, -92.0329, -88.2729, -84.5125, -80.7521, -76.9921, -73.2317, -69.4717, -65.7113, -61.9508, -58.1908, -54.4304, -50.6704, -46.91, -43.15, -39.3896, -35.6292, -31.8692, -28.1090, -24.3483, -20.5885, -16.8281, -13.0679, -9.3077, -5.5475, -1.7871, 1.9731, 5.7333, 9.4938, 13.2537, 17.0142, 20.7746, 24.5346, 28.2950, 32.0552, 35.8154, 39.5756, 43.3358, 47.0963, 50.8565, 54.6167, 58.3769, 62.1379, 65.8975, 69.6577, 73.4179, 77.1783, 80.9383, 84.6983, 88.4583, 92.2183, 95.9783]

lat_b0_list_M10= []
lat_b1_list_M10= []
lat_b2_list_M10= []
lat_b3_list_M10= []
lat_b4_list_M10= []
lat_b5_list_M10= []
lat_b6_list_M10= []
lat_b7_list_M10= []
lat_b8_list_M10= []

long_b0_list_M10= []
long_b1_list_M10= []
long_b2_list_M10= []
long_b3_list_M10= []
long_b4_list_M10= []
long_b5_list_M10= []
long_b6_list_M10= []
long_b7_list_M10= []
long_b8_list_M10= []

for i in range(len(lat_zenith_list_M10)):
    lat_b0_list_M10.append(lat_zenith_list_M10[i]+0)
    lat_b1_list_M10.append(lat_zenith_list_M10[i]+0)
    lat_b2_list_M10.append(lat_zenith_list_M10[i]-12.5)
    lat_b3_list_M10.append(lat_zenith_list_M10[i]-12.5)
    lat_b4_list_M10.append(lat_zenith_list_M10[i]-12.5)
    lat_b5_list_M10.append(lat_zenith_list_M10[i]+0)
    lat_b6_list_M10.append(lat_zenith_list_M10[i]+12.5)
    lat_b7_list_M10.append(lat_zenith_list_M10[i]+12.5)
    lat_b8_list_M10.append(lat_zenith_list_M10[i]+12.5)
     
    long_b0_list_M10.append(long_zenith_list_M10[i]+0)
    long_b1_list_M10.append(long_zenith_list_M10[i]-12.5)
    long_b2_list_M10.append(long_zenith_list_M10[i]-12.5)
    long_b3_list_M10.append(long_zenith_list_M10[i]+0)
    long_b4_list_M10.append(long_zenith_list_M10[i]+12.5)
    long_b5_list_M10.append(long_zenith_list_M10[i]+12.5)
    long_b6_list_M10.append(long_zenith_list_M10[i]+12.5)
    long_b7_list_M10.append(long_zenith_list_M10[i]+0)
    long_b8_list_M10.append(long_zenith_list_M10[i]-12.5)

#%% TEMPERATURA SEQUENCE BUILDING
frequencies_saving= []
for n in np.arange(30,45.5,0.5):
    frequencies_saving.append(str(n)+'_MHz')

for j in range(1,32):
    T_map= data_all[:, j]
    nside=hp.npix2nside(len(T_map))
    vmin = percentile(T_map, 0)
    vmax = percentile(T_map, 100)
    
    QDC_b0_M10= []
    QDC_b1_M10= []
    QDC_b2_M10= []
    QDC_b3_M10= []
    QDC_b4_M10= []
    QDC_b5_M10= []
    QDC_b6_M10= []
    QDC_b7_M10= []
    QDC_b8_M10= []
    
    P_n_b0_M10= []
    P_n_b1_M10= []
    P_n_b2_M10= []
    P_n_b3_M10= []
    P_n_b4_M10= []
    P_n_b5_M10= []
    P_n_b6_M10= []
    P_n_b7_M10= []
    P_n_b8_M10= []

    for i in range(len(lat_b0_list_M10)):
        lat_b0_M10= lat_b0_list_M10[i]
        long_b0_M10= long_b0_list_M10[i]
        vec_b0_M10=hp.ang2vec(np.radians(lat_b0_M10), np.radians(long_b0_M10))
        ipix_disc_b0_M10= hp.query_disc(nside=nside, vec=vec_b0_M10, radius=np.radians(25.))
        mean_b0_M10= np.mean(T_map[ipix_disc_b0_M10])
        QDC_b0_M10.append(mean_b0_M10)
        P_n_b0_M10.append(power_dbm(power_noise(mean_b0_M10)))
        
        lat_b1_M10= lat_b1_list_M10[i]
        long_b1_M10= long_b1_list_M10[i]
        vec_b1_M10=hp.ang2vec(np.radians(lat_b1_M10), np.radians(long_b1_M10))
        ipix_disc_b1_M10= hp.query_disc(nside=nside, vec=vec_b1_M10, radius=np.radians(25.))
        mean_b1_M10= np.mean(T_map[ipix_disc_b1_M10])
        QDC_b1_M10.append(mean_b1_M10)
        P_n_b1_M10.append(power_dbm(power_noise(mean_b1_M10)))
        
        lat_b2_M10= lat_b2_list_M10[i]
        long_b2_M10= long_b2_list_M10[i]
        vec_b2_M10=hp.ang2vec(np.radians(lat_b2_M10), np.radians(long_b2_M10))
        ipix_disc_b2_M10= hp.query_disc(nside=nside, vec=vec_b2_M10, radius=np.radians(25.))
        mean_b2_M10= np.mean(T_map[ipix_disc_b2_M10])
        QDC_b2_M10.append(mean_b2_M10)
        P_n_b2_M10.append(power_dbm(power_noise(mean_b2_M10)))
        
        lat_b3_M10= lat_b3_list_M10[i]
        long_b3_M10= long_b3_list_M10[i]
        vec_b3_M10=hp.ang2vec(np.radians(lat_b3_M10), np.radians(long_b3_M10))
        ipix_disc_b3_M10= hp.query_disc(nside=nside, vec=vec_b3_M10, radius=np.radians(25.))
        mean_b3_M10= np.mean(T_map[ipix_disc_b3_M10])
        QDC_b3_M10.append(mean_b3_M10)
        P_n_b3_M10.append(power_dbm(power_noise(mean_b3_M10)))
        
        lat_b4_M10= lat_b4_list_M10[i]
        long_b4_M10= long_b4_list_M10[i]
        vec_b4_M10=hp.ang2vec(np.radians(lat_b4_M10), np.radians(long_b4_M10))
        ipix_disc_b4_M10= hp.query_disc(nside=nside, vec=vec_b4_M10, radius=np.radians(25.))
        mean_b4_M10= np.mean(T_map[ipix_disc_b4_M10])
        QDC_b4_M10.append(mean_b4_M10)
        P_n_b4_M10.append(power_dbm(power_noise(mean_b4_M10)))
        
        lat_b5_M10= lat_b5_list_M10[i]
        long_b5_M10= long_b5_list_M10[i]
        vec_b5_M10=hp.ang2vec(np.radians(lat_b5_M10), np.radians(long_b5_M10))
        ipix_disc_b5_M10= hp.query_disc(nside=nside, vec=vec_b5_M10, radius=np.radians(25.))
        mean_b5_M10= np.mean(T_map[ipix_disc_b5_M10])
        QDC_b5_M10.append(mean_b5_M10)
        P_n_b5_M10.append(power_dbm(power_noise(mean_b5_M10)))
        
        lat_b6_M10= lat_b6_list_M10[i]
        long_b6_M10= long_b6_list_M10[i]
        vec_b6_M10=hp.ang2vec(np.radians(lat_b6_M10), np.radians(long_b6_M10))
        ipix_disc_b6_M10= hp.query_disc(nside=nside, vec=vec_b6_M10, radius=np.radians(25.))
        mean_b6_M10= np.mean(T_map[ipix_disc_b6_M10])
        QDC_b6_M10.append(mean_b6_M10)
        P_n_b6_M10.append(power_dbm(power_noise(mean_b6_M10)))
        
        lat_b7_M10= lat_b7_list_M10[i]
        long_b7_M10= long_b7_list_M10[i]
        vec_b7_M10=hp.ang2vec(np.radians(lat_b7_M10), np.radians(long_b7_M10))
        ipix_disc_b7_M10= hp.query_disc(nside=nside, vec=vec_b7_M10, radius=np.radians(25.))
        mean_b7_M10= np.mean(T_map[ipix_disc_b7_M10])
        QDC_b7_M10.append(mean_b7_M10)
        P_n_b7_M10.append(power_dbm(power_noise(mean_b7_M10)))
        
        lat_b8_M10= lat_b8_list_M10[i]
        long_b8_M10= long_b8_list_M10[i]
        vec_b8_M10=hp.ang2vec(np.radians(lat_b8_M10), np.radians(long_b8_M10))
        ipix_disc_b8_M10= hp.query_disc(nside=nside, vec=vec_b8_M10, radius=np.radians(25.))
        mean_b8_M10= np.mean(T_map[ipix_disc_b8_M10])
        QDC_b8_M10.append(mean_b8_M10)
        P_n_b8_M10.append(power_dbm(power_noise(mean_b8_M10)))
        
    X1= np.linspace(0, 24, len(QDC_b0_M10)) #UTC
    X1_resh= np.array(X1).reshape(1, len(X1)) 

    fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
    fig.suptitle('Brightness Temperature Day Curve (FWHM 25$^o$ at '+str(frequencies_saving[j-1])+') on March 10, 2004')
    
    axs[0, 0].plot(X1, QDC_b4_M10, c='r')
#    axs[0, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +12.5^o)$')
    axs[0, 0].set_xlim([0,24])
    axs[0, 0].set_ylim([0,55000])
    
    axs[0, 1].plot(X1, QDC_b3_M10, c='r')
#    axs[0, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, +12.5^o)$')
    axs[0, 1].set_xlim([0,24])
    axs[0, 1].set_ylim([0,55000])
    
    axs[0, 2].plot(X1, QDC_b2_M10 , c='r')
#    axs[0, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +12.5^o)$')
    axs[0, 2].set_xlim([0,24])
    axs[0, 2].set_ylim([0,55000])
    
    axs[1, 0].plot(X1, QDC_b5_M10, c='g')
#    axs[1, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, 0^o)$')
    axs[1, 0].set_xlim([0,24])
    axs[1, 0].set_ylim([0,55000])
    
    axs[1, 1].plot(X1, QDC_b0_M10, c='g')
#    axs[1, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, 0^o)$')
    axs[1, 1].set_xlim([0,24])
    axs[1, 1].set_ylim([0,55000])
    
    axs[1, 2].plot(X1, QDC_b1_M10, c='g')
#    axs[1, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, 0^o)$')
    axs[1, 2].set_xlim([0,24])
    axs[1, 2].set_ylim([0,55000])
    
    axs[2, 0].plot(X1, QDC_b6_M10, c='b')
#    axs[2, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -12.5^o)$')
    axs[2, 0].set_xlim([0,24])
    axs[2, 0].set_ylim([0,55000])
    
    axs[2, 1].plot(X1, QDC_b7_M10, c='b')
#    axs[2, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, -12.5^o)$')
    axs[2, 1].set_xlim([0,24])
    axs[2, 1].set_ylim([0,55000])
    
    axs[2, 2].plot(X1, QDC_b8_M10, c='b')
#    axs[2, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -12.5^o)$')
    axs[2, 2].set_xlim([0,24])
    axs[2, 2].set_ylim([0,55000])

#    for ax in axs.flat:
#        ax.set(xlabel='Universal Time [h] (UTC)', ylabel='B. Temperature [K]')
#        ax.label_outer()
    
    fig.text(0.5, 0.04, 'UTC from 00:00 to 23:59', ha='center')
    fig.text(0.04, 0.5, 'Brightness temperature [K]', va='center', rotation='vertical')
    
    savename= 'drift_curve_IRIS_'+str(frequencies_saving[j-1])+'.png'
    plt.savefig(savename)
#    plt.show()
    plt.cla()
    plt.clf()
    plt.close('all')
    plt.close(fig)
    
    fig, axs = plt.subplots(3, 3, sharex=True, sharey=True)
    fig.suptitle('Noise Power Quiet Day Curve (FWHM 25$^o$ at '+str(frequencies_saving[j-1])+') on March 10, 2004')

    axs[0, 0].plot(X1, P_n_b4_M10, c='r')
#    axs[0, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, +12.5^o)$')
    axs[0, 0].set_xlim([0,24])
    axs[0, 0].set_ylim([-140,-114])
    
    axs[0, 1].plot(X1, P_n_b3_M10, c='r')
#    axs[0, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, +12.5^o)$')
    axs[0, 1].set_xlim([0,24])
    axs[0, 1].set_ylim([-140,-114])
    
    axs[0, 2].plot(X1, P_n_b2_M10 , c='r')
#    axs[0, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, +12.5^o)$')
    axs[0, 2].set_xlim([0,24])
    axs[0, 2].set_ylim([-140,-114])
    
    axs[1, 0].plot(X1, P_n_b5_M10, c='g')
#    axs[1, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, 0^o)$')
    axs[1, 0].set_xlim([0,24])
    axs[1, 0].set_ylim([-140,-114])
    
    axs[1, 1].plot(X1, P_n_b0_M10, c='g')
#    axs[1, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, 0^o)$')
    axs[1, 1].set_xlim([0,24])
    axs[1, 1].set_ylim([-140,-114])
    
    axs[1, 2].plot(X1, P_n_b1_M10, c='g')
#    axs[1, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, 0^o)$')
    axs[1, 2].set_xlim([0,24])
    axs[1, 2].set_ylim([-140,-114])
    
    axs[2, 0].plot(X1, P_n_b6_M10, c='b')
#    axs[2, 0].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(+12.5^o, -12.5^o)$')
    axs[2, 0].set_xlim([0,24])
    axs[2, 0].set_ylim([-140,-114])
    
    axs[2, 1].plot(X1, P_n_b7_M10, c='b')
#    axs[2, 1].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(0^o, -12.5^o)$')
    axs[2, 1].set_xlim([0,24])
    axs[2, 1].set_ylim([-140,-114])
    
    axs[2, 2].plot(X1, P_n_b8_M10, c='b')
#    axs[2, 2].set_title('$(\\Delta \\alpha, \\Delta \\delta)=(-12.5^o, -12.5^o)$')
    axs[2, 2].set_xlim([0,24])
    axs[2, 2].set_ylim([-140,-114])
    
#    for ax in axs.flat:
#        ax.set(xlabel='Universal Time [h] (UTC)', ylabel='Noise P. [DBm]')
#        ax.label_outer()
        
    fig.text(0.5, 0.04, 'UTC from 00:00 to 23:59', ha='center')
    fig.text(0.04, 0.5, 'Noise power [dBm]', va='center', rotation='vertical')

    savename2= 'noise_power_curve_IRIS_'+str(frequencies_saving[j-1])+'.png'
    plt.savefig(savename2)
#    plt.show()
    plt.cla()
    plt.clf()
    plt.close('all')
    plt.close(fig)
    
    grid= np.zeros((3,3))
    time=['00:00', '00:15', '00:30', '00:45', '01:00', '01:15', '01:30', '01:45', '02:00', '02:15', '02:30', '02:45', '03:00', '03:15', '03:30', '03:45', '04:00', '04:15', '04:30', '04:45', '05:00', '05:15', '05:30', '05:45', '06:00', '06:15', '06:30', '06:45', '07:00', '07:15', '07:30', '07:45', '08:00', '08:15', '08:30', '08:45', '09:00', '09:15', '09:30', '09:45', '10:00', '10:15', '10:30', '10:45', '11:00', '11:15', '11:30', '11:45', '12:00', '12:15', '12:30', '12:45', '13:00', '13:15', '13:30', '13:45', '14:00', '14:15', '14:30', '14:45', '15:00', '15:15', '15:30', '15:45', '16:00', '16:15', '16:30', '16:45', '17:00', '17:15', '17:30', '17:45', '18:00', '18:15', '18:30', '18:45', '19:00', '19:15', '19:30', '19:45', '20:00', '20:15', '20:30', '20:45', '21:00', '21:15', '21:30', '21:45', '22:00', '22:15', '22:30', '22:45', '23:00', '23:15', '23:30', '23:45', '24:00']
    for i in range(len(QDC_b0_M10)):
        grid[1,1]= QDC_b0_M10[i]
        grid[1,2]= QDC_b1_M10[i]
        grid[0,2]= QDC_b2_M10[i]
        grid[0,1]= QDC_b3_M10[i]
        grid[0,0]= QDC_b4_M10[i]
        grid[1,0]= QDC_b5_M10[i]
        grid[2,0]= QDC_b6_M10[i]
        grid[2,1]= QDC_b7_M10[i]
        grid[2,2]= QDC_b8_M10[i]
        plt.figure(figsize=(7,5))
        plt.imshow(grid, cmap='viridis', extent=[25.0,-25.0,-25.0,25.0])
        plt.title(str(time[i]))
        plt.colorbar().set_label('Brightness temperature [K]', rotation= 270, labelpad=15)
        plt.clim(vmin=5000, vmax=55000)
        plt.savefig(str(frequencies_saving[j-1])+'_AP_SYN_CRN'+str(i)+'_'+str(X1[i])+'.png')
        plt.cla()
        plt.clf()
        plt.close('all')
        plt.close(fig)
        
    grid2= np.zeros((3,3))
    for i in range(len(QDC_b0_M10)):
        grid2[1,1]= P_n_b0_M10[i]
        grid2[1,2]= P_n_b1_M10[i]
        grid2[0,2]= P_n_b2_M10[i]
        grid2[0,1]= P_n_b3_M10[i]
        grid2[0,0]= P_n_b4_M10[i]
        grid2[1,0]= P_n_b5_M10[i]
        grid2[2,0]= P_n_b6_M10[i]
        grid2[2,1]= P_n_b7_M10[i]
        grid2[2,2]= P_n_b8_M10[i]
        plt.figure(figsize=(7,5))
        plt.imshow(grid2, cmap='magma', extent=[25.0,-25.0,-25.0,25.0])
        plt.title(str(time[i]))
        plt.colorbar().set_label('Noise Power [dBm]', rotation= 270, labelpad=15)
        plt.clim(vmin=-140, vmax=-114)
        plt.savefig(str(frequencies_saving[j-1])+'POWER_AP_SYN_CRN'+str(i)+'_'+str(X1[i])+'.png')    
        plt.cla()
        plt.clf()
        plt.close('all')
        plt.close(fig)