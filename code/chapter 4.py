# Find Maximum Subarray
# 4.1-2
def violence(list):
    max = float("-inf")
    low, high = 0
    for i in range(len(list)):
        sum = 0
        for j in range(i, len(list)):
            sum += list[j]
            if (max < sum):
                max = sum
                low = i
                high = j
    return low, high, max

# P40 divide and conquer
def find_max_crossing_subarray(list, low, mid, high):
    left_sum = 0
    left_pos = mid
    sum = 0
    for i in reversed(range(low, mid)):
        sum += list[i]
        if sum > left_sum:
            left_sum = sum
            left_pos = i
    right_sum = list[mid]
    right_pos = mid
    sum = list[mid]
    for i in range(mid + 1, high + 1):
        sum += list[i]
        if sum > right_sum:
            right_sum = sum
            right_pos = i
    return left_pos, right_pos, left_sum + right_sum

def find_maximum_subarray(list, low, high):
    if low == high:
        return low, high, list[low]
    else:
        mid = int((low + high) / 2)
        left_low, left_high, left_sum = find_maximum_subarray(list, low, mid)
        right_low, right_high, right_sum = find_maximum_subarray(list, mid + 1, high)
        cross_low, cross_high, cross_sum = find_max_crossing_subarray(list, low, mid, high)
        if left_sum > right_sum and left_sum > cross_sum:
            return left_low, left_high, left_sum
        elif right_sum > left_sum and right_sum > cross_sum:
            return right_low, right_high, right_sum
        else:
            return cross_low, cross_high, cross_sum

# 4.1-5
def dynamic_programming(list):
    dp = []
    res = list[0]
    for i in range(len(list)):
        if i == 0:
            dp.append(list[0])
        else:
            dp.append(max(dp[i - 1] + list[i], list[i]))
            if dp[i] > res:
                res = dp[i]
    return res


if __name__ == "__main__":
    list = list(map(int, input().strip().split()))
    print(find_maximum_subarray(list, 0, len(list) - 1))

# 13 -3 -25 20 -3 -16 -23 18 20 -7 12 -5 -22 15 -4 7

