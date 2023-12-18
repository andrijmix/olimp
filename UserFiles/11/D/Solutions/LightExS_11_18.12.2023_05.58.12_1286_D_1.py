def lower_layer(nums):
    if nums == []:
        return 0
    count = 0

    for i in range(nums[0] + 1):
        count += calc_layer(nums, i)
    return count


def calc_layer(nums, first_num):
    possible_array = [None] * (len(nums) + 1)
    possible_array[0] = first_num
    for n in range(1, len(nums) + 1):
        possible_num = nums[n - 1] - possible_array[n - 1]
        if possible_num < 0:
            return 0
        possible_array[n] = possible_num
    return 1


nums = list(map(int, input().split()))
print(lower_layer(nums))
