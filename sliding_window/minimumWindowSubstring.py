from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = defaultdict(int)
        dic2 = defaultdict(int)
        totalChar = len(t)
        for char in t:
            if char not in dic:
                dic[char] = 1
            else:
                dic[char] += 1
        start = 0
        end = 0
        res = ""
        charCounter = 0
        while end < len(s):
            dic2[s[end]] += 1
            if dic2[s[end]] <= dic[s[end]]:
                charCounter += 1
            while charCounter == totalChar:
                if res == "" or len(res) > end-start+1:
                    res = s[start: end+1]
                dic2[s[start]] -= 1
                if dic2[s[start]] < dic[s[start]]:
                    charCounter -= 1
                start += 1
            end += 1
        return res

# i could not solve because thda tricky tha ques.
# main funda here is firstly hm apne wo window dhudhnge j valid hge matlb jisme sare chars t k hnge
# for that hmne ek dic banay h that holds all chars of t
# and dic2 is for holdng all chars freq..so now hm charCounter tab badhaynge jab dic me wo char
# hga so dic2[s[end]] <= dic[s[end]]..dic me a suppose 2 times hai and hme a milta h then
# dic2 would be 1 so its less islie charCounter badhaya whereas f nhi hai dic2 me but dic2
# me f ka count 1 h gya because of  dic2[s[end]] += 1 so ye matching banda nhi h islie charCOunter
# nhi badhaya.. now as jaise h valid window milta h then hm charCounter == 0 pe tabtak window
# shrink krenge jab tak aur chta ans na milta ..ab scene ye hga ki dic2 se dec kro
# agr dic2 se dec dic1 se kam hga..jaise a 2 hna chahye..now its beccome 1 matlb ek char
# us window se kam h gya hai islie charCounter += 1 krna padega bt agr f hai usko dec kia
# toh wo 0 hua and dic1  me wo h nhi so dic2[s[start]] cant be less than dic[s[start]] so charCounter
# inc k need h nhi in such way window shrink krenge to get min window substring
# interstng way of solving
# space - 0(t+s) -
# time  - o(t) + o(s)+o(s) as hm char freq k lie iterate kr rhe hai...o(n)+o(n) islie because end pointer
# till end tak s k ja skta hai and strt pointer shrinking me bhi ja skte h toh two times
# ek char traverse h rha hai islie o(2n) but as we dont care about constants so o(s)+o(t)