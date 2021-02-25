class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            i += 1
        if i < len(intervals):
            newInterval[0] = min(newInterval[0], intervals[i][0])
        j = len(intervals) - 1
        while j >= 0 and intervals[j][0] > newInterval[1]:
            j -= 1
        if j >= 0:
            newInterval[1] = max(newInterval[1], intervals[j][1])
        return intervals[:i] + [newInterval[:]] + intervals[j+1:]
