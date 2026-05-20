class Solution:
    # find all courses that have no prerequisites
    # bfs 'removing' each course as a prerequisite of all dependant courses
    # add courses that end of with no prerequisites.
    # repeat until no courses can be visited
    # if numCourses != num courses visited then we have a cycle
    # we can complete the courses in the order we visit them 
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        depMap = defaultdict(list)
        preCount = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            depMap[b].append(a)
            preCount[a]+=1
        
        q = deque()

        for i in range(numCourses):
            if preCount[i] == 0:
                q.append(i)
        
        order = []

        while q:
            b = q.popleft()
            order.append(b)
            for a in depMap[b]:
                preCount[a] -= 1
                if preCount[a] == 0:
                    q.append(a)
        
        return order if len(order) == numCourses else []


