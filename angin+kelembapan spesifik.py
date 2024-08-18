import pylab
import numpy as np
from netCDF4 import Dataset
import numpy.ma as ma
import datetime
from mpl_toolkits.basemap import cm, Basemap

file_nc = 'E:/Magang/H4/data sebenarnya.nc'

f = Dataset(file_nc,'r')

lon  = ma.getdata(f.variables['longitude'][:])
lat  = ma.getdata(f.variables['latitude'][:])
p = ma.getdata(f.variables['level'][:])
time = ma.getdata(f.variables['time'][:])
q = ma.getdata(f.variables['q'][:])
u = ma.getdata(f.variables['u'][:])
v = ma.getdata(f.variables['v'][:])

#variable waktu
t0 = datetime.datetime(1900,1,1,00,00)
time = np.array(time,dtype=('f'))
t = []
for i in time:
    t1=t0+datetime.timedelta(hours=i*1)
    t.append(t1)
ts = [i.strftime('%Y-%m-%d-%H:%M') for i in t]
ts2 = [i.strftime('%Y%m%d%H%M') for i in t]

#plot kelembapan spesifik
for i in range (len(time)):

    level = 2 #level ketinggian (pressure)
    uapair = q[i][level]
    wind_u = u[i][level]
    wind_v = v[i][level]
    speed = np.sqrt(wind_u*wind_u + wind_v*wind_v)

    ####basemap setting   
    
    #clev = np.arange(0,1201,100)

    cs_p = m.contourf(x,y,uapair)#,cmap='GnBu',extend='max')
    cs_w = m.quiver(x[points],y[points],wind_u[points],wind_v[points],color='k',scale=300,linewidth=0.8)
    pylab.quiverkey(cs_w, 0.76, 0.18, 10, r'10 $m.s^{-1}$', labelpos='E',
                    coordinates='figure')

    cbar = m.colorbar(cs_p,location="bottom",pad="15%")
    cbar.set_label("$Kg/m^{-2}$",fontsize=8)

    pylab.title("Angin dan Kelembapan Spesifik - "+str(p[level])+'mb'+'\n'+ts[i]
                +" UTC",fontsize=8)

    pathhasil = 'E:/Magang/H5/1000/'
    pylab.savefig(pathhasil+'angin dan kelembapan spesifik_'+ts2[i]+'.png',dpi=300,bbox_inches='tight')

    pylab.close()
