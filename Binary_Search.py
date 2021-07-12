
#recurssive algorithm
def binary_search(arr,high,low,x):
    if high>=low:
        mid = (high+low)//2
        print(f"current mid {mid}")

        if arr[mid] == x:
            return mid
        elif arr[mid]> x:
            return binary_search(arr,mid-1,low,x)
        else:
            return binary_search(arr,high,mid+1,x)
    else:
        return -1

        

if __name__ == '__main__':
    arr = [2,3,4,5,6,7,8,9]
    x= 7

    result = binary_search(arr,len(arr)-1,0,x)

    if result != -1:
        print(f'The element {x} found at the index {result}')
    else:
        print(f"the element {x} not dfound in this array")
