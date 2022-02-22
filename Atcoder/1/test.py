# Array Challenge
# Have the function ArrayChallenge(arr) take the array of numbers stored in arr which will contain integers that represent the amount in dollars that a single stock is worth, and return the maximum profit that could have been made by buying stock on day x and selling stock on day y where y > x. For example: if arr is [44, 30, 24, 32, 35, 30, 40, 38, 15] then your program should return 16 because at index 2 the stock was worth $24 and at index 6 the stock was then worth $40, so if you bought the stock at 24 and sold it at 40, you would have made a profit of $16, which is the maximum profit that could have been made with this list of stock prices.

# If there is not profit that could have been made with the stock prices, then your program should return -1. For example: arr is [10, 9, 8, 2] then your program should return -1.
# Once your function is working, take the final output string and combine it with your ChallengeToken, both in reverse order and separated by a colon.

# Your ChallengeToken: 4y8jmxhq10
# Examples
# Input: [10,12,4,5,9]
# Output: 5
# Final Output: 5:01qhxmj8y4
# Input: [14,20,4,12,5,11]
# Output: 8
# Final Output: 8:01qhxmj8y4
# Browse Resources
# Search for any help or documentation you might need for this problem. For example: array indexing, Ruby hash tables, 

def ArrayChallenge(arr):
    N = len(arr)
    ans = [0 for _ in range(N)]
    for i in range(N):
        for j in range(i+1, N):
            if arr[j] - arr[i] > ans[i]:
                ans[i] = arr[j] - arr[i]
    return max(ans) if max(ans) != 0 else -1
