class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        seen = set()
        prereqs = collections.defaultdict(list)
        numberOfPrereqs = [0] * numCourses
        
        for course, prereq in prerequisites:
            prereqs[prereq].append(course)
            numberOfPrereqs[course] += 1
            
        q = collections.deque()
        for course in range(numCourses):
            if numberOfPrereqs[course] == 0:
                q.append(course)
        
        count = 0
        while len(q) > 0:
            course = q[0]
            count += 1
            q.popleft()
            
            for i in prereqs[course]:
                numberOfPrereqs[i] -= 1
                if numberOfPrereqs[i] == 0:
                    q.append(i)
        return count == numCourses
