import urllib
import re

url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

# get the first nothing
responses = urllib.urlopen(url)
data = responses.read()
old_nothing = re.findall('nothing=\w+', data)[0].split('=')[-1]
url = url + '?nothing=' + old_nothing

# loop through the chains, and see if we can find anything
for i in range(400):
    responses = urllib.urlopen(url)
    data = responses.read()
    nothing = data.split(' ')[-1]
    url = url.replace(old_nothing, nothing)
    old_nothing = nothing
    print url