import cartopy.crs as ccrs
import matplotlib.pyplot as plt

_all__ = ['mapping']

"""
    Functions to set up the cartopy axes and plot the data on to them,
    as well as conduct normal matplotlib formatting
"""


def map_plotter(x, y):
    # setting up the axes to plot into 
    ax = plt.axes(projection=ccrs.OSGB()) 
    ax.set_extent([307000.0, 336000.0, 657000.0, 684000.0], crs = ccrs.OSGB())
    
    # looping through the dictionary data for plotting
    for b in range(len(x)):
        plt.plot(x[b], y[b], color='black', linewidth=0.8, transform=ccrs.OSGB())
    
    # loading the SAVI basemap
    fname = 'edin_SAVI_277.tif' # satellite image for basemap
    img_extent = (307059.5282843578606844,335615.2470486343372613,656490.9100024187937379,683219.2234168014256284)
    img = plt.imread(fname)
    ax.imshow(img, origin='upper', extent=img_extent, transform=ccrs.OSGB())
    ax.set_xticks([308000, 335000], crs=ccrs.OSGB())
    ax.set_yticks([658000, 681000], crs=ccrs.OSGB())
    
    # manual labels as cartopy doesn't support OSGB grid labels yet
    ax.text(307000, 669000, 'Northing', va='bottom', ha='center',
        rotation='vertical', rotation_mode='anchor',
        transform=ccrs.OSGB())
    ax.text(321500, 655500, 'Easting', va='bottom', ha='center',
        rotation='horizontal', rotation_mode='anchor',
        transform=ccrs.OSGB())

    return(map_plotter)
    
def map_format(title):
    # generating general formats for the output plot
    plt.title(title)
    plt.ylim(658000, 681000)
    plt.xlim(308000, 335000)
    plt.arrow(332900,677000,0,1700, head_width = 900, color='black')
    plt.text(332500,676000,'N',color='black')
    plt.show()
    return (map_format)
