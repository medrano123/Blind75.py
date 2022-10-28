
def pivotIndex(nums):
    total = sum(nums) 

    leftSum = 0
    for i in range(len(nums)):
        rightSum = total - nums[i] -leftSum
        if leftSum == rightSum:
            return i
        leftSum += nums[i]
    return -1



def main():
    nums = [1,7,3,6,5,6]
    sol = pivotIndex(nums)
    print(sol)

if __name__ == "__main__":
    main()