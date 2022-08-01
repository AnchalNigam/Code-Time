from collections import defaultdict
from typing import List


class Solution:
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        n = len(s)
        self.letterDict = defaultdict(list)
        for i, c in enumerate(s):
            if c not in self.letterDict:
                self.letterDict[c] = [i,i]
            else:
                self.letterDict[c][1] = i

        def findEnd(i):
            s1, e1 = self.letterDict[s[i]]
            # print(i, 'check', s1, e1)
            j = s1
            while j < e1+1:
                s2, e2 = self.letterDict[s[j]]
                if s2 < s1:
                    return -1
                if e2 > e1:
                    e1 = e2
                j += 1
            return e1
                    
        last = -1
        ans = []
        for i, c in enumerate(s):
            if i != self.letterDict[c][0]:
                continue
            end = findEnd(i)
            if end == -1:
                continue
            # print(c, i, end, 'hii')
            if i > last:
                # print(s[i:end+1], 'k', ans)
                ans.append(s[i:end+1])
            else:
                ans[-1] = s[i:end+1]
            last = end
        return ans
# here i was not able to solve..
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/discuss/1201904/Python3-greedy-clean-code
# the logic is "adefaddaccc"
# take above example so frstly we are maintaining k us particular char k frst and end index kya h
# after maintaining that dic...we are agin iteratng on that str to check ki j bhi range
# bane h for that char uske range eme koi aur char bahar toh ni ja rha hai end se 
# eg ..a is [0,7](start, end) so now we are iterating from 0 to 7 and check
# ki koi aur char k end 7 se bahar toh nhi hai ar agr hai toh extend end of a
# and  if s2 < s1: return -1 this condoion baically checks that j bhi range bane h
# eg defadd [d ka start,end = 1,6] so ye str bana bt we weill check ki j 1 to 6 k chars h 
# unka start agr d k start se pehle h that means its a invalid substr so we will not entertain 
# that..now come to 
#   if i > last:
                # print(s[i:end+1], 'k', ans)
            #     ans.append(s[i:end+1])
            # else:
            #     ans[-1] = s[i:end+1]
            # last = end
# this block of code is suppose i > last toh hm us str k ans me append kr denge
# bt agr suppose us bada substring me ek chota substr valid hai like
# hme pehle ye mila tha - adefadda but agr iske beech me valid substr mil jay then well and gd
# like e f so hm usko hm entertain kr rhe h last one j usse bada h use replace kr de re
# so greedy approach, whatever last str is agr wo bade hai and us bade str me koi substr valid h
# then will give prority to it by replacing it with that chota substr..so this way solved..
# time complexity , frst loop takes o(n)and below loop only can run 26 times..because dic k dekh rhe 
# h hm which is   if i != self.letterDict[c][0]: continue so hardly 26 times*n - i guess...
# so n +26n = 0(n)
# space - o(26) as smallcae letter bola h...