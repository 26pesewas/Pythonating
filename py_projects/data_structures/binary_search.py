def linear_search(my_list, search_term):
    for index, element in enumerate(my_list):
        if element == search_term:
            return index

    return -1


def binary_search(my_list, search_term):
    left_index = 0
    right_index = len(my_list) - 1
    #mean of the left and right index
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = my_list[mid_index]

        if mid_number == search_term: # return the index of the midnumber if it is the same as the search term
            return mid_index

        # if midnumber is less than search term, reassign left index to index of number after midnumber
        if mid_number < search_term:
            left_index = mid_index + 1
        else: # if midnumber == search_term
            right_index = mid_index - 1

    return -1


numbers = [10,20,30,40,50,60,70]
number_search = 70

# linear search
index = linear_search(numbers,number_search)
if index == -1:
    print("Number not found in list")
else:
    print(f"Number found at index {index} using linear search")

# binary search
index = binary_search(numbers,number_search)
if index == -1:
    print("Number not found in list")
else:
    print(f"Number found at index {index} using binary search")



