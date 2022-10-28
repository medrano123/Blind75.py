
def runningSum(nums):
    sum = 0
    newsum = []
    for i in nums:
        sum += i 
        newsum.append(sum)
    return(newsum)

def main():
    nums = [1,2,3,4]
    sol = runningSum(nums)
    print(sol)

if __name__ == "__main__":
    main()