from vending_machine import VendingMachine
from product import Product
from coin import Coin
from note import Note

class VendingMachineDemo:
    @staticmethod
    def run():
        vending_machine = VendingMachine()

        # Add products to the inventory
        coke = Product("Coke", 10)
        pepsi = Product("Pepsi", 10)
        water = Product("Water", 5)

        vending_machine.inventory.add_product(coke, 5)
        vending_machine.inventory.add_product(pepsi, 3)
        vending_machine.inventory.add_product(water, 2)

        # Select a product
        vending_machine.select_product(coke)

        # Insert coins
        vending_machine.insert_coin(Coin.TWO)
        vending_machine.insert_coin(Coin.TWO)
        vending_machine.insert_coin(Coin.TWO)

        # Insert a note
        vending_machine.insert_note(Note.FIVE)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

        # Select another product
        vending_machine.select_product(pepsi)

        # Insert insufficient payment
        vending_machine.insert_coin(Coin.ONE)

        # Try to dispense the product
        vending_machine.dispense_product()

        # Insert more coins
        vending_machine.insert_coin(Coin.FIVE)
        vending_machine.insert_coin(Coin.TWO)
        vending_machine.insert_coin(Coin.TWO)

        # Dispense the product
        vending_machine.dispense_product()

        # Return change
        vending_machine.return_change()

if __name__ == "__main__":
    VendingMachineDemo.run()