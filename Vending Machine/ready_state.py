from vending_machine_state import VendingMachineState
from product import Product
from note import Note
from coin import Coin

class ReadyState(VendingMachineState):
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
        if self.vending_machine.total_payment > 0:
            print("User cancelled the transaction. Returning any money added")
            self.vending_machine.reset_payment()
        else:
            print("No change to return")
        self.vending_machine.set_state(self.vending_machine.idle_state)

    def _check_payment_status(self) -> None:
        amount_to_pay = self._vending_machine.selected_product.price
        if self.vending_machine.total_payment >= amount_to_pay:
            print("Added sufficient funds. Proceeding to dispensing the product")
            self.vending_machine.set_state(self.vending_machine.dispense_state)
        else:
            print("Insufficient funds. Add more money")
