#Exercise 1

a = 100
b = 100.0
 #An error appears for invalid decimal literal when you define # c = 100L


type(a)
type(b)

#Getting the Squares of numbers
def main():
    num = input("Enter a number to get its square:")
    result = int(num)**2                #The correction was to convert the num variable to an int
    print ("The square of",num, "is:", result)
    print()     #To create space
    

main ()


#Modify the program to print square roots
import math
def main():
    number = input("Enter any number to get the square root:")
    result = math.sqrt(int(number))    #Using sqrt you must import math
    print ("The square root of",number, "is:", result)
    print()


main()

#Getting the factorial of a number using the math function
import math
def main ():
    digit = input("Enter any number to find factorial:")
    factorial = math.factorial (int(digit))
    print ("The factorial of", digit, "is:", factorial)
    print()


main ()

#Getting the factorial of a number using Forloop

def factor():
    n = input("Please enter a whole number to get its factorial:")
    fact = 1                               #The factorial of any number will not be less than                                      #We have to define n
    for factor in range (1,int(n)+1):      # The correction is to convert n to an int
        fact = fact * factor
    print("The factorial of",n,"is", fact)
    print()
        


factor()


#Replace fact = fact * factor with fact = fact * 5

def factor():
    n = input("Please enter a whole number to get its factorial:")
    fact = 1
    for factor in range (1,int(n)+1):      
        fact = fact * 5                      #This formula is taking the value of n as a power of 5. E.g input n as 4 and the result is 5**4
    print("The factorial of",n,"is", fact)
        


factor()
    






    




