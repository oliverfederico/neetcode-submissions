class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = []
        for strng in strs:
            for char in strng:
                encoded.append(str(ord(char)))
                encoded.append('|')
            encoded.append('#')
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        strs = []
        string = []
        chr_end = []
        for char in s:
            if char == '#':
                strs.append("".join(string))
                string = []
            elif char == '|':
                string.append(chr(int("".join(chr_end))))
                chr_end = []
            else:
                chr_end.append(char)
        return strs


