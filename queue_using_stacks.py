class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while len(self.s1) !=0:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while len(self.s2)!=0:
            self.s1.append(self.s2.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.s1.pop()
    

    def peek(self):
        """
        :rtype: int
        """
        return self.s1[-1]
            

    def empty(self):
        """
        :rtype: bool
        """
        if self.s1:
            return False
        else:
            return True
        
