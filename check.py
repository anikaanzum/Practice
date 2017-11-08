a = [4,2,3,1,5,6,5]
length=len(a)
print("array length: ",length)
i=0
while(i<length):
    if 5 in a:
        b=a.index(5)
        print("exist")
        print("index:",b)
    i=i+1