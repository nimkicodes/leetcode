class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        all_words = s.split()
        if len(all_words) > 1 :
            return len(all_words[len(all_words)-1])
        elif len(all_words) == 1:
            return len(all_words[0])
        elif len(all_words) == 0:
            return 0