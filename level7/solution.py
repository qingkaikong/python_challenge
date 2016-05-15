import re, Image

import urllib,StringIO
url = "http://www.pythonchallenge.com/pc/def/oxygen.png"

img = urllib.urlopen(url).read()
i = Image.open(StringIO.StringIO(img))

#i = Image.open("oxygen.png") # http://www.pythonchallenge.com/pc/def/oxygen.png
row = [i.getpixel((x, 45)) for x in range(0, i.size[0], 7)]
ords = [r for r, g, b, a in row if r == g == b]

print "".join(map(chr, map(int, re.findall("\d+", "".join(map(chr, ords))))))