class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        dictionary = {}
        
        for i in nums1:
            dictionary[i[0]] = i[1]

        for i in nums2:
            if i[0] not in dictionary.keys():
                dictionary[i[0]] = i[1]
            else :
                dictionary[i[0]] = i[1] + dictionary[i[0]]
        
        result = []
        for i in sorted(dictionary.keys()):
            result.append([i, dictionary[i]])
        
        return result