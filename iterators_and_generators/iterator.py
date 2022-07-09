class force3():
    def __init__(self,max = 0):
        self.max = max
        self.force = 0
    def __iter__(self):
        return self
    def __next__(self):
        if(self.force <= self.max):
            result = 3 ** self.force
            self.force += 1
            return result
        else:
            self.force = 0
            raise StopIteration

force = force3(6)
for i in force:
    print(i)