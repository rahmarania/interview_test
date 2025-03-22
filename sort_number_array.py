# sorting number from smallest to biggest
def sorting_arr(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            min_index = j
    # swap position
    arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# illustration
# [c,a,e,b,d]
# check the a's index, a is smallest number
# swap a into the first index of the array
# [c,e,b,d] check with similar step
# [e,b,d]
# [b,d]
# [d]
