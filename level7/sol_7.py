import re
from PIL import Image
import urllib,StringIO
url = "http://www.pythonchallenge.com/pc/def/oxygen.png"

img = urllib.urlopen(url).read()
data = Image.open(StringIO.StringIO(img))

imageW = data.size[0]
imageH = data.size[1]

# if you look at the RGB color, for the grey to black squares, they have all 3 channel number equal, 
# this gives us a way to separate that out
# http://www.w3schools.com/colors/colors_picker.asp
rgbs = []
for y in range(0, imageH):
    for x in range(0, imageW):
        offset = y*imageW + x
        xy = (x, y)
        rgb = data.getpixel(xy)
        if (rgb[0] == rgb[1] ==rgb[2]):
            rgbs.append(rgb[0])
            
# get the 7th element in each group, since they are all the same
print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, rgbs[::7]))))))