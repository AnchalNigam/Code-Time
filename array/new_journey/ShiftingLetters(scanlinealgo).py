from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(shifts)
        s = list(s)
        n2 = len(s)
        chars = [ "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        prefix = [0] * (n2+1)
        for shift in shifts:
            diff = 1 if shift[2] == 1 else -1
            prefix[shift[0]] += diff
            prefix[shift[1]+1] -= diff
        # print(prefix, 'check')
        for i in range(n2):
            shift = prefix[i]
            s[i] = chars[(ord(s[i])-97+shift)%26]
            prefix[i+1] += prefix[i]
        return "".join(s)
                
# bht interestng