class Solution:
    def fib(self, n: int, memory: dict = None) -> int:
        if memory is None:
            memory = {}

        if n in memory:
            return memory[n]

        if n == 0:
            result = 0
        elif n == 1:
            result = 1
        else:
            result = self.fib(n - 1, memory) + self.fib(n - 2, memory)

        memory[n] = result
        return result