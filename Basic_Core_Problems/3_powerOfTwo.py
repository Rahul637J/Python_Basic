'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Calculate the exponent of 2 for the N time
'''

def print_power_of_2(n):
    '''
    Description:
        This function generate the exponent of 2 by n times 
    Parameters:
        n: The user input for the exponent of 2
    Return:
        None
    '''
    
    if n<0 or n>31:
        print("Invalid input : The number should below or equal to 31 and greater than or equal to 0")
        return
    
    for i in range(0,n+1):
        expo=2**i
        print("2 ^",i,"=",expo)

def main():    
    n=int(input("Enter the number to print for exponent of 2: "))
    print_power_of_2(n)

if __name__=="__main__":
    main()