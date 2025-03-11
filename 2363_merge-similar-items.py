class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        merge = {}
        for i in items1:
            merge[i[0]] = i[1]
        
        for i in items2:
            if i[0] not in merge.keys():
                merge[i[0]] = i[1]
            else:
                merge[i[0]] = i[1] + merge[i[0]]
        
        result = []
        for i in sorted(merge.keys()):
            result.append([i, merge[i]])

        return result