class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = []
        for name, height in zip(names, heights):
            people.append((name, height))

        people.sort(key = lambda x:x[1], reverse = True)
    
        return [name for name,_ in people]