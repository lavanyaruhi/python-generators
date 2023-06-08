# running average of numbers using generators 
def running_average(nums):
    total_sum = 0
    count = 0
    for num in nums:
        total_sum += num
        count += 1
        yield total_sum / count

l1=[2,3,4,5,7,9]
avg=running_average(l1)
for i in avg:
    print(i)