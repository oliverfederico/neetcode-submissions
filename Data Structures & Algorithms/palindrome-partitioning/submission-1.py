class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = [[s[0]]]

        for i in range(1,len(s)):
            for j in range(len(res)):
                sl = len(res[j][-1])
                if res[j][-1] == s[i]*sl:
                    res.append(res[j][:-1])
                    res[-1].append(s[i]*(sl+1))
                elif len(res[j]) > 1 and res[j][-2] == s[i]:
                    res.append(res[j][:-2])
                    res[-1].append(s[i] + res[j][-1] + s[i])

                res[j].append(s[i])
        return res
            

