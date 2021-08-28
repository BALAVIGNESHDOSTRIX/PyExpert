#binary search

class BinarySearch:

    def __init__(self):
        self.elements = [10,12,15,18,19,22,27,32,38]

    def SearchElm(self,elem):
        start = 0
        stop = len(self.elements)-1
        while start <= stop:

            mid_point = start + (stop - start)

            if self.elements[mid_point] == elem:
                return mid_point
            
            elif elem > self.elements[mid_point]:
                start = mid_point + 1
            else:
                stop = mid_point - 1
        
        return -1


binary = BinarySearch()

element = int(input("Enter the element you want search :"))

res = binary.SearchElm(element)

if res != -1:
    print("The position of the {x} is  {y} ".format(x = element,y=res))
else:
    print("The element is not presented in the array")
