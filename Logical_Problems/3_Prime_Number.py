'''
@Author: Rahul
@Date: 2024-07-26
@Last Modified by: Rahul
@Last Modified: 2024-07-26
@Title: Program to check the input number is prime or not
'''

def factors(num):
     """
    Description: 
        Function to find the factors for the num.
    Parameters:
       num : int: the value for finding the factors
    Returns:
       count : int : the count of the factors
    """
     count=0
     for i in range(1,num//2+1):
         if num%i==0:
             count+=1
             
     return count

def is_prime(num):
     """
    Description:   
        Function to check the count of the factors of the num.
    Parameters:
       num: int: input from the user 
    Returns:
       None
    """
     
     factors_count=factors(num)
     if factors_count<=2:
         print(num,"is a prime number")
 
     else:
         print(num,"is not a prime number")    

def main():
    num=int(input("Enter the number to check prime or not: "))
    is_prime(num)

if __name__ == "__main__":
    main()