def canSum(target_sum, nums, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    elif target_sum == 0:
        return True
    elif target_sum < 0:
        return False

    for i in nums:
        remainder = target_sum - i
        if canSum(remainder, nums, memo):
            memo[target_sum] = True
            return True
    memo[target_sum] = False
    return False


print(canSum(7, [2, 3]))  # T
print(canSum(7, [5, 3, 4, 7]))  # T
print(canSum(7, [2, 4]))  # F
print(canSum(8, [2, 3, 5]))  # T
print(canSum(300, [7, 14]))  # F
