
# Número mayor y número menor

largest= None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        value = int(num)
        maxi = value
        mini = value

        if largest is None:
            largest = maxi
        elif maxi > largest:
            largest = maxi
        
        if smallest is None:
            smallest = mini
        elif mini < smallest:
            smallest = mini
    except:
        print("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)

# Excersie 5.1

num = 0
num = 0.0
while True :
    sval = input("Enter a number: ")
    if sval == 'done':
        break
    try:
        fval = float(sval)
    except:
        print('Invalid input')
        continue
    # print(fval)
    num = num + 1
    tot = tot + fval
# print ('All Done')
print (tot, num,tot/num)