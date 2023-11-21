import sqlite3
import handling_bd as hand_bd

conn = sqlite3.connect('magazyn.db')
c = conn.cursor()


c.execute('''CREATE TABLE IF NOT EXISTS produkty (
                id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                description TEXT,
                price REAL,
                quantity INTEGER
            )''')
conn.commit()


while True:
    print("1. Add new product")
    print("2. Search product")
    print("3. Update")
    print("4. Generate report")
    print("5. Delete product")
    print("0. Exit")

    x = input("Select option: ")
    if x == "1":
        hand_bd.add_product(c, conn)
    elif x == "2":
        hand_bd.search_product(c)
    elif x == "3":
        hand_bd.update(c, conn)
    elif x == "4":
        option = input("Overall or filtered report? O/F: ")
        if option.upper() == "O":
            hand_bd.report(c)
        elif option.upper() == "F":
            hand_bd.filtering_report(c)
        else:
            print("Option not corrected. Select again.")
    elif x == "5":
        hand_bd.delete_product(c, conn)
    elif x == "0":
        break
    else:
        print("Option not corrected. Select again.")

conn.close()