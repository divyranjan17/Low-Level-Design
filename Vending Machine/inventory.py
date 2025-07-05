from product import Product

class Inventory:
    def __init__(self):
        self._products = {}
    
    @property
    def products(self):
        return self._products

    def add_product(self, product: Product, quantity: int) -> None:
        self._products[product] = quantity

    def remove_product(self, product: Product) -> None:
        del self._products[product]

    def get_quantity(self, product: Product) -> int:
        return self._products.get(product, 0)
    
    def update_quantity(self, product: Product, quantity: int):
        if quantity > 0:
            self._products[product] = quantity
        else:
            self.remove_product(product)

    def is_available(self, product: Product) -> bool:
        return True if self.get_quantity(product) > 0 else False