class Product:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def is_available(self) -> bool:
        return self.quantity > 0

    def buy(self) -> bool:
        if self.quantity > 0:
            self.quantity -= 1
            return True
        return False
