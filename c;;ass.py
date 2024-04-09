class a:
    def __init__(self,r):
        self.radius=r

    def __rper__(self):
        return self.result()
    
     ,0def result(self):
        return self.circle_area(self.radius)
    
    @staticmethod
    def circle_area(r):
        return r**2*3.14
    
    
aa=a(4)
print(aa.result())


