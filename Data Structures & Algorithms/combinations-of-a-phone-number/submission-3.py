from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        numpad = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
                  '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
                  
        total_combs = 1
        for digit in digits:
            total_combs *= len(numpad[digit])
            
        # 1. Pre-allocate a 2D list of empty characters instead of strings
        # This avoids string immutability issues during construction
        combinations = [[""] * len(digits) for _ in range(total_combs)]
        
        block_size = total_combs 
        
        for i, digit in enumerate(digits):
            letters = numpad[digit]
            block_size //= len(letters) 
            
            # 2. Generate the block pattern for this specific digit
            # e.g., ['a', 'a', 'a'] + ['b', 'b', 'b'] + ['c', 'c', 'c']
            pattern = []
            for letter in letters:
                pattern.extend([letter] * block_size)
            
            # 3. Repeat that pattern until it fills the whole column length
            repeats = total_combs // len(pattern)
            full_column = pattern * repeats
            
            # 4. Drop the generated column into our 2D array
            for x in range(total_combs):
                combinations[x][i] = full_column[x]

        # 5. Join the characters into strings at the very end (highly optimized in C)
        return ["".join(row) for row in combinations]