print("Execution Started")

import numpy as np
import matplotlib as plt

##########################
# Amazon Basin Declarations
##########################
basin = 'amz'
# Georeferences
xllcorner = -79.5
yllcorner = -20.75
cellsize = 0.25  #1/8 Degree
nodata_value = -9999

georef = np.array([xllcorner,yllcorner,cellsize,nodata_value]);

# Read in Flow Directions and Gauge Info for Basin
flow_dir = np.genfromtxt(basin+'.dir')
flow_dir[flow_dir < 0] = np.NAN
[nrows,ncols] = flow_dir.shape
ncells = np.nansum(np.nansum(flow_dir*0+1))

gauge_list = np.genfromtxt(basin+'_gauge_list.txt')

# Constant Declarations
flow_vel = 1.5  # Flow Velocity (m/s)
flow_dif = 0.1  # Flow Diffusivity (m/s)
tstep = 86400   # Timestep Size (s)


# Read Gauge Data and Remove Unused Gauges
gauge_list = np.load(basin+'_gauge_list.txt')







# Perform Basin and Gauge Analysis














print("Execution Complete")
