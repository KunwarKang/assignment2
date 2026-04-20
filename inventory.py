import ctypes
from typing import List, Optional
from dynamic_array import DynamicArray
from product import Product

class Inventory:

    '''
    %  This function should create a Product object for each product represented
    ^  in the information provided in the function arguments, and it should store
    *  those products in a dynamic array. Each product will have a name, stock (number
    !  in stock), and price attribute. In particular, you should create a list implemented
    $  as a dynamic array, and append newly constructed product objects into it, 
    @  such that the i'th product you add to the the array has the i'th name, the
    (  i'th stock, and the i'th price from the provided arrays arguments.  Your constructor 
    <  should use the product constructor method defined in products.py to initialize each
    >  product struct stored in the array, and you should use the provided dynamic 
    ?  array functions to allocate and work with the dynamic array.  At the end of 
    .  the function, you should return the dynamic array with product structures 
    '  stored in it.
    '''
    def __init__(self, product_names: List[str], stocks: List[int], prices: List[float]) -> None:
        # Store products in a private DynamicArray member
        self._products: DynamicArray = DynamicArray(dtype=ctypes.py_object)
        
        # Logic to iterate through arguments and insert_last into self._products
        for i in range(len(product_names)):
            product = Product(product_names[i], stocks[i], prices[i])
            self._products.insert_last(product)

    '''
    ## Dynamic Array helper functions. These three functions will be how you interface
    ## the Dynamic Array. Below these three functions you cannot use self._products
    ## but within these functions you can.
    '''

    '''
    This method should return the total number of products in the inventory.
    '''
    def get_total_products(self) -> int:
        return len(self._products)

    '''
    This method should return the Product indexed by i in the dynamic array.
    It should return None if the number of products is zero (empty dynamic array)
    and it should return None if the index i is out of range of the valid
    indices in the dynamic array. Otherwise, it should return the product -- not a
    copy of the product, but the Product itself (i.e. don't allocate new memory)
    '''
    def get_product(self, i: int) -> Optional[Product]:
        if self.get_total_products() == 0:
            return None
        if i < 0 or i >= self.get_total_products():
            return None
        return self._products[i]

    '''
    This method should assign the value of the input Product "product"
    to index i. It should overwrite any data at index i unforturnately, this 
    is not an "insert" function. If the index is out of range of the size of the 
    product array, it should print the error message: 'Error: out of range!'
    and exit. 
    '''
    def set_product(self, i: int, product: Product) -> None:
        if i < 0 or i >= self.get_total_products():
            print('Error: out of range!')
            exit()
        self._products[i] = product

    '''
    *** Below here you are not to access self._products dynamic array directly ***

    You should only use the helper functions defined above to acceess elements of
    the dynamic array

    '''


    '''
    This function should return a pointer to the product in a given array
    with the highest price.  You should not make a copy of the product being
    returned, i.e. this function should not allocate any new memory.  Instead, you
    should return the product object that's already stored in the array.  You 
    must use the provided dynamic array functions to access the data stored in 
    the array. If the _products list is emtpy, it should return None.
    '''
    def find_max_price(self) -> Optional[Product]:
        if self.get_total_products() == 0:
            return None
        
        max_product = self.get_product(0)
        for i in range(1, self.get_total_products()):
            current = self.get_product(i)
            if current.price > max_product.price:
                max_product = current
        return max_product

    '''
    This function should return the product in a given Inventory object with
    the largest investment, defined as stock*price. 
    
    investment = stock*price
    
    meaning how many does the store have times the cost of each. You should 
    not make a copy of the product being returned, i.e. this function should 
    not allocate any memory.  Instead, you should simply return the product 
    object that's already stored in the dynamic array.  You must use the 
    provided dynamic array functions to access the data stored in the array.
    If the _products array is empty, it should return None
    '''
    def find_max_investment(self) -> Optional[Product]:
        if self.get_total_products() == 0:
            return None
        
        max_product = self.get_product(0)
        max_investment = max_product.stock * max_product.price
        
        for i in range(1, self.get_total_products()):
            current = self.get_product(i)
            current_investment = current.stock * current.price
            if current_investment > max_investment:
                max_investment = current_investment
                max_product = current
        return max_product

    '''
    This function should sort the products stored in a dynamic array by
    ascending stock (i.e. lowest stock at the beginning of the array).
    You may implement any sorting algorithm you want, with the following
    constraints:
       1. You must sort in place, i.e. you can't allocate additional memory.
       2. You may not use built-in sorting functions like sorted(), i.e. you
          must implement the sort yourself.  You may implement any in-place sorting
          algorithm you like.  Some possibilities are bubble sort, merge sort, 
          or quick sort, but also feel free to use another algorithm that you implement.
          don't use python's built-in sort method. 
    '''
    def sort_by_stock(self) -> None:
        n = self.get_total_products()
        if n <= 1:
            return
        
        # Bubble sort - in place
        for i in range(n - 1):
            for j in range(n - 1 - i):
                product_j = self.get_product(j)
                product_j_next = self.get_product(j + 1)
                if product_j.stock > product_j_next.stock:
                    self.set_product(j, product_j_next)
                    self.set_product(j + 1, product_j)

    '''
    This function should return string containing a comma-separated list of all products
    '''
    def __str__(self) -> str:
        if self.get_total_products() == 0:
            return ""
        
        result = []
        for i in range(self.get_total_products()):
            product = self.get_product(i)
            result.append(str(product))
        return ", ".join(result)


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
