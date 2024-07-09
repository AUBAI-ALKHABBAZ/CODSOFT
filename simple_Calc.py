"""
Company : CodeSoft
_______________________________________
Student : AUBAI ALKHABBAZ
_______________________________________
Program :  Simple Calculator  with Extra features using python
_______________________________________
py version : 3.8
_______________________________________
Libraries :  math, numpy, pyplot
_______________________________________
"""
import math
import numpy as np
import matplotlib.pyplot as plt
#______________________________________________________
# define Class name : rad_fun
#______________________________________________________
class rad_fun:
    def __init__(self, R_S, R_E, opt):
        self.R_S = R_S
        self.R_E = R_E
        self.opt = opt

    # define All operation func  ( #Declaring private methods -  you can't access them)
    def __cos(self):
        print(f"the cos of {self.R_S} is  =", math.cos(self.R_S))
        return math.cos(self.R_S)
    def __sin(self):
        print(f"the sin of {self.R_S} is  =", math.sin(self.R_S))
        return math.sin(self.R_S)
    def __tang(self):
        print(f"the tan of {self.R_S} is  =", math.tan(self.R_S))
        return math.tan(self.R_S)

    def __graph_cos(self):
        # linspace method  user enter start and end for plot - step =20
        in_array = np.linspace(self.R_S, self.R_E, 20)
        out_array = []
        # for loop to append range that user selected in array  --out_array = []
        for i in range(len(in_array)):
            out_array.append(math.cos(in_array[i]))
            i += 1
        # plot  x and y  plot for cos
        plt.plot(in_array, out_array, color='red', marker="o")
        plt.title("math.cos()")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    def __graph_sin(self):
        # linspace method  user enter start and end for plot - step =20
        in_array = np.linspace(self.R_S, self.R_E, 20)
        out_array = []
        #for loop to append range that user selected in array  --out_array = []
        for i in range(len(in_array)):
            out_array.append(math.sin(in_array[i]))
            i += 1
        # plot  x and y  plot for sin
        plt.plot(in_array, out_array, color='blue', marker="o")
        plt.title("math.sin()")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.show()

    # define func for  Opt cos,sin,tan,graph_cos,graph_sin  (# Declaring public method)
    def result(self):
        if (self.opt == 'graph_cos'):
            # call graph_cos func
            self.__graph_cos()
        elif(self.opt == 'graph_sin'):
            # call graph_sin func
            self.__graph_sin()
        elif (self.opt == 'cos'):
            # call cos func
            self.__cos()
        elif(self.opt == 'sin'):
            # call sin func
            self.__sin()
        elif(self.opt == 'tan'):
            # call tan func
            self.__tang()
        else:
            print("you Enter Non valid operation ! please try Again")


#______________________________________________________
# define Class name : cal_fun
#______________________________________________________
class cal_fun:
    def __init__(self, x, y, opt):
        self.x = x
        self.y = y
        self.opt = opt
    # define All operation func  ( #Declaring private methods -  you can't access them)
    # return used for testing all functions  using unittest in file testing_simple_Calc.py
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
    def __sum_array_A(self):
        print(f"the Array A = {self.x} \n")
        print("Sum of arr A : ", np.sum(self.x))
    def __prod_array_A_B(self):
        try :

            print(f"the Array A = {self.x} \n")
            print(f"the Array B = {self.y} \n")
            print("the prod of array A and B = ", np.multiply(self.x, self.y))
        except ValueError as pe:

            print(f'You entered  A ={self.x} and  B ={self.y},  you should check prod rules mxn for A and B  .',pe)
            return "nan"
    def __max_array_A(self):
        # map function Syntax : map(fun, iter) , returns a list of elements for max number in raws of array A so we apply max twice to get the max number
        self.y =list(map(max, self.x))
        print("the max numbers in Raws are  = ",self.y)
        print(f"the max number in Array A {self.x} =",max(map(max, self.x)))

    def __min_array_A(self):
        # map function Syntax : map(fun, iter) , returns a list of elements for min number in raws of array A so we apply min twice to get the min number
        self.y =list(map(min, self.x))
        print("the min numbers in Raws are  = ",self.y)
        print(f"the min number in Array A {self.x} =", min(map(min, self.x)))

    def __fabo_fun(self):
        '''
        The Fibonacci series follows a simple mathematical logic. The first two numbers in the sequence are 0 and 1.
        From the third number onward, each number is the sum of the two preceding ones. Mathematically,
        Syntax :
                                F(self.x)=F(self.x−1)+F(self.x−2)
                where F(n) is the nth number in the Fibonacci sequence.
        '''
        #In below, the function uses a list to store the Fibonacci numbers :
        # 1-  It starts with the initial values [0, 1]
        fib_series = [0, 1]
        # 2- and iterates through the range from 2 to self.x
        for i in range(2, self.x):
            #3- calculating each Fibonacci number and appending it to the list
            fib_series.append(fib_series[-1] + fib_series[-2])
        print(f"Fibonacci Series for {self.x} is =", fib_series, "\nand the sum of Fibonacci Series is = ",sum(fib_series))
        return sum(fib_series)

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
        elif self.opt == 'SA':
            # call sum_array_A() func
            self.__sum_array_A()
        elif self.opt == "PA":
            # call prod_array_A_B() func
            self.__prod_array_A_B()
        elif self.opt == 'MA':
            # call max_array_A() func
            self.__max_array_A()
        elif self.opt == "MIA":
            # call min_array_A() func
            self.__min_array_A()
        elif self.opt == "fab":
            # call fabo_fun() func
            self.__fabo_fun()
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
                    "7-fab for Fibonacci\n\t"
                    "8-A for Array\n\t"
                    "9-R for Rad - cos/sin/tan/cot\n\t"
                    "10-q to quit\n\t"
                    "Enter your OPT =")
        if opt == 'q':
            break
        # ('F' or 'S' or 'E' or 'L' or 'E') don't need Y Input so y =0
        elif (opt == 'F' or  opt =='S' or  opt =='E' or  opt =='L' or  opt =='E' or opt =='P' or opt =='fab'):
            # convert input from str to int
            x = int(input("Enter first number x  = \n"))
            y=0
            # class  cal_fun  - parameters (x, y, opt )
            cal = cal_fun(x, y , opt)
            # call func result from class cal_fun
            cal.result()
            #cal._cal_fun__sum()
        elif (opt == "A") :
            opt = input("\t__________Enter opt of Array __________\t\n\t"
                        "1-SA for sum the array \n\t"
                        "2-PA for prod two arrays\n\t"
                        "3-MA for MAX number in array\n\t"
                        "4-MIA for MIN number in array = ")
            # A basic code for matrix input from user
            if (opt == 'SA' or opt == "MA" or opt == 'MIA'):
                x = int(input("Enter the number of rows for A Array:"))
                y = int(input("Enter the number of columns for A Array :"))

                print("Enter the entries in a single line (separated by space): ")

                # User input of entries in a
                # single line separated by space
                # using map function than for loop function to input the array
                entries = list(map(int, input().split()))
                matrix_1 = np.array(entries).reshape(x, y)
                y=0
                x=matrix_1
                cal = cal_fun(x,y,opt)
                cal.result()
            elif ( opt == 'PA'):
                # A basic code for matrix input from user
                x = int(input("Enter the number of rows for A Array:"))
                y = int(input("Enter the number of columns for A Array:"))

                # Initialize matrix A
                matrix_1 = []

                print("Enter the entries rowwise for Array A:")

                # For user input
                for i in range(x):  # x for loop for row entries
                    a = []
                    for j in range(y):  # y for loop for column entries
                        a.append(int(input()))
                    matrix_1.append(a)

                # B basic code for matrix input from user
                x = int(input("Enter the number of rows for B Array:"))
                y = int(input("Enter the number of columns for B Array:"))

                # Initialize matrix B
                matrix_2 = []

                print("Enter the entries rowwise for Array B:")

                # For user input
                for i in range(x):  # x for loop for row entries
                    a = []
                    for j in range(y):  # y for loop for column entries
                        a.append(int(input()))
                    matrix_2.append(a)
                y = matrix_2
                x = matrix_1
                cal = cal_fun(x, y, opt)
                cal.result()
        elif(opt == 'R'):
            opt = input("\t__________Enter opt of Rad __________\t\n\t"
                        "1-cos for cos(rad) \n\t"
                        "2-sin for sin(rad) \n\t"
                        "3-tan for tan(rad) \n\t"
                        "4-graph_cos for plot cos(start,end) or graph_sin for plot sin(start,end)  = ")
            if (opt == 'graph_cos'or opt=='graph_sin'):
                R_S =  float(input(f"Enter start number for{opt}  = \n"))
                R_E = float(input(f"Enter end number {opt}  = \n"))
                cal = rad_fun(R_S,R_E,opt)
                cal.result()
            elif(opt == 'cos' or opt == 'sin' or opt == 'tan' ):
                R_S =  float(input(f"Enter Rad number for {opt}  = \n"))
                R_E = 0
                cal = rad_fun(R_S,R_E,opt)
                cal.result()
            else:
                R_S = float(input(f"Enter Rad number for {opt}  = \n"))
                R_E = float(input(f"Enter end number {opt}  = \n"))
                cal = rad_fun(R_S, R_E, opt)
                cal.result()

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