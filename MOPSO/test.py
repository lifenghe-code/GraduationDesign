def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    n = len(nums)
    result = [0] * n
    for i in range(n):
        result[(i + k) % n] = nums[i]
    nums[:] = result
    print(result)


rotate([1, 2, 3, 4, 5, 6, 7], 3)
