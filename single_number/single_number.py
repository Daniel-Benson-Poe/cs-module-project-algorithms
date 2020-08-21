'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # iterate through array, checking each element
    # against its neighboring element
    # This will require us to use i and i+1

    # start by sorting our array
    arr = sorted(arr)
 
    # iterate through our array with a step of 2
    for i in range(0, len(arr), 2):
        # compare value at index i to value at 
        # index i + 1 to determine if they're the same
        try:
            if arr[i] != arr[i + 1]:
                # in this case there is only one
                # possible scenario; the value at 
                # index i must be the odd number out
                return arr[i]

        # If an IndexError exception is thrown, that means
        # we have reached the second to last element of 
        # our array without finding the odd number out; because
        # this means there is only one number left to check, 
        # we can conclude that the value in the last index of
        # the array will be the odd number out, so we return
        # the value at that index
        except(IndexError):
            return arr[-1]


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")