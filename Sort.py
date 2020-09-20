#Bubble-sort
def bubbleSort(arr):
    swap = True
    while swap:
        swap = False
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swap = True
    return arr

arr = [8,4,1,7,9,-1]
print ("Bubble-sort:")
print (bubbleSort(arr))

#************#

#Selection-sort
def selectionSort(arr):
    for j in range(0,len(arr)-1):
        for i in range(j+1,len(arr)):
            if arr[j]>arr[i]:
                arr[j],arr[i] = arr[i],arr[j]
    return arr

arr = [8,4,1,7,9,-1]            
print ("Selection-sort:")
print (selectionSort(arr))

#************#

#Quick-sort
def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        smaller,equal,larger = [],[],[]
        pivot = arr[-1]
        for i in arr:
            if i<pivot:
                smaller.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                larger.append(i)
    return quickSort(smaller) + equal + quickSort(larger)

arr = [8,4,1,7,9,-1]            
print ("Quick Sort:")
print (quickSort(arr))

#***********#

#Binary-search
def binarySearch(n,arr,start,stop):
    if start >= stop:
        return (f"{n} not found in list")
    else:
        mid = int((start + stop)/2)
        if n > arr[mid]:
            return binarySearch(n,arr,mid+1,stop)
        elif n < arr[mid]:
            return binarySearch(n,arr,start,mid-1)
        else:
            return "value found"

arr = [1,2,3,4,5]
print ("Binary Search:")
print (binarySearch(8,arr,0,len(arr)))
            
        

                
                






