from product import Product


class Store:
    def __init__(self, name: str):
        self.name = name
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self.products.append(product)

    def list_products(self) -> str:
        if not self.products:
            return "No products available."
        lines = []
        for i, product in enumerate(self.products, start=1):
            lines.append(
                f"{i}. {product.name} - {product.price:.2f} EUR (qty: {product.quantity})"
            )
        return "\n".join(lines)

    def order(self, product_number: int) -> str:
        if product_number < 1 or product_number > len(self.products):
            return "Invalid product number."
        product = self.products[product_number - 1]
        if product.buy():
            return f"Order confirmed: {product.name}"
        return f"Out of stock: {product.name}"
