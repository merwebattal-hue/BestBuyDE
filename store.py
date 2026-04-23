from typing import List, Tuple

from products import Product


class Store:
    """Represents a store containing multiple products."""

    def __init__(self, product_list: List[Product]):
        if not isinstance(product_list, list):
            raise TypeError("product_list must be a list")

        for product in product_list:
            if not isinstance(product, Product):
                raise TypeError("all items in product_list must be Product instances")

        self.products = product_list

    def add_product(self, product: Product):
        """Add a product to the store."""
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        if not isinstance(product, Product):
            raise TypeError("product must be a Product instance")

        if product not in self.products:
            raise ValueError("product not found in store")

        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> List[Product]:
        """Return all active products."""
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Buy all products from the shopping list and return the total cost."""
        if not isinstance(shopping_list, list):
            raise TypeError("shopping_list must be a list")

        total_cost = 0.0

        for item in shopping_list:
            if not isinstance(item, tuple) or len(item) != 2:
                raise TypeError("each shopping list item must be a tuple of (Product, quantity)")

            product, quantity = item

            if not isinstance(product, Product):
                raise TypeError("first item in tuple must be a Product")
            if not isinstance(quantity, int):
                raise TypeError("second item in tuple must be an int")

            total_cost += product.buy(quantity)

        return total_cost
        