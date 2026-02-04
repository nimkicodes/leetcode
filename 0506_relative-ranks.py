class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # athletes = [(s,i) for i, s in enumerate(score)]
        # athletes.sort(reverse=True)
        
        # answer = [""] * len(score)
        # for rank, (_,index) in enumerate(athletes):
        #     if rank == 0:
        #         answer[index] = "Gold Medal"
        #     elif rank == 1:
        #         answer[index] = "Silver Medal"
        #     elif rank == 2:
        #         answer[index] = "Bronze Medal"
        #     else:
        #         answer[index] = str(rank + 1)

        # return answer

        sorted_score = sorted(score, reverse=True)
        
        s_map = {}
        for i, s in enumerate(sorted_score):
            if i == 0:
                s_map[s] = "Gold Medal"
            elif i == 1:
                s_map[s] = "Silver Medal"
            elif i == 2:
                s_map[s] = "Bronze Medal"
            else:
                s_map[s] = str(i+1)

        return [s_map[s] for s in score]