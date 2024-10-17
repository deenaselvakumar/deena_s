def remove_smallest(arr):
    if arr:
        arr.remove(min(arr)) 
    return arr

# Example usage:
arr = [5,3,4,5,2,4,3,2,1,4,1]
result = remove_smallest(arr)
print(result) 