# Write a Python class to find a pair of elements (indices of the two numbers)
# from a given array whose sum equals a specific target number.

class py_solution(object):
   def twoSum(self, nums, target_num):      
       """
       :type nums: list[int]
      :type target: int
      :return type: list[int]
      """
       result_dict = dict()
       pos = 0
       while pos < len(nums):
           if (target_num - nums[pos]) not in result_dict:
               result_dict[nums[pos]] = pos
               pos += 1
           else:
               return [result_dict[target_num - nums[pos]], pos]
print(py_solution().twoSum([10,20,10,40,50,60,70],50))
print(py_solution().twoSum([10,20,10,40,50,60,70],52))
print(py_solution().twoSum([10,20,10,40,50,60,70],130))
