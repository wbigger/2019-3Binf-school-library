class Locker:
    def __init__(self, position,w,h,d,m,pk):
        self.position = position
        self.width = w
        self.height = h
        self.depth = d
        self.material = m
        self.private_key = pk
        self.is_bulky = w*h*d/1000000 > 2
    
    def is_code_valid(self,code):
        return len(code) >=4 and len(code) <=8
    
    def is_secret_passed(self,code):
        accumulator = 0
        for c in code:
            if (c == "A"):
                accumulator += 1
            if (c == "B"):
                accumulator += 2
        accumulator %= self.private_key
        return accumulator == 0