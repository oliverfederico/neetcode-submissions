class Solution:
    # true if we can take numCourses courses
    # false if we have cycles, if a -> b -> c -> a we can't take any of them
    # the biggest cycle can be all nodes so numCourses long

    # we could sort 
    # we could create a dependancy map

    # if there are v nodes (courses) and E edges (prerequisites)
    # then to avoid cycles
    # v == 1 -> E == 0
    # v == 2 -> E == 1
    # v == 3 -> E == 3
    # v == 4 -> E == 6
    # v == n -> E == (n-1)+(n-2)+..0 == (n * (n-1))/2 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) > ((numCourses *(numCourses-1))//2):
            return False
        requires = defaultdict(set)
        # required_by = defaultdict(set)
        for a, b in prerequisites:
            requires[a].add(b)
            # required_by[b].add(a)
        
        visiting = set()
        def dfs(a):
            if a in visiting:
                return False
            if len(requires[a]) == 0:
                return True
            
            visiting.add(a)
            for b in requires[a]:
                if not dfs(b):
                    return False
            visiting.remove(a)
            requires[a].clear()
            return True
        
        for a in range(numCourses):
            if not dfs(a):
                return False
        
        # for a in requires.keys():
            # these are leaf nodes so can't be in cycle but might have upstream cycles
            # if a not in required_by:
                # q = deque(a)
                # while q:
                    # q.popleft()
                    




                
        return True







