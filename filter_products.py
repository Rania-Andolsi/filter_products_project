import csv

def get_prices(filename):
    """
    Reads a CSV file containing product names and prices.
    
    Args:
        filename (str): Path to the CSV file.
    
    Returns:
        list: A list of tuples where each tuple contains a product name (str) and its price (float).
    """
    products = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 2:  # Ensures each row has exactly 2 values
                    product_name = row[0].strip()
                    try:
                        price = float(row[1].strip())  # Convert price to float
                        products.append((product_name, price))
                    except ValueError:
                        print(f"Skipping invalid price entry: {row[1]} in {row}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    
    return products

def filter_products():
    """
    Filters products into two categories based on their price:
    - Products costing less than $100 go into `cheap_products.csv`
    - Products costing at least $100 go into `expensive_products.csv`
    
    It prompts the user for a file name, reads data, filters it, and writes results to output files.
    """
    # Step 1: Ask user to input the filename
    filename = input("Insert the file name: ").strip()

    # Step 2: Retrieve product data from the file using `get_prices`
    products = get_prices(filename)

    # Step 3: Separate products into cheap and expensive categories
    cheap_products = [(name, price) for name, price in products if price < 100]
    expensive_products = [(name, price) for name, price in products if price >= 100]

    # Step 4: Write to `cheap_products.csv`
    with open('data/cheap_products.csv', mode='w', newline='', encoding='utf-8') as cheap_file:
        writer = csv.writer(cheap_file)
        for product in cheap_products:
            writer.writerow(product)

    # Step 5: Write to `expensive_products.csv`
    with open('data/expensive_products.csv', mode='w', newline='', encoding='utf-8') as expensive_file:
        writer = csv.writer(expensive_file)
        for product in expensive_products:
            writer.writerow(product)

    print("Files created!")

# Call the function to start the process
filter_products()

