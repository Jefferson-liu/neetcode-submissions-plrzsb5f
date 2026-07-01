from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        required = [0 for i in range(numCourses)]
        courses = {i: set() for i in range(numCourses)}
        for req, prereq in prerequisites:
            required[req] += 1
            courses[prereq].add(req)
        
        canTake = deque([])
        for i in range(numCourses):
            if required[i] == 0:
                canTake.append(i)
        
        while canTake:
            cur = canTake.popleft()
            for course in courses[cur]:
                required[course] -= 1
                if required[course] == 0:
                    canTake.append(course)
        
        return sum(required) == 0
        
