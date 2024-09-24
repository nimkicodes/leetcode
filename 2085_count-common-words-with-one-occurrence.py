class Solution:
    def noDuplicate(self, w: List[str]) -> List[str]:
        new_list = []
        count = {}
        for x in w:
            if x in count:
                count[x] += 1
            else:
                count[x] = 1
        for x in w:
            if count[x] == 1:
                new_list.append(x)   
        return new_list

    def countWords(self, words1: List[str], words2: List[str]) -> int:
        new_list1 = self.noDuplicate(words1)
        new_list2 = self.noDuplicate(words2)
        s1,s2 = set(new_list1), set(new_list2)
        return len(s1.intersection(s2))

        