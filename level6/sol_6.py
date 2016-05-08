import glob
import zipfile

nothing = '90052'
'''
while True:
    filename = './channel/' + nothing + '.txt'
    f = open(filename, 'rb')
    data = f.read()
    nothing = data.split(' ')[-1]
    f.close()
    
    if not nothing.isdigit():
        print data
        break
    print nothing
'''
file = zipfile.ZipFile('./channel.zip', 'r')
comments_list = []
while True:
    name = nothing + '.txt'
    data = file.read(name)
    nothing = data.split(' ')[-1]

    if not nothing.isdigit():
        print data
        break
    comments_list.append(file.getinfo(name).comment)
    print nothing
    
print ''.join(comments_list)


        
    
    