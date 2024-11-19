nums = [1,5,10]
for i in range(len(nums)):
    print(i, nums[i])

for i, v in enumerate(nums):
    print(i,v)

nums = 123456
digits = list(map(int, str(nums)))
print(digits)

digits = list(map(lambda x: int(x), str(nums)))
print(digits)

sum_square_digits = sum(map(lambda x: int(x)**2, str(nums)))
print(sum_square_digits)

dic = {1: "one", 2: "two"}
str_keys = list(map(str, dic))
print(str_keys)