class Solution:
    def partition(self, s: str) -> list[list[str]]:
        if not s:
            return []
            
        res = [[s[0]]]

        for c in s[1:]:
            next_res = []
            
            for part in res:
                last_pal = part[-1]
                is_uniform = (last_pal == c * len(last_pal))
                
                # 1. Uniform Expansion: e.g., "bb" + "b" -> "bbb"
                if is_uniform:
                    next_res.append(part[:-1] + [last_pal + c])
                
                # 2. Wrap-around Expansion: e.g., ["a", "b"] + "a" -> ["aba"]
                # We skip this if the center is uniform of `c` to prevent duplicates.
                if len(part) > 1 and part[-2] == c:
                    if not is_uniform:
                        next_res.append(part[:-2] + [c + last_pal + c])
                
                # 3. Single Character: always append as a new palindrome
                next_res.append(part + [c])
                
            res = next_res

        return res