class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_string = list(set(list1) & set(list2))
        
        if len(common_string) == 1:
            return common_string

        dict1 = {}
        for i in range(len(list1)):
            dict1[list1[i]] = i

        dict2 = {}
        for i in range(len(list2)):
            dict2[list2[i]] = i
        
        result = []
        minimum = float(inf)
        for item in common_string:
            if item in dict1 and item in dict2:
                index_sum = dict1.get(item) + dict2.get(item)
                if index_sum < minimum: 
                    result = [item]
                    minimum = index_sum
                elif index_sum == minimum:
                    result.append(item)
        
        return result