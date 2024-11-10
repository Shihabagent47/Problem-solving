class Vector:
    def __init__(self):
        self._capacity=1
        self._size=0
        self._array=[None]*self._capacity
    
    def _resize(self,new_capacity):
        new_array=[None] * new_capacity
        for i in range(self._size):
            new_array[i]=self._array[i]
        self._array=new_array
        self._capacity=new_capacity
    
    def append(self,value):
        if self._size==self._capacity:
            self._resize(2*self._capacity)
        self._array[self._size]=value
        self._size+=1

    def _getItem_(self,index):
        if 0<=index<self._size:
            return self._array[index]
        else:
            raise IndexError("Index out of bound")
        
        
    
    def __str__(self):

        return str([self._array[i] for i in range(self._size)])




#Example 

vec = Vector()
vec.append(10)
vec.append(20)

print(vec._getItem_(0)) 
print(vec)  # Output: [10, 20, 30]

