# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
g = None
n = None
for line in fh:    
    if line.startswith("X-DSPAM-Confidence:"):       
        if n is None:
        	n = 1
        else:
            n = n + 1
        #print (n)
        
        h = line.find(':')
        t = line[h + 1: ]
        fl = float(t)
        
        if g is None:
            g = fl
        else:
            g = g + fl
            #print (g)
tl = g/n
print("Average spam confidence:", tl)
