class Solution:
    def longestPalindrome(self, s: str) -> int:
        collection = defaultdict(int)
        for char in s:
            collection[char] += 1

        result, flag = 0, 0
        for char, count in collection.items():
            if count % 2 == 0:
                result += count
            else:
                if flag == 0:
                    result += count
                else:
                    result += count - 1
                flag = 1
            
        return result