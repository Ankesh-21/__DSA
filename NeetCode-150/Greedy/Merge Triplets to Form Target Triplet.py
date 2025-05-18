'''
* LeetCode : 1899
* T.C : O(N)
* S.C : O(N)
'''
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        trips = []
        # Removing the triplet whose value exceed our target's of same position
        for i in range(len(triplets)):
            valid = True
            for j in range(3):
                if triplets[i][j] > target[j]:
                    valid = False
                    break
            if valid:
                trips.append(triplets[i])
        #print(trips)
        # Position array to check position of the target num is same or present or not in triplets 
        positions = [False,False,False]
        for i in range(len(trips)):
            for j in range(3):
                if trips[i][j] == target[j]:
                    print(trips[i])
                    positions[j] = True
            if positions == [True,True,True]:
                return True
        
        return positions == [True,True,True]

