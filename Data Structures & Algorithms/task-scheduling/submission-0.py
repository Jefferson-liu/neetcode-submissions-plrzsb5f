from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        taskCount = Counter(tasks)
        maxFreq = max(taskCount.values())
        maxFreqCount = 0
        for val in taskCount:
            if taskCount[val] == maxFreq:
                maxFreqCount += 1
        print(maxFreq)
        return max(len(tasks), (n + 1) * (maxFreq - 1) + maxFreqCount)
