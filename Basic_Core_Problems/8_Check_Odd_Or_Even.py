'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Program for find N number is odd or even
'''

def check_odd_or_even(num):
     '''
    Description: 
        This function find all the number is odd or even   
    Parameters:
        num: int: The user input 
    Return :
        None
    '''
      
     if num%2==0:
         print(num,"---> is an even number")
     else:
         print(num,"---> is an odd number")
    
def main():
    num=int(input("Enter the number to check odd or even: "))
    check_odd_or_even(num)

if __name__=="__main__":
    main()
