from vending_machine_state import VendingMachineState
from product import Product
from note import Note
from coin import Coin

class DispenseState(VendingMachineState):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product) -> None:
        print("Product selection already completed. Please collect the dispensed product.")

    def insert_note(self, note: Note) -> None:
        print("Payment already made. Please collect the dispensed product.")

    def insert_coin(self, coin: Coin) -> None:
        print("Payment already made. Please collect the dispensed product.")

    def dispense_product(self) -> None:
        product = self.vending_machine.selected_product
        quantity = self.vending_machine.inventory.get_quantity(product)
        print(f"Money successfully added. Dispensing product {product.name}")
        self.vending_machine.inventory.update_quantity(product, quantity-1)
        self.vending_machine.set_state(self.vending_machine.return_change_state)

    def return_change(self) -> None:
        print("Please collect the dispensed product first")
