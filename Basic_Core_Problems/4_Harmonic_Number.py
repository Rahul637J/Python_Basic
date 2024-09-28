'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by:  Rahul
@Last Modified time: 2024-07-29
@Title: Calculate the sum of the Harmonic series     
'''

def harmonic_sum(num):
    '''
    Description:
        This function will sum and return all the numbers with reciprocal of 1 from the 1 till num   
    Parameters:
        num: The user input in int type 
    Return:
        sum: a sum of all numbers with reciprocal with 1 
    '''

    i=1
    sum=0.0
    for i in range(1,num+1):
        sum+=1/i
    return sum

def main():
    num=int(input("Enter the number for sum of harmonic sum: "))
    print("The sum is",round(harmonic_sum(num),5))

if __name__=="__main__":
    main()

