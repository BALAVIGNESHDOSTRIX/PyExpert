'''

            DEVELOPER NAME : BALAVIGNESH.M

            

            IMPLEMENTED DATE : 28/11/2018



            SCOPE OF IMPLEMENTATION : To understanding the SingleLiked List by implementing with python





'''



class Node:



    def __init__(self,datavalue):

        self.datavalue = datavalue

        self.nextvalue = None 



class SingleLinkedList:



    def __init__(self):

        self.headvalue = None 



    def listprint(self):

        printval = self.headvalue

        while printval is not None:

            print(printval.datavalue)

            printval = printval.nextvalue



    def addItem(self,data):

        self.NextNode = Node(data)

        self.NextNode.nextvalue = self.headvalue

        self.headvalue = self.NextNode



    def addLast(self,data):

        self.NewNode = Node(data)

        temp = self.headvalue

        while temp is not None:

            if temp.nextvalue == None:

                temp.nextvalue = self.NewNode

                break

            temp = temp.nextvalue

    

    def findLength(self):

        self.length = 0

        temp = self.headvalue



        while temp is not None:

            self.length += 1

            temp = temp.nextvalue

        return self.length

       



    def addtheEmid(self,data):

        NewNode = Node(data)

        tempRange = int(self.findLength() / 2)

        tempNode = self.headvalue

        i = 1

        while tempNode is not None:

            if i == tempRange:

                NewNode.nextvalue = tempNode.nextvalue

                tempNode.nextvalue = NewNode

                break

            tempNode = tempNode.nextvalue

            i += 1



    #Removel operation



    def RemoveFirstItem(self):

        i = 1

        temp = 1

        tempNode = self.headvalue

        while tempNode is not None:

            if i == temp:

                self.headvalue = tempNode.nextvalue

                tempNode.nextvalue = None 

                break

            tempNode = tempNode.nextvalue

    

    def RemoveMid(self):

        tempNode = self.headvalue

        tempRange = int(self.findLength() / 2)

        prviousnodeindex = int(tempRange - 1)

        i = 1

        while tempNode is not None:

            if i == prviousnodeindex:

                self.previousnode = tempNode

            if i == tempRange:

                self.previousnode.nextvalue = tempNode.nextvalue

                tempNode.nextvalue = None   

                break 

            tempNode = tempNode.nextvalue

            i +=1



    

    def RemoveLast(self):

        tempNode = self.headvalue

        tempRange = int(self.findLength())

        lastpreviousIndex = int(tempRange - 1)

        i = 1

        while tempNode is not None:

            if i == lastpreviousIndex:

                previousnode = tempNode

            if i == tempRange:

                previousnode.nextvalue = None 

                break

            tempNode = tempNode.nextvalue

            i +=1



   



linked = SingleLinkedList()



print("SingleLinkedList....")

print("")

print("choice 1 for numeric & 2 for string list initialization")

target = int(input("Enter choice:"))



def targets():

    while True:

         print("Choice - 1 adding the item to first")

         print("Chocie - 2 adding the item to last")

         print("Chocie - 3 adding the item to middle")

         print("Choice - 4 Removing the element from (1) index")

         print("Choice - 5 Removing the elemnt from Middle Index")

         print("Chocie - 6 Removing the elemnt from Last index")

         print("Chocie - 7 Show The LinkedList Nodes..")

         print("Chocie - 8 For Quit...")

         print()

         choice = int(input("Enter the chocie: "))

         

         if choice == 1:

             data = input("Enter the Element: ")

             linked.addItem(data)

         elif choice == 2:

             data = input("Enter the Element: ")

             linked.addLast(data)

         elif choice == 3:

             data = input("Enter the Element: ")

             linked.addtheEmid(data)

         elif choice == 4:

             linked.RemoveFirstItem()

         elif choice == 5:

             linked.RemoveMid()

         elif choice == 6:

             linked.RemoveLast()

         elif choice == 7:

             linked.listprint()

         elif choice == 8:

             quit()



if target == 1:

    linked.headvalue = Node(0)

    print()

    targets()

elif target == 2:

    linked.headvalue = Node("hello")

    print()

    targets()