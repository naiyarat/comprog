# 000099999888765
nums = [str(i) for i in range(10)]
s = input()
for char in s:
    if char in nums:
        nums.remove(char)

if not nums:
    print('None')
else:
    print(','.join(nums))