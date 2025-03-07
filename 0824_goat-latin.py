class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()     
        for i in range(len(words)):
            if words[i][0] in ('a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"):
                words[i] = words[i] + 'ma'
            else:
                words[i] = words[i][1:] + words[i][0] + "ma"

        result = [word + "a" * (i + 1) for i, word in enumerate(words)]
        return " ".join(result)