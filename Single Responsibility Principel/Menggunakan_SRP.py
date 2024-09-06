class Order:
    def __init__(self, items, quantities, prices):
        self.items = items
        self.quantities = quantities
        self.prices = prices

class OrderCalculator:
    def calculate_total(self, order):
        total = 0
        for i in range(len(order.items)):
            total += order.quantities[i] * order.prices[i]
        return total

class InvoicePrinter:
    def print_invoice(self, order, calculator):
        for i in range(len(order.items)):
            print(f'{order.items[i]}: {order.quantities[i]} x {order.prices[i]} = {order.quantities[i] * order.prices[i]}')
        total = calculator.calculate_total(order)
        print(f'Total: {total}')

order = Order(['Apple', 'Banana'], [5, 3], [10, 5])
calculator = OrderCalculator()
printer = InvoicePrinter()

printer.print_invoice(order, calculator)
