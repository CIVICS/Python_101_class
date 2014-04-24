numbers = [1, 2, 3, 4, 5]
print(numbers)
print(len(numbers))

for i in range(len(numbers)):
    numbers[i] = numbers[i]**2

print(numbers)

#same idea only using in and append
alist = [4,2,8,6,5]
blist = [ ]
for item in alist:
   blist.append(item+5)
print(blist)
