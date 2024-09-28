'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Program to swap the two numbers
'''

def swap_two_numbers(a,b):
     '''
    Description: 
        This function find all the prime factors of the num   
    Parameters:
        a: any type :The input value of the user 
        b: any type :The input value of the user 
    Return :
        None
    '''
     a=a+b
     b=a-b
     a=a-b
     print("After swap a=",a,"b=",b)

def main():
    a=int(input("Enter the 1st value for swap: "))
    b=int(input("Enter the 2nd value for swap: "))
    
    print("Before swap a="+str(a)+" b="+str(b))
    swap_two_numbers(a,b)

if __name__=="__main__":
    main()


