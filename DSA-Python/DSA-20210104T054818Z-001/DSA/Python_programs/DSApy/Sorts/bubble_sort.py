
def bubbleSort(arr):

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


#Dec. array
myArray = [40, 20, 50, 60, 30, 10]

#calling function
bubbleSort(myArray)

#test case for function
for i in myArray:
    print(i, end=", ")