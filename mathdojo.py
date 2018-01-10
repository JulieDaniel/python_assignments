class mathdojo(object):
    def __init__(self):
        self.result = 0

    def add(self, num1, *nums):
        if isinstance(num1, list) or isinstance(num1, tuple):
            for num in num1:
                self.result = self.result + num
        else:
            self.result = self.result + num1
        for val in nums:
            if isinstance(val, list) or isinstance(val, tuple):
                for num in val:
                    self.result = self.result + num
            else:
                self.result = self.result + val
        return self



    def subtract(self, num1, *nums):
        if isinstance(num1, list) or isinstance(num1, tuple):
            for num in num1:
                self.result = self.result - num
        else:
            self.result = self.result - num1
        for val in nums:
            if isinstance(val, list) or isinstance(val, tuple):
                for num in val:
                    self.result = self.result - num
            else:
                self.result = self.result - val
        return self






md = mathdojo()
md.add(2).add(2,5).subtract(3,2).result
print md.result

print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, [2,3], [1.1,2.3], (1,1)).result