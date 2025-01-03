class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key= lambda x:x[1])
        count, prev = 0, intervals[0]
        
        for i in range(1,len(intervals)):
            if intervals[i][0] >= prev[1]:
                prev = intervals[i]
                continue
            else:
                count += 1

        return count
