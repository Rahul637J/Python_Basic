'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by:  Rahul
@Last Modified time: 2024-07-29
@Title: Find all the factors which all are prime for N input
'''

import math
def prime_factors(num):
    '''
    Description: 
        This function find all the prime factors of the num   
    Parameters:
        num: The user input in int type
    Return :
        factors: list: All the prime factors in list
    '''
    factors=[]

    while num%2==0:
        factors.append(2)
        num=num//2

    for i in range(3,int(math.sqrt(num))+1,2):
        while num%i==0:
            factors.append(i)
            num=num//i

    if num>2:
        factors.append(num)

    return factors    

def main():
    num=int(input("Enter the number to find prime factors: "))
    print(prime_factors(num))

if __name__=="__main__":
    main()


