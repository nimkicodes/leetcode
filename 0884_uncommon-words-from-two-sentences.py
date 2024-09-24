class Solution:
    def noDuplicate(self, l1: List[str]) -> List[str]:
        new_list = []
        word_count = {}
        for x in l1:
            if x in word_count:
                word_count[x] += 1
            else:
                word_count[x] = 1
        
        for x in l1:
            if word_count[x] == 1:
                new_list.append(x)
           
        return new_list

    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        list1 = s1.split()
        list2 = s2.split()
        answer = self.noDuplicate(list1 + list2)
        return answer