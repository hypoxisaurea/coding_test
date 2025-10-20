product_name, product_code = input().split()
product_code = int(product_code)

class Product:
    def __init__(self, product_name="", product_code=0):
        self.product_name = product_name
        self.product_code = product_code

    def __str__(self):
        return f"product {self.product_code} is {self.product_name}"

A = Product('codetree', 50)
B = Product(product_name, product_code)

print(A)
print(B)