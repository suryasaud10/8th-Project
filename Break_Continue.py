# Break
i=1
while i<=5:
    print(i)
    if (i==3):
        break
    i+=1

print("End of loop")

# continue
i=0
while i<=5:
    if(i==3):
        i+=1
        continue
    print(i)
    i+=1

# odd number
i=1
while i<=20:
    if(i%2 !=0):
        i+=1
        continue
    print(i)
    i+=1
    
