class Solution:
    def countPrimes(self, n: int) -> int:
        # Sieve Of Eratosthenes 
        # Time Complexity: O(N*log(log(N))) , Space: O(N)

        if n <= 2:
            return 0  

        prime = [True] * n  
        prime[0] = prime[1] = False  

        num = 2
        while (num * num < n):
            if (prime[num] == True):
                for i in range(num * num, n, num):
                    prime[i] = False
            num += 1

        return sum(prime)