from product import Product
from store import Store


def seed_store() -> Store:
    store = Store("BestBuyDE")
    store.add_product(Product("Laptop", 999.99, 3))
    store.add_product(Product("Mouse", 24.99, 10))
    store.add_product(Product("Keyboard", 79.99, 5))
    return store


def main() -> None:
    store = seed_store()

    while True:
        print("\n=== BestBuyDE ===")
        print("1) List products")
        print("2) Order product")
        print("3) Exit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\nProducts:")
            print(store.list_products())

        elif choice == "2":
            print("\nProducts:")
            print(store.list_products())
            selection = input("Enter product number: ").strip()
            if not selection.isdigit():
                print("Please enter a valid number.")
                continue
            print(store.order(int(selection)))

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
