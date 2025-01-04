class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1])
        result = 0
        
        for index, fare in enumerate(costs):
            if index < len(costs)/2:
                result += fare[0]
            else:
                result += fare[1]
        
        return result