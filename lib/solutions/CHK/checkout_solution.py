from collections import Counter
from itertools import count


class CheckoutSolution:
    def best_offer(self,sku, quantity):
        price = 0

        if sku =="A":

            price += (quantity // 5) * 200
            quantity %= 5
            price += (quantity // 3) * 130
            quantity %= 3
            price += quantity * 50
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
        elif sku=="F":
            price += (quantity // 3) * 20
            quantity %= 3
            price += quantity * 10
            return price
        else:
            return -1


    # skus = unicode string
    def checkout(self,skus):
        prices = {
            'A': 50,
            'B': 30,
            'C': 20,
            'D': 15,
            'E': 40,
            'F': 10,
            'G': 20,
            'H': 10,
            'I': 35,
            'J': 60,
            'K': 80,
            'L': 90,
            'M': 15,
            'N': 40,
            'O': 10,
            'P': 50,
            'Q': 30,
            'R': 50,
            'S': 30,
            'T': 20,
            'U': 40,
            'V': 50,
            'W': 20,
            'X': 90,
            'Y': 10,
            'Z': 50
        }

        for sku in skus:
            if sku not in prices:
                return -1


        total = 0


        counts=Counter(skus)

        free_Bs=counts.get('E',0)//2
        counts['B']=max(0,counts.get('B',0)-free_Bs)

        for sku, count in counts.items():
            price=self.best_offer(sku, count)
            if price==-1:
                return -1
            total+=price



        return total




checkout = CheckoutSolution()
print(checkout.checkout("FFF"))


