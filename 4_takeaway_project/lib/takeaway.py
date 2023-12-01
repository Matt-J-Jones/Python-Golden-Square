import csv
from lib.menu_item import MenuItem

class Takeaway:
    def __init__(self):
        self.menu = []
        self.order = []

    def add_item(self, item):
        self.menu.append(item)

    def return_menu(self):
        x = 1
        full_menu = []
        for item in self.menu:
            full_menu.append(str(x) + ": " + item.return_formatted_item())
            x+=1
        return "\n".join(full_menu)

    def printed_menu(self):
        for item in self.menu:
            print(item.return_formatted_item())

    def add_item_to_order(self, item):
        if item.return_status() == "Available":
            self.order.append(item)

    def return_order(self):
        return self.order

    def confirm_order(self):
        total_price = 0
        items = []
        for item in self.order:
            items.append(item.return_name())
            total_price += item.return_price()
        return ", ".join(items) + " - Total: £" + self.format_price_as_str(total_price)
    
    def format_price_as_str(self, price):
        temp_price = str(price).split(".")
        if len(temp_price[1]) == 1:
            return str(temp_price[0] + "." + temp_price[1] + "0")
        return str(".".join(temp_price))