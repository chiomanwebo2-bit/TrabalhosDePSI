products = []


# ----------------------------
# Add Product
# ----------------------------
def add_product():
    id = int(input("Product ID: "))
    name = input("Product Name: ")
    price = float(input("Price: "))
    quantity = int(input("Quantity: "))

    product = (id, name, price, quantity)
    products.append(product)

    print("Product added successfully!\n")


# ----------------------------
# Show Products
# ----------------------------
def show_products():
    if len(products) == 0:
        print("No products available.\n")
    else:
        print("\n--- Product List ---")
        for p in products:
            print(f"ID: {p[0]} | Name: {p[1]} | Price: {p[2]} | Quantity: {p[3]}")
        print()


# ----------------------------
# Search Product
# ----------------------------
def search_product():
    search_id = int(input("Enter ID to search: "))

    found = False

    for p in products:
        if p[0] == search_id:
            print("Product Found:")
            print(f"ID: {p[0]} | Name: {p[1]} | Price: {p[2]} | Quantity: {p[3]}\n")
            found = True

    if found == False:
        print("Product not found.\n")


# ----------------------------
# Remove Product
# ----------------------------
def remove_product():
    remove_id = int(input("Enter ID to remove: "))

    for p in products:
        if p[0] == remove_id:
            products.remove(p)
            print("Product removed successfully!\n")
            return

    print("Product not found.\n")


# ----------------------------
# Update Quantity
# ----------------------------
def update_quantity():
    update_id = int(input("Enter product ID to update: "))

    for i in range(len(products)):
        if products[i][0] == update_id:
            new_quantity = int(input("New quantity: "))

            # Create new tuple (because tuples are immutable)
            updated_product = (
                products[i][0],
                products[i][1],
                products[i][2],
                new_quantity
            )

            products[i] = updated_product
            print("Quantity updated successfully!\n")
            return

    print("Product not found.\n")


# ----------------------------
# Total Stock Value
# ----------------------------
def total_stock_value():
    total = 0

    for p in products:
        total += p[2] * p[3]

    print(f"Total stock value: {total}\n")


# ----------------------------
# Main Menu
# ----------------------------
def show_menu():
  while True:

    print("====== STORE MANAGEMENT SYSTEM ======")
    print("1 - Add Product")
    print("2 - Show All Products")
    print("3 - Search Product")
    print("4 - Remove Product")
    print("5 - Update Quantity")
    print("6 - Show Total Stock Value")
    print("7 - Exit")

    option = input("Choose an option: ")

    if option == "1":
        add_product()

    elif option == "2":
        show_products()

    elif option == "3":
        search_product()

    elif option == "4":
        remove_product()

    elif option == "5":
        update_quantity()

    elif option == "6":
        total_stock_value()

    elif option == "7":
        print("Exiting program...")
        break

    else:
        print("Invalid option! Try again.\n")
if __name__ == "__main__":
    show_menu()