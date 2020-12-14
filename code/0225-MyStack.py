class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        
        为什么这里使用的是这个

        """
        self.queue = collections.deque()


    def push(self, x):
        """
        Push element x onto stack.
        """
        n = len(self.queue)
        self.queue.append(x)
        for _ in range(n):
            self.queue.append(self.queue.popleft())


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        return self.queue.popleft()


    def top(self):
        """
        Get the top element.
        """
        return self.queue[0]


    def empty(self):
        """
        Returns whether the stack is empty.
        """
        return not self.queue

