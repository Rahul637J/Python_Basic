'''
@Author: Rahul 
@Date: 2024-07-31
@Last Modified by: Rahul 
@Last Modified time: 2024-07-31
@Title: convert to Binary using toBinary function and perform the following functions.
        i. Swap nibbles and find the new number.
        ii. Find the resultant number is the number is a power of 2.       
'''

from _6_ToBinary import Util

class SwapNibble:
    @staticmethod
    def powOftwo(num):
         '''
         Description: 
              This function will checks for the num is exponent of 2 
         Parameters:
              num: int: the input value for checking exponent of 2          
         Return:
               boolean: it will return the boolean value based on the exponent of 2
         '''
         expo = 1
         while expo <= num:
             if expo == num:
                 return True
             expo *= 2
         return False
 
    @staticmethod
    def toDecimal(binary):
         '''
         Description: 
              This function will find the decimal of the binary 
         Parameters:
              binary: int: the binary value as input         
         Return:
              sum: the decimal value of binary
         '''
         sum = 0
         for i in range(len(binary)):
             sum += binary[i] * (2 ** (len(binary) - 1 - i))
         return sum

    @staticmethod
    def binary(decimal):
         '''
         Description: 
              This function find the binary value for decimal 
         Parameters:
              num: int: the user input value         
         Return:
              None
         '''
         binary = Util.toBinary(decimal)
         binarySwap = []
         
         mid = len(binary) // 2
         binarySwap = binary[mid:] + binary[:mid]
         
         decimal_value = SwapNibble.toDecimal(binarySwap)
         result = SwapNibble.powOftwo(decimal_value)
         print(f"Swapped binary: {''.join(map(str, binarySwap))}")
         print(f"Decimal value of swapped binary: {decimal_value}")
         print(f"Is decimal value a power of 2: {result}")
        
        
def main():
    decimal = int(input("Enter the decimal value: "))
    SwapNibble.binary(decimal)

if __name__ == "__main__":
    main()

