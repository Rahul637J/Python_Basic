'''
@Author: Rahul 
@Date: 2024-07-31
@Last Modified by: Rahul 
@Last Modified time: 2024-07-31
@Title: Finding the binary for decimal    
'''
class Util:
    @staticmethod
    def toBinary(decimal):
         '''
         Description: 
              This function to find the square root 
         Parameters:
              num: int: the user input for findig num         
         Return:
              t:  the squareroot of num
         '''
         binary = []
         while decimal > 0:
             remainder = decimal % 2  
             binary.append(remainder)  
             decimal = decimal // 2
         
         binary.reverse()
         return binary

def main():
    decimal = int(input("Enter the decimal number: "))
    binary = Util.toBinary(decimal)
    for i in binary:
        print(i, end="") 

if __name__ == "__main__":
    main()

