class Vector:
    def __init__(self,*components):
        self.components = components
        
    #Printing vectors
    
    def print_vector(self):
        return Vector(*(self.components))
    
    # Addition
    
    def add(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("We need all the components to add the vectors")
        else:
            return Vector(*(a+b for a,b in zip(self.components,other.components)))
        
    #Subtraction    
        
    def subtr(self,other):
        if len(self.components) != len(other.components):
            raise ValueError("We need all the components to subtract the vectors")
        else:
            return Vector(*(a-b for a,b in zip(self.components,other.components)))
        
    #Dot product
    
    def dot_product(self,other):
        return Vector(*(a*b for a,b in zip(self.components,other.components)))
    
    #Cross product
    
    def constant_product(self,var):
        return Vector(*(a*var for a in self.components))
    
    #Magnitude 
    
    def magnitude(self):
        return (sum(a**2 for a in self.components))**0.5
    
    #Normalize
    
    def normalize(self):
        return Vector(*(a/((sum(a**2 for a in self.components))**0.5) for a in self.components))
                
            