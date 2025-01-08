# Initialize an empty dictionary to store product names and prices
product_prices = {}

# Function to add products and prices to the dictionary
def add_products():
    while True:
        product_name = input("Enter product name (or type 'done' to finish): ")
        if product_name.lower() == 'done':
            break
        try:
            price = float(input(f"Enter price for '{product_name}': "))
            product_prices[product_name] = price
        except ValueError:
            print("Invalid price. Please enter a numerical value.")

# Function to retrieve product prices
def get_product_price():
    while True:
        product_name = input("Enter a product name to get its price (or type 'exit' to quit): ")
        if product_name.lower() == 'exit':
            break
        if product_name in product_prices:
            print(f"The price of '{product_name}' is: ${product_prices[product_name]:.2f}")
        else:
            print(f"'{product_name}' is not in the product list.")

# Main function to run the program
def main():
    print("Welcome to the Product Price Manager!")
    add_products()
    get_product_price()
    print("Thank you for using the Product Price Manager!")

# Run the main function
if __name__ == "__main__":
    main()