#--------------- Pattern 1----------
for i in range(1, 21, 2):
    print(i, end=' ')
print()
#--------------- Pattern 2----------

for i in range(0,101,10):
    print(i , end= ' ')

print()

#--------------- Pattern 3----------
for i in range(20 , -1 , -1):
    print(i,end=" ")
print()

#--------------- Pattern 4----------
n_star = int(input("Number of stars: "))
for  i in range(n_star):
    print( "*" , end=" ")
print()

#--------------- Pattern 5----------
for i in range(n_star+1):
    for j in range(i):
        print("*",end="")
    print()
