class Solution:
    def reverseWords(self, s: str) -> str:
        # words = s.split()
        # reverse = words[::-1]
        # return " ".join(reverse)
    
        return " ".join(reversed(s.split()))
        
        # words = s.split()
        # left, right = 0, len(words)-1

        # while left < right:
        #     words[left], words[right] = words[right], words[left]
        #     left += 1
        #     right -= 1
            
        # return " ".join(words)