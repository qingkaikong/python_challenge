import pickle

data = pickle.load(open('./banner.p', 'rb'))

for item in data:
    st = ''
    for (a, b) in item:
        st += a*b
    
    print st +  '\n' 