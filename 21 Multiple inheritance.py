class Dad:
    def pocket_money(self):
        print("3000rs")

class Mom:
    def khana_khaa_lo(self):
        print("paneer tikka, Daal mhakanni")

class Son(Dad,Mom):
    pass


sonu = Son()
sonu.pocket_money()
sonu.khana_khaa_lo()