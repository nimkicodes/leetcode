class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k <= numZeros + numOnes:
            return numOnes 
        elif k > numZeros + numOnes:
            return numOnes - (k - numOnes - numZeros)
    
        # items = [1] * numOnes + [0] * numZeros + [-1] * numNegOnes
    
        # result = 0
        # for item in range(k):
        #     result += items[item]
        # return result