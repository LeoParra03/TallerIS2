class Item:
    def __init__(self, name, price, qty):
        if price < 0 or qty < 0:
            raise ValueError("Price and quantity must be non-negative.")
        self.name = name
        self.price = price
        self.qty = qty
        self.category = "general"
        self.env_fee = 0

        if self.category == "electronics":
            self.env_fee = 5  # Set environmental fee for electronics

    def get_total(self):
        """Calculate the total price for the item based on quantity."""
        return self.price * self.qty

    def get_env_fee(self):
        """Calculate the environmental fee based on quantity."""
        return self.env_fee * self.qty


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.tax_rate = 0.08
        self.member_discount = 0.05
        self.big_spender_discount = 10
        self.coupon_discount = 0.15
        self.currency = "USD"

    def add_item(self, item):
        """Add an item to the shopping cart."""
        self.items.append(item)

    def calculate_subtotal(self):
        """Calculate the subtotal of the items in the cart."""
        subtotal = 0
        for item in self.items:
            subtotal += item.get_total()
            subtotal += item.get_env_fee()
        return subtotal

    def apply_discounts(self, subtotal, is_member):
        """Apply discounts based on membership and subtotal."""
        if is_member:
            subtotal -= subtotal * self.member_discount
        if subtotal > 100:
            subtotal -= self.big_spender_discount
        return subtotal

    def calculate_total(self, is_member, has_coupon):
        """Calculate the total price after discounts and tax."""
        subtotal = self.calculate_subtotal()
        subtotal = self.apply_discounts(subtotal, is_member)
        total = subtotal + (subtotal * self.tax_rate)

        if has_coupon == "YES":
            total -= total * self.coupon_discount

        return total


def main():
    cart = ShoppingCart()
    items_data = [
        ("Apple", 1.5, 10),
        ("Banana", 0.5, 5),
        ("Laptop", 1000.0, 1)
    ]

    for name, price, qty in items_data:
        try:
            item = Item(name, price, qty)
            if name.lower() == "laptop":  # Set category for the laptop
                item.category = "electronics"
            cart.add_item(item)
        except ValueError as e:
            print(f"Error adding item '{name}': {e}")

    is_member = True
    has_coupon = "YES"

    try:
        total = cart.calculate_total(is_member, has_coupon)

        if total < 0:
            print("Error in calculation!")
        else:
            print(f"The total price is: ${total:.2f}")

    except Exception as e:
        print(f"An error occurred during calculation: {e}")


# Ensures main is only executed when the script is run directly
if __name__ == "__main__":
    main()