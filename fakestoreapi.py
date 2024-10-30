import requests

BASE_URL = "https://fakestoreapi.com/products"

def show_all_products():
    
    try:
        response = requests.get(BASE_URL)
        response.raise_for_status()
        products = response.json()
        print("All Products:")
        for product in products:
            print(f" - {product['title']}")
    except requests.exceptions.RequestException as e:
        print("Error fetching products:", e)

def show_product_details():
    product_id = input("Enter the Product ID: ")
    try:
        response = requests.get(f"{BASE_URL}/{product_id}")
        response.raise_for_status()
        product = response.json()
        print("\nProduct Details:")
        print(f"Product name: {product['title']}")
        print(f"Price: ${product['price']}")
        print(f"Description: {product['description']}")
        print(f"Category: {product['category']}")
    except requests.exceptions.RequestException as e:
        print("Error fetching product details:", e)
    except KeyError:
        print("Product not found!")

def add_new_product():
    title = input("Enter product name: ")
    price = input("Enter product price: ")
    description = input("Enter product description: ")
    category = input("Enter product category: ")

    new_product = {
        "title": title,
        "price": float(price),
        "description": description,
        "category": category,
    }

    try:
        response = requests.post(BASE_URL, json=new_product)
        response.raise_for_status()
        created_product = response.json()
        print("New Product Created Successfully:")
        print(f"ID: {created_product['id']}, Title: {created_product['title']}")
    except requests.exceptions.RequestException as e:
        print("Error adding product:", e)

def menu():
    while True:
        print("\nProduct Menu:")
        print("1. Show all products")
        print("2. Show product details")
        print("3. Add a new product")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            show_all_products()
        elif choice == "2":
            show_product_details()
        elif choice == "3":
            add_new_product()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select 1-4.")

menu()
