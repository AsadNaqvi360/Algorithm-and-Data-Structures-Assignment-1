import time

class Product:
    def __init__(self, product_id, name, price, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category

def load_products_from_file(file_name):
    products = []
    with open(file_name, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            product_id, name, price, category = data
            products.append(Product(product_id, name, float(price), category))
    return products

def insert_product(products, product):
    products.append(product)

def update_product(products, product_id, new_name, new_price, new_category):
    for product in products:
        if product.product_id == product_id:
            product.name = new_name
            product.price = new_price
            product.category = new_category
            break

def delete_product_by_id(products, product_id):
    for product in products:
        if product.product_id == product_id:
            products.remove(product)
            break

def delete_product_by_index(products, index):
    del products[index]

def search_product_by_id(products, product_id):
    for product in products:
        if product.product_id == product_id:
            return product
    return None

def search_product_by_name(products, product_name):
    found_products = []
    for product in products:
        if product.name.lower() == product_name.lower():
            found_products.append(product)
    return found_products

def bubble_sort(products):
    n = len(products)
    for i in range(n):
        # Last i elements already placed
        for j in range(0, n - i - 1):
            if products[j].price > products[j + 1].price:
                products[j], products[j + 1] = products[j + 1], products[j]

def measure_sorting_time(sorting_function, data):
    start_time = time.perf_counter()
    sorting_function(data)
    end_time = time.perf_counter()
    return end_time - start_time

def main():
    file_name = 'product_data.txt'
    products = load_products_from_file(file_name)
    
    # Example insert
    new_product = Product("1005", "New Product", 29.99, "Electronics")
    insert_product(products, new_product)
    
    # Example update
    update_product(products, "1002", "Updated Product", 49.99, "Fashion")
    
    # Example delete1
    delete_product_by_id(products, "1003")
    
    # Example search1
    searched_product = search_product_by_id(products, "1001")
    if searched_product:
        print(f"Found Product: {searched_product.name}")
    else:
        print("Product not found.")

    # Example search2
    searched_products = search_product_by_name(products, "Phone")
    if searched_products:
        print("Found Products:")
        for product in searched_products:
            print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")
    else:
        print("No products found.")
    
    # Make copies of the products list for sort
    sorted_data = products.copy()
    reverse_sorted_data = products.copy()
    
    # Measure 
    sorting_time_sorted = measure_sorting_time(bubble_sort, sorted_data)

    # Measure 
    reverse_sorted_data.reverse()
    sorting_time_reverse_sorted = measure_sorting_time(bubble_sort, reverse_sorted_data)

    # Print sorted data
    print("\nSorted Data by Price:")
    for product in sorted_data:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Print reverse-sorted data
    print("\nReverse Sorted Data by Price:")
    for product in reverse_sorted_data:
        print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Category: {product.category}")

    # Print sorting items
    print(f"\nTime taken to sort sorted data: {sorting_time_sorted:.6f} seconds")
    print(f"Time taken to sort reverse-sorted data: {sorting_time_reverse_sorted:.6f} seconds")

if __name__ == "__main__":
    main()
