"""Store model that composes multiple Product instances."""

from __future__ import annotations

from typing import List, Tuple

from products import Product


class Store:
    """Represents a store containing a list of products."""

    def __init__(self, product_list: List[Product]) -> None:
        """Create a store with an initial list of products."""
        self.products: List[Product] = list(product_list)

    def add_product(self, product: Product) -> None:
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity across all products (active or not)."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """Return a list of active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        """Process a list of (Product, quantity) purchases and return total cost."""
        total_cost = 0.0
        for product, qty in shopping_list:
            total_cost += product.buy(qty)
        return total_cost
