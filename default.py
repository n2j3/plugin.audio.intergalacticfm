# Step 1 - load in xbmc core support and setup the environment 
import xbmcplugin
import xbmcgui
import sys

# magic; id of this plugin - cast to integer 
thisPlugin = int(sys.argv[1])

# Step 2 - create the support functions (or classes)
# replace Simon's list with mine

def createListing(): 
    """
    Creates a listing that XBMC can display as a directory listing
    @return list
    """
    listing = []
    listing.append(['IFM 1 | Murdercapital FM','http://radio.intergalactic.fm/1.m3u']) 
    listing.append(['IFM 2 | Intergalactic Classix','http://radio.intergalactic.fm/2.m3u'])
    listing.append(['IFM 3 | Radio Galaxia','http://radio.intergalactic.fm/3.m3u']) 
    listing.append(['IFM 4 | The Dream Machine','http://radio.intergalactic.fm/4.m3u'])
    return listing


def sendToXbmc(listing): 
    """
    Sends a listing to XBMC for display as a directory listing Plugins always result in a listing
    @param list listing 
    @return void
    """

    #access global plugin id 
    global thisPlugin

    # send each item to xbmc 
    for item in listing:
        listItem = xbmcgui.ListItem(item[0]) 
        xbmcplugin.addDirectoryItem(thisPlugin,item[1],listItem)

    # tell xbmc we have finished creating the directory listing 
    xbmcplugin.endOfDirectory(thisPlugin)

# Step 3 - run the program 
sendToXbmc(createListing())
