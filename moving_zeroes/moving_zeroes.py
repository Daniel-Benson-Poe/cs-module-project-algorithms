'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Here we are inputting an array with any possible
    # number of zeros mixed in with non-zero numbers. 
    # We are being asked to group each non-zero number
    # together on the left side of the array and each
    # zero value on the right side of the array.
    # We will have to iterate through the list one index
    # at a time to check if index i is 0. 
    # Essentially our goal is to move each zero to the 
    # right side of the array one at a time, until all
    # the values are grouped correctly.
    # Your code here
    # set a new array to empty
    new_arr = [] 
    # start our iteration through the array
    for i in range(len(arr)):
        if arr[i] == 0: # Check condition: if the value at index i is 0
            new_arr.append(arr[i]) # we append the value (0) to the end of our new array
        else: # if above condition not met: i.e. the value is nonzero
            new_arr.insert(0, arr[i]) # we insert the value into new array at index 0

    return new_arr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")