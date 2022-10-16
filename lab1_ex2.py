#Write a program that finds the sum of numbers from 1 to 1000 using a for loop.
#Output; sum of numbers 1 to 1000
#Program; Sumation using a forloop

def main():
    sum = 0
    for i in range (1,1001): #range (Start, stop, step)
        sum = sum + i
    print("The sum of numbers 1 to 1000 is", sum)
    print()

    
main()


#Write a program that inputs 5 numbers from the user in a loop and finds the sum of the numbers.
#input = any numbers you would want to sum
#Output = Sum of the listed numbers
#process; Get the list of numbers, convert them to intergers and then sum them

#1st

def main():
    numbers = input('Enter at any 5 numbers separated by space:') 
    list_of_numbers = list (map(int,numbers.split()))        #use map() to convert each number on the list of integers ## map is used when you want to apply a single transformation function to all the iterable elements
    total = 0
    for numbers in list_of_numbers:
        total = total + numbers
    print("The total sum of", list_of_numbers,"is", total)
    print()
    print()

main()


#2nd Way

def main():
    sum = 0
    for i in range (5):
        numbers = int(input("Enter any 5 numbers to sum:"))
        sum = sum + numbers

    print("The sum of the numbers:", sum)
    print()
    print()


main()                 


#1st way to do it

#Modify the above program so that it finds the sum and also the average of the 5 numbers.

def main():
    numbers = input('Enter any 5 numbers separated by space:') 
    list_of_numbers = list (map(int,numbers.split()))        #use map() to convert each number on the list of integers ## map is used when you want to apply a single transformation function to all the iterable elements
    total = 0
    n = len(list_of_numbers)
    for numbers in list_of_numbers:
        total = total + numbers
        average = total / n
    print("The total sum of", list_of_numbers,"is", total, "and the total average is", average)
    print()
    print()



main()


#2nd way to do it

def main():
    sum = 0
    for i in range (5):
        numbers = int(input("Enter any 5 numbers to sum:"))
        sum = sum + numbers
        average = sum /5

    print("The average of the numbers:", average)
    print()
    print()


main()  
