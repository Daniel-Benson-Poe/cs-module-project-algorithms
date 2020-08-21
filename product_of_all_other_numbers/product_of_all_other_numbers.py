'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # create new array and set it to a copy of input array
    # this avoids making any changes to the original array
    new_arr = arr.copy()
    # create a new empty list we will use to append our products
    mult_list = []
    # create first for loop that runs through the length of input array
    for i in range(len(arr)):
        # set result, which we will use in our productization, to 1
        # through each new iteration
        result = 1
        # remove the value at index i from the new_arr array
        new_arr.pop(i)
        # create a nested for loop using the new array minus the value at 
        # index i
        for x in new_arr:
            # multiply result by x in each iteration through the new_arr array
            result = result * x
        # append the final result to our mult_list to create our list of products
        mult_list.append(result)
        # reset new_arr to a copy of the original array
        new_arr = arr.copy()
        
    # return mult_list    
    return mult_list


if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
