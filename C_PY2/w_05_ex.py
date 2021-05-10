# Lee el email de las lineas que empieza por From:, lo añade a un diccionario y el loop final 
# determina el de mayor valor en el histograma.
name = input("Enter file:")
handle = open(name)
dic = dict()

for line in handle:
    line = line.rstrip()
    wds = line.split()

    if len(wds) < 3 or wds[0] != "From":
        continue
    #else :
    email = wds[1]
    dic[email] = dic.get(email,0) + 1
    # my solution    
    #if line.startswith('From:'):
        #c = line.split()
        #email = c[1]
        #dic[email] = dic.get(email,0) + 1

bigc = None
bige = None

for em,nu in dic.items():
    if bigc is None or nu > bigc:
        bige = em
        bigc = nu

print(bige, bigc)