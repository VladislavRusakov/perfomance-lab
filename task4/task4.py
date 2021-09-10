from sys import argv


nums = []
with open(argv[1], 'r') as f:
    for line in f.readlines():
        nums.append(int(line.strip()))


median = sorted(nums)[len(nums) // 2]
result = 0
for number in nums:
    result += abs(number - median)
print(result)
