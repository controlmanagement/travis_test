# -*- coding: utf-8 -*-


import pylab
import matplotlib.ticker
import matplotlib.dates
import pandas
import astropy.time
import astropy.units
import astropy.coordinates

# 時刻
today = pandas.to_datetime('today')
tomorrow = today + pandas.tseries.offsets.Day()
date1 = pandas.date_range(today, tomorrow, freq='10min')
date2 = astropy.time.Time(date1.to_datetime().tolist(), format='datetime')

# NANTEN2 座標
NANTEN2_LONGITUDE = -67.70308139 # deg
NANTEN2_LATITUDE = -22.96995611  # deg
NANTEN2_HEIGHT = 4863.85 # m

longitude = astropy.coordinates.Longitude(NANTEN2_LONGITUDE * astropy.units.deg)
latitude = astropy.coordinates.Latitude(NANTEN2_LATITUDE * astropy.units.deg)
height = NANTEN2_HEIGHT * astropy.units.m
nanten2 = astropy.coordinates.EarthLocation(longitude, latitude, height)

# 軌道
jup = astropy.coordinates.get_body('jupiter', date2)
jup.location = nanten2
jup.pressure = 0 * astropy.units.Pa

# plot
pylab.rcParams['font.family'] = 'arial'

date_locator = matplotlib.dates.HourLocator()
date_formatter = matplotlib.dates.DateFormatter('%H')

az_locator = matplotlib.ticker.MultipleLocator(90)

fig = pylab.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
ax1.plot(date1, jup.altaz.alt, label='jupiter')
ax2.plot(date1, jup.altaz.az, label='jupiter')
ax1.xaxis.set_major_locator(date_locator)
ax2.xaxis.set_major_locator(date_locator)
ax1.xaxis.set_major_formatter(date_formatter)
ax2.xaxis.set_major_formatter(date_formatter)
ax2.yaxis.set_major_locator(az_locator)
ax1.grid(True)
ax2.grid(True)
ax1.set_ylabel('El (deg)')
ax2.set_ylabel('Az (deg)')
ax2.set_xlabel('UTC (hour)')
ax1.set_title('%s UTC'%(date1[0].strftime('%Y/%m/%d')))
ax1.legend()
ax1.set_ylim(0, 90)
ax2.set_ylim(0, 360)
# fig.savefig('elplot_jupiter_%s.png'%(date1[0].strftime('%Y%m%d')))
pylab.show()
