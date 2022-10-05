def binary_search (list_of_nums,key ):
    left = 0
    attempts = 0
    right = len(list_of_nums) - 1
    print(right)
    while left <= right:
        middle = (left + right) // 2
        print(middle)
        
        if list_of_nums[middle] == key:
            print("Key found in {} attempts".format(attempts))
            return middle
        if list_of_nums[middle] > key:
            right = middle - 1
        if list_of_nums[middle] < key:
            left = middle + 1
        attempts += 1
    return -1

binary_search([5,7,8,9,13,14,643], 8)