'''
@Author: Rahul
@Date: 2024-07-29
@Last Modified by: Rahul
@Last Modified: 2024-07-29
@Title: Program to generate distinct coupon numbers in n limit
'''

import random
class DistinctCoupons:
    @staticmethod
    def generate_coupon(length):
         """
         Description: Function to generate distinct numbers using random module.
         Parameters:
            length: length of the coupon number
         Returns:
            distinct_coupon: the set of the sistinct coupon numbers
         """
         coupons=set()
         while len(coupons)<length:
             random_num=random.randint(0,9)
             coupons.add(random_num)
         return coupons

    def main(self):
        length_of_coupon = int(input("Enter the length of the distinct coupon: "))
        coupon = DistinctCoupons.generate_coupon(length_of_coupon)
        for i in coupon:
            print(i,end="")

if __name__ == "__main__":
    DistinctCoupons().main()
    

