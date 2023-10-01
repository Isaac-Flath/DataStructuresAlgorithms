'''

You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
from collections.abc import Callable

# Simple
def merge1(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    del nums1[m:]
    nums1.extend(nums2[:n])
    nums1.sort()

# Fast
def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
	a, b, write_index = m-1, n-1, m + n - 1

	while b >= 0:
		if a >= 0 and nums1[a] > nums2[b]:
			nums1[write_index] = nums1[a]
			a -= 1
		else:
			nums1[write_index] = nums2[b]
			b -= 1

		write_index -= 1

def test_merge(fn: Callable[[]], result: list[int], nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        fn(num1,3,nums2,3)
        assert num1 == result


if __name__ == "__main__":
    # Test Case 1
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge1(nums1,3,nums2,3)
    assert nums1 == [1,2,2,3,5,6]
    
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    merge2(nums1,3,nums2,3)
    assert nums1 == [1,2,2,3,5,6]

    # Test Case 2
    nums1 = [1]
    nums2 = []
    merge1(nums1,1,nums2,0)
    assert nums1 == [1]
    
    nums1 = [1]
    nums2 = []
    merge2(nums1,1,nums2,0)
    assert nums1 == [1]

    # Test Case 3
    nums1 = [0]
    nums2 = [1]
    merge1(nums1,0, nums2, 1)
    assert nums1 == [1]
    
    nums1 = [0]
    nums2 = [1]
    merge2(nums1,0, nums2, 1)
    assert nums1 == [1]
