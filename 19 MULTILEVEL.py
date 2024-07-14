class Grandfather:
    def meri_jamin(self):
        print("2 lakh square feet")


class Father(Grandfather):
    pass

class Beti(Father):
    pass

class Beti_ka_beta(Beti):
    pass

chinku = Beti_ka_beta()
chinku.meri_jamin()