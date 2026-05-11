class Solution:
    # we could use a stack 
    # we could do a bfs/dfs to find tree nodes
    # we could use recursion to achieve this.
    # n = 1 -> ()
    # n = 2 -> (()) ()()
    # n = 3 -> ((())) (()()) (())() ()(()) ()()()
    # we either place () after ( or after )
    def generateParenthesis(self, n: int) -> List[str]:
        res = [[] for _ in range(n+1)]
        res[0] = [""]
        
        for k in range(n+1):
            for i in range(k):
                for left in res[i]:
                    for right in res[k-i-1]:
                        res[k].append("(" + left + ")" + right)

        return res[-1]
