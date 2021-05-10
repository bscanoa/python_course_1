name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
dic = dict()

for line in handle:
    line = line.rstrip()
    wsp = line.split()

    if len(wsp) < 3 or wsp[0] != "From":
        continue
    
    time = wsp[5]
    smc = time.split(':')
    hour = smc[0]
    dic[hour] = dic.get(hour, 0) + 1

for v,k in sorted(dic.items()):
    print(v,k)