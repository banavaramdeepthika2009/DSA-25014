'''
def launch(n):
    for i in range(n,-1,-1):
        
        if i==0:
            print("launch")
            
        else:
            print(i)
            
    
n=int(input("enter no.of seconds to launch:"))
launch(n)

'''

'''
def intrest(p,n):
    if n==0:
        return 1
    else:
        return p*intrest(p,n-1)
n=int(input("enter no.of years:"))
p=int(input("enter a number:"))
res=intrest(p,n)
print(res)
'''
'''
def search(m):
    
    key=m
    for i in range(n-1):
        if arr[i]==key:
            return i

n=int(input("enter no.of employees to add:"))
arr=[]
for i in range(n):
    a=int(input("enter a value:"))
    arr.append(a)
print(arr)
m=int(input("enter a element to search:"))

result=search(m)
print("employee id is stored at the index:",result)
'''
'''
def fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        
    return fact
n=int(input("enter a number to find its factorial:"))
result=fact(n)
print(result)
'''
'''
def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
             return fib(n-1)+fib(n-2)

n=int(input("enter no of terms:"))
if n<=-1:
    print("invalid input")
else:
    for i in range(n):
        print(fib(i),end=" ")
'''
