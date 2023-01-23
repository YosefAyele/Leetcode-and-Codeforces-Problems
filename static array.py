class StaticArrays:
    def __init__(self, arr = [0, 0, 0, 0], capacity = 4, length = 0):
        # write your code here
        self.staticArray=arr
        self.capacity=capacity
        self.length=length

   
    def insertEnd(self, value):
        # write your code here
        self.staticArray[self.length]=value
        self.length+=1
      
       
    def removeEnd(self):
        # write your code here
        self.staticArray[self.length]=0
        self.length-=1
    
   
    def insertMiddle(self, index, value):
        # write your code here, you need to shift elements after insertion
        for i in range(index,self.capacity):

        return 
       
    def removeMiddle(self, index):
        # write your code here, you need to shift elements after removal
        return
   
    def printArr(self):
        # write your code here