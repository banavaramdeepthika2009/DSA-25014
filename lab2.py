'''
def bubble_sort():
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
n=int(input("enter no.of elements:"))
arr=[]
for i in range(n):
    a=int(input("enter a number:"))
    arr.append(a)
print("original list:",arr)

result=bubble_sort()
print("new sorted list:",result)

'''




'''
def insertion_sort():
    for i in range(n-1):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
n=int(input("enter no.of elements:"))
arr=[]
for i in range(n):
    a=int(input("enter a number:"))
    arr.append(a)
print("original list:",arr)

result=insertion_sort()
print("new sorted list:",result)
'''






'''
def selection_sort():
    for i in range(n-1):
        min=i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min=j
                arr[i],arr[min]=arr[min],arr[i]
    return arr
    
n=int(input("enter no.of elements:"))
arr=[]
for i in range(n):
    a=int(input("enter a number:"))
    arr.append(a)
print("original list:",arr)

result=selection_sort()
print("new sorted list:",result)

'''


def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=len(arr)//2
    left=[]
    middle=[]
    right=[]
    for i in range(len(arr)):
        if arr[i]<arr[pivot]:
            left.append(arr[i])
        
        elif arr[i]==arr[pivot]:
            middle.append(arr[i])
        else:
            right.append(arr[i])
    return quick_sort(left)+middle+quick_sort(right)

    
n=int(input("enter no.of elements:"))
arr=[]
for i in range(n):
    a=int(input("enter a number:"))
    arr.append(a)
print("original list:",arr)

result=quick_sort(arr)
print("new sorted list:",result)  
        
    
  







  





