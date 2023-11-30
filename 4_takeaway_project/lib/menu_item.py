class MenuItem:
    def __init__(self, name, price, availability):
        self.name = name
        self.price = price
        self.availability = availability

    def return_formatted_item(self):
        return f"{self.name}: £{self.return_price_as_string()}, {self.return_status()}"

    def mark_sold_out(self):
        self.availability = False

    def return_price_as_string(self):
        temp_price = str(self.price).split(".")
        if len(temp_price[1]) == 1:
            return str(temp_price[0] + "." + temp_price[1] + "0")
        return str(".".join(temp_price))

    def returns_name(self):
        return self.name

    def return_status(self):
        if self.availability:
            return "Available"
        return "Sold Out"
