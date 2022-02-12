"""
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly, they also use English lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.
Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographically in this alien language.

Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation: As 'd' comes after 'l' in this language, then words[0] > words[1], hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation: The first three characters "app" match, and the second string is shorter (in size.) According to lexicographical rules "apple" > "app", because 'l' > '∅', where '∅' is defined as the blank character which is less than any other character (More info).
 

Constraints:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are English lowercase letters.
"""
from typing import List


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        self.dict_index = {item: i for i, item in enumerate(order)}
        
        for i in range(len(words)-1):
            # compare words[i] and words[i+1]
            if not self.isRightSorted(words[i], words[i+1]):
                return False
        return True
            
    def isRightSorted(self, word1, word2):
        min_length = len(word1) if len(word1) < len(word2) else len(word2)
        for j in range(min_length):
            if self.dict_index[word1[j]] < self.dict_index[word2[j]]:
                return True
            elif self.dict_index[word1[j]] > self.dict_index[word2[j]]:
                return False
            else:
                # compare to last char but length of word1 is larger than word2
                if j == min_length - 1 and min_length < len(word1):
                    return False
        return True

words = ["apple", "app"]
order = "abcdefghijklmnopqrstuvwxyz"

# words = ["hello","leetcode", "hhihi"]
# order = "hlabcdefgijkmnopqrstuvwxyz"
solution = Solution()
x = solution.isAlienSorted(words, order)
print(x)