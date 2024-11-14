from datetime import datetime

class Product:
    def __init__(self, name=None, price=0, quantity=1):
        self._name = name
        self._price = price
        self._quantity = quantity
        
        
        if name is not None:
            if len(name) < 3 or len(name) > 8:
                raise ValueError("Ürün adi 3 ile 8 karakter arasinda olmalidir.")
            print(f"Ürün adi: {name}, Tarih: {datetime.now()}")

       
        if price < 0:
            raise ValueError("Fiyat 0'dan küçük olamaz.")
        
       
        if quantity < 1:
            raise ValueError("Adet en az 1 olmalidir.")

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @property
    def quantity(self):
        return self._quantity

    def get_total_price(self):
        return self._price * self._quantity

    def __str__(self):
        return f"Product(Name: {self._name}, Price: {self._price}, Quantity: {self._quantity})"