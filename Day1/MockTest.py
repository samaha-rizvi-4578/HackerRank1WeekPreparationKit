#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
def findMedian(arr):
    # Sort the array
    arr.sort()
    length = len(arr)
    
    # Check if the length is odd
    if length % 2 != 0:
        middle_index = length // 2 # Use integer division
        median = arr[middle_index]
    else: # If the length is even
        first_middle_index = (length // 2) - 1
        second_middle_index = length // 2
        median = (arr[first_middle_index] + arr[second_middle_index]) // 2
 
    return median