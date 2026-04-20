import ctypes
from typing import List, Optional
from dynamic_array import DynamicArray
from product import Product

class Inventory:
    def __init__(self, product_names: List[str], stocks: List[int], prices: List[float]) -> None:
        self._products: DynamicArray = DynamicArray(dtype=ctypes.py_object)
        for i in range(len(product_names)):
            self._products.insert_last(Product(product_names[i], stocks[i], prices[i]))

    def get_total_products(self) -> int:
        return len(self._products)

    def get_product(self, i: int) -> Optional[Product]:
        if self.get_total_products() == 0 or i < 0 or i >= self.get_total_products():
            return None
        return self._products[i]

    def set_product(self, i: int, product: Product) -> None:
        if i < 0 or i >= self.get_total_products():
            print('Error: out of range!')
            exit()
        self._products[i] = product

    
    def find_max_price(self) -> Optional[Product]:
        if self.get_total_products() == 0:
            return None
        max_p = self.get_product(0)
        for i in range(1, self.get_total_products()):
            cur = self.get_product(i)
            if cur.price > max_p.price:
                max_p = cur
        return max_p

    def find_max_investment(self) -> Optional[Product]:
        if self.get_total_products() == 0:
            return None
        max_p = self.get_product(0)
        max_inv = max_p.stock * max_p.price
        for i in range(1, self.get_total_products()):
            cur = self.get_product(i)
            inv = cur.stock * cur.price
            if inv > max_inv:
                max_inv = inv
                max_p = cur
        return max_p

    def sort_by_stock(self) -> None:
        n = self.get_total_products()
        if n <= 1:
            return
        # Selection sort (in‑place)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if self.get_product(j).stock < self.get_product(min_idx).stock:
                    min_idx = j
            if min_idx != i:
                temp = self.get_product(i)
                self.set_product(i, self.get_product(min_idx))
                self.set_product(min_idx, temp)

    def __str__(self) -> str:
        if self.get_total_products() == 0:
            return ""
        return "\n".join(str(self.get_product(i)) for i in range(self.get_total_products()))


if __name__ == "__main__":
    names = ["apples", "soup", "milk", "tofu", "poptarts", "lightbulbs", "soda", "chips"]
    stocks = [7, 6, 3, 1, 2, 0, 5, 24]
    prices = [3.99, 1.99, 2.50, 4.50, 5.99, 8.05, 2.99, 1.99]

    inventory = Inventory(names, stocks, prices)
    print("==", "Here are the results of creating the Inventory")
    print(inventory)

    max_price = inventory.find_max_price()
    print("==", "Here's' the product with the maximum price:")
    print(max_price)

    max_investment = inventory.find_max_investment()
    print("==", "Here's the product with the maximum investment:")
    print(max_investment)

    inventory.sort_by_stock()
    print("==", "Here are the products ordered by increasing stock-count: ")
    print(inventory)
