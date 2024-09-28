'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Finding the day by the date    
'''

class Util:
    @staticmethod
    def findingDay(d,m,y,days):
          '''
          Description: 
              This function will finding the day using the date   
          Parameters:
              day: int: user input day of the date
              month: user input month of the date 
              year: user input year of the date
              days: list of the days in week       
          Return :
              None
          '''

          yo = y - (14 - m) // 12
          x = yo + yo // 4 - yo // 100 + yo // 400
          mo = m + 12 * ((14 - m) // 12) - 2
          do = (d + x + (31 * mo) // 12) % 7
          print(days[do])
        
def main():
    day=int(input("Enter the day: "))
    month=int(input("Enter the month: "))
    year=int(input("Enter the year: "))
    days=["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    Util.findingDay(day,month,year,days)
    
if __name__=="__main__":
    main()