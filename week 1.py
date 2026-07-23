"""
#print prime numbers in the given interval
a= int(input("enter a number:"))
for i in range(2,a+1):
    is_prime = True ;
    for j in range(2,i):
        if i%j ==0:
            is_prime = False;
            break
    if is_prime:
        print(i)
"""
"""
a= int(input("enter no.of rows:"))
for i in range(1,a+1,1):
    for j in range(1,i+1,1):
        if j<=i:
            print(i,end="*");
    print()
"""
"""
a="hello world hello world hello"
s= a.split();
new={}
for word in s:
    new[word] = new.get(word,0) +  1
print(new) 
"""
"""
a="greeks for geeks"
b="everyone can use greeks for geeks"
new1=a.split()
new2=b.split()
for word in new2:
    if word not in new1:
        print(word)
print()
"""
"""
def check_number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return n, n - 1


num = int(input("Enter a number: "))


result = check_number(num)
print(result)
"""

        
        
