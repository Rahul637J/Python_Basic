'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: Find the Fewest Notes to be returned for Vending Machine  
'''

class Util:
    @staticmethod
    def change(amount, changes):
        '''
         Description: 
              This function recursively call the calculate function 
         Parameters:
              amount: The amount in RS entered by the user 
              changes: The list contains the denominations present        
         Return:
              calculate(amount,changes): it implicitly calls the calculate function 
         '''
        changes.sort(reverse=True)  
        ret_change = []  

        def calculate(amount, changes):
            '''
            Description: 
                 This function will find the denaminations to return and calls itself recursively 
            Parameters:
                 amount: The amount in RS entered by the user 
                 changes: The list contains the denominations present        
            Return:
                 calculate(amount,changes): This function will calls itself recursively untill find the denaminations and returns dinaminations in list  
            '''
            if amount == 0 or not changes:  
                return ret_change
            if amount >= changes[0]:  
                ret_change.append(changes[0])
                return calculate(amount - changes[0], changes)  
            else:
                return calculate(amount, changes[1:])  

        return calculate(amount, changes)  

def main():
    amount = int(input("Enter the amount in Rs: "))
    changes = [1, 5, 10, 50, 100, 500, 1000]
    amounts= Util.change(amount, changes)
    print(f"Denominations used: {amounts}")

if __name__ == "__main__":
    main()
