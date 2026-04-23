import products
import store


def list_products(best_buy: store.Store):
    """Show all active products in the store."""
    active_products = best_buy.get_all_products()

    if not active_products:
        print("No active products available.")
        return

    print("\nProducts:")
    for product in active_products:
        product.show()


def show_total_amount(best_buy: store.Store):
    """Show the total amount of products in the store."""
    print(f"Total quantity in store: {best_buy.get_total_quantity()}")


def make_order(best_buy: store.Store):
    """Create and process a single order from user input."""
    active_products = best_buy.get_all_products()

    if not active_products:
        print("No active products available.")
        return

    print("\nProducts:")
    for index, product in enumerate(active_products, start=1):
        print(f"{index}. {product.name} (Price: {product.price}, Qty: {product.get_quantity()})")

    selection = input("Enter product number: ").strip()
    quantity = input("Enter quantity: ").strip()

    if not selection.isdigit() or not quantity.isdigit():
        print("Please enter valid numbers.")
        return

    product_index = int(selection) - 1
    order_quantity = int(quantity)

    if product_index < 0 or product_index >= len(active_products):
        print("Invalid product number.")
        return

    try:
        total = best_buy.order([(active_products[product_index], order_quantity)])
        print(f"Order confirmed. Total: {total}")
    except (TypeError, ValueError) as error:
        print(f"Order failed: {error}")


def start(best_buy: store.Store):
    """Start the command-line user interface."""
    while True:
        print("\n=== BestBuyDE ===")
        print("1) List all products in store")
        print("2) Show total amount in store")
        print("3) Make an order")
        print("4) Quit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            list_products(best_buy)
        elif choice == "2":
            show_total_amount(best_buy)
        elif choice == "3":
            make_order(best_buy)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


def main():
    """Create the initial inventory and start the application."""
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
    