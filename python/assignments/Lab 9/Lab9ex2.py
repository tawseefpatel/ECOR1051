def big_diff(nums):
  """
  """
  diff = 0
  for i in nums:
    for j  in nums:
      if (i > j):
        if (abs(i - j) > diff):
          diff = abs(i - j)
  return diff
nums = [40,2,5,6,9]
print(big_diff(nums))