'''
        DEVELOPER NAME: BALAVIGNESH.M
        IMPLEMENTED DATE: 18-11-2018

                    ProjectName : Movie Theatre

                    Project Scope:
                        To imlementing the real Movie Theatre ticket reservation simulation project

                    Impelemtation Details:
                         I have initialize the dictionary.
                         key is flim name and value is [age,available_ticket,rupees]

                         like Ex: a = {"Sarkar" : [18,10,20]} here "Sarkar" is the Movie name (key) and values
                                  [18,10,20] 18 is the Age restriction, 10 is the available tickets, 20 is the 
                                  amount of one ticket. these details in the form fo list [18,10,20]

                                  Accessing the value Like:

                                  dictionary_name[key][value_index] ====> a["sarkar"][0] = 18
                                                                          a["sarkar"][1] = 10
                                                                          a["sarkar"][2] = 20
'''

import time 

class Flim:

    def __init__(self,Moviconfig):
        self.Flim_database = Moviconfig

    

    def ShowTheFlimDetails(self):
        for key,value in self.Flim_database.items():
            print("Available Movie Names : {x}. One Ticket Rate is: {y} Rupees.".format(x=key,y=value[1]))
            print("")    
        
        user_input = str(input("Are you want to buy choose(yes/no): "))

        if user_input == "yes":
            self.TicketReservation()
        else:
            print("Thakyou welcome....")
            time.sleep(1)
            

    
    def TicketReservation(self):

        while True:
            userchocie = input("Enter the Flim name to check : ").strip().title()

            if userchocie in self.Flim_database:
                 print("Processing.....")
                 time.sleep(2)

                 age = int(input("Please enter your age to confirm Age Restriction: "))
                 print("Verifying the Age.....")
                 time.sleep(3)
                 if age >= self.Flim_database[userchocie][0]:
                      print("")
                      print("Yes you can watch the Movie....")
                      print("")
                      print("Available Tickets for your movie: ",self.Flim_database[userchocie][1])

                      userTicket = int(input("Enter the No Ticket you want: "))

                      if userTicket <= self.Flim_database[userchocie][1]:
                          total = userTicket * self.Flim_database[userchocie][2]
                          print("Processing.....")
                          time.sleep(3)
                          print("Your total cost of {x} {y} flim Ticket is :{z}".format(x=userTicket,y=userchocie,z= total))
                          amount = int(input("Please enter the amount:"))

                          if amount == total:
                              print("Please Wait for few moments ......")
                              time.sleep(4)
                              print("Yor have receive the {x} Tickets for {y} Flim.".format(x=userTicket,y=userchocie))
                              print("")
                              print("Thankyou for Coming....Enjoy the Movie...")
                              break
                          else:
                              print("Invalid amount Please try again")
                                
                      else:
                          print("Sorry your need tickets not available.....")
                          print("")
                          print("Available Tickets count is: {x}".format(x=self.Flim_database[userchocie][1]))
                 else:
                     
                     print("You are not Eligible to watch this movie because your age is restricted to watch")
                        
            else:
                print("Sorry The Flim is not available Please select another Flim")
                    

flim = Flim({"Ice Age":[18,20,5],"Tom & Jerry":[10,10,10],"Men in Block":[12,5,20],"Sarkar":[18,5,100],"Devil strom":[21,6,30],"sex city2":[20,10,150],
        "Crazy Girl3":[22,10,160],"Harry Potter":[12,19,100],"IronMan2":[18,20,100]})
flim.ShowTheFlimDetails()
                



           

            
            
               
                

                
                    
                    

                   
                       
                      
                    
                        
               
                    
      
            


        


                    
                    


        

