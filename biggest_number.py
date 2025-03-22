# search biggest number in an array
def biggest_num(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        return max_num
