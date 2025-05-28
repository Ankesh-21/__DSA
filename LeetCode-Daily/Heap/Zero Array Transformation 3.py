### Tle 
class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        maxh = []
        heapq.heapify(maxh)
        past = []
        usedQuery = 0
        heapq.heapify(past)
        j = 0
        for i in range(len(nums)):
            while j<len(queries) and queries[j][0] == i:
                heapq.heappush(maxh,-queries[j][1])
                j += 1
            nums[i] -= len(past)
            while nums[i] > 0 and maxh and heapq.nsmallest(1,maxh)[0] <= -i:
                nums[i] -= 1
                el = heapq.heappop(maxh)
                heapq.heappush(past,-el)
                usedQuery += 1
                # print(maxh)
            if (nums[i] > 0):
                return -1
            
            while past and heapq.nsmallest(1,past)[0] == i:
                # print(i)
                heapq.heappop(past)
        return len(queries) - usedQuery
            
