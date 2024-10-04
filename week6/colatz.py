n = int(input())
nums = [str(n)]
while n != 1:
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = 3*n + 1
    nums.append(str(n))
    
if len(nums) > 15:
    nums = nums[-15:]
        
print('->'.join(nums))