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
            return quantity*20
        elif sku=="D":
            return quantity*15
        elif sku=="E":
            return quantity*40
        else:
            return -1


    # skus = unicode string
    def checkout(self,skus):
        prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
            'E':40,
        }

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

        counts=Counter(skus)


        for sku, count in counts.items():
            price=self.best_offer(sku, count)
            if price==-1:
                return -1
            total+=price



        return total




checkout = CheckoutSolution()
print(checkout.checkout("AAAC"))
