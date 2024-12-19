class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict1 = {}
        for index, item in enumerate(list1):
            dict1[item] = index
        
        result = []
        minimum = float(inf)
        for index, item in enumerate(list2):
            if item in dict1:
                index_sum = index + dict1[item]
                if index_sum < minimum: 
                    result = [item]
                    minimum = index_sum
                elif index_sum == minimum:
                    result.append(item)
        return result