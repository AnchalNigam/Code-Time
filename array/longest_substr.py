def lengthOfLongestSubstring(self, s: str) -> int:
        maxStr = ""
        string = ""
        if len(s) == 1:
            return 1
        for idx1 in range(len(s)):
            string = s[idx1]
            flag = False
            for idx2 in range(idx1+1, len(s)):
                if s[idx2] not in string:
                    string += s[idx2]
                elif s[idx2] in string:
                    if len(maxStr) < len(string):
                        flag = True
                        maxStr = string
                    break
            print(string)
            if not flag and len(maxStr) < len(string):
                maxStr = string
                
                    
            
        return len(maxStr)