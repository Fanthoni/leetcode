from collections import defaultdict

# Failed


def findSubarraySum(arr, Sum):

    # Dictionary to store number of subarrays
    # starting from index zero having
    # particular value of sum.
    prevSum = defaultdict(lambda: 0)

    res = 0

    # Sum of elements so far.
    currsum = 0

    for i in range(0, len(arr)):

        # Add current element to sum so far.
        currsum += arr[i]

        # If currsum is equal to desired sum,
        # then a new subarray is found. So
        # increase count of subarrays.
        if currsum == Sum:
            res += 1

        # currsum exceeds given sum by currsum  - sum.
        # Find number of subarrays having
        # this sum and exclude those subarrays
        # from currsum by increasing count by
        # same amount.
        if (currsum - Sum) in prevSum:
            res += prevSum[currsum - Sum]

        # Add currsum value to count of
        # different values of sum.
        prevSum[currsum] += 1

    return res


print(findSubarraySum([2, 1, 5, -3, 0, 6], 3))
