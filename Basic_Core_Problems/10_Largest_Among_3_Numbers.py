'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Find the largest of the 3 numbers
'''
def find_largest(numbers):
     '''
    Description: 
        This function will find the largest of 3 num
    Parameters:
        numbers: list : The user input in list type 
    Return :
         large_num: The largest number in list
        
    '''
      
     large_num=numbers[0]
     for num in numbers:
         if num>large_num:
             large_num=num
     return large_num

def main():
    numbers=[]
    for i in range(1,4):
        numbers.append(int(input("Enter the number to check : ")))
    print(find_largest(numbers),"is the largest of 3")

if __name__=="__main__":
    main()
