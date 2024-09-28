'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified time: 2024-07-29
@Title: Finds wether the year is Laep year or not 
'''

def check_leapyear():
    '''
    Description: 
        This function will find the year is leap year or not 
    Parameters:
        None
    Return:
        None
    '''

    year=int(input("Enter the year to check leap year or not in 4 digits: "))
    if year<1000 or year>9999 :
        year=int(input("Enter the year in 4 digits: "))   
    if year%4==0 :
      if year%100==0 and year%400!=0:
        print(year,"is not a leap year")
      else:
        print(year,"is leap year")
    else:
     print(year,"is not a leap year")    

def main():
   check_leapyear()

if __name__=="__main__":
    main()
   
         
