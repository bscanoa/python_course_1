# Exercise 2
sh = input("Enter Hours:")
sr = input("Enter Rate:")
try:
    fh = float(sh)
    fr = float(sr)
except:
    print("Error, please write a numeric input")
    quit()


if fh>40 :
    reg = fr * fh
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else:
    xp = fr *fh

print("Pay:", xp)