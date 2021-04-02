#Week 5 - Conditional Statements
# Assigment 3.1

# My Solution

hrs=input("Enter Hours:")
h=float(hrs)
rat=input("Enter Rate:")
r=float(rat)

if h>40:
    he=h-40
    he=he*(r*1.5)
    print((40*r)+(he))
else:
    print(h*r)

# Instructor solution

sh = input("Enter Hours:")
sr = input("Enter Rate:")
fh = float(sh)
fr = float(sr)

if fh>40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fr *fh

print("Pay:", xp)



# Exercise 2
sh = input("Enter Hours:")
sr = input("Enter Rate:")
try:
    fh = float(sh)
except:
    print("Error, please write a numerical character")
fr = float(sr)

if fh>40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fr *fh

print("Pay:", xp)


