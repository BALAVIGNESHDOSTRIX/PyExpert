'''

DEVELOPER NAME: BALAVIGNESH.M
IMPLEMENTED DATE : 17-11-2018

            ProjectName : DomainSlice

            Project Scope Details:
                This project is intresting to slice the user entered string to get the seprate information from
                that string about the user

            Implementation Details:
                User have to enter the email like (lazylaearners@gmail.com) i have to slice this string by using
                list or str slicing method like email[::] here first declaration is strating index called as
                inclution range , execulation range , 3 parameter is iteration step but in this project we not
                using 3-rd parameter

                if i want slice :===> x = lazy@gmail.com means

                name = x[:x.index("@"):]
                this declaration slice l to @ before here inclution is (l) index = 0,
                exclution point is ("@) so answer is: lazy
'''

class DomainSlice:

    @staticmethod
    def GetDomainInfo():

        print("Example : lazylaearners@gmail.com")
        Email = str(raw_input("Enter Your Email String : "))

        User_Info = Email[:Email.index("@"):]
        Domain_Info = Email[Email.index("@") + 1:Email.index("."):]
        Domain_Category = Email[Email.index(".") + 1::]

        print("User Name is : ", User_Info)
        print("Domain Name is :",Domain_Info)

        if Domain_Category == "com":
            print("Domain Info :com : {com}".format(com = "Commercial"))
        elif Domain_Category == "org":
            print("Domain Info :org : {org}".format(org = "Organization"))
        elif Domain_Category == "edu":
            print("Domain Info :edu : {edu}".format(edu = "Education"))
        elif Domain_Category == "gov":
            print("Domain Info: gov : {gov}".format(gov = "Goverment"))
        else:
            print("Domain Info :",Domain_Category)



domain = DomainSlice()
domain.GetDomainInfo()
