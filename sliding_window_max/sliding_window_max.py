'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
def sliding_window_max(nums, k):
    # Your code here
    # create index tracker - set to 0
    i = 0
    # create empty list for our maxes
    max_list = []
    # create loop: while i != len(nums) + 1
    while i+k != (len(nums) + 1):
        # create 'window'
        window = nums[i:i+k]
        max_val = window[0]
        for val in window:
            if val > max_val:
                max_val = val
        max_list.append(max_val)
        i += 1

    return max_list


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    # arr = [1, 3, -1, -3, 5, 3, 6, 7]
    # k = 3

    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 2
    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
