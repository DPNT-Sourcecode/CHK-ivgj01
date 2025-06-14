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
            return quantity*10
        elif sku=="G":
            return quantity*20
        elif sku=="H":
            price += (quantity // 10) * 80
            quantity %= 10
            price += (quantity // 5) * 45
            quantity %= 5
            price += quantity * 10
            return price
        elif sku=="I":
            return quantity * 35
        elif sku=="J":
            return quantity * 60
        elif sku=="K":
            price += (quantity // 2) * 150
            quantity %= 2
            price += quantity * 80
            return price
        elif sku=="L":
            return quantity*90
        elif sku=="M":
            return quantity*15
        elif sku=="N":
            return quantity*40
        elif sku=="O":
            return quantity*10
        elif sku=="P":
            price += (quantity // 5) * 200
            quantity %= 5
            price += quantity * 50
            return price
        elif sku=="Q":
            price += (quantity // 3) * 80
            quantity %= 3
            price += quantity * 30
            return price
        elif sku=="R":
            return quantity*50
        elif sku=="S":
            return quantity*30
        elif sku=="T":
            return quantity*20
        elif sku=="U":
            return quantity*40
        elif sku=="V":
            price += (quantity // 3) * 130
            quantity %= 3
            price += (quantity // 2) * 90
            quantity %= 2
            price += quantity * 50
            return price
        elif sku=="W":
            return quantity*20
        elif sku=="X":
            return quantity*90
        elif sku=="Y":
            return quantity*10
        elif sku=="Z":
            return quantity*50
        else:
            return -1

    def apply_group_discount(self,counts, prices):
        group_skus = ['S','T','X','Y','Z']
        group_price=45
        group_size=3
        group_items=[]
        for sku in group_skus:
            group_items+=[sku]*counts.get(sku,0)

        group_items.sort(key=lambda sku: prices[sku], reverse=True)

        num_groups = len(group_items)//group_size
        total=num_groups*group_price

        for i in range(num_groups*group_size):
            counts[group_items[i]]-=1

        return total,counts


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

        free_Fs=counts.get('F',0)//3
        counts['F']=max(0,counts.get('F',0)-free_Fs)

        free_Ms=counts.get('N',0)//3
        counts['M']=max(0,counts.get('M',0)-free_Ms)

        free_Qs = counts.get('R', 0) // 3
        counts['Q'] = max(0, counts.get('Q', 0) - free_Qs)

        free_Us = counts.get('U', 0) // 4
        counts['U'] = max(0, counts.get('U', 0) - free_Us)

        group_total,counts = self.apply_group_discount(counts, prices)
        total += group_total


        for sku, count in counts.items():
            price=self.best_offer(sku, count)
            if price==-1:
                return -1
            total+=price



        return total




checkout = CheckoutSolution()
print(checkout.checkout("FFFF"))



