
class Columns(list):
    def __init__(self):
        pass
    
    def names(self):
        for i in self:
            print (i.name)
