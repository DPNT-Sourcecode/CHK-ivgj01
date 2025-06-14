
class CheckoutSolution:
    def best_offer(self, prices, offers):
    # skus = unicode string
    def checkout(self,skus):
        prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
            'E':40,
        }
        offers = {
            'A': (3,130),
            'A': (5,200),
            'B': (2,45)

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

        A_Offers=A_count//offers['A'][0]
        print(A_Offers)
        A_non_offers=A_count%offers['A'][0]
        print(A_non_offers)


        B_Offers=B_count//offers['B'][0]
        print(B_Offers)
        B_non_offers=B_count%offers['B'][0]
        print(B_non_offers)
        total_price=A_Offers*offers['A'][1]+A_non_offers*prices['A']+B_Offers*offers['B'][1]+B_non_offers*prices['B']+C_count*prices['C']+D_count*prices['D']
        return total_price





