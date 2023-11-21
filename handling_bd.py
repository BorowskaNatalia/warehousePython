def add_product(c, conn):
    print("Adding a product:")
    product_name = input("Product name: ")
    description = input("Description: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    c.execute("INSERT INTO produkty (product_name, description, price, quantity) VALUES (?, ?, ?, ?)",
              (product_name, description, price, quantity))
    conn.commit()
    print("Product added")


def search_product(c):
    x = input("Enter product name or id: ")
    c.execute("SELECT * FROM produkty WHERE product_name LIKE ? OR id = ?", ('%' + x + '%', x))
    result = c.fetchall()

    if len(result) > 0:
        print("Found products:")
        for product in result:
            print(f"ID: {product[0]}, Product name: {product[1]}, Quantity: {product[4]}, Price: {product[3]}")
    else:
        print("No products in stock")


def update(c, conn):
    print("Updating inventory status")
    id_product = int(input("Id product: "))
    q = int(input("New quantity: "))
    c.execute("UPDATE produkty SET quantity = ? WHERE id = ?", (q, id_product))
    conn.commit()


def report(c):
    print("Generate report")
    c.execute("SELECT * FROM produkty")
    result = c.fetchall()

    if len(result) > 0:
        print("Report:")
        for product in result:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[4]}, Price: {product[3]}")
    else:
        print("No products in stock")


def delete_product(c, conn):
    print("Removing the product")
    id_product = int(input("Enter the product id to be removed: "))
    c.execute("SELECT * FROM produkty WHERE id = ?", (id_product,))
    product = c.fetchone()

    if product is not None:
        confirm = input(f"Are you sure you want to delete the product named '{product[1]}'? (Y/N): ")

        if confirm.upper() == "Y":
            c.execute("DELETE FROM produkty WHERE id = ?", (id_product,))
            conn.commit()
            print("The product has been removed.")
        else:
            print("Canceled")
    else:
        print("No product found with this ID.")


def sort_results(results, x):
    if x == "price":
        return sorted(results, key=lambda y: y[3])
    elif x == "quantity":
        return sorted(results, key=lambda y: y[4])
    else:
        return results


def filtering_report(c):
    result = []
    print("Filtering the report")
    x = input("Enter the field to filter (name/price/quantity): ")

    if x == "name":
        search_product(c)
    elif x == "price":
        min_p = input("Enter minimum price: ")
        max_p = input("Enter maximum price: ")
        c.execute("SELECT * FROM produkty WHERE price BETWEEN ? AND ?", (min_p, max_p))
        result = c.fetchall()
    elif x == "quantity":
        min_q = input("Enter minimum quantity: ")
        max_q = input("Enter maximum quantity: ")
        c.execute("SELECT * FROM produkty WHERE quantity BETWEEN ? AND ?", (min_q, max_q))
        result = c.fetchall()
    else:
        print("Bad value. Back to main page.")
        return

    if len(result) > 0 and x != "name":
        sorted_results = sort_results(result, x)
        print("Filter results:")
        for product in sorted_results:
            print(f"ID: {product[0]}, Name: {product[1]}, Quantity: {product[4]}, Price: {product[3]}")
    elif x == "name":
        return
    else:
        print("There are no products matching the filter criteria.")
