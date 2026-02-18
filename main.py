"""CLI entry point for the BestBuyDE store application."""

import products
import store


def start(best_buy: store.Store) -> None:
    """Run the interactive CLI menu for a given store instance."""
    while True:
        print("\n=== BestBuyDE ===")
        print("1) List all products in store")
        print("2) Show total amount in store")
        print("3) Make an order")
        print("4) Quit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            active_products = best_buy.get_all_products()
            if not active_products:
                print("No active products available.")
                continue

            print("\nProducts:")
            for product in active_products:
                product.show()

        elif choice == "2":
            print(f"Total quantity in store: {best_buy.get_total_quantity()}")

        elif choice == "3":
            active_products = best_buy.get_all_products()
            if not active_products:
                print("No active products available.")
                continue

            print("\nProducts:")
            for index, product in enumerate(active_products, start=1):
                print(
                    f"{index}. {product.name} "
                    f"(Price: {product.price}, Qty: {product.get_quantity()})"
                )

            selection = input("Enter product number: ").strip()
            qty = input("Enter quantity: ").strip()

            if not selection.isdigit() or not qty.isdigit():
                print("Please enter valid numbers.")
                continue

            idx = int(selection) - 1
            qty_int = int(qty)

            if idx < 0 or idx >= len(active_products):
                print("Invalid product number.")
                continue

            try:
                total = best_buy.order([(active_products[idx], qty_int)])
                print(f"Order confirmed. Total: {total}")
            except ValueError as exc:
                print(f"Order failed: {exc}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


def main() -> None:
    """Create initial inventory and start the CLI."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
