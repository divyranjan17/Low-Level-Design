class Product:
    def __init__(self, name: str, price: int):
        self._name = name
        self._price = price

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def price(self) -> int:
        return self._price
    
    @price.setter
    def price(self, price: int) -> None:
        self._price = price