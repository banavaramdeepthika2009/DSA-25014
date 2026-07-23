'''
def fun(x):
    x[0]=20;
b=[10,30,40,50,20]
fun(b)  #lists are mutable
print(b)

def fun2(x):
    x=20;
a=10
fun2(a)  #integers are immutable
print(a)
'''
'''
def B():
    print("inside method A")
def A():
    print("inside method B")
    return B;
func=A()
func();
'''
'''
def fun(x):
    if x==0:
        return 0;
    else:
        return 2*x
b=fun(8);
print(b)
'''
'''
n=input("enter something:")
def fun(n):
    if len(n)==0:
        print("hello");
    else:
        print(n)
fun(n)
'''
'''
a=int(input("enter a value:"))
b=int(input("enter a value:"))
def sum(a,b):
    c= a+b
    return c
result=sum(a,b)
print(result)

'''
'''
#print first digit of a number
n=int(input("enter a number:"))
temp=n;
def fun(n):
    if n==0:
        return 0
    elif n>=10:
        digit=n%10;
        n=n//10
        return fun(n) 
    else:
        return n
result=fun(n)
print(result)
        
'''
'''
def fun(n):
    for i in range(1,n+1,1):
        print("GFG\t")
n=int(input("enter a number:"))
fun(n)
'''

list=[]
for i in range(1,101,1):
    list.append(i);
for m in range(2,10,1):
    list.remove(list[m])
n=int(input("enter a number"))

def fun(n):
    if n in list:
        print("lucky number:")
    else:
        print("not a lucky number")
fun(n)
    
       



































