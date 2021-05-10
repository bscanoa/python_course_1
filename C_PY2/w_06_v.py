fname = input("Enter file:")
if len(fname) < 1 : fname = 'clown.txt'
hand = open(fname)
di = dict()

for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        di[w] = di.get(w,0) + 1 
        # if w in di:
        #     dic[w] = dic[w] + 1
        # else:
        #     dic[w] = 1

# x = sorted(di.items())
# print (x[:5])
tmp = list()
for k,v in di.items():
    # print(k,v)
    newt = (v,k)
    tmp.append(newt)

tmp = sorted(tmp, reverse=True)
print(tmp[:5])

for v,k in tmp[:5]:
    print(k,v)