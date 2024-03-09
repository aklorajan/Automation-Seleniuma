# CREATE TABLE IF NOT EXISTS customers (
#     customer_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     email VARCHAR(100)
# );
#
# CREATE TABLE IF NOT EXISTS products (
#     product_id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(100),
#     price DECIMAL(10, 2)
# );
#
# CREATE TABLE IF NOT EXISTS orders (
#     order_id INT AUTO_INCREMENT PRIMARY KEY,
#     customer_id INT,
#     product_id INT,
#     quantity INT,
#     total_amount DECIMAL(10, 2),
#     order_date TIMESTAMP,
#     FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
#     FOREIGN KEY (product_id) REFERENCES products(product_id)
# );
