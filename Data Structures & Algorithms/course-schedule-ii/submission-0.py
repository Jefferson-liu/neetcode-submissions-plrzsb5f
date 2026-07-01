class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        required = [0 for i in range(numCourses)]
        courses = {i: set() for i in range(numCourses)}
        for req, prereq in prerequisites:
            required[req] += 1
            courses[prereq].add(req)
        ans = []
        canTake = deque([])
        for i in range(numCourses):
            if required[i] == 0:
                canTake.append(i)
                ans.append(i)
        
        while canTake:
            cur = canTake.popleft()
            for course in courses[cur]:
                required[course] -= 1
                if required[course] == 0:
                    canTake.append(course)
                    ans.append(course)
        
        if sum(required) == 0:
            return ans
        else:
            return []