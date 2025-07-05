from abc import ABC, abstractmethod
from product import Product
from note import Note
from coin import Coin

class VendingMachineState(ABC):
    def __init__(self, vending_machine):
        self._vending_machine = vending_machine

    @property
    def vending_machine(self):
        return self._vending_machine

    @abstractmethod
    def select_product(self, product: Product) -> None:
        pass

    @abstractmethod
    def insert_note(self, note: Note) -> None:
        pass

    @abstractmethod
    def insert_coin(self, coin: Coin) -> None:
        pass

    @abstractmethod
    def dispense_product(self) -> None:
        pass

    @abstractmethod
    def return_change(self) -> None:
        pass