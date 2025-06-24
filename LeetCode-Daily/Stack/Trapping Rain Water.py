def getleft(heights):
    lefts = [-1 for _ in range(len(heights))]
    maxi = 0
    for i in range(len(heights)):
        lefts[i] = i if max(heights[i],heights[maxi]) == heights[i] else maxi
        maxi = i if max(heights[i],heights[maxi]) == heights[i] else maxi
    return lefts
def getright(heights):
    rights = [-1 for _ in range(len(heights))]
    maxi = len(heights) - 1
    for i in range(len(heights)-1,-1,-1):
        rights[i] = i if max(heights[i],heights[maxi]) == heights[i] else maxi
        maxi = i if max(heights[i],heights[maxi]) == heights[i] else maxi
    return rights
class Solution:
    def trap(self, height: List[int]) -> int:
        left = getleft(height)
        right = getright(height)
        # print(right)
        ans = 0
        for i in range(len(height)):
            if height[left[i]] != height[i] and height[right[i]] != height[i]:
                mini = min(height[left[i]],height[right[i]])
                ans += mini - height[i]
                # print(f'{i}th index: {ans}')
            else:
                
                continue
        return ans