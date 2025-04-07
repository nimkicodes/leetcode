class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        below_20 = [ "", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                     "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",     "Fourteen","Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        
        thousands = ["", "Thousand", "Million", "Billion"]

        def toWord(n):
            if n == 0:
                return ""
            elif n < 20:
                return below_20[n] + " "
            elif n < 100:
                return tens[n // 10] + " " + toWord(n % 10)
            else:
                return below_20[n // 100] + " Hundred " + toWord(n % 100)

        result = ""
        i = 0

        while num > 0:
            if num % 1000 != 0:
                result = toWord(num % 1000) + thousands[i] + " " + result
            num //= 1000
            i += 1

        return result.strip()