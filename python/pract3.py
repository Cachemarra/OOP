#%% Class design.
# A mini project of a store service.

class Product:
    product_id = 0

    def __init__(self, name: str, price: float):
        Product.product_id += 1
        self._product_id = Product.product_id
        self._name = name
        self._price = float(price)

    # Getters and setters.
    # Get method for _price attribute.
    @property
    def price(self):
        return self._price

    # Returning a representation of the object.
    def __str__(self):
        return f"ID Product: {self._product_id}, Name: {self._name}, Price: {self._price}"


if __name__ == "__main__":
    # Creating a product.
    product = Product("Laptop", 1_000)
    print(product)

    product2 = Product("TV", 500)
    print(product2)
    
# %% Creating a Order class.
class Order:
    order_cont = 0

    def __init__(self, products: list) -> None:
        Order.order_cont += 1
        self._order_id = Order.order_cont
        self._products = list(products)
        
    # Aggregation method
    def agg_product(self, product: Product) -> None:
        self._products.append(product)
    
    # Calculating the total.
    # Sum of all prices to get the total price.
    def total(self) -> float:
        total = 0
        for product in self._products:
            total += product.price
        return total

    def __str__(self) -> str:
        # Will store every call of product.__str__()
        products_str = ''
        for product in self._products:
            products_str += f"{product} |\n"
        return f"Order ID: {self._order_id}, \nProducts: {products_str}"


if __name__ == "__main__":
    # Creating a product.
    product = Product("Laptop", 1_000)
    product2 = Product("TV", 500)
    product3 = Product("Tablet", 300)

    # Creating a order.º
    order = Order([product, product2, product3])
    print(order)
    print(order.total())

# %% Adding new products to the order.
product4 = Product("Mouse", 50)
order.agg_product(product4)
product5 = Product("Keyboard", 100)
order.agg_product(product5)
print(order)
print(order.total())

print('Other Order'.center(50, '-'))
order2 = Order([product4, product5])
print(order2)
print(order2.total())
# %%
