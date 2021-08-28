#Linear Search

class LinearSerach:

    def __init__(self):
        self.elements = [10,52,14,8,1,400,900,200,2,0]
    
    def SearchEm(self,elem):
        y = 0 
        if elem in self.elements:
            print("{x} is in the position of {y}".format(x = elem,y = self.elements.index(elem)))
        else:
            print("The element {x} not presented in the list".format(x = elem))

       
            

linear = LinearSerach()
task_elem = int(input("Enter the element:"))
linear.SearchEm(task_elem)


    
