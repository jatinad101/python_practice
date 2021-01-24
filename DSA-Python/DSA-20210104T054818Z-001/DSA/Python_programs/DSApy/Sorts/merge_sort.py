
def mergesort(arr):
    if len(arr) > 1:
        midpoint = len(arr)//2
        LEFT = arr[:midpoint]
        RIGHT = arr[midpoint:]

        mergesort(LEFT)
        mergesort(RIGHT)

        i = j = k = 0

        while i < len(LEFT) and j < len(RIGHT):
            if LEFT[i] < RIGHT[j]:
                arr[k] = LEFT[i]
                i += 1
            else:
                arr[k] = RIGHT[j]
                j += 1
            k += 1

        while i < len(LEFT):
            arr[k] = LEFT[i]
            i += 1
            k += 1

        while j < len(LEFT):
            arr[k] = LEFT[j]
            j += 1
            k += 1


            # TODO: WAF to print array
            # TODO: Write driver code to test this function