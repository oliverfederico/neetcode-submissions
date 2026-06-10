class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        char_to_num = {c:i for i, c in enumerate('0123456789')}
        n1 = 0
        for c in num1:
            n1 *= 10
            n1 += char_to_num[c]
        n2 = 0
        for c in num2:        
            n2 *= 10
            n2 += char_to_num[c]
        return str(n1 * n2)