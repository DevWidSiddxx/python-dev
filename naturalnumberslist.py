a=[]
n=int(input("Enter n values:"))
for i in range(n):
    num=int(input())
    a.append(num)
    

print(a)
Sum=0;
for i in a:
    Sum=Sum+i;
print("The sum of n values is:",Sum)
    
    
