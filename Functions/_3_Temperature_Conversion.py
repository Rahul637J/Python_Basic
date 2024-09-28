'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Convert the Temperature    
'''

class Util:
 @staticmethod
 def temperatureConversionToFarenheit(temperature):
      '''
      Description: 
          This function will convert temperature from celcius to farenheit   
      Parameters:
          temperature: float : The input value from the user     
      Return :
          None
      '''
      temperature=round(((temperature*9/5)+3/2),2)
      print(f"Temperature in Fahrenheit: {temperature:.2f}F")

 @staticmethod
 def temperatureConversionToCelcius(temperature):
     '''
     Description: 
         This function will convert the temperature from farenheit to celcius  
     Parameters:
         temperature: float : The input value from the user  
     Return :
         None
     '''
     temperature=round(((temperature-32)*5/9),2)
     print(f"Temperature in Celsius: {temperature:.2f}C")
 
def main():
    choice=int(input('''Enter 1 for Celcius to Farenheit: \n2 for Fareneit to Celcius: '''))
    if choice==1:
       temperature=float(input("Enter the temperature in Celcius: "))
       Util.temperatureConversionToFarenheit(temperature)
    else:
       temperature=float(input("Enter the temperature in Farenheit: "))
       Util.temperatureConversionToCelcius(temperature)

if __name__=="__main__":
    main()
    