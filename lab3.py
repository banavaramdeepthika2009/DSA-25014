'''
def bubble_sort():
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
arr=[]
n=int(input("enter no.of elements to add"))
for i in range(n):
    a=int(input("enter a element:"))
    arr.append(a)
print("the original array is",arr)

result=bubble_sort()
print("the new sorted array is",result)
'''
'''

def insertion_sort():
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
arr=[]
n=int(input("enter no.of elements to add"))
for i in range(n):
    a=int(input("enter a element:"))
    arr.append(a)
print("the original array is",arr)

result=insertion_sort()
print("the new sorted array is",result)
'''
'''
def selection_sort():
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
    return arr
arr=[]
n=int(input("enter no.of elements to add"))
for i in range(n):
    a=int(input("enter a element:"))
    arr.append(a)
print("the original array is",arr)

result=selection_sort()
print("the new sorted array is",result)
'''
'''
def quick_sort(arr):
    left=[]
    right=[]
    middle=[]
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    pivot=arr[mid]
    for i in range(len(arr)):
        if arr[i]<pivot:
            left.append(arr[i])
        elif arr[i]>pivot:
            right.append(arr[i])
        else:
            middle.append(arr[i])
    return quick_sort(left)+quick_sort(middle)+quick_sort(right)
arr=[]
n=int(input("enter no.of elements to add"))
for i in range(n):
    a=int(input("enter a element:"))
    arr.append(a)
print("the original array is",arr)

result=quick_sort(arr)
print("the new sorted array is",result)
    
'''
def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left=arr[:mid]
    right=arr[mid:]
    merge_sort(left)
    merge_sort(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            arr[k]=left[i]
            i+=1
        else:
            arr[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        arr[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        arr[k]=right[j]
        j+=1
        k+=1
    return arr
arr=[]
n=int(input("enter no.of elements to add"))
for i in range(n):
    a=int(input("enter a element:"))
    arr.append(a)
print("the original array is",arr)

result=merge_sort(arr)
print("the new sorted array is",result)    
