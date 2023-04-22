class CashRegister:
     tax = 5

     def __init__(self, products, cashier):
          self._products = products
          self.cashier = cashier
               
     @property
     def products(self):
          return self._products

     @products.setter
     def add_product(self, item):
          for prod in self._products:
               if prod['name'] == item['name']:
                    prod['quantity'] += item['quantity']
                    return
          self._products.append(item)

     @products.setter
     def remove_product(self, item):
          for prod in self._products:
               if prod['name'] == item['name']:
                    prod['quantity'] -= item['quantity']
                    if prod['quantity'] == 0:
                         self._products.remove(prod)
                         return
                    return
          self._products.remove(item)

     def calculate_total(self):
          return sum([item['price'] for item in self._products])

my_purchase = CashRegister([{"name":"Pizza", "price":10.34, "quantity":1},{"name":"chleba", "price":5, "quantity":1}],'Katka')

my_purchase.add_product = {"name":"Jahody","price":8, "quantity":1}

print(my_purchase.products)
my_purchase.add_product = {"name":"Jahody","price":8, "quantity":1}
my_purchase.add_product = {"name":"Maso","price":20, "quantity":1}
my_purchase.add_product = {"name":"Maso","price":20, "quantity":1}

print(my_purchase.products)
# my_purchase.remove_product = {"name":"Jahody","price":8, "quantity":1}

print(my_purchase.products)
print(my_purchase.cashier)
print("Total price: $", my_purchase.calculate_total())
print(f"Total price: ${my_purchase.calculate_total()}")