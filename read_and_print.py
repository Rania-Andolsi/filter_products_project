import csv

# Open and read the file properly
with open("IT_products.csv", mode="r", encoding="utf-8") as file:
    reader = csv.reader(file)  # Using CSV reader for proper parsing
    for row in reader:
        if len(row) == 2:  # Ensure each row has exactly 2 columns (product and price)
            product_name = row[0].strip()
            price = row[1].strip()
            print(f"Product: {product_name}, Price: {price}")
