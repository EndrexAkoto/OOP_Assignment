# Smartphone Class with Inheritance
class Smartphone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        return f"{self.brand} {self.model} costs ${self.price}"

class GamingSmartphone(Smartphone):  
    def __init__(self, brand, model, price, gpu):
        super().__init__(brand, model, price)
        self.gpu = gpu

    def details(self):
        return f"{self.brand} {self.model} with {self.gpu} GPU costs ${self.price}"

# Creating objects
phone = Smartphone("Samsung", "Galaxy S23", 999)
gaming_phone = GamingSmartphone("ASUS", "ROG Phone 7", 1299, "Adreno 730")

print(phone.details())            
print(gaming_phone.details())     
