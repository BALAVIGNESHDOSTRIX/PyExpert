'''
            DATE : 26/04/2019

            SCOPE : 
                    For Generating the 10 digit Random Password with given Sequence.
'''

from random import randint as rn 
import os 

class PasswordGenerator:

    def __init__(self):
        if os.path.isfile('pass.txt'):
            os.remove('pass.txt')
            # print('Exsisted')
        else:
            # print('Not Exsisted')
            with open('pass.txt','w') as writer:
                writer.close()


    def GenRandom_10_pass(self):
        print()
        thr_digit = str(input('Enter First 3 digit Sequence: '))
        s = ''.join(["%s" % rn(0,9) for dig in range(0,7)])
        res = str(thr_digit) + s
        print(res) 

    def GenRandom_10_pass_list(self):
        print()
        thr_digit = str(input('Enter First 3 digit Sequence: '))
        no_of_p = int(input('How Many Password you Need: '))
        is_con_check = str(input('Print the List in Console "yes" or "no : '))

        for x in range(0,int(no_of_p)):
            if is_con_check == 'yes':
                s = ''.join(["%s" % rn(0,9) for dig in range(0,7)])
                res = str(thr_digit) + s 
                print(res)
            elif is_con_check == 'no':
                s = ''.join(["%s" % rn(0,9) for dig in range(0,7)])
                res = str(thr_digit) + s
                with open('pass.txt','a') as writer:
                    writer.write(res + '\n')

    @staticmethod
    def Terminate():
        print('Thankyou For using PasswordGenerator.....')
        quit()

PasGen = PasswordGenerator()

print(10 * '*' + '' + 'PassWord Generator' + '' + '*' * 10)

def ActionDispatcher(choice):
    {
        1 : PasGen.GenRandom_10_pass,
        2 : PasGen.GenRandom_10_pass_list,
        3 : PasGen.Terminate
    }.get(choice)()

print()
print('Enter Choice 1 for Generate "7" digit Random Password.')
print('Enter Choice 2 for Generate List of "7" digit Random Password.')
print('Enter Choice 3 for Quit....')
print()

while True:
    print()
    choice = int(input('Please Enter Your Choice: ')) 
    ActionDispatcher(choice)
