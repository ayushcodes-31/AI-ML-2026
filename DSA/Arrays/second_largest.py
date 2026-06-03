nums=[1,2,4,70,7,9]
max=nums[0]
sec_max=nums[0]
for i in nums:
    if i>=max:
        sec_max=max
        max=i
    elif i>=sec_max and  i!=max:
        sec_max=i
print(sec_max)
        
    