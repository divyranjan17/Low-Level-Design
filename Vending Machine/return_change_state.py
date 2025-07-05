from vending_machine_state import VendingMachineState
from product import Product
from note import Note
from coin import Coin

class ReturnChangeState(VendingMachineState):
    def __init__(self, vending_machine):
        super().__init__(vending_machine)

    def select_product(self, product: Product) -> None:
        print("Product selection already completed")

    def insert_note(self, note: Note) -> None:
        self.vending_machine.add_note(note)
        print(f"Note added: {note}. Checking payment status")
        self._check_payment_status()

    def insert_coin(self, coin: Coin) -> None:
        self.vending_machine.add_coin(coin)
        print(f"Coin added: {coin}. Checking payment status")
        self._check_payment_status()

    def dispense_product(self) -> None:
        print("Add money for payment first.")

    def return_change(self) -> None:
        """
        Here it will be activated only if user cancels the transaction. 
        So return the entire amount user has provided.
        """
        change = self.vending_machine.total_payment - self.vending_machine.selected_product.price
        if change > 0:
            print(f"Transaction completed. Please collect your change of {change}")
            self.vending_machine.reset_payment()
        else:
            print("No change to return")
        self.vending_machine.reset_selected_product()
        self.vending_machine.set_state(self.vending_machine.idle_state)