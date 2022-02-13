"""
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.
Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 

Example 1:
Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:
Input: s = "a)b(c)d"
Output: "ab(c)d"

Example 3:
Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
 
Constraints:
1 <= s.length <= 105
s[i] is either'(' , ')', or lowercase English letter.
"""
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        output = []
        remain_open = []  # stack
        invalid_close = set()
        for i, char in enumerate(s):
            if char == '(':
                remain_open.append(i)
            elif char == ')':
                if not remain_open:
                    invalid_close.add(i)
                else:
                    remain_open.pop()

        invalid_parentheses = invalid_close.union(set(remain_open))  # optimize search
        for i, char in enumerate(s):
            if i in invalid_parentheses:
                continue
            output.append(char)
                
        return "".join(output)



s = "lee(t(c)o)de())))"
x = Solution().minRemoveToMakeValid(s)
print(x)
