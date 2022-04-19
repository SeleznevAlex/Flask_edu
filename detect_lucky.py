def detect_lucky(number):
    sum_left = 0
    sum_right = 0
    nums = str(number)
    for i in range(3):
        sum_left += int(nums[i])
    for j in range(3, 6):
        sum_right += int(nums[j])
    return sum_left == sum_right


print(detect_lucky(985778))
