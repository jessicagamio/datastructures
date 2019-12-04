import unittest
"""
## using a helper function ##
def countzero(nums):
    #count the number of zeros in a list

    count = 0

    for i in nums:
        if i == 0:
            count += 1
    return count

def helper(nums):

    if len(nums) == 0:
        return 0

    num = nums.pop()

    if num == 0:
        return countzero(nums) + 1

    else:
        return countzero(nums)


class TestFunction (unittest.TestCase):
    def test_method(self):
        self.assertEqual(helper([1,2,0,3,0]),2)

"""

## same helper function calling itself

def helper(nums):

    if len(nums) == 0:
        return 0

    num = nums.pop()

    if num == 0:
        return helper(nums) + 1

    else:
        return helper(nums)


class TestFunction (unittest.TestCase):
    def test_method(self):
        self.assertEqual(helper([1,2,0,3,0]),2)

if __name__ =="__main__":
    unittest.main()
