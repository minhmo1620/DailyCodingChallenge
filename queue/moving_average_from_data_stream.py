# Link: https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.queue = []

    def next(self, val: int) -> float:
        self.queue.append(val)
        if len(self.queue) >= self.size:
            return mean(self.queue[(len(self.queue) - self.size):])
        else:
            return mean(self.queue)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)