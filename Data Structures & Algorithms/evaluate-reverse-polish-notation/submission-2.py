class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        ops = {'+', '-', '*', '/'}
        for t in tokens:
            if t in ops:
                b = st.pop()
                if t == '+':
                    st[-1] += b
                elif t == '-':
                    st[-1] -= b
                elif t == '*':
                    st[-1] *= b
                else:
                    st[-1] /= b
                    st[-1] = int(st[-1])
            else:
                st.append(int(t))
        return st[0]
        