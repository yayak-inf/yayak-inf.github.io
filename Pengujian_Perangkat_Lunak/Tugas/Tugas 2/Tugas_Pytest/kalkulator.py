class Kalkulator:

    def tambah(self, a, b):
        return a + b

    def kurang(self, a, b):
        return a - b

    def kali(self, a, b):
        return a * b

    # ❌ BUG SENGAJA (harusnya a / b)
    def bagi(self, a, b):
        return a * b