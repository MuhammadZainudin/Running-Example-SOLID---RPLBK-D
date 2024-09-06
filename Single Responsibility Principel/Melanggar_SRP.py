class Order:
    def __init__(self, items, quantities, prices):
        self.items = items
        self.quantities = quantities
        self.prices = prices

    def calculate_total(self):
        total = 0
        for i in range(len(self.items)):
            total += self.quantities[i] * self.prices[i]
        return total

    def print_invoice(self):
        for i in range(len(self.items)):
            print(f'{self.items[i]}: {self.quantities[i]} x {self.prices[i]} = {self.quantities[i] * self.prices[i]}')
        print(f'Total: {self.calculate_total()}')

order = Order(['Apple', 'Banana'], [5, 3], [10, 5])
order.print_invoice()
