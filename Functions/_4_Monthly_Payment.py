'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: calculates the monthly payments    
'''
class Util:
    def calculatePayment(P,Y,R):
        '''
         Description: 
             This function to calculate the monthly payments by P,Y,R    
         Parameters:
             P: Principle amount 
             Y: Duration of loan in years
             R: Rate of intrest 
         Return :
             None
         '''
        n=Y*12
        r=R/(12*100)
        payment = round((P * r / 1 - (1 + r) ** -n),2)
        print(f"The payment for your loan is : {payment}")

def main():
    principle=int(input("Enter the principal amount: "))
    year=int(input("Enter the years of loan duration: "))
    rate=int(input("Enter the rate of intrest: "))
    Util.calculatePayment(principle,year,rate)

if __name__=="__main__":
    main()