'''
@Author: Rahul 
@Date: 2024-07-30
@Last Modified by: Rahul 
@Last Modified time: 2024-07-30
@Title: compute the square root of a nonnegative number     
'''
class Util:
    def sqrt(num):
            '''
            Description: 
                 This function to find the square root 
            Parameters:
                 num: int: the user input         
            Return:
                 t:  the squareroot of num
            '''
            epsilon = 1e-15
            t = num

            while abs(t - num / t) > epsilon * t:
                t = (t + num / t) / 2
            return t

def main():
    num=int(input("Enter the minimum positive number to find squareroot: "))
    squrt=Util.sqrt(num)
    print(round(squrt,2))
    
    
if __name__=="__main__":
    main()
