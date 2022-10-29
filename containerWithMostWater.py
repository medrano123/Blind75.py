
def maxArea(height):
    res = 0
    l = 0
    r = len(height) - 1

    while l < r:
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return res

def main():
    nums = [1,8,6,2,5,4,8,3,7]
    sol = maxArea(nums)
    print(sol)

if __name__ == "__main__":
    main()