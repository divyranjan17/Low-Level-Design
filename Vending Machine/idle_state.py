from vending_machine_state import VendingMachineState
from product import Product
from note import Note
from coin import Coin

class IdleState(VendingMachineState):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product) -> None:
        self.vending_machine.selected_product = product
        if self.vending_machine.inventory.get_quantity(product) <= 0:
            print("Product not in the inventory. Please check again later")
            return
        print(f"Product name: {product.name} and price: {product.price} selected successfully ")
        self.vending_machine.set_state(self.vending_machine.ready_state)

    def insert_note(self, note: Note) -> None:
        print("Select the product first.")

    def insert_coin(self, coin: Coin) -> None:
        print("Select the product first.")

    def dispense_product(self) -> None:
        print("Select the product first.")

    def return_change(self) -> None:
        print("Select the product first.")