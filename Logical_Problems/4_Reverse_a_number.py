'''
@Author: Rahul
@Date: 2024-07-26
@Last Modified by: Rahul
@Last Modified: 2024-07-26
@Title: Program to reverse the number
'''

def reverse(num):
     """
    Description: 
        Function to reverse the number.
    Parameters:
        num: int: input from the user
    Returns:
       None
    """
     
     reverse_num=0
     while num>0:
         reverse_num=reverse_num*10+num%10
         num//=10
     print("After reverse = ",reverse_num)    

def main():
    num=123
    print("Before reverse = ",num)
    reverse(num)

if __name__ == "__main__":
    main()

