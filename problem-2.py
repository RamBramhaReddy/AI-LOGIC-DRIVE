def max_sum(nums, k):

    cs = 0

    for i in range(k):
        cs += nums[i]

    max = cs

    for i in range(k, len(nums)):
        cs = cs - nums[i - k]
        cs = cs + nums[i]

        if cs > max:
            max = cs

    return max


n = int(input())
nums = list(map(int, input().split()))
k = int(input())

print(max_sum(nums, k))
