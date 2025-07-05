from inventory import Inventory
from vending_machine_state import VendingMachineState
from idle_state import IdleState
from ready_state import ReadyState
from dispense_state import DispenseState
from return_change_state import ReturnChangeState
from product import Product
from note import Note
from coin import Coin

class VendingMachine:
    def __init__(self):
        self.total_payment = 0
        self.selected_product = None
        self.inventory = Inventory()
        self.idle_state = IdleState(self)
        self.ready_state = ReadyState(self)
        self.dispense_state = DispenseState(self)
        self.return_change_state = ReturnChangeState(self)
        self.current_state = self.idle_state
    
    def set_state(self, state: VendingMachineState):
        self.current_state = state

    def display_products(self):
        for product in self.inventory.products:
            print(f"Product {product.name} found with quantity {self.inventory.get_quantity(product)}")
    
    def select_product(self, product: Product):
        self.current_state.select_product(product)

    def insert_note(self, note: Note):
        self.current_state.insert_coin(note)

    def insert_coin(self, coin: Coin):
        self.current_state.insert_note(coin)

    def dispense_product(self):
        self.current_state.dispense_product()

    def return_change(self):
        self.current_state.return_change()
    
    def add_note(self, note: Note):
        self.total_payment += note.value

    def add_coin(self, coin: Coin):
        self.total_payment += coin.value

    def reset_payment(self):
        self.total_payment = 0

    def reset_selected_product(self):
        self.selected_product = None

