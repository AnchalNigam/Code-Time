class Solution:
    def isValid(self, s: str) -> bool:
        dic = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        for bracket in s:
            if bracket == '(' or bracket == '[' or bracket == '{':
                stack.append(bracket)
            elif len(stack) == 0:
                return False
            elif stack.pop() != dic[bracket]:
                return False
        return True if len(stack) == 0 else False
# did it by own - o(n) , space - o(type of bracket)
# basic thoiught we will append open bracket in stack and they are saying that order matter krta hai
# mns if any bracket gets open toh next racket tabhi mana jaega jab purana wala close h jaega
# toh simple hme bs ye track krna h pechla close hua k nhi...that we track using stack
# last elem in stack must always equal to closing brack that just comes...len(stack) and all
# handling edge case if frst elem is close one then it shoudl return false...last len(stack)
# is for if len(stack) end me 0 ni hua mns ek open brack ka close nhi h islie
