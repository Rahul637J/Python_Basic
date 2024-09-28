'''
@Author: Rahul
@Date: 2024-07-26
@Last Modified by: Rahul
@Last Modified: 2024-07-26
@Title: Program to print the fibbonacci series by the user limit
'''
def fibbonacci_series(limit):
     """
    Description: 
        Function to demonstrate a simple operation and return a value.
    Parameters:
       limit: int: input from the user
    Returns:
       None
    """
     series=[0,1]
     for i in range(2,limit+1):
         sum=series[i-1]+series[i-2]
         series.append(sum)
     print(series)    

def main():
    limit=int(input("Enter the limit for the fibbonacci series: "))
    fibbonacci_series(limit)

if __name__ == "__main__":
    main()