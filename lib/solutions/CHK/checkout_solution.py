
class CheckoutSolution:

    # skus = unicode string
    def checkout( skus):
        prices = {
            'A':50,
            'B':30,
            'C':20,
            'D':15,
        }
        offers = {
            'A': (3,130)
            ,'B': (2,45),
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

        A_Offers=A_count/offers['A'][0]
        print(A_Offers)


    checkout("AAAB")





