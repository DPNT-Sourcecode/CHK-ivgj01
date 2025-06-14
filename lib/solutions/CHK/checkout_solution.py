from collections import Counter
from itertools import count


class CheckoutSolution:
    def best_offer(self,sku, quantity):
        price = 0
        if sku =="A":

            if quantity >=5:
                price += (quantity //5 *200)
                quantity%5
            if quantity >=3:
                price += (quantity //3 *130)
                quantity%3
            price+=quantity*50
            return price
        elif sku =="B":
            price += (quantity //2 *45)+(quantity%2*30)
            return price
        elif sku=="C":
            return count*20
        elif sku=="D":
            return count*15
        elif sku=="E":
            return count*40
        else:
            return -1


    # skus = unicode string
    def checkout(skus):
        prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
            'E':40,
        }
        '''
        offers = {
            'A': (3,130),
            'A': (5,200),
            'B': (2,45)

        }
        '''
        for sku in skus:
            if sku not in prices:
                return -1

        A_count=0
        B_count=0
        C_count=0
        D_count=0

        total = 0
        for sku in skus:
            if sku =='A':
                A_count+=1
            elif sku=='B':
                B_count+=1
            elif sku=='C':
                C_count+=1
            elif sku=='D':
                D_count+=1

        A_Offers=A_count//offers['A'][0] # number of offer items
        A_non_offers=A_count%offers['A'][0] # number of non offer items


        B_Offers=B_count//offers['B'][0]
        B_non_offers=B_count%offers['B'][0]

        total_price= A_Offers * best_offer("A", A_count) + A_non_offers * prices['A'] + B_Offers * best_offer("B", B_count) + B_non_offers * prices['B'] + C_count * prices['C'] + D_count * prices['D']
        return total_price










