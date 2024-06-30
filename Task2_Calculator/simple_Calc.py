"""
Company : CodeSoft
_______________________________________
Student : AUBAI ALKHABBAZ
_______________________________________
Program :  Simple Calculator using python
_______________________________________
py version : 3.8
_______________________________________
Libraries :  math
_______________________________________
"""
import math
# define Class name : cal_fun
class cal_fun:
    def __init__(self, x, y, opt):
        self.x = x
        self.y = y
        self.opt = opt
    # define All operation func  ( #Declaring private methods -  you can't access them)
    def __sum (self):
        print("the sum is =", self.x + self.y)
        return self.x + self.y
    def __sub (self):
        print("the subtract is =", self.x - self.y)
        return self.x - self.y
    def __prod (self):
        print("the prod is =", self.x * self.y)
        return self.x * self.y
    def __div (self):
        print("the div is =", self.x / self.y)
        return self.x / self.y
    def __Log_cal(self):
        print(f"the Log of {self.x} is = ", math.log(self.x))
        return math.log(self.x)
    def __Exp_cal(self):
        print(f"the Exp of {self.x}  is = ", round(math.exp(self.x),2))
        return round(math.exp(self.x),2)
    def __factorial_cal(self):
        print(f"the factorial  {self.x}  of is = ",math.factorial(self.x))
        return math.factorial(self.x)
    def __Sqrt_cal(self):
        try:
            print (f"the Sqrt of {self.x} is = ",math.sqrt(self.x))
            return math.sqrt(self.x)
        except ValueError as ve:
            print(f'You entered {self.x}, which is not a positive number.',ve)
            return "nan"
    def __prim_cal(self):
        '''Check if num is prime or not.'''
        for i in range(2, int(math.sqrt(self.x)) + 1):
            if self.x % i == 0:
                print(f"the number {self.x}  is not a prime number !")
                return False
        print(f"the number {self.x}  is a prime number !")
        return True
    #______________________________________________________________________

    #define func for  Opt +,-,*,/   (# Declaring public method)
    def result(self):
        if self.opt == '+':
            # call sum func
            self.__sum()
        elif self.opt == '-':
            # call abs func
            self.__sub()
        elif self.opt == '*':
            # call prod func
            self.__prod()
        elif self.opt == '/':
            # call div func
            self.__div()
        elif self.opt == 'L':
            # call Log(x) func
            self.__Log_cal()
        elif self.opt == 'E':
            # call Exp(x) func
            self.__Exp_cal()
        elif self.opt == 'F':
            # call Factorial(x) func
            self.__factorial_cal()
        elif self.opt == "S":
            # call sqrt(x) func
            self.__Sqrt_cal()
        elif self.opt =="P":
            # call prime(x) func
            self.__prim_cal()
        else:
            print("you Enter Non valid operation ! please try Again")



# ______________________________Main func_______________________________
def main():
    # loop break if you enter q
    while True:
        # inpt opt value
        opt = input("__________________________ ##Welcome to simple Calculator , Created by AUBAI ALKHABBAZ## __________________________ \n\t"
                    "1-Enter opt +  , - , * , /\n\t"
                    "2-L for Log\n\t"
                    "3-E for Exp\n\t"
                    "4-F for Factorial\n\t"
                    "5-S for sqrt\n\t"
                    "6-P for prime\n\t"
                    "7-q to quit\n"
                    "Enter your OPT =")
        if opt == 'q':
            break
        # ('F' or 'S' or 'E' or 'L' or 'E') don't need Y Input so y =0
        elif (opt == 'F' or  opt =='S' or  opt =='E' or  opt =='L' or  opt =='E' or opt =='P'):
            # convert input from str to int
            x = int(input("Enter first number x  = \n"))
            y=0
            # class  cal_fun  - parameters (x, y, opt )
            cal = cal_fun(x, y , opt)
            # call func result from class cal_fun
            cal.result()
            #cal._cal_fun__sum()
        else :
            #  enter x and y and convert input from str to int
            x = int(input("Enter first number x  = \n"))
            y = int(input("Enter second number y  = \n"))
            # class  cal_fun  - parameters (x, y, opt )
            cal = cal_fun(x, y, opt)
            # call func result from class cal_fun
            cal.result()
            #cal._cal_fun__sum()

if __name__ == "__main__":
    main()