<h1>Tidal Flood Analysis (Wind and Humidity)</h1>
<p align="right">
Supervised by: <br/>
<p align="right">
Prof. Dr. Ir. Eddy Hermawan, M.Sc.
<br/>
<p align="right">
Risyanto, S.Si., M.Sc.
<br/>

<h2>Description</h2>
On May 23, 2022, a significant tidal flood occurred in Semarang, Indonesia. One of the causes was extreme weather, which led to the breach of a levee in the Tanjung Emas Port area. The floodwaters covered a total area of 300 hectares, affecting nine neighborhoods (RW) with a population of 8,335 people. In response to this event, the aim of this project is to analyze the upper atmosphere at the 850 mb, 925 mb, and 1000 mb (surface) levels, focusing on wind and humidity. This analysis will help to understand the cloud formation and movement patterns two days before the event, with hourly observations starting from 7 AM WIB on May 21, 2022.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Phyton</b> 
- <b>PSTA LAPAN (BRIN)</b>

<h2>Environments Used </h2>

- <b>Windows 10</b>

<h2>Data</h2>
- The data used in this study includes hourly wind data (u and v components) and specific humidity (p) from 00 UTC on May 21, 2022, to 23 UTC on May 22, 2022, sourced from the Himawari 8 satellite. The data, provided in netCDF (.nc) format, was downloaded via access from BRIN (PSTA) or can be obtained through this link (https://www.eorc.jaxa.jp/ptree/).

<p align="center">
<img src="https://drive.google.com/uc?id=17npXbfv2B2kUhQ5sYfbyHBYCAt9fPM_e"/>
<br />

<h2>Program walk-through:</h2>

<p align="left">
The project is relatively straightforward: it aims to determine which satellite bands are most suitable for flood analysis and to understand the configuration of Himawari satellite data. Following this, I visualized the wind and humidity in the same figure and created a .gif from the images. This allows for the observation of wind and humidity patterns at different air pressure levels (which indicate altitude) prior to the flood, and helps to understand how clouds formed during that period.
<br/>
  
<h3>Imported and Data Extraction</h3>
<p align="left">
I began by importing the necessary libraries for data manipulation and visualization, including pylab, numpy, and netCDF4. The primary dataset, stored in a file called 'data sebenarnya.nc', contains key meteorological variables such as longitude, latitude, pressure levels, time, specific humidity (q), and wind components (u for the zonal wind and v for the meridional wind).
<br/>

<p align="left">
Using the Dataset function from the netCDF4 library, I opened the netCDF file and extracted the relevant variables. These variables include:
<ul>
  <li><strong>Longitude and Latitude:</strong> To define the geographical grid.</li>
  <li><strong>Pressure Levels:</strong> To analyze different atmospheric layers.</li>
  <li><strong>Time:</strong> To track changes over the specified period.</li>
  <li><strong>Specific Humidity (q):</strong> To assess moisture content in the air.</li>
  <li><strong>Wind Components (u and v):</strong> To understand the wind direction and speed.</li>
</ul>
</p>

<p align="center">
<img src="https://drive.google.com/uc?id=1XPQDQE0D1EXGDkcAOZfgPvfG0-JkxH7Y"/>
<br />
  
<p align="left">
The code initialized a reference datetime (`t0`) and converted the `time` array into a list of `datetime` objects by adding the hours specified in `time` to `t0`. It then formatted these datetime objects into two lists of strings: `ts` for 'YYYY-MM-DD-HH:MM' format and `ts2` for 'YYYYMMDDHHMM' format. This conversion provided a more readable representation of the time data for further analysis.
<br/>

<p align="center">
<img src="https://drive.google.com/uc?id=19jDYmaG1RCTNOc1j6Ak-CUybpWT1WJFD"/>
<br />

<h3>Data Visualization</h3>
<p align="left">
The code snippet generated and saved plots of wind speed and specific humidity at a specified pressure level for each time step:

1. **Plot Generation:**  
   For each time step, the code extracted data for a specific pressure level (e.g., 2) from the arrays `q` (specific humidity), `u` (zonal wind), and `v` (meridional wind). It calculated the wind speed using these components.

2. **Basemap Plotting:**  
   The code then plotted the specific humidity using a contour plot (`cs_p`) and the wind vectors using a quiver plot (`cs_w`). It also added a colorbar to indicate the specific humidity levels and a quiver key to show the wind speed scale.

3. **Title and Save Plot:**  
   Each plot was titled with the pressure level and timestamp, and saved as a PNG file in a specified directory with high resolution (300 dpi). The file was named using the formatted timestamp.

4. **Close Plot:**  
   After saving the plot, the code closed the figure to free up resources before generating the next plot.

This process was repeated for each time step, creating a series of plots that visualized the changes in wind and specific humidity over time.
<br/>

<p align="center">
<img src="https://drive.google.com/uc?id=1FffBr3hkN7qWQLABZp7ypF6FKXIbWzyX"/>
<br />

<p align="left">
The displayed results are illustrative of the analysis, covering only the period from 00 UTC to 12 UTC on May 22, 2022. The analysis includes data for the 850 mb level (left), 925 mb level (center), and 1000 mb level (right). Please note that the grid of the base map is not uniformly sized, and the legends are not yet standardized across the same range. For creating a comparable GIF, ensure that the legends are set to the same range across all frames.
<br/>

<p align="center">
  <img src="https://drive.google.com/uc?id=1dw2yxAZcGkuQCAdbrKMhwW40_-mGc4k4" width="30%" />
  <img src="https://drive.google.com/uc?id=1_gP7I5xiJv2vFO5R2JOEqyFPe_QVZ-2G" width="30%" />
  <img src="https://drive.google.com/uc?id=1W8RoaawAEeOcZusYntQ08Jl4M5AnspC8" width="30%" />
</p>
