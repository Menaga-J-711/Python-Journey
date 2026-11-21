
# 🟡 Task 3 — Simple Shopping Bill
# Ask for:
# - Product name
# - Quantity
# - Price of one product
# Then calculate:

# Total = Quantity × Price


#CODE

product_name = input("Enter Product Name:")
quantity = int(input("Enter Quantity:"))
price= float(input("Enter Price of one Product:"))
total= price*quantity
print()
print()
print("-------BILL--------")
print()
print("Product name:",product_name )
print("Quantity:",quantity)
print("Total : ", total)
print("-----------------------------")
print()

#OUTPUT

# Enter Product Name:Parker Pen
# Enter Quantity:4
# Enter Price of one Product:234.56


# -------BILL--------

# Product name: Parker Pen
# Quantity: 4
# Total :  938.24
# -----------------------------