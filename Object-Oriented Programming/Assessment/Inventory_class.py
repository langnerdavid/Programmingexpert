class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.num_of_items = 0

    def add_item(self, name, price, quantity):
        self.num_of_items += quantity
        if self.num_of_items <= self.max_capacity and name not in self.items:
            self.items[name] = {"price": price, "quantity": quantity}
            return True

        return False

    def delete_item(self, name):
        if name in self.items:
            self.num_of_items -= self.items[name]["quantity"]
            del self.items[name]
            return True

        return False

    def get_items_in_price_range(self, min_price, max_price):
        items_in_range = []
        for name in self.items:
            if self.items[name]["price"] <= max_price and self.items[name]["price"] >= min_price:
                items_in_range.append(name)

        return items_in_range
        
        
    def get_most_stocked_item(self):
        most_stocked = []
        if len(self.items) == 0:
            return None

        highest_quantity = 0

        for item in self.items:
            if self.items[item]["quantity"] > highest_quantity:
                most_stocked = [item]
                highest_quantity = self.items[item]["quantity"] 
            elif self.items[item]["quantity"] == highest_quantity:
                most_stocked.append(item)

        return most_stocked[0] 

# print(i.items)
# for name in i.items:
#     print(i.items[name]["price"])
inventory = Inventory(4)
print(inventory.add_item('Chocolate', 4.99, 4))
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Chocolate'))
print(inventory.delete_item('Bread'))
print(inventory.add_item('Chocolate', 4.99, 2))
print(inventory.add_item('Bread', 4.99, 2))
print(inventory.items)
print(inventory.get_most_stocked_item() == ('Chocolate', 'Bread'))
i = ["bread"]
print(i)
