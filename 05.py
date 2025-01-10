class string():
    def __init__(self):
        self.s=''
    def getstring(self):
        self.s=input("Enter a string: ")
    def outstring(self):
        print(self.s.upper())  
str=string()
str.getstring()
str.outstring()

