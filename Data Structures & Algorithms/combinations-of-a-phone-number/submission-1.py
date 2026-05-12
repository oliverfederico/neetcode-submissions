from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
            
        numpad = {'2':"abc", '3':"def", '4':"ghi", '5':"jkl",
                  '6':"mno", '7':"pqrs", '8':"tuv", '9':"wxyz"}
                  
        total_combs = 1
        for digit in digits:
            total_combs *= 3 if digit != '7' and digit != '9' else 4
            
        # Pre-allocate array exactly as you did
        combinations = ["" for _ in range(total_combs)]
        
        # Start the block size at the total size of the array
        block_size = total_combs 
        dl = len(digits)
        
        for i in range(dl):
            letters = numpad[digits[i]]
            
            # The chunk size shrinks as we move to subsequent digits
            block_size //= len(letters) 
            
            for x in range(total_combs):
                # Math magic: Calculate exactly which letter belongs at index 'x'
                letter_index = (x // block_size) % len(letters)
                combinations[x] += letters[letter_index]

        return combinations