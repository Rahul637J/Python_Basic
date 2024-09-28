'''
@Author: Rahul 
@Date: 2024-07-29
@Last Modified by: Rahul 
@Last Modified time: 2024-07-29
@Title: Calculate the Difference in Probability of Heads and Tails Over N Flips
'''

import random

def calculate(flips):
     '''
    Description: 
        This function will calculate the probability of heads and tails in percentage  
    Parameters:
        flips: The user input for the Flips
    Return :
        None
    '''
      
     head,tail=0,0
     
     for i in range(1,flips+1):
         random_number = random.randint(0,1)
         if random_number==0:tail+=1
         else:head+=1
     
     head=int(head/flips*100)
     tail=int(tail/flips*100)
     print("Percentage of Head vs Tails is ",head,"% ",tail,"%")
  
def main():
    flips=int(input("Enter the Number of times to flip coins in positive Integer: "))
    if flips<1 : flips=int(input("Enter the positive Integer: "))
    calculate(flips)
     
if __name__=="__main__":
    main()

