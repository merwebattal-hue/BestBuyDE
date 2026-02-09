from typing import List, Tuple
from products import Product


class Store:
    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[Tuple[Product, int]]) -> float:
        total_cost = 0.0

        for product, qty in shopping_list:
            # buy() zaten hatalı durumda exception fırlatıyor (yetersiz stok, qty<=0 vb.)
            total_cost += product.buy(qty)

        return total_cost

