class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        if not isinstance(price, (int, float)):
            raise TypeError("price must be an int or float")
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an int")

        if not name.strip():
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Product price cannot be negative")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative")

        self.name = name
        self.price = float(price)
        self.quantity = quantity
        self.active = True

        if self.quantity == 0:
            self.active = False

    def get_quantity(self) -> int:
        """Return the current quantity."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Set the quantity and deactivate if it reaches zero."""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an int")
        if quantity < 0:
            raise ValueError("quantity cannot be negative")

        self.quantity = quantity

        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Return whether the product is active."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def show(self):
        """Print the product details."""
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        """Buy a given quantity and return the total price."""
        if not isinstance(quantity, int):
            raise TypeError("quantity must be an int")

        if not self.is_active():
            raise ValueError("Product is not active")

        if quantity <= 0:
            raise ValueError("quantity must be greater than 0")

        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        new_quantity = self.quantity - quantity
        self.set_quantity(new_quantity)

        return quantity * self.price
        