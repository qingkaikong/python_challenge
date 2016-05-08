import urllib, re
prefix = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
findnothing = re.compile(r"nothing is (\d+)").search
nothing = '12345'
while True:
    text = urllib.urlopen(prefix + nothing).read()
    print text
    match = findnothing(text)
    if match:
        nothing = match.group(1)
        print "   going to", nothing
    else:
        break