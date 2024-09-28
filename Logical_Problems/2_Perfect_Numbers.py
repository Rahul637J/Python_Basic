'''
@Author: Rahul
@Date: 2024-07-26
@Last Modified by: Rahul
@Last Modified: 2024-07-26
@Title: Program to check the input number is perfect or not.
'''

def is_perfect(num):
     """
    Description: 
        Function to check the number is perfect or not.
    Parameters:
       num: int : input from the user
    Returns:
       None
    """
     sum=0
     for i in range(1,round(num/2)+1):
         if num%i==0:
             sum+=i
 
     if sum==num:
         print(num," is a perfect number!!!")
 
     else:
         print(num," is not a perfect number!!")            

def main():     
  num=int(input("Enter the positive number to check for Perfect or Not: "))
  is_perfect(num)

if __name__ == "__main__":
    main()
