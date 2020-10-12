# Link: https://leetcode.com/problems/design-a-stack-with-increment-operation/submissions/
class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) > 0:
            return self.stack.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        curr = 0
        while curr <= min(k - 1, len(self.stack) - 1):
            self.stack[curr] += val
            curr += 1


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)