nums = [1,2,4,6]
# p = [0] * len(nums)
# # p[0] = nums[0]
# for i in range(len(nums)):
#     p[-i-1] = p[-i] + nums[-i-1]
    
#     print(p)

# # [1, 3, 7, 13]


def productExceptSelf(nums):
    prefix = [1] * len(nums)
    postfix = [1] * len(nums)
    final_list = [0] * len(nums) 
    for i in range(len(nums)):
        prefix[i] = prefix[i-1] * nums[i]
        postfix[-i-1] = postfix[-i] * nums[-i-1]

        final_list[i-1] = prefix[i-2] * postfix[i]
    return final_list
    
print(productExceptSelf(nums))