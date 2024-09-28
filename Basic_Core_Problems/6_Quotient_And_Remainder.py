'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by:  Rahul
@Last Modified time: 2024-07-29
@Title: Program for finding the Quotient and Remainder for the dividend and divisor
'''

def division(dividend,divisor):
     '''
    Description: 
        This will calculate the Quotient and Remainder for the dividened and divisor   
    Parameters:
        dividend: The user input for the numerator value
        divisor: The user unput for the Denaminator value
    Return :
        None
    '''
      
     quotient=dividend//divisor
     remainder=dividend%divisor
     print("The quotient is",quotient)
     print("The remainder is",remainder)
 
def main():
    dividend=int(input("Enter the dividend: "))
    divisor=int(input("Enter the divisor: "))
    division(dividend,divisor)

if __name__=="__main__":
    main()

