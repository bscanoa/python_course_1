# Assigment 3.3

score = input ("Enter the score: ")

s = float(score)

if s > 1.0:
    print("Out of range")
    quit()
elif s >= 0.9:
    print("A")
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
else:
    print("F")
    
